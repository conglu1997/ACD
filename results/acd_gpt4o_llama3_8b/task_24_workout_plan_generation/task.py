class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"goal": "weight loss", "days": 3, "equipment": "none"},
            "2": {"goal": "muscle gain", "days": 5, "equipment": "dumbbells"},
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        goal = t["goal"]
        days = t["days"]
        equipment = t["equipment"]
        return f"""Generate a detailed workout plan for the goal of {goal}. The plan should span {days} days per week and use {equipment}. Ensure that each day's workout includes a warm-up, main exercises, and a cool-down. Each section should be clearly labeled, and the exercises should be varied and appropriate for the goal. Submit your plan as a plain text string with each day's workout separated by a newline character. Format each day's workout as follows:\nDay X: \nWarm-up: description \nMain exercises: list of exercises \nCool-down: description\nFor example: \nDay 1: \nWarm-up: 5 minutes jogging \nMain exercises: Push-ups, Squats \nCool-down: Stretching \nDay 2: \nWarm-up: 5 minutes jumping jacks \nMain exercises: Lunges, Plank \nCool-down: Yoga poses."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The plan should span the specified number of days.", 
            "Each day's workout should include a warm-up, main exercises, and a cool-down.", 
            "The exercises should be varied and appropriate for the specified goal.",
            "The plan should use the specified equipment."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
