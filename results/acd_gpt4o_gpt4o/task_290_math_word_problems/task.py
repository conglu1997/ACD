class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "prompt": "Generate a word problem involving the calculation of compound interest for a savings account over a period of time."
            },
            "2": {
                "problem": "John has $1000 in his savings account, which earns 5% interest per year, compounded annually. How much money will he have in the account after 3 years? Provide the steps and calculations in your solution."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to generate a mathematical word problem based on the following prompt:\n\n{t['prompt']}\n\nEnsure that the problem is clear, contextually appropriate, and involves the calculation of compound interest. Provide the word problem in plain text format. The problem should be challenging enough to test a range of mathematical skills."""
        else:
            instructions = f"""Your task is to solve the following mathematical word problem:\n\n{t['problem']}\n\nProvide your solution in plain text format, including the final amount in the account and the steps taken to arrive at it. Ensure that your explanation is clear and logically structured."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The word problem should clearly describe a scenario involving compound interest.",
                "The problem should be contextually appropriate and involve realistic values.",
                "The problem should require the calculation of compound interest.",
                "The problem should be challenging and test multiple mathematical skills."
            ]
        else:
            criteria = [
                "The solution should correctly calculate the compound interest.",
                "The solution should include the final amount in the account and the steps taken to arrive at it.",
                "The solution should be clear and logically structured.",
                "The explanation should be comprehensive and free from errors."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
