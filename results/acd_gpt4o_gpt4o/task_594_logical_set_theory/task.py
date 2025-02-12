class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task": "relationship",
                "sets": [
                    {"A": [1, 2, 3], "B": [2, 3, 4]},
                    {"A": [5, 6, 7], "B": [7, 8, 9]}
                ]
            },
            "2": {
                "task": "operation",
                "sets": [
                    {"A": [1, 2, 3], "B": [3, 4, 5]},
                    {"A": [10, 20, 30], "B": [20, 30, 40]}
                ],
                "operation": "union"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "relationship":
            sets = t['sets'][0]
            return (
                f"Your task is to determine the relationship between the given sets.\n"
                f"Set A: {sets['A']}\n"
                f"Set B: {sets['B']}\n"
                "Provide a detailed explanation of whether A is a subset of B, B is a subset of A, A and B are equal, or they are disjoint."
            )
        elif t["task"] == "operation":
            sets = t['sets'][0]
            return (
                f"Your task is to perform the specified set operation on the given sets.\n"
                f"Set A: {sets['A']}\n"
                f"Set B: {sets['B']}\n"
                f"Operation: {t['operation']}\n"
                "Provide the resulting set after performing the operation."
            )

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t["task"] == "relationship":
            criteria = [
                "The response should accurately determine the relationship between the sets.",
                "The explanation should be clear and logically sound."
            ]
        elif t["task"] == "operation":
            criteria = [
                "The resulting set should be correct based on the specified operation.",
                "The response should clearly show the correct elements in the resulting set."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
