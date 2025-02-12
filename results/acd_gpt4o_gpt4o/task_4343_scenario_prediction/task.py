class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A small town is experiencing an unusually harsh winter. The town relies on a single road for supplies, which is now blocked by heavy snowfall. The residents have enough food for one more week, and the nearest help is two weeks away. Predict the outcome based on the available information and provide a detailed explanation.",
                "variables": ["harsh winter", "blocked road", "one week of food", "help two weeks away"]
            },
            "2": {
                "scenario": "A tech company is launching a new product. The product has received mixed reviews during beta testing, but the company has invested heavily in its marketing campaign. Predict the outcome of the product launch and provide a detailed explanation.",
                "variables": ["new product", "mixed reviews", "heavy marketing investment"]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        variables = ", ".join(t["variables"])
        instructions = f"""Your task is to read the given scenario and predict the outcome based on the provided variables.\n\nScenario: {scenario}\n\nVariables: {variables}\n\nYour prediction should include:\n1. A logical and coherent outcome based on the scenario and variables.\n2. A detailed explanation of how you arrived at this outcome.\n\nEnsure that your response is between 200 and 400 words long, clearly outlines your reasoning, and considers all the provided variables. Provide your response in plain text format.\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a logical and coherent outcome based on the scenario and variables.",
            "The response provides a detailed explanation of how the outcome was determined.",
            "The response is between 200 and 400 words long.",
            "The response clearly outlines the reasoning and considers all the provided variables."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
