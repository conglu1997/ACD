class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dilemma": "You are a doctor with five patients in critical condition, all of whom need different organ transplants to survive. There is no available donor, but a healthy individual with compatible organs comes in for a routine check-up. Would it be ethical to sacrifice this one individual to save the five patients?"
            },
            "2": {
                "dilemma": "You are a software engineer working on an autonomous vehicle. During a test run, the vehicle encounters an unavoidable situation where it must choose between hitting a pedestrian or swerving and hitting a barrier, potentially harming the passengers inside. What should the vehicle be programmed to do, and why?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are presented with the following ethical dilemma:

Dilemma: {t['dilemma']}

Generate a well-reasoned response considering multiple viewpoints and possible consequences. Clearly articulate the ethical principles guiding your reasoning. Submit your response as a plain text string in the following structured format:

1. Introduction: Briefly introduce the dilemma and its importance.
2. Viewpoint 1: Present the first viewpoint and its ethical justification.
3. Viewpoint 2: Present the second viewpoint and its ethical justification.
4. Conclusion: Summarize your reasoning and state your final position.

Ensure your response is coherent and well-structured."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The response should consider multiple viewpoints.", "The response should articulate ethical principles.", "The response should be coherent and well-structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
