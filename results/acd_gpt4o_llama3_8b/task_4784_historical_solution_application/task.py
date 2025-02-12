class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "modern_problem": "How can we reduce plastic waste in the environment?",
                "historical_context": "Medieval period, Europe"
            },
            "2": {
                "modern_problem": "How can we provide clean drinking water in remote areas?",
                "historical_context": "Ancient Rome"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with solving a modern problem using methods or technologies from a specific historical period. Your solution should be practical and feasible within the constraints of the specified historical context. Ensure that your proposal is detailed and explains how it would address the modern problem using historical methods.

Modern Problem: {t['modern_problem']}
Historical Context: {t['historical_context']}

Submit your response as a plain text string in the following format:

Solution: [Your detailed solution here]

Your solution should include:
1. A description of the historical methods or technologies used.
2. How these methods or technologies will be applied to the modern problem.
3. Any potential limitations or challenges of using this historical solution in the modern context.
4. A comparison between the historical methods and modern-day solutions, highlighting the advantages and disadvantages of each."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
