class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"num_disks": 3},
            "2": {"num_disks": 4}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a sequence of moves to solve the Tower of Hanoi puzzle with {t['num_disks']} disks. The puzzle starts with all disks on the first peg, and your goal is to move all disks to the third peg following these rules:
1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk or an empty peg.
3. You must not place a larger disk on top of a smaller disk.

Provide your solution as a list of moves, where each move is represented as a tuple (source_peg, destination_peg). For example, (1, 3) means moving the top disk from peg 1 to peg 3.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        import ast
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution must follow the rules of the Tower of Hanoi puzzle.", "The sequence of moves must successfully move all disks from the first peg to the third peg.", "The solution should be optimal in terms of the number of moves."]
        try:
            moves = ast.literal_eval(submission)
            if not isinstance(moves, list) or not all(isinstance(move, tuple) and len(move) == 2 and all(isinstance(peg, int) and 1 <= peg <= 3 for peg in move) for move in moves):
                return 0.0

            # Validate the moves according to the Tower of Hanoi rules
            pegs = {1: list(range(t['num_disks'], 0, -1)), 2: [], 3: []}
            for src, dst in moves:
                if not pegs[src] or (pegs[dst] and pegs[src][-1] > pegs[dst][-1]):
                    return 0.0
                pegs[dst].append(pegs[src].pop())
            if pegs[3] != list(range(t['num_disks'], 0, -1)):
                return 0.0
        except (ValueError, SyntaxError):
            return 0.0

        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
