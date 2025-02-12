class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "explanation",
                "principle": "Photosynthesis"
            },
            "2": {
                "task_type": "application",
                "principle": "Newton's Third Law of Motion"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'explanation':
            return f"""Explain the following scientific principle in a clear and concise manner, suitable for a high school student:

Principle: {t['principle']}

Ensure your explanation includes the key concepts, underlying mechanisms, and real-world examples where applicable. Submit your explanation as a plain text string between 150-200 words in the following format:

Explanation: [Your explanation]"""
        else:
            return f"""Generate a creative application of the following scientific principle in a fictional scenario:

Principle: {t['principle']}

Describe a scenario where this principle is applied in a novel or imaginative way, such as in a futuristic or fantasy setting. Ensure your description is detailed, coherent, and clearly illustrates the principle in action. Submit your application as a plain text string between 200-300 words in the following format:

Application: [Your application]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'explanation':
            validation_criteria = [
                "The explanation should accurately cover the key concepts and mechanisms of the principle.",
                "The explanation should be clear, concise, and suitable for a high school student.",
                "The explanation should include real-world examples where applicable."
            ]
        else:
            validation_criteria = [
                "The application should creatively and accurately apply the scientific principle.",
                "The scenario should be detailed, coherent, and engaging.",
                "The description should illustrate the principle in action in a novel or imaginative way."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
