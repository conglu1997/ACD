class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "issue": "Food insecurity in developing countries.",
                "constraints": "Design a comprehensive solution to address food insecurity in developing countries. Consider social, economic, and environmental factors, including agricultural innovation, economic policies, and community programs. Address potential challenges such as resource limitations and political instability, and propose strategies to overcome them."
            },
            "2": {
                "issue": "Climate change and its impact on coastal cities.",
                "constraints": "Design a comprehensive solution to mitigate the impact of climate change on coastal cities. Consider social, economic, and environmental factors, including infrastructure development, economic incentives, and community engagement. Address potential challenges such as funding limitations and public resistance, and propose strategies to overcome them."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and describe a comprehensive solution to the following contemporary global issue:

Issue:
{t['issue']}

Constraints:
{t['constraints']}

Your solution should be well-reasoned, innovative, and feasible. Consider the broader implications on social, economic, and environmental aspects, and address potential challenges and how to overcome them. Submit your response as a plain text string in the following format:

Solution: [Your detailed solution]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The solution should be well-reasoned and feasible.",
            "The solution should be innovative and consider broader implications.",
            "The response should address social, economic, and environmental aspects.",
            "The response should include potential challenges and how to overcome them.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
