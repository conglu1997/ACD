class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "pairs": [
                    ["sun", "moon"],
                    ["wise", "foolish"],
                    ["leader", "follower"],
                    ["victory", "defeat"]
                ]
            },
            "2": {
                "pairs": [
                    ["fire", "ice"],
                    ["strong", "weak"],
                    ["truth", "lie"],
                    ["hope", "despair"]
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate analogies based on the given pairs of concepts. For each pair, create a sentence that demonstrates the relationship between the two concepts.

Pairs:
1. {t['pairs'][0][0]} and {t['pairs'][0][1]}
2. {t['pairs'][1][0]} and {t['pairs'][1][1]}
3. {t['pairs'][2][0]} and {t['pairs'][2][1]}
4. {t['pairs'][3][0]} and {t['pairs'][3][1]}

Ensure that each analogy is clear, logical, and creatively illustrates the relationship between the concepts. Submit your analogies as a plain text string in the following format:

1. [Analogy for the first pair]
2. [Analogy for the second pair]
3. [Analogy for the third pair]
4. [Analogy for the fourth pair]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The analogies should clearly illustrate the relationship between the given pairs of concepts.",
            "The analogies should be logical and creative.",
            "Each analogy should correspond correctly to the given pairs of concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
