class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A diagram of a pulley system with labeled parts including a fixed pulley, a movable pulley, and a load."},
            "2": {"description": "A diagram of a lever with labeled parts including the fulcrum, effort, and load."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        instructions = f"""Your task is to interpret the following mechanical diagram and describe how the depicted machine works:

Description: {description}

Ensure that your explanation is clear, detailed, and accurately describes the function of each part and the overall mechanism. Your response should include the following elements:
1. The function of each labeled part.
2. The overall function of the machine.
3. How the parts work together to achieve the machine's function.

Provide your explanation in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should match the given description.",
            "The explanation should be clear and detailed.",
            "The explanation should accurately describe the function of each part and the overall mechanism.",
            "The explanation should include how the parts work together to achieve the machine's function."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
