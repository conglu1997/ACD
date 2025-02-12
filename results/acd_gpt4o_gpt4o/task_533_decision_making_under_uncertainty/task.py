class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are a doctor tasked with deciding whether to administer a new drug to a patient. The drug has a 70% chance of curing the disease but a 30% chance of causing severe side effects, including a 10% chance of death from the side effects. The disease itself has a 50% mortality rate if untreated. What is your decision, and why?"
            },
            "2": {
                "scenario": "You are an investor deciding whether to invest in a new startup. The startup has a 60% chance of becoming highly profitable, generating a 10x return on investment, but a 40% chance of failing, resulting in a complete loss of investment. Additionally, you have the option to invest in a stable bond that guarantees a 5% return annually with no risk. What is your decision, and why?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to make an optimal decision based on the following scenario:\n\n{t['scenario']}\n\nProvide a clear rationale for your decision, taking into account the probabilities and potential outcomes. Your response should be formatted as follows:\n\nDecision: [Your decision]\nRationale: [Your rationale]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The decision should be logically sound and take into account the given probabilities and potential outcomes.",
            "The rationale should be clear and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
