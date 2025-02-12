class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "You are in a park. To your north, there is a playground. To your east, there is a pond. To your west, there is a forest. Describe the shortest route to get from the playground to the pond."},
            "2": {"description": "You are at the entrance of a museum. To your right, there is an information desk. Straight ahead, there is an exhibition hall. To your left, there is a gift shop. Describe the route to get from the entrance to the gift shop, passing by the information desk."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        description = t["description"]
        return f"""Using the following description of an environment, generate a clear set of directions to navigate from one location to another. Focus on the spatial relationships and ensure your directions are accurate based on the given information. Mention each landmark in your directions. Submit your response as a plain text string in the following format:\n\nDirections: [Your directions here]\n\nDescription: {description}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The directions should be clear and follow the described spatial relationships.", "The route should be accurate based on the given description.", "All mentioned landmarks should be included in the directions."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
