class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "phenomenon": "Explain the Doppler Effect and how it applies to both sound and light."
            },
            "2": {
                "phenomenon": "Explain the concept of entropy in thermodynamics and its implications for the second law of thermodynamics."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Explain the following physical phenomenon in simple terms that a layperson can understand:\n\nPhenomenon:\n{t['phenomenon']}\n\nFormat your response as follows:\n1. Provide a clear and simple explanation of the phenomenon.\n2. Use analogies or examples where necessary to aid understanding.\n3. Ensure the explanation is accurate and covers the essential aspects of the phenomenon.\n4. Keep the explanation concise, ideally within 200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be clear and simple.",
            "The explanation should be accurate and cover the essential aspects of the phenomenon.",
            "Analogies or examples should be used where necessary to aid understanding.",
            "The explanation should be concise, ideally within 200 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
