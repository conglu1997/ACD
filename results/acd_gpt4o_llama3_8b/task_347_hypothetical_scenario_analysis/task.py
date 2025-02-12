class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Imagine a world where humans can no longer use fossil fuels. What are the possible outcomes or implications for global economies and societies?"
            },
            "2": {
                "scenario": "Suppose that all forms of digital communication suddenly stopped working. What are the potential impacts on daily life, businesses, and governments?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given hypothetical scenario and provide detailed possible outcomes or implications. Ensure your analysis is comprehensive, logically consistent, and creatively explores various aspects of the scenario. Your response should be between 150-300 words. Submit your response as a plain text string.\n\nScenario: {t['scenario']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should be logically consistent.",
            "The response should be comprehensive, addressing multiple aspects of the scenario.",
            "The response should be creative, exploring various potential outcomes or implications."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
