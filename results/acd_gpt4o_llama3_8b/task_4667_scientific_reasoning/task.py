class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "observations": "Plants in a particular garden are growing noticeably faster than similar plants in other areas. The garden is exposed to natural sunlight and is watered daily with a solution prepared by the gardener.",
                "constraints": "Generate a plausible hypothesis that explains the faster growth of the plants in this garden. Design an experiment to test this hypothesis, including control and experimental groups, variables to be measured, and expected outcomes."
            },
            "2": {
                "observations": "A group of students observed that a specific type of fish in a lake tend to swim closer to the surface during the early morning and late evening hours. During the rest of the day, the fish are found deeper in the water.",
                "constraints": "Generate a plausible hypothesis that explains the observed behavior of the fish. Design an experiment to test this hypothesis, including control and experimental groups, variables to be measured, and expected outcomes."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are tasked with generating a scientific hypothesis based on the given observations and designing an experiment to test this hypothesis. Ensure that your hypothesis is plausible and that your experimental design is thorough and coherent. Include the following elements in your response:
1. Hypothesis: [Your hypothesis]
2. Experimental Design: [Your experimental design, including control and experimental groups, variables to be measured, and expected outcomes]

Observations: {t['observations']}
Constraints: {t['constraints']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The hypothesis should be plausible and relevant to the given observations.",
            "The experimental design should be thorough and logically coherent.",
            "The submission should include control and experimental groups, variables to be measured, and expected outcomes."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
