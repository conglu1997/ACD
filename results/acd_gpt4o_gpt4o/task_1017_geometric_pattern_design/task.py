class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"description": "Create a geometric pattern using only circles and triangles. The pattern should be symmetric along at least one axis and should not exceed a 5x5 grid.", "criteria": "Symmetric pattern, uses only circles and triangles, fits within a 5x5 grid."},
            "2": {"description": "Describe a geometric pattern that uses squares and hexagons in an alternating fashion. The pattern should form a repeating sequence and should not exceed a 4x4 grid.", "criteria": "Alternating squares and hexagons, forming a repeating sequence, fits within a 4x4 grid."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create or describe a geometric pattern based on the following criteria:\n\n{t['description']}\n\nEnsure your pattern adheres to the specified criteria and provide a clear and detailed response. Format your response as follows:\n\nPattern: [Your pattern description or creation]\nExplanation: [Your detailed explanation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t['criteria'].split(', ')
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
