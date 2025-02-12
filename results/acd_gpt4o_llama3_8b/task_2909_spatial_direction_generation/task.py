class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "starting_point": "Library",
                "destination": "Cafeteria",
                "map_description": "The library is located on the north side of the campus. To the east of the library is the Science Building. South of the Science Building is the Administration Building. The Cafeteria is directly south of the Library. There is a small garden between the Library and the Cafeteria."
            },
            "2": {
                "starting_point": "Main Entrance",
                "destination": "Gymnasium",
                "map_description": "The Main Entrance is at the center of the park. To the west of the Main Entrance is a Playground. North of the Playground is the Gymnasium. East of the Gymnasium is the Swimming Pool. There is a statue between the Main Entrance and the Playground."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate clear and coherent written directions from the starting point to the destination based on the given map description.

Starting Point: {t['starting_point']}
Destination: {t['destination']}
Map Description: {t['map_description']}

Format your response as follows:
Directions: [Your directions here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The directions should accurately guide from the starting point to the destination.",
            "The directions should be clear and coherent."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
