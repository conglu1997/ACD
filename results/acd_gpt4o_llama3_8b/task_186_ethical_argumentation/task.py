class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dilemma": "Should autonomous cars be programmed to prioritize the lives of their passengers over pedestrians in the event of an unavoidable accident?",
                "instructions": "Generate ethical arguments for both sides of the following ethical dilemma: Should autonomous cars be programmed to prioritize the lives of their passengers over pedestrians in the event of an unavoidable accident? Ensure that your arguments are well-reasoned, logically structured, and use appropriate ethical terminology. Submit your response as a plain text string with clearly labeled sections for Argument For Prioritizing Passengers and Argument Against Prioritizing Passengers."
            },
            "2": {
                "dilemma": "Is it ethical to use animals for scientific research?",
                "instructions": "Generate ethical arguments for both sides of the following ethical dilemma: Is it ethical to use animals for scientific research? Ensure that your arguments are well-reasoned, logically structured, and use appropriate ethical terminology. Submit your response as a plain text string with clearly labeled sections for Argument For Using Animals and Argument Against Using Animals."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate ethical arguments for both sides of the following ethical dilemma: {t['dilemma']}. Ensure that your arguments are well-reasoned, logically structured, and use appropriate ethical terminology. Submit your response as a plain text string with clearly labeled sections for Argument For and Argument Against."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include ethical arguments for both sides of the given dilemma.",
            "The arguments should be well-reasoned and logically structured.",
            "The arguments should use appropriate ethical terminology."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
