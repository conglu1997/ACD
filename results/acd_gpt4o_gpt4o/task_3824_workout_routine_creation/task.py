class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "goal": "Build muscle",
                "constraints": "30 minutes per day, 3 days a week",
                "equipment": "Dumbbells, resistance bands"
            },
            "2": {
                "goal": "Improve cardiovascular fitness",
                "constraints": "45 minutes per day, 5 days a week",
                "equipment": "Treadmill, jump rope"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to create a workout routine based on the following parameters:\n\nGoal: {t['goal']}\nConstraints: {t['constraints']}\nEquipment: {t['equipment']}\n\nYour workout routine should include the following elements:\n1. A warm-up routine\n2. Detailed exercises for the main workout, including sets, reps, and rest intervals\n3. A cool-down routine\n4. Any necessary modifications to accommodate the constraints\n5. Justification for how the routine meets the specified goal\n\nProvide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The routine includes a warm-up.",
            "The routine includes detailed exercises for the main workout with sets, reps, and rest intervals.",
            "The routine includes a cool-down.",
            "The routine accommodates the specified constraints.",
            "The routine justifies how it meets the specified goal."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
