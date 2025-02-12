class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premises": ["All mammals are warm-blooded.", "All whales are mammals."]},
            "2": {"syllogism": ["All dogs are mammals.", "All cats are mammals.", "Therefore, all dogs are cats."], "is_valid": "False"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'premises' in t:
            return f"Your task is to generate a valid conclusion from the given premises. Here are the premises:\n{t['premises'][0]}\n{t['premises'][1]}\nPlease provide the conclusion in one sentence."
        elif 'syllogism' in t:
            return f"Your task is to assess the validity of the given syllogism. Here are the syllogism's premises and conclusion:\nPremises:\n{t['syllogism'][0]}\n{t['syllogism'][1]}\nConclusion:\n{t['syllogism'][2]}\nPlease respond with 'Valid' or 'Invalid' based on the logic of the syllogism."
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'premises' in t:
            criteria = ["The conclusion should logically follow from the given premises."]
        elif 'syllogism' in t:
            criteria = ["The assessment should correctly determine the validity of the syllogism.", "The response should be either 'Valid' or 'Invalid'."]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
