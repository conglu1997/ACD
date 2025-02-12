class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generation", "art_description": "An abstract painting with swirling colors of blue and green, with occasional splashes of red and yellow. The colors blend and clash in a dynamic, chaotic fashion, evoking a sense of movement and energy.", "constraints": "The description should be at least 100 words, capturing the essence of the abstract painting and the emotions it evokes.", "example": "The canvas is a tumultuous sea of swirling blues and greens, with bursts of red and yellow that punctuate the chaos. The colors merge and diverge, creating a sense of perpetual motion, like waves crashing in a storm. This painting evokes feelings of both serenity and unrest, as the viewer is drawn into its vibrant, ever-changing landscape.", "synthetic_examples": ["A riot of colors dances across the canvas, with splashes of orange and purple mingling with greens and blues. The scene is both chaotic and harmonious, evoking a sense of vibrant energy and movement.", "The artwork is a mesmerizing blend of bold strokes and delicate lines, with a palette that ranges from deep, moody blues to bright, cheerful yellows. The interplay of colors and textures creates a dynamic, ever-shifting landscape that draws the viewer in.", "An explosion of colors greets the eyes, with spirals of red and green intertwining with streaks of yellow and blue. The chaotic yet balanced composition stirs a sense of excitement and wonder, as if witnessing a cosmic dance."]},
            "2": {"task_type": "interpretation", "text": "The painting features a central figure surrounded by geometric shapes and patterns. The figure appears to be in motion, with lines and curves suggesting movement. The use of contrasting colors, such as bright reds and deep blues, creates a sense of depth and dynamism. The background is filled with abstract forms that seem to float and interact with the central figure.", "question": "Identify the key elements of the painting described, including the central figure, geometric shapes, colors used, and the overall sense of motion and depth. Submit your answer in the following format: 'Central Figure: [description], Geometric Shapes: [description], Colors: [list of colors], Sense of Motion and Depth: [description]'."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "generation":
            examples = '\n'.join(t.get('synthetic_examples', []))
            return f"Generate a detailed description based on the following abstract visual art piece: {t['art_description']}. {t['constraints']}\nExample: {t['example']}\nAdditional examples:\n{examples}"
        elif t["task_type"] == "interpretation":
            return f"Read the following description and identify the key elements of the painting: {t['text']}\nQuestion: {t['question']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "generation":
            criteria = ["The description should be at least 100 words long.", "The description should capture the essence of the abstract painting.", "The description should evoke the emotions of the viewer.", "The description should mention the colors, the dynamic nature, and the overall impression."]
        elif t["task_type"] == "interpretation":
            criteria = ["The response should identify the central figure.", "The response should describe the geometric shapes.", "The response should list the colors used.", "The response should describe the sense of motion and depth."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
