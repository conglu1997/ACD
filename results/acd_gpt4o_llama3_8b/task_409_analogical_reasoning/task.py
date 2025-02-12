class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pair": ["The structure of an atom", "The solar system"],
                "context": "Consider the similarities and differences in the structure of an atom and the solar system."
            },
            "2": {
                "pair": ["A company", "A beehive"],
                "context": "Consider the similarities and differences in the organization and functioning of a company and a beehive."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        pair = t["pair"]
        context = t["context"]
        return f"""Identify and explain the analogy between the following pair of concepts or situations: {pair[0]} and {pair[1]}.\n
{context}\n
Submit your response as a plain text string in the following format: 'Analogy: [Your explanation of the analogy]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should clearly identify similarities and differences between the given pair.", "The analogy should be logical and coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
