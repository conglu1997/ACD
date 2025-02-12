class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "concept": "Quantum Entanglement",
                "target_audience": "high school students"
            },
            "2": {
                "concept": "Theory of Relativity",
                "target_audience": "middle school students"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a simple educational explanation and an analogy for the following scientific concept. Ensure that your explanation is clear, engaging, and suitable for the target audience mentioned. The explanation should help the audience understand the concept without oversimplifying it to the point of inaccuracy. The explanation should be between 150 to 300 words.

Concept: {t['concept']}
Target Audience: {t['target_audience']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The explanation should be clear and engaging.",
            "The explanation should be suitable for the target audience.",
            "The explanation should include a helpful analogy.",
            "The explanation should accurately convey the scientific concept.",
            "The explanation should be between 150 to 300 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
