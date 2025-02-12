class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "You are designing a garden with the following features: a rectangular lawn in the center (10m x 20m), a circular flower bed (radius 3m) at the northeast corner, a rectangular pond (5m x 10m) at the southwest corner, and a pathway (1m wide) connecting the flower bed to the pond. The garden has a boundary fence that is 30m x 30m. Ensure the pathway does not intersect the lawn.",
                "criteria": "Generate a detailed spatial layout of the garden based on the given description. Ensure that the layout is logically consistent and includes all specified features with appropriate dimensions and relative positioning."
            },
            "2": {
                "description": "You are arranging a living room with the following items: a sofa (2m x 0.8m) against the north wall, a coffee table (1m x 0.5m) in front of the sofa (0.5m distance), a TV stand (1.5m x 0.4m) against the south wall, and a bookshelf (0.8m x 1.8m) in the southeast corner. The room's dimensions are 5m x 4m. Ensure there is at least 1m of free space in the center of the room.",
                "criteria": "Generate a detailed spatial layout of the living room based on the given description. Ensure that the layout is logically consistent and includes all specified items with appropriate dimensions and relative positioning."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a textual description and are required to generate a corresponding spatial layout.\n\nDescription:\n{t['description']}\n\nTask:\n{t['criteria']}\n\nYour response should include a detailed spatial layout that is logically consistent and adheres to the given constraints. Submit your response as a plain text string with the following format:\n- Layout: [Your detailed description of the layout, including dimensions and relative positioning of each feature or item]\n\nExample format:\n- Layout: The garden has a rectangular lawn (10m x 20m) positioned in the center of a 30m x 30m boundary. A circular flower bed (radius 3m) is placed at the northeast corner, and a rectangular pond (5m x 10m) is positioned at the southwest corner. A 1m wide pathway connects the flower bed to the pond without intersecting the lawn."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The layout should be logically consistent.",
            "The layout should include all specified features or items with appropriate dimensions and relative positioning.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
