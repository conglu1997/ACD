class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"language": "English", "type": "idiom"},
            "2": {"language": "Spanish", "type": "proverb"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        language = t["language"]
        type_ = t["type"]
        return f"""Generate a(n) {type_} in {language} and explain its meaning and context. Ensure that the {type_} is commonly used in the given language and provide a detailed explanation of its usage, including any cultural or historical significance. Submit your response as a plain text string in the following format:\n\n{type_.capitalize()}: [Generated {type_} here]\nExplanation: [Your explanation here]\n\nExample:\nIdiom: 'Break the ice'\nExplanation: This idiom means to initiate conversation in a social setting, making people feel more comfortable. It is often used in situations where people feel awkward or shy, and someone makes an effort to start talking and ease the tension. The phrase likely originates from the literal act of breaking ice to make way for ships to pass, symbolizing the clearing of a barrier."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated idiom or proverb should be appropriate and commonly used in the specified language.",
            "The explanation should accurately convey the meaning and context of the idiom or proverb.",
            "The explanation should include any relevant cultural or historical significance."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
