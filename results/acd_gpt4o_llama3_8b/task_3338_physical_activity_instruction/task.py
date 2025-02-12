class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "activity": "How to perform a proper push-up"
            },
            "2": {
                "activity": "How to correctly perform a yoga sun salutation"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        activity = t["activity"]
        return f"""Generate a detailed step-by-step instruction for the following physical activity:

Activity: {activity}

Your instructions should be clear, logically sequenced, and detailed enough for someone to follow accurately. Include any necessary preparation steps, safety tips, and common mistakes to avoid. Submit your response as a plain text string in the following format:

1. Step 1: [First step]
2. Step 2: [Second step]
...

Example:
1. Step 1: Start in a plank position with your hands directly under your shoulders and your body forming a straight line from head to heels.
2. Step 2: Lower your body by bending your elbows, keeping them close to your body, until your chest nearly touches the floor.
3. Step 3: Push back up to the starting position by straightening your arms, ensuring your body remains in a straight line throughout the movement.

Ensure your instructions are comprehensive and can be easily followed by someone new to the activity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The steps should be clear, logically sequenced, and detailed.", "The instructions should include preparation steps, safety tips, and common mistakes to avoid."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
