class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "start": "City A",
                "end": "City B",
                "constraints": {
                    "distance": "minimize",
                    "time": "within 5 hours",
                    "cost": "under $50"
                },
                "options": [
                    {"route": "A -> C -> B", "distance": 100, "time": 4, "cost": 45},
                    {"route": "A -> D -> B", "distance": 120, "time": 3, "cost": 55},
                    {"route": "A -> E -> B", "distance": 110, "time": 5, "cost": 50}
                ]
            },
            "2": {
                "start": "City X",
                "end": "City Y",
                "constraints": {
                    "distance": "within 200 miles",
                    "time": "minimize",
                    "cost": "under $100"
                },
                "options": [
                    {"route": "X -> Z -> Y", "distance": 180, "time": 2, "cost": 95},
                    {"route": "X -> W -> Y", "distance": 150, "time": 3, "cost": 85},
                    {"route": "X -> V -> Y", "distance": 200, "time": 1.5, "cost": 105}
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        constraints = t['constraints']
        options = "\n".join([f"Route: {opt['route']}, Distance: {opt['distance']} miles, Time: {opt['time']} hours, Cost: ${opt['cost']}" for opt in t['options']])
        return f"Plan an optimal route for travel from {t['start']} to {t['end']} based on the given constraints:\n\nConstraints:\n- Distance: {constraints['distance']}\n- Time: {constraints['time']}\n- Cost: {constraints['cost']}\n\nAvailable options:\n{options}\n\nChoose the best option that meets the constraints and explain your choice in detail. Your explanation should justify why the chosen route is optimal considering all the constraints. Submit your response as a plain text string."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The chosen route should meet the given constraints.", "The explanation should justify the choice logically and in detail."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
