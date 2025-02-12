class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "Break the ice (English)", "context": "Meeting new people at a party"},
            "2": {"idiom": "Tomar el pelo (Spanish)", "context": "Joking or teasing someone"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts:

1. Interpret the given idiomatic expression from the specified culture.
2. Explain its meaning and describe an appropriate context for its use.

Idiom: {t['idiom']}
Context: {t['context']}

Provide your response in the following format:

Interpretation: [Your interpretation of the idiom]
Explanation: [Your explanation of the idiom's meaning and appropriate context for use]

Example:
Idiom: Break the ice (English)
Context: Meeting new people at a party

Interpretation: To initiate conversation in a social setting.
Explanation: The idiom 'break the ice' means to initiate conversation or interaction in a social setting where people may feel awkward or shy. It is often used when meeting new people at a party or gathering to make everyone feel more comfortable."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately interpret the given idiomatic expression.", 
            "The response should correctly explain the idiom's meaning and appropriate context for use.",
            "The interpretation should reflect an understanding of the cultural nuances of the idiom."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
