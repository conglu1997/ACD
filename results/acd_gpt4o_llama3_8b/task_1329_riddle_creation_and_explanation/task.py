class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "time"},
            "2": {"theme": "nature"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        return f"""Create a complex riddle based on the given theme and provide a detailed explanation of the solution. Ensure that the riddle is original, creative, and challenging. The riddle should not give away the solution and must involve logical reasoning and creative thinking. The explanation should clearly demonstrate the logical reasoning behind the solution. Submit your response as a plain text string in the following format:

Riddle: [Your riddle]
Solution Explanation: [Your detailed explanation]

Consider the following points while creating the riddle and the solution explanation:
- The riddle should be unique and not easily guessable.
- The riddle should require the solver to think deeply and use logic.
- The solution explanation should be thorough and logically sound, explaining each step clearly.
- Avoid using common riddles or easily searchable solutions."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The riddle should be clearly stated, original, and challenging.",
            "The riddle should not give away the solution.",
            "The riddle should require deep thinking and logical reasoning.",
            "The solution explanation should be thorough, logically sound, and clearly explain each step."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
