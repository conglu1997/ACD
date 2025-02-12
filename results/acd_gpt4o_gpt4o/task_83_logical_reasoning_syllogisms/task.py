class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"syllogism": "All mammals are animals. All humans are mammals. Therefore, all humans are animals."},
            "2": {"logical_statement": "If a person is a teacher, then they have students. Alice is a teacher. Therefore, Alice has students."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'syllogism' in t:
            return f"""Your task is to interpret the following logical syllogism and determine if the conclusion is logically valid based on the premises. Provide a justification for your answer in the following format:

Validity: [Valid/Invalid]
Justification: [Your justification]

Syllogism: {t['syllogism']}"""
        elif 'logical_statement' in t:
            return f"""Your task is to interpret the following logical statement and determine if the conclusion is logically valid based on the premises. Provide a justification for your answer in the following format:

Validity: [Valid/Invalid]
Justification: [Your justification]

Statement: {t['logical_statement']}"""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly determine the logical validity of the given syllogism or statement.",
            "The response should include a justification for the validity determination.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
