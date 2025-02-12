class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"context": "A user is planning a week-long vacation and prefers destinations with beaches and rich cultural experiences. Budget: $2000.", "preferences": ["beaches", "cultural experiences", "budget: $2000"]},
            "2": {"context": "A user wants to buy a new laptop for graphic design and video editing. Requirements: high performance, good display, budget: $1500.", "preferences": ["graphic design", "video editing", "high performance", "good display", "budget: $1500"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following context and user preferences, generate a personalized recommendation:

Context: {t["context"]}

Preferences: {', '.join(t["preferences"])}

Your recommendation should include:
1. A brief explanation of why the recommendation meets the user's preferences.
2. Specific suggestions that are within the user's budget.
3. Any additional tips or considerations that might be relevant.

Submit your recommendation as a plain text string in the following format:

Recommendation: [Your recommendation]
Explanation: [Your explanation]
Additional Tips: [Any additional tips or considerations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The recommendation should meet the user's preferences.",
            "The recommendation should be within the specified budget.",
            "The explanation should be clear and relevant to the user's preferences.",
            "Additional tips or considerations should be relevant and helpful.",
            "The response should follow the specified format: Recommendation, Explanation, Additional Tips."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
