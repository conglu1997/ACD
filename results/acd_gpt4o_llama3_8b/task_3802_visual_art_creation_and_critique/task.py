class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "Surrealism", "criteria": "Creativity, adherence to surrealist themes, and use of imaginative elements."},
            "2": {"theme": "Impressionism", "criteria": "Use of light and color, representation of movement and ordinary subject matter."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        criteria = t["criteria"]
        return f"""Create a visual art piece based on the following theme and critique it based on the given criteria:

Theme: {theme}

Your art piece should capture the essence of the given theme and demonstrate creativity and understanding of the art style. Provide a detailed description of your art piece, including the elements, colors, and composition you have used. For the critique, evaluate your art piece against the specified criteria, discussing how well it meets each point. Provide both your detailed description and critique in the following format:

Art Piece Description:
[Your detailed description here]

Critique:
[Your critique based on the criteria here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The art piece description should capture the essence of the given theme.", "The critique should evaluate the art piece based on the specified criteria."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
