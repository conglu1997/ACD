class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"num_disks": 4},
            "2": {"num_disks": 5}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to solve the Tower of Hanoi puzzle for {t['num_disks']} disks. You need to move all the disks from the source peg to the destination peg using an auxiliary peg, following these rules:
1. Only one disk can be moved at a time.
2. A disk can only be placed on top of a larger disk or on an empty peg.
3. Provide a step-by-step explanation of each move you make.

Provide your solution in the following format:
Move 1: [Move disk X from Peg A to Peg B]
Move 2: [Move disk Y from Peg A to Peg C]
..."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution should follow the rules of the Tower of Hanoi puzzle.",
            "The explanation should clearly describe each move step-by-step in the specified format.",
            "The solution should correctly move all disks from the source peg to the destination peg following the rules."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
