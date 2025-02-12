class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "A young girl discovers a hidden portal in her backyard."},
            "2": {"story": "Once upon a time, in a small village surrounded by forests, there lived a kind old man named Gregory. One day, Gregory found a wounded bird and took it home to nurse it back to health. As the bird healed, it revealed itself to be a magical creature capable of granting wishes. Gregory, being selfless, wished for the prosperity and happiness of his village. From that day on, the village flourished, and Gregory became a beloved figure whose kindness and generosity were remembered for generations."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'prompt' in t:
            return f"""Write a short story (300-500 words) based on the following prompt:

Prompt: {t['prompt']}

Ensure that your story has a clear beginning, middle, and end. Include descriptive elements to make the narrative engaging. Provide your response in plain text format. Use paragraph breaks to separate different sections of your story."""
        else:
            return f"""Interpret the following story and explain its main message and key elements:

Story: {t['story']}

Your response should be at least 150 words and include an analysis of the main message, characters, and any significant elements or themes present in the story. Provide your response in plain text format. Use clear paragraphs to structure your analysis."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'prompt' in t:
            criteria = [
                "The story should be based on the given prompt.",
                "The story should have a clear beginning, middle, and end.",
                "The story should include descriptive elements to make the narrative engaging.",
                "The story should be between 300-500 words.",
                "The story should use paragraph breaks to separate different sections."
            ]
        else:
            criteria = [
                "The interpretation should include an analysis of the main message, characters, and key elements.",
                "The interpretation should be at least 150 words.",
                "The interpretation should use clear paragraphs to structure the analysis."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
