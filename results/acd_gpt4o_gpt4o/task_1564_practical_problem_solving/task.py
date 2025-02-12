class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"problem": "Reduce plastic waste in urban areas.", "instruction": "Propose a detailed and innovative solution to reduce plastic waste in urban areas. Consider practical constraints and potential challenges."},
            "2": {"problem": "Improve access to clean drinking water in remote villages.", "instruction": "Propose a detailed and innovative solution to improve access to clean drinking water in remote villages. Consider practical constraints and potential challenges."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to generate an innovative solution for the following real-world problem:

Problem: {t['problem']}

{t['instruction']}

Ensure that your solution:
1. Is detailed and well-structured.
2. Is creative and innovative.
3. Considers practical constraints and challenges.
4. Is feasible, with a clear explanation of how it can be implemented and its potential impact.

Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should be detailed and well-structured.",
            "The solution should be creative and innovative.",
            "The solution should consider practical constraints and challenges.",
            "The solution should be feasible and include a clear explanation of implementation and potential impact."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
