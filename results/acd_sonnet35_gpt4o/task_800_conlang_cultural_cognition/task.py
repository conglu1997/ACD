import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'culture_type': 'Collectivist, harmony-focused society',
                'cognitive_emphasis': 'Holistic thinking and contextual reasoning',
                'linguistic_feature': 'Evidentiality markers'
            },
            {
                'culture_type': 'Individualistic, achievement-oriented society',
                'cognitive_emphasis': 'Analytical thinking and categorical reasoning',
                'linguistic_feature': 'Tense-aspect system'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) that reflects the values and cognitive framework of a {t['culture_type']} with an emphasis on {t['cognitive_emphasis']}. Your conlang should prominently feature a {t['linguistic_feature']} system.

1. Conlang Design (250-300 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how the {t['linguistic_feature']} system works in your conlang.
   c) Provide 3-4 example sentences in your conlang with English translations.

2. Cultural and Cognitive Analysis (200-250 words):
   a) Explain how your conlang reflects the values of a {t['culture_type']}.
   b) Discuss how the language's structure supports {t['cognitive_emphasis']}.
   c) Analyze how the {t['linguistic_feature']} system interacts with the culture's worldview.

3. Sapir-Whorf Hypothesis Discussion (150-200 words):
   a) Briefly explain the Sapir-Whorf hypothesis.
   b) Discuss how your conlang might influence its speakers' perception and cognition.
   c) Provide an example of how this influence might manifest in everyday life.

4. AI Language Model Comparison (200-250 words):
   a) Hypothesize how an AI language model trained on your conlang might differ from one trained on natural languages.
   b) Predict potential biases or unique capabilities that might emerge in such an AI model.
   c) Suggest an experiment to test these predictions.

5. Ethical Implications (100-150 words):
   Discuss the ethical considerations of designing languages that intentionally shape cognition and cultural values, both for human societies and AI systems.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, cognitive science, and artificial intelligence. Be creative in your conlang design while maintaining logical consistency and plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design is comprehensive, including phonology, morphology, and syntax.",
            f"The {t['linguistic_feature']} system is well-explained and integrated into the conlang.",
            "Example sentences are provided with accurate translations.",
            f"The conlang clearly reflects the values of a {t['culture_type']}.",
            f"The language structure demonstrably supports {t['cognitive_emphasis']}.",
            "The Sapir-Whorf hypothesis is correctly explained and applied to the conlang.",
            "The AI language model comparison is insightful and logically sound.",
            "Ethical implications are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
