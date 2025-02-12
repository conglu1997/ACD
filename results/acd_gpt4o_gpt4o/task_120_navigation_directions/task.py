class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"start": "Central Park, New York", "end": "Times Square, New York"},
            "2": {"directions": "Start at the Eiffel Tower. Head northeast on Avenue Gustave Eiffel. Turn right onto Quai Branly. Continue straight until you reach the intersection with Rue de l'Université. Your destination will be on the right."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "start" in t and "end" in t:
            return f"Generate step-by-step walking directions from {t['start']} to {t['end']}. Ensure the directions are clear and easy to follow."
        elif "directions" in t:
            return f"Based on the following directions, identify the final destination: '{t['directions']}'. Provide the name of the location in plain text."
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "start" in t and "end" in t:
            criteria = [
                "The directions should be clear and easy to follow.",
                "The directions should logically connect the start and end locations.",
                "The directions should use appropriate street names and landmarks."
            ]
        elif "directions" in t:
            criteria = [
                "The identified destination should match the end location implied by the given directions.",
                "The response should be in plain text format."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
