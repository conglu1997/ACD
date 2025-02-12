class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"map": "A-B-C-D-E-F\n| | | | \nG-H-I-J-K-L", "requirements": "Start at A, visit C, H, and E, and end at F."},
            "2": {"map": "1-2-3-4-5-6\n| | | | \n7-8-9-10-11-12", "requirements": "Start at 1, visit 3, 8, and 5, and end at 6."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to plan and describe a route through the following map based on the requirements given:

Map: {t['map']}
Requirements: {t['requirements']}

Your route description should be clear, follow the given requirements, and be in the following format:

Route: [Your planned route]. For example, a valid route might look like this: A -> B -> C -> D -> E."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        # Define criteria for evaluation
        criteria = [
            "The route should start at the specified starting point.",
            "The route should visit all specified points in the correct order.",
            "The route should end at the specified ending point.",
            "The route description should be clear and follow the given requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
