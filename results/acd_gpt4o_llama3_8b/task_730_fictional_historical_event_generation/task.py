class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Imagine a major technological breakthrough occurring in the 18th century. Describe the event and its impact on society.", "theme": "technology"},
            "2": {"prompt": "Imagine a significant political revolution occurring in the 19th century. Describe the event and its impact on society.", "theme": "politics"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following prompt, create a detailed fictional historical event and describe its impact on society:

Prompt: {t['prompt']}

Your response should include:
1. A clear description of the event, including when and where it took place.
2. The key figures involved, including their roles and motivations.
3. The immediate and long-term impact on society, including social, economic, and political changes.
4. Any cultural, political, or technological changes that resulted from the event.
5. Ensure your narrative is coherent, logically structured, and engaging.

Your response should be at least 200 words. Submit your response as a plain text string in the following format:

Event Description: [Your detailed description of the event and its impact]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The event description should be clear, detailed, and include when and where it took place.",
            "The key figures involved should be mentioned, including their roles and motivations.",
            "The immediate and long-term impact on society should be explained, including social, economic, and political changes.",
            "Any cultural, political, or technological changes should be included.",
            "The narrative should be coherent, logically structured, and engaging.",
            "The response should be at least 200 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
