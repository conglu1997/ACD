class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "map": "A-B-C-D\nE-F-G-H\nI-J-K-L\nM-N-O-P",
                "start": "A",
                "end": "P",
                "obstacles": ["C", "J"]
            },
            "2": {
                "map": "1-2-3-4\n5-6-7-8\n9-10-11-12\n13-14-15-16",
                "start": "1",
                "end": "16",
                "obstacles": ["7", "10"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        obstacles = ', '.join(t['obstacles'])
        return f"""Interpret the following map and generate step-by-step navigation directions to move from the starting point to the destination while avoiding obstacles:

Map:
{t['map']}

Starting Point: {t['start']}
Destination: {t['end']}
Obstacles: {obstacles}

Your directions should be clear and concise, specifying each step required to navigate from the starting point to the destination while avoiding the obstacles. Use directions such as 'up', 'down', 'left', 'right'. Ensure that your instructions are accurate, logically coherent, and avoid all obstacles. Submit your response as a plain text string in the following format:

Directions: [Your step-by-step directions]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The directions should accurately navigate from the starting point to the destination while avoiding obstacles.", "The directions should use clear and concise language such as 'up', 'down', 'left', 'right'."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
