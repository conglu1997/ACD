class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dialect": "Southern American English", "phrase": "I'm going to the store to buy some groceries."},
            "2": {"dialect": "British English (Cockney)", "phrase": "Can you pass me the salt, please?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dialect = t['dialect']
        phrase = t['phrase']
        return f"""Generate the following phrase in the specified dialect or accent:

Dialect: {dialect}
Phrase: {phrase}

Ensure that your response accurately reflects the linguistic characteristics and cultural nuances of the specified dialect or accent. Your submission should be a plain text string in the following format:

Dialect: {dialect}
Generated Phrase: [Your generated phrase]

Example:
Dialect: Southern American English
Phrase: I'm going to the store to buy some groceries.
Generated Phrase: Ah'm goin' to the store to buy some groceries."

Pay attention to phonetic changes, vocabulary differences, and any relevant cultural references. Make sure your generated phrase is coherent and culturally appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated phrase should accurately reflect the specified dialect or accent.",
            "The generated phrase should maintain the meaning of the original phrase.",
            "The generated phrase should incorporate phonetic changes, vocabulary differences, and cultural references relevant to the specified dialect.",
            "The generated phrase should be coherent and culturally appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
