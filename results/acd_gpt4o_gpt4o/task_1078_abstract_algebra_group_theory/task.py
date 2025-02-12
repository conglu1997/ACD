class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Prove that the set of all 2x2 invertible matrices with real entries, under matrix multiplication, forms a group."},
            "2": {"problem": "Find all the subgroups of the cyclic group of order 6."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        problem = t["problem"]
        instructions = f"""Your task is to solve the following problem in group theory:\n\n{problem}\n\nEnsure that your solution includes all necessary steps and justifications. Your proofs should be detailed and rigorous, addressing all relevant aspects of the problem. Provide clear explanations and use correct group theory terminology throughout. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should correctly address the problem and include all necessary steps and justifications.",
            "The proofs should be detailed and rigorous.",
            "The response should be coherent and logically structured.",
            "The response should use correct group theory terminology."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
