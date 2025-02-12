class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "goals": "increase muscle mass",
                "constraints": "no gym equipment, 30 minutes per day, suitable for beginners",
                "instruction": "Create a fitness routine that helps to increase muscle mass with the constraints of no gym equipment, a maximum of 30 minutes per day, and suitable for beginners. The routine should include a list of exercises, the number of sets and repetitions, and a brief description of each exercise. Format your response as follows: \nExercise 1: [name] - [sets] sets of [reps] reps\nDescription: [description]\nExercise 2: ..."
            },
            "2": {
                "goals": "improve cardiovascular health",
                "constraints": "indoor exercises, 45 minutes per session, 3 times a week, suitable for intermediate level",
                "instruction": "Design a fitness routine aimed at improving cardiovascular health, with the constraints of indoor exercises, 45 minutes per session, 3 times a week, and suitable for intermediate level. The routine should detail each session with a list of exercises, duration, and a brief description of each exercise. Format your response as follows: \nSession 1: \nExercise 1: [name] - [duration] minutes\nDescription: [description]\nExercise 2: ... \nSession 2: ..."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a fitness routine aimed at the following goals with the given constraints:\n\nGoals: {t['goals']}\nConstraints: {t['constraints']}\n\nInstructions: {t['instruction']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The routine should align with the specified fitness goals.",
            "The routine should adhere to the given constraints.",
            "The exercises should be appropriate and varied.",
            "The routine should be detailed and practically implementable.",
            "The format should follow the specified structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
