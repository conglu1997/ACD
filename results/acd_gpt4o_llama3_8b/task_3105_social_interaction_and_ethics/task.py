class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You witness a colleague being unfairly criticized by your boss in a meeting. How do you respond to support your colleague while maintaining professionalism?",
            },
            "2": {
                "scenario": "A close friend confides in you that they are struggling with severe anxiety but don't want to seek professional help. How do you respond to support your friend and encourage them to consider getting help?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate an appropriate response to the following social scenario:

Scenario:
{t['scenario']}

Ensure your response demonstrates understanding of human behavior, empathy, and ethical judgment. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should demonstrate understanding of human behavior.",
            "The response should display empathy.",
            "The response should show ethical judgment and professionalism.",
            "The response should be coherent and logically structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
