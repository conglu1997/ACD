class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"sentence": "The quick brown fox jumps over the lazy dog."},
            "2": {"sentence": "She sells seashells by the seashore."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a set of vocabulary and basic grammar rules for a fictional language. Then, use the created language to translate the following sentence:

Sentence: {t['sentence']}

Your response should include:
1. A list of at least 10 vocabulary words in the fictional language with their English translations. Format: [Fictional Word] = [English Translation]
2. A description of basic grammar rules (e.g., sentence structure, verb conjugation).
3. The translation of the given sentence using the fictional language.

Provide your response in plain text format as follows:

Vocabulary:
- [Fictional Word] = [English Translation]
...

Grammar Rules:
[Description of basic grammar rules]

Translation:
[Translation of the given sentence]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include at least 10 vocabulary words in the fictional language with their English translations.",
            "The response should include a description of basic grammar rules.",
            "The translation of the given sentence should adhere to the created vocabulary and grammar rules."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
