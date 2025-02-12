class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "You are in a rectangular room measuring 20 feet by 15 feet, with a door centered in the north wall and a window centered in the south wall. There is a table positioned exactly in the center of the room, and a chair placed directly to the west of the table. Describe how to navigate from the door to the window.", "environment": "rectangular room (20ft x 15ft) with door in north wall, window in south wall, table in center, chair to west of table"},
            "2": {"description": "You are in a park that is a perfect square with sides measuring 50 meters. In the center of the park is a fountain. To the north of the fountain is a playground 10 meters away, to the east is a bench 10 meters away, to the south is a pond 10 meters away, and to the west is a flower garden 10 meters away. Describe how to navigate from the playground to the pond.", "environment": "square park (50m x 50m) with fountain in center, playground 10m to north, bench 10m to east, pond 10m to south, flower garden 10m to west"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following spatial description and generate navigational instructions. Provide clear and precise steps to navigate within the described environment.

Environment: {t['environment']}

Task: {t['description']}

Your response should be in the following format:
Step-by-step instructions: [Your navigational steps]
Make sure your instructions are detailed, logically lead from the starting point to the destination, and avoid any ambiguity. The instructions should ensure a clear and logical flow without any missing steps."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The instructions should logically connect the starting point to the destination.", "The steps should be clear, detailed, and unambiguous.", "The instructions should ensure a clear and logical flow without any missing steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
