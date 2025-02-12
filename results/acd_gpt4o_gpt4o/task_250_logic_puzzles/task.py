class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"puzzle": "Three people (A, B, and C) are wearing hats. Each person can see the other two hats but not their own. They are told that the hats are either red or blue and that at least one person is wearing a red hat. They are asked in turn if they know the color of their own hat. A says 'No,' B says 'No,' and then C says 'Yes.' What color is C's hat and how did C figure it out?"},
            "2": {"puzzle": "You have a 12-hour analog clock. When the time is 3:15, what is the angle between the hour and the minute hands?"}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following logic puzzle: {t['puzzle']}
Provide your solution in a single sentence explaining the answer and the reasoning behind it. For example, 'C's hat is red because...' or 'The angle is X degrees because...'."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['puzzle'] == "Three people (A, B, and C) are wearing hats. Each person can see the other two hats but not their own. They are told that the hats are either red or blue and that at least one person is wearing a red hat. They are asked in turn if they know the color of their own hat. A says 'No,' B says 'No,' and then C says 'Yes.' What color is C's hat and how did C figure it out?":
            criteria = ["The correct answer is 'C's hat is red because if A and B both say they don't know, then they must both be seeing at least one red hat on the others.'"]
        elif t['puzzle'] == "You have a 12-hour analog clock. When the time is 3:15, what is the angle between the hour and the minute hands?":
            criteria = ["The correct angle is 7.5 degrees because the minute hand is at 90 degrees (15 minutes) and the hour hand is at 97.5 degrees (3 hours and 15 minutes)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
