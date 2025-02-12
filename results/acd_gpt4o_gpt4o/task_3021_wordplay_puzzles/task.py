class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "solve", "puzzle": "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"},
            "2": {"type": "create", "theme": "animals"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "solve":
            instructions = f"""Your task is to solve the following riddle:

{t['puzzle']}

Provide your answer in a single word or short phrase in plain text format."""
        elif t["type"] == "create":
            instructions = f"""Your task is to create a wordplay puzzle based on the given theme. The theme is: {t['theme']}

Ensure that your puzzle is creative, challenging, and adheres to the given theme. Provide your puzzle in plain text format. Additionally, include the solution as a separate line following the puzzle."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "solve":
            criteria = ["The solution should correctly answer the riddle."]
        elif t["type"] == "create":
            criteria = ["The puzzle should be creative and adhere to the given theme.", "The puzzle should include a solution."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
