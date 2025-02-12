class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "constraints": "Design a 5x5 maze where the start is at the top-left corner ('S') and the end is at the bottom-right corner ('E'). Ensure there is only one unique solution path from start to end, and include at least 3 dead ends.",
                "maze": "S####\n#...#\n#.#.#\n#...#\n###E#"
            },
            "2": {
                "constraints": "Design a 7x7 maze where the start is at the top-left corner ('S') and the end is at the bottom-right corner ('E'). Ensure there is only one unique solution path from start to end, and include at least 5 dead ends.",
                "maze": "S######\n#.....#\n#.###.#\n#.#.#.#\n#.#.#.#\n#...#.#\n######E"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following tasks based on the given constraints and maze:

Constraints:
{t['constraints']}

Your task is to:
1. Design a maze based on the given constraints. Represent the maze using a grid of characters, where '#' represents a wall, '.' represents an open path, 'S' represents the start, and 'E' represents the end.
2. Solve the provided maze and describe the solution path from start 'S' to end 'E'. Use 'U' for up, 'D' for down, 'L' for left, and 'R' for right.

Submit your response as a plain text string in the following format:
- Maze Design: [Your maze design here]
- Solution Path: [Your solution path here]

Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of the spatial and logical constraints provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The maze design should adhere to the given constraints.",
            "The solution path should accurately navigate from start 'S' to end 'E' using the provided maze.",
            "The response should be well-structured, coherent, and demonstrate a deep understanding of the spatial and logical constraints provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
