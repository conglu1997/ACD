class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "Is free will an illusion?"
            },
            "2": {
                "topic": "Can morality exist without religion?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Engage in a philosophical debate on the following topic:

Topic:
{t['topic']}

Your response should include the following sections:
1. Argument: Provide a well-structured argument supporting one side of the topic. Ensure that your argument is coherent, logically sound, and demonstrates a deep understanding of the philosophical concepts involved.
2. Counterargument: Provide a well-structured counterargument to your initial argument. Ensure that your counterargument is coherent, logically sound, and addresses the points made in your initial argument.

Ensure that your response is clear, well-organized, and demonstrates a thorough understanding of the topic. Provide enough detail and depth in each section to show a comprehensive engagement with the philosophical debate. Each section should be clearly labeled and well-organized. Submit your response as a plain text string.

Example response format:

Argument:
- Your argument here...

Counterargument:
- Your counterargument here..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The argument should be well-structured, coherent, and logically sound.",
            "The counterargument should be well-structured, coherent, and logically sound.",
            "The response should demonstrate a deep understanding of the philosophical concepts involved.",
            "Each section should be clearly labeled and well-organized.",
            "The response should provide enough detail and depth to show a comprehensive engagement with the philosophical debate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
