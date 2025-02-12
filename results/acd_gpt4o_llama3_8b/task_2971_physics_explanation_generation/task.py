class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"phenomenon": "Why do objects of different masses fall at the same rate in a vacuum?"},
            "2": {"phenomenon": "Explain how a rainbow is formed."},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a clear and accurate explanation for the following physical phenomenon using fundamental principles and laws of physics:

Phenomenon: {t["phenomenon"]}

Ensure that your explanation is scientifically accurate, logically coherent, and easy to understand. Provide your explanation as a plain text string. Format your response as follows:

Explanation: [Your explanation]

Example:
For the phenomenon 'Why do objects of different masses fall at the same rate in a vacuum?', a suitable explanation could be: 'In a vacuum, there is no air resistance to slow down the objects. According to the principle of equivalence, the acceleration due to gravity is constant for all objects regardless of their mass. Therefore, objects of different masses fall at the same rate in a vacuum.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should be scientifically accurate.",
            "The explanation should be logically coherent.",
            "The explanation should be clear and easy to understand.",
            "The explanation should use fundamental principles and laws of physics.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
