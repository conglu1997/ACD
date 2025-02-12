class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"map": "A 10x10 grid map with landmarks A at (1,1), B at (1,10), C at (10,1), D at (10,10), E at (5,5), and F at (7,3)", "start": "A", "end": "D"},
            "2": {"map": "A city map with landmarks such as Central Park at (3,3), Lincoln School at (4,2), City Library at (2,4), Museum at (5,5), and Hospital at (6,6)", "landmark_query": "Identify the landmark located at the intersection of Main St. and 2nd Ave., which corresponds to (4,2)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "start" in t and "end" in t:
            return f"""Your task is to provide detailed directions from point {t['start']} to point {t['end']} on the following map:

{t['map']}

Ensure your directions are clear and accurate. Provide your response in plain text format. Your directions should include turns at specific intersections and distances between grid points. For example, 'Move 3 blocks north, then turn east and move 2 blocks.'"""
        elif "landmark_query" in t:
            return f"""Your task is to identify the landmark based on the query and the following map:

{t['map']}

Query: {t['landmark_query']}

Provide your response in plain text format. State the name of the landmark clearly. For example, 'The landmark is Lincoln School.'"""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly provide accurate directions including turns at specific intersections and distances between grid points.",
            "The response should correctly identify the landmark based on the query."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
