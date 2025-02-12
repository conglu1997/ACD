class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"puzzle": "You have four cards on the table. Each card has a letter on one side and a number on the other side. The visible faces of the cards are: 'A', '4', 'D', '7'. Which cards must you turn over to test the rule: 'If a card has a vowel on one side, then it has an even number on the other side'?"},
            "2": {"puzzle": "In a certain town, there are three houses in a row, each painted a different color: red, blue, and green. People of three different professions live in these houses: a teacher, a doctor, and an artist. The following facts are known: 1) The teacher lives in the red house. 2) The doctor does not live in the blue house. 3) The artist lives next to the green house. Determine the color of the house each person lives in."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Solve the following logical puzzle:\n\n{t['puzzle']}\n\nProvide your answer with a clear explanation of your reasoning. Submit your response as a plain text string in the format: 'Answer: [Your answer] Reasoning: [Your reasoning]'."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if t['puzzle'].startswith('You have four cards'):
            criteria = ['The answer should indicate which cards to turn over to test the rule that a vowel on one side implies an even number on the other side.']
        else:
            criteria = ['The answer should correctly identify the color of the house each person lives in based on the given constraints.']
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
