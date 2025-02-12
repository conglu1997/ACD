import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        grammatical_features = [
            "time-independent verbs",
            "color-based noun classes",
            "emotional state indicators",
            "perspective-shifting pronouns",
            "probabilistic tense markers"
        ]
        return {
            "1": {"feature": random.choice(grammatical_features)},
            "2": {"feature": random.choice(grammatical_features)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) with the unique grammatical feature of {t['feature']}. Your task has four parts:

1. Language Design (250-300 words):
   a) Explain how the grammatical feature works in your conlang.
   b) Provide 5-7 example words or phrases that demonstrate this feature.
   c) Describe one other notable aspect of your conlang's grammar or phonology.

2. Translation (100-150 words):
   Translate the following English sentence into your conlang, and explain how your unique grammatical feature affects the translation:
   "The scientist believed that the experiment would change our understanding of the universe."

3. Sapir-Whorf Analysis (200-250 words):
   Analyze how your conlang's unique feature might influence the thought patterns and worldview of its speakers. Consider:
   a) How might it affect their perception of reality?
   b) What concepts might be easier or more difficult to express in this language?
   c) How might it impact the culture and society of its speakers?

4. Practical Implications (150-200 words):
   Discuss potential real-world applications or implications of your conlang:
   a) How might it be useful in fields like psychology, anthropology, or artificial intelligence?
   b) What challenges might arise in teaching or learning this language?
   c) How could it contribute to our understanding of the relationship between language and thought?

Ensure your response demonstrates a deep understanding of linguistic concepts, creative language design, and analytical reasoning about the connections between language, thought, and culture."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design clearly incorporates the grammatical feature of {t['feature']}.",
            "The language design is creative, coherent, and linguistically plausible.",
            "The translation and explanation demonstrate a consistent application of the conlang's rules.",
            "The Sapir-Whorf analysis shows insightful reasoning about the potential cognitive and cultural impacts of the language feature.",
            "The discussion of practical implications is thoughtful and considers multiple disciplines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
