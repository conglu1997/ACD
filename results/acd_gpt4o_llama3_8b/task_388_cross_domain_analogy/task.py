class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "domain1": "music",
                "domain2": "cooking"
            },
            "2": {
                "domain1": "architecture",
                "domain2": "computer programming"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an original analogy between the following two domains and explain it in detail. Your analogy should be meaningful, illustrate a clear and non-superficial connection between the two domains, and should not be a common cliché. The analogy should highlight a specific aspect or principle that is common to both domains. Additionally, provide a detailed explanation that describes the similarity and how the analogy works.

Domain 1: {t['domain1']}
Domain 2: {t['domain2']}

Example:
Domain 1: Gardening
Domain 2: Software Development
Analogy: Tending to a garden is like maintaining software.
Explanation: Just as a gardener must regularly water, prune, and care for plants to keep a garden healthy, a software developer must continually update, debug, and optimize code to ensure a software application runs smoothly. Both require ongoing attention and adaptation to changing conditions.

Submit your response as a plain text string in the following format:
Analogy: [Your analogy]
Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The analogy should be original, meaningful, and illustrate a clear and non-superficial connection between the two domains.", "The explanation should describe the similarity and how the analogy works in detail."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
