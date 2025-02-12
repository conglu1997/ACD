class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "interpretation", "analogy": "Bird is to Sky as Fish is to Water."},
            "2": {"type": "generation", "pair1": "Pen", "pair2": "Paper"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['type'] == 'interpretation':
            return f"""Your task is to interpret the given analogy and explain the relationship between the pairs of words.

Analogy: {t['analogy']}

Your response should include:
1. A clear explanation of the relationship between the first pair of words.
2. A clear explanation of the relationship between the second pair of words.
3. How the two relationships are analogous to each other.

Provide your response in plain text format.

Example:
Analogy: Cat is to Fur as Bird is to Feather.
1. A cat has fur covering its body.
2. A bird has feathers covering its body.
3. Just as fur is a covering for a cat, feathers are a covering for a bird."""
        elif t['type'] == 'generation':
            return f"""Your task is to generate an analogy based on the given pairs of words.

Pair 1: {t['pair1']}
Pair 2: {t['pair2']}

Your response should include:
1. A new pair of words that have a similar relationship to Pair 1.
2. A new pair of words that have a similar relationship to Pair 2.
3. An explanation of how the relationships in your generated pairs are analogous to the provided pairs.

Provide your response in plain text format.

Example:
Pair 1: Key is to Lock
Pair 2: Brush is to Paint
1. Password is to Safe
2. Pen is to Ink
3. Just as a key opens a lock, a password opens a safe. Just as a brush is used for applying paint, a pen is used for applying ink."""
        else:
            raise ValueError("Unknown task type.")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['type'] == 'interpretation':
            criteria = [
                "The explanation of the relationship between the first pair of words should be accurate.",
                "The explanation of the relationship between the second pair of words should be accurate.",
                "The explanation should correctly describe how the two relationships are analogous to each other."
            ]
        elif t['type'] == 'generation':
            criteria = [
                "The generated pair of words for Pair 1 should have a similar relationship to the provided Pair 1.",
                "The generated pair of words for Pair 2 should have a similar relationship to the provided Pair 2.",
                "The explanation should correctly describe how the relationships in the generated pairs are analogous to the provided pairs."
            ]
        else:
            raise ValueError("Unknown task type.")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
