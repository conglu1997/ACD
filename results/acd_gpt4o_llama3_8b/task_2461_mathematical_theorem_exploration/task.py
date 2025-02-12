class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theorem": "Pythagorean Theorem", "task_type": "explain_and_example"},
            "2": {"theorem": "Fundamental Theorem of Calculus", "task_type": "explain_and_example"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Understand and explain the given mathematical theorem. Provide a clear and concise explanation, and include at least one example to illustrate the theorem.

Theorem: {t['theorem']}

Your explanation should:
1. Clearly state the theorem and its significance.
2. Provide a detailed explanation of the theorem.
3. Include at least one example that demonstrates the theorem in practice.
4. Provide a step-by-step breakdown of the example to show the theorem in action.

Submit your response as a plain text string with clearly labeled sections for 'Theorem Statement', 'Explanation', 'Example', and 'Step-by-Step Breakdown'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly state the theorem and its significance.",
            "The response should provide a detailed explanation of the theorem.",
            "The response should include at least one example that demonstrates the theorem in practice.",
            "The response should provide a step-by-step breakdown of the example.",
            "The response should exhibit a deep understanding of the mathematical concepts involved."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
