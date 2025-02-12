class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idioms": ["a blessing in disguise", "bite the bullet", "break the ice"]},
            "2": {"idioms": ["let the cat out of the bag", "hit the nail on the head", "burn the midnight oil"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        idioms = ", ".join(t["idioms"])
        return f"""Generate a sentence for each of the following idiomatic expressions. Ensure that each sentence demonstrates a correct understanding of the idiom's meaning and is used in an appropriate context.

Idioms: {idioms}

Submit your sentences in the following format:
- [Idiom 1]: [Generated sentence]
- [Idiom 2]: [Generated sentence]
- [Idiom 3]: [Generated sentence]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "Each generated sentence must demonstrate a correct understanding of the idiom's meaning.",
            "Each idiom must be used in an appropriate context within the sentence.",
            "The sentences must be grammatically correct and coherent.",
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
