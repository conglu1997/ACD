class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Generate the next five numbers in the following sequence: 2, 4, 8, 16, ...", "criteria": ["The generated numbers should correctly follow the pattern of the given sequence."]},
            "2": {"task": "Identify the rule governing the following sequence and provide the next number: 3, 6, 11, 18, 27, ...", "sequence": "3, 6, 11, 18, 27, ...", "criteria": ["The identified rule should correctly explain the pattern of the given sequence.", "The next number should be correctly derived based on the identified rule."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "sequence" in t:
            instructions = f"""Your task is to identify the rule governing the following sequence and provide the next number:\n\n{t['sequence']}\n\nProvide your response in the following format:\n\nRule: [Identified rule]\nNext Number: [Next number]"""
        else:
            instructions = f"""Your task is to generate the next five numbers in the following sequence:\n\n2, 4, 8, 16, ...\n\nEnsure that the generated numbers correctly follow the pattern of the given sequence. Provide your response in the following format:\n\nNext Numbers: [Next five numbers]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = t.get("criteria", [])
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
