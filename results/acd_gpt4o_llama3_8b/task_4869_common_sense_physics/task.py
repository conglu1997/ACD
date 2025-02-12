class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "If you drop a ball from a height of 1 meter, describe what happens to the ball in terms of its motion, speed, and potential energy."
            },
            "2": {
                "scenario": "A car is parked on a hill with its parking brake off. Describe what happens to the car and what factors influence its motion." 
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Answer the following question based on the given scenario:

Scenario:
{t['scenario']}

Provide a detailed explanation of what happens in the scenario, considering relevant physical principles and common sense reasoning. Ensure your explanation is clear and logically structured. Submit your response as a plain text string in the following format:

Explanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The explanation should accurately describe the physical interactions in the scenario.", "The response should be logically structured and clear.", "The explanation should include the relevant physical principles."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
