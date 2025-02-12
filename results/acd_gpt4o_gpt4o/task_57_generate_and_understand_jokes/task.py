class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Why did the scarecrow win an award?"},
            "2": {"joke": "Parallel lines have so much in common. It’s a shame they’ll never meet."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "prompt" in t:
            instructions = f"""Your task is to generate a joke based on the following prompt:

{t['prompt']}

Ensure that the joke is funny, coherent, and appropriate. The joke should be original and reflect a good understanding of humor. Consider aspects such as wordplay, puns, and cultural references that make jokes humorous. Provide your response in plain text format."""
        else:
            instructions = f"""Your task is to explain the humor behind the following joke:

{t['joke']}

Ensure that your explanation is clear, detailed, and demonstrates an understanding of why the joke is funny. Your explanation should cover the play on words, cultural context, or any other relevant aspect of the joke. Provide your response in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "prompt" in t:
            criteria = [
                "The joke should be funny and coherent.",
                "The joke should be original.",
                "The joke should be appropriate.",
                "The joke should reflect a good understanding of humor, including wordplay, puns, or cultural references."
            ]
        else:
            criteria = [
                "The explanation should demonstrate an understanding of why the joke is funny.",
                "The explanation should cover the play on words, cultural context, or any other relevant aspect of the joke."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
