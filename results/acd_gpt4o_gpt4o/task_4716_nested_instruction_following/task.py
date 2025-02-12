class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"instructions": "Step 1: Write the word 'apple'. Step 2: Reverse the word you wrote in Step 1 and write it down. Step 3: Take the result from Step 2 and replace each vowel with the next vowel in the sequence 'a, e, i, o, u'. Write down the final result."},
            "2": {"instructions": "Step 1: Write the word 'banana'. Step 2: Replace each 'a' in the word with 'o' and write it down. Step 3: Take the result from Step 2 and reverse it. Write down the final result."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = t["instructions"]
        return f"Your task is to follow the series of steps provided and give the final result.\n\nInstructions: {instructions}\n\nProvide your final result in plain text format: 'Final result: <result>'\n\nExample format: 'Final result: elppi'"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The final result should be the correct output after following all steps.", "The intermediate steps must be followed exactly as described.", "The result should be provided in the format 'Final result: <result>'"]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
