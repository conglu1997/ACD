class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": {
                    "field": "quantum computing",
                    "application": "medical diagnostics"
                }
            },
            "2": {
                "data": {
                    "field": "biotechnology",
                    "application": "environmental cleanup"
                }
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        field = t['data']['field']
        application = t['data']['application']
        return f"""Develop a description and use-case scenario for a new fictional technology based in the field of {field} with an application in {application}. Ensure that the technology is scientifically plausible, integrates relevant scientific principles, and is described in detail. Include a use-case scenario that illustrates how this technology would function in a real-world setting with specific examples of its operation.

Submit your response as a plain text string in the following format:

Technology Description: [Your description]
Use-Case Scenario: [Your use-case scenario]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The technology should be scientifically plausible.",
            "The description should integrate relevant scientific principles.",
            "The use-case scenario should be detailed, provide specific examples, and illustrate real-world functionality."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
