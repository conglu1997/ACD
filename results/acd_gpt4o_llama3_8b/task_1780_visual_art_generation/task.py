class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Generate a detailed description of a surrealist painting that features a melting clock, a floating elephant, and a distorted landscape."
            },
            "2": {
                "prompt": "Describe an impressionist painting that depicts a bustling city street at sunset, with people walking, cars moving, and buildings bathed in golden light."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = "You will be given a prompt to generate a detailed description of a visual art piece. Your description should be vivid, coherent, and capture the essence of the given artistic style."
        instructions += f"\nPrompt: {t['prompt']}"
        instructions += "\nSubmit your description as a plain text string."
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The description should be vivid and coherent.",
            "The description should capture the essence of the given artistic style.",
            "The description should include all elements mentioned in the prompt."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
