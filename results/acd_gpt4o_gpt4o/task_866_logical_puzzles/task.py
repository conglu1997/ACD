class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "Three people need to cross a river using a boat that can only carry one person at a time. Each person has a different crossing time: 1 minute, 2 minutes, and 5 minutes. If two people cross together, they must go at the slower person's pace. What is the minimum time required for all three to cross the river?", "type": "river_crossing"},
            "2": {"puzzle": "You are on an island where one type of person always tells the truth and another type always lies. You meet two people: A and B. A says, 'We are both truth-tellers.' B says, 'A is a liar.' Who is telling the truth?", "type": "truth_teller_liar"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following logical puzzle. Carefully analyze the details and provide a clear and logical solution.

Puzzle: {t['puzzle']}

Provide your solution in the following format:

Solution: [Your detailed solution explaining the reasoning and steps to reach the answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'river_crossing':
            criteria = ["The solution should identify the correct minimum time for all three people to cross the river."]
        elif t['type'] == 'truth_teller_liar':
            criteria = ["The solution should correctly identify who is telling the truth and who is lying."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
