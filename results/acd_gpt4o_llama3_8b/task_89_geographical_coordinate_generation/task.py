class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "A landmark located at the midpoint between the Equator and the North Pole, directly on the Prime Meridian.", "task_id": "1"},
            "2": {"description": "A city known for its iconic opera house, located at approximately 34° S latitude and 151° E longitude.", "task_id": "2"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given geographical description:

Description: {t['description']}

Generate the most accurate map coordinates (latitude and longitude) based on the given description. Ensure that your coordinates are as precise as possible.

Submit your coordinates as a plain text string in the following format: 'Latitude: [value], Longitude: [value]'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_id = t['task_id']
        # Expected coordinates for task 1 and task 2
        expected_coordinates = {
            "1": "Latitude: 45.0, Longitude: 0.0",
            "2": "Latitude: -34.0, Longitude: 151.0"
        }
        criteria = ["The response should be in the format 'Latitude: [value], Longitude: [value]'.", f"The response should match the coordinates: {expected_coordinates[task_id]}"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
