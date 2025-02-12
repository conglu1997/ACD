class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "animals"},
            "2": {"theme": "objects"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theme = t["theme"]
        return f"""Create a riddle based on the theme '{theme}' and provide its solution. The riddle should be clever and engaging, using wordplay or lateral thinking if possible. Ensure that the solution to the riddle is accurate and makes sense in the context of the riddle. Submit your response as a plain text string in the following format:\nRiddle: [Your riddle here]\nSolution: [Your solution here]\n\nExample:\nTheme: 'fruits'\nRiddle: I am a fruit that is always sad. What am I?\nSolution: A blueberry."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The riddle should be based on the given theme.",
            "The riddle should be clever and engaging.",
            "The solution should make sense and be accurate."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
