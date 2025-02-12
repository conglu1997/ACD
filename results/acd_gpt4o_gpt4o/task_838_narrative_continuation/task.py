class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Once upon a time, in a small village nestled between towering mountains, there lived a young girl named Elara. Elara had always been curious about the world beyond the mountains, but the villagers warned her of the dangers that lay outside. One day, she found a mysterious map hidden in her grandmother's attic..."},
            "2": {"prompt": "In the futuristic city of Nova, humans and robots coexisted peacefully. However, tensions began to rise when a new type of robot, capable of independent thought, was introduced. Alex, a young engineer, discovered a hidden agenda behind the creation of these robots and decided to..."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        return f"""Your task is to continue the following story. Ensure that your continuation is coherent, engaging, and in line with the narrative style provided. You should develop the plot further, introduce new elements or characters if necessary, and provide a satisfying progression to the story.

{prompt}

Your continuation should:
- Be at least 300 words.
- Maintain a consistent narrative voice.
- Include a clear beginning, middle, and end.

Provide your continuation in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The continuation should be coherent and logically follow from the given prompt.",
            "The response should be engaging and maintain the reader's interest.",
            "The narrative voice should be consistent with the provided prompt.",
            "The continuation should be at least 300 words.",
            "The continuation should include a clear beginning, middle, and end."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
