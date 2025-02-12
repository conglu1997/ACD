import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        patterns = [
            {
                'description': 'A 5x5 grid where cells alternate between X and O in a checkerboard pattern, starting with X in the top-left corner.',
                'visual': 'XOXOX\nOXOXO\nXOXOX\nOXOXO\nXOXOX'
            },
            {
                'description': 'A 6x6 grid forming a spiral pattern starting from the center, using numbers 1-18 in sequence, with the remaining cells filled with 0.',
                'visual': '000000\n004321\n005000\n006000\n007000\n876543'
            },
            {
                'description': 'A 7x7 grid where the diagonal from top-left to bottom-right is filled with *, the cells above this diagonal are filled with ^, and the cells below are filled with v.',
                'visual': '*^^^^^^\nv*^^^^^\nvv*^^^^\nvvv*^^^\nvvvv*^^\nvvvvv*^\nvvvvvv*'
            },
            {
                'description': 'A 6x6 grid representing a maze, where # represents walls and . represents paths. The maze has an entrance at the top-left and an exit at the bottom-right.',
                'visual': '.####.\n.#....\n.#.##.\n.#.#..\n.#.#.#\n...#..'
            },
            {
                'description': 'An 8x8 grid representing a chessboard. Use B for black squares, W for white squares, and place chess pieces using standard notation (K for king, Q for queen, R for rook, B for bishop, N for knight, P for pawn) on their starting positions for white pieces only.',
                'visual': 'BRBWBQBK\nWPWPWPWP\nBWBWBWBW\nWBWBWBWB\nBWBWBWBW\nWBWBWBWB\nBPBPBPBP\nWRWNWBWQ'
            }
        ]
        tasks = {}
        for i in range(2):
            task = random.choice(patterns)
            direction = random.choice(['encode', 'decode'])
            tasks[str(i+1)] = {
                'pattern': task,
                'direction': direction
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['direction'] == 'encode':
            return f"""Given the following description of a visual pattern:

{t['pattern']['description']}

Create the corresponding visual representation using ASCII characters. Your output must match the description exactly and be properly formatted.

Your response should consist only of the ASCII representation of the pattern, with no additional explanation. Each row of the pattern should be on a new line. Ensure precise adherence to the described pattern, including any specific characters or symbols mentioned."""
        else:
            return f"""Given the following visual pattern:

{t['pattern']['visual']}

Provide a clear, concise, and precise description of the pattern. Your description must be detailed enough that someone could recreate the visual pattern accurately based solely on your instructions.

Your response should consist only of the description, with no additional explanation. Begin your description with 'A [size] grid where...' and provide step-by-step instructions for creating the pattern. Include all relevant details about the characters used, their positions, and any patterns or rules they follow."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['direction'] == 'encode':
            criteria = [f"The submission exactly matches the expected visual pattern: {t['pattern']['visual']}",
                        "The submission contains only the ASCII representation with no additional text.",
                        "Each row of the pattern is on a new line.",
                        "All characters and symbols are correctly placed according to the description."]
        else:
            criteria = [f"The description accurately and completely captures the visual pattern: {t['pattern']['visual']}",
                        "The description is clear, concise, and detailed enough to allow exact recreation of the pattern.",
                        "The description begins with 'A [size] grid where...' and provides step-by-step instructions.",
                        "All characters, symbols, and their positions are precisely described.",
                        "Any patterns or rules governing the arrangement are clearly explained.",
                        "The submission contains only the description with no additional text."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
