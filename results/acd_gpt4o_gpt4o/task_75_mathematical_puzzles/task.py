class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"puzzle": "What number comes next in the sequence: 2, 6, 12, 20, 30, ?"},
            "2": {"puzzle": "You have a 3-liter jug and a 5-liter jug, and you need to measure exactly 4 liters of water. How do you do it?"}
        }
        assert len(tasks) == 2, "There should be exactly two tasks."
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following mathematical puzzle: {t['puzzle']}
Provide your solution in a single sentence. For example, 'The next number is 42.' or 'Fill the 3-liter jug, then pour its contents into the 5-liter jug.'"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['puzzle'] == "What number comes next in the sequence: 2, 6, 12, 20, 30, ?":
            criteria = ["The correct answer is 42."]
        elif t['puzzle'] == "You have a 3-liter jug and a 5-liter jug, and you need to measure exactly 4 liters of water. How do you do it?":
            criteria = [
                "The correct method involves the following steps:",
                "1. Fill the 3-liter jug.",
                "2. Pour the 3 liters into the 5-liter jug.",
                "3. Fill the 3-liter jug again.",
                "4. Pour 2 liters into the 5-liter jug to fill it, leaving exactly 1 liter in the 3-liter jug.",
                "5. Empty the 5-liter jug.",
                "6. Pour the remaining 1 liter from the 3-liter jug into the 5-liter jug.",
                "7. Fill the 3-liter jug again.",
                "8. Pour the 3 liters into the 5-liter jug, resulting in exactly 4 liters in the 5-liter jug."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
