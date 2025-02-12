class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A farmer who works tirelessly on his land but does not see immediate growth in his crops."},
            "2": {"scenario": "An entrepreneur who invests all her savings into a startup, and eventually, the startup becomes highly successful."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a culturally appropriate idiom or proverb for the following scenario: '{t["scenario"]}'. The idiom should be original, meaning it should not be a well-known existing idiom or proverb. Ensure that the idiom reflects the cultural context and conveys a meaningful and relevant message related to the scenario. For example, consider cultural values, common phrases, and societal norms when creating the idiom. Submit your idiom as a single sentence."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The idiom should be culturally appropriate.",
            "The idiom should be original and not a well-known existing idiom.",
            "The idiom should convey a meaningful and relevant message related to the scenario.",
            "The idiom should be submitted as a single sentence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
