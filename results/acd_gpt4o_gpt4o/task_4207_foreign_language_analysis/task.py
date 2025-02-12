class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "La casa está vacía.", "task": "Translate the sentence into English and then rewrite it in the passive voice."},
            "2": {"text": "Il gatto dorme sulla sedia.", "task": "Translate the sentence into English and then form a question asking where the cat is sleeping."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        text = t["text"]
        task = t["task"]
        instructions = f"""Your task is to perform linguistic analysis and manipulation in the specified foreign language. Follow the instructions below:

Text: {text}
Task: {task}

Provide your response in the following format:

Translation: [Your translation]
Manipulation: [Your manipulated sentence based on the task]

Example:
Text: El perro corre rápido.
Task: Translate the sentence into English and then rewrite it in the past tense.
Response:
Translation: The dog runs fast.
Manipulation: The dog ran fast.

Ensure your response is accurate and follows the specified linguistic operation exactly."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The translation should accurately convey the original meaning.",
            "The manipulation should correctly follow the specified linguistic operation."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
