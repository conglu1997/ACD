class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "puzzle": "Three friends, Alice, Bob, and Charlie, each have a different favorite fruit: apple, banana, and cherry. Based on the following clues, determine which fruit is each person's favorite:\n1. Alice does not like apples.\n2. Bob likes neither bananas nor cherries.\n3. Charlie's favorite fruit is not cherries.",
                "solution": {"Alice": "cherry", "Bob": "apple", "Charlie": "banana"}
            },
            "2": {
                "puzzle": "Four children, Emily, Frank, Grace, and Henry, each have a different favorite color: red, blue, green, and yellow. Based on the following clues, determine each child's favorite color:\n1. Emily's favorite color is not green.\n2. Frank's favorite color is blue.\n3. Grace's favorite color is neither red nor yellow.\n4. Henry's favorite color is green.",
                "solution": {"Emily": "yellow", "Frank": "blue", "Grace": "green", "Henry": "red"}
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to solve the following logical deduction puzzle based on the provided clues. Determine the correct answer based on logical reasoning and provide your solution in the format: Person: Favorite Fruit/Color.\n\nPuzzle: {t['puzzle']}\n\nProvide your solution in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The solution should match the logical deductions based on the given clues.", "The solution should be correct and complete."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
