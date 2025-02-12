class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "The data shows that Plant A grows 25% faster under blue light compared to red light.",
                "argument_to_critique": "Blue light is preferable for all plants because it universally enhances growth."
            },
            "2": {
                "data": "Study X found that students who slept 8 hours performed 20% better on exams than those who slept 6 hours.",
                "argument_to_critique": "Increasing sleep to 8 hours will improve academic performance for all students."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Task 1: Based on the following data, generate a coherent scientific argument:

{t['data']}

Ensure your argument is logical and well-structured.

Task 2: Critique the following argument based on the provided data:

{t['argument_to_critique']}

Identify any logical fallacies, unsupported assumptions, or areas for improvement. Submit both tasks as a plain text string in the following format:

1. Argument: [Your generated argument]
2. Critique: [Your critique of the provided argument]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The generated argument should be logical and well-structured.",
            "The critique should identify logical fallacies, unsupported assumptions, or areas for improvement."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
