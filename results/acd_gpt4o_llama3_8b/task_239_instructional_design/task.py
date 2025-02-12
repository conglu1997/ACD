class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "materials": ["cardboard", "scissors", "tape", "markers"],
                "object": "a small model house"
            },
            "2": {
                "materials": ["plastic bottles", "glue", "string", "paint"],
                "object": "a bird feeder"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate step-by-step instructions for building the following object:

Object: {t['object']}
Materials: {', '.join(t['materials'])}

Ensure that the instructions are clear, logical, and feasible using the provided materials. Your instructions should be detailed enough for someone to follow and build the object successfully. Break down your instructions into numbered steps and aim for a length of 150-300 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The instructions should be clear and logical.",
            "The instructions should be feasible using the provided materials.",
            "The instructions should be detailed enough to follow and build the object successfully.",
            "The instructions should be broken down into numbered steps.",
            "The response should be between 150-300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
