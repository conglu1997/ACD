class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "conflict": "Roommates disagreeing over cleanliness standards in common areas. Roommate A values strict cleanliness, while Roommate B is more relaxed about it. They have had several heated arguments about this.",
                "parties_involved": ["Roommate A", "Roommate B"]
            },
            "2": {
                "conflict": "Colleagues having a dispute over credit for a project. Colleague A feels they did most of the work, while Colleague B believes their contributions were critical. The conflict is affecting their teamwork and productivity.",
                "parties_involved": ["Colleague A", "Colleague B"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate practical and empathetic advice for resolving the following social conflict:

Conflict: {t['conflict']}

The advice should include the following sections:
1. Understanding the Conflict: Briefly explain the nature of the conflict and the perspectives of the parties involved.
2. Communication Strategies: Suggest effective communication techniques that the parties can use to discuss their differences.
3. Practical Solutions: Offer specific, actionable steps that the parties can take to resolve the conflict.
4. Emotional Considerations: Highlight any emotional aspects that should be considered and addressed.
5. Long-term Strategies: Provide recommendations for preventing similar conflicts in the future.

The advice should be clear, empathetic, and practical. Avoid overly simplistic solutions and ensure your advice addresses the nuances of the conflict. Use plain text for your submission. Here is an example format for the Practical Solutions section:

1. Solution 1 description
2. Solution 2 description
3. Solution 3 description
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The advice should be empathetic and understanding of all parties involved.",
            "The communication strategies should be effective and applicable.",
            "The practical solutions should be actionable and realistic.",
            "The emotional considerations should be relevant and sensitive to the parties' feelings.",
            "The long-term strategies should be sensible and aimed at preventing future conflicts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
