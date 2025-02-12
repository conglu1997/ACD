class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "event": "The signing of the Treaty of Versailles in 1919",
                "alteration": "Germany was not held responsible for the war and was not required to pay reparations"
            },
            "2": {
                "event": "The fall of the Berlin Wall in 1989",
                "alteration": "The Soviet Union did not collapse and continued to exert influence over Eastern Europe"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Simulate the following historical event with the given alteration: {t['event']} with the alteration: {t['alteration']}. Provide a detailed explanation of how this alteration could have changed the course of history, including potential short-term and long-term impacts. Ensure that your response is coherent, historically plausible, and demonstrates a deep understanding of the historical context. Submit your simulation as a plain text string in the following format: 'Simulation: [Your simulation]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The simulation should be coherent and historically plausible.",
            "The response should include potential short-term and long-term impacts.",
            "The simulation should demonstrate a deep understanding of the historical context.",
            "The submission should be in the correct format: 'Simulation: [Your simulation]'."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
