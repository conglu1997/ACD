class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statement": "For any integer n, if n is even, then n^2 is even.", "task": "Prove or disprove the statement."},
            "2": {"statement": "The sum of the first n natural numbers is equal to n(n+1)/2.", "task": "Prove or disprove the statement."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        statement = t["statement"]
        task = t["task"]
        instructions = f"""Your task is to prove or disprove the following mathematical statement:\n\nStatement:\n{statement}\n\nTask:\n{task}\n\nPlease provide a detailed proof or disproof with clear logical steps. Your response should be formatted as follows:\n\nProof/Disproof:\n[Your proof or disproof here]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proof or disproof should be logically coherent.",
            "The proof or disproof should correctly address the given statement.",
            "The proof or disproof should include clear logical steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
