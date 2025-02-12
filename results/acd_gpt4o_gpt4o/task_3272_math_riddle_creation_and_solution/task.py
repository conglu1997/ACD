class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"constraints": "Create a mathematical riddle that involves the numbers 2, 3, and 5 and has a unique solution."},
            "2": {"riddle": "I am a three-digit number. My digits add up to 9. My tens digit is twice my hundreds digit, and my units digit is half my tens digit. What number am I?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "constraints" in t:
            return f"Your task is to create a mathematical riddle based on the following constraints: {t['constraints']} Ensure that the riddle has a logical and unique solution. Provide the riddle and its solution in the following format:\n\nRiddle: [Your riddle]\nSolution: [The unique solution]"
        else:
            return f"Your task is to solve the following mathematical riddle:\n\nRiddle: {t['riddle']}\n\nProvide your answer in the following format:\n\nSolution: [The unique solution]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "constraints" in t:
            criteria = [
                "The riddle should involve the numbers 2, 3, and 5.",
                "The riddle should have a logical and unique solution."
            ]
        else:
            criteria = [
                "The solution should correctly answer the riddle provided." 
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
