class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idiom": "Break the ice"},
            "2": {"idiom": "Hit the nail on the head"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the meaning of the given idiom and create a new idiom with an explanation:

Idiom: {t['idiom']}

1. Interpret the given idiom and explain its meaning in your own words. Ensure your explanation is clear, accurate, and contextually appropriate.
2. Create a new idiom and provide an explanation of its meaning and context. The new idiom should be original, coherent, and culturally appropriate.

Provide your response in the following format:

Interpretation: [Your interpretation]
New Idiom: [Your new idiom]
Explanation: [Explanation of your new idiom]

Example:
Idiom: A piece of cake
Interpretation: This idiom means that something is very easy to do.
New Idiom: As cool as a cucumber
Explanation: This idiom means that someone is very calm and composed, even in a difficult situation.

Make sure your new idiom is something that could be understood and used in common language."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include an accurate interpretation of the given idiom.", 
            "The new idiom should be original, coherent, and culturally appropriate.", 
            "The explanation of the new idiom should clearly describe its meaning and usage."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
