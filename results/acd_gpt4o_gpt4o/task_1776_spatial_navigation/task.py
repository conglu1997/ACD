class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {
                'map': 'A - B - C\n|   |   |\nD - E - F\n|   |   |\nG - H - I',
                'start': 'A',
                'end': 'I'
            },
            '2': {
                'map': 'A - B - C - D\n|       |   |\nE - F - G - H\n|       |   |\nI - J - K - L',
                'start': 'A',
                'end': 'L'
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return (
            'Given the following map, your task is to provide the shortest path from the start point to the end point. '
            'The map is represented as a grid with nodes connected by edges. Each node is represented by a letter. '
            'You can move horizontally or vertically between connected nodes. Provide the path as a sequence of nodes.\n\n'
            f'Map:\n{t["map"]}\n'
            f'Start point: {t["start"]}\n'
            f'End point: {t["end"]}\n\n'
            'Response format: [Node1 -> Node2 -> ... -> NodeN]'
        )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ['The path should be the shortest path from the start point to the end point.',
                    'The path should be represented as a sequence of nodes in the format [Node1 -> Node2 -> ... -> NodeN].']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
