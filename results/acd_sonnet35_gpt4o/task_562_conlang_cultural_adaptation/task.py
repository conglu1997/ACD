import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "culture": "Nomadic desert dwellers with a complex social hierarchy",
                "environment": "Harsh desert with scarce resources and frequent sandstorms",
                "values": "Resource conservation, social cohesion, and respect for elders"
            },
            {
                "culture": "Technologically advanced underwater civilization",
                "environment": "Deep ocean with bioluminescent life forms and strong currents",
                "values": "Scientific progress, environmental harmony, and collective knowledge"
            },
            {
                "culture": "Tree-dwelling society in a dense rainforest",
                "environment": "Lush canopy with diverse flora and fauna, frequent rainfall",
                "values": "Ecological balance, vertical spatial awareness, and communal living"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) for the following scenario:

Culture: {t['culture']}
Environment: {t['environment']}
Core Values: {t['values']}

Your task is to create a conlang that reflects the given cultural and environmental parameters, then use it to translate and generate text. Follow these steps:

1. Conlang Design (250-300 words):
   a) Describe the phonology of your conlang, including unique sounds that reflect the environment.
   b) Explain the morphological and syntactic structure, showing how it embodies the culture's values.
   c) Describe at least two unique linguistic features that are specifically adapted to the given scenario.
   d) Provide 5-10 sample vocabulary words with their meanings and etymological explanations.

2. Grammar Rules (150-200 words):
   Outline 3-5 key grammar rules of your conlang, explaining how they relate to the culture and environment. Include examples for each rule.

3. Translation (100-150 words):
   Translate the following English text into your conlang, then provide a gloss (word-by-word breakdown) and explain how the translation reflects the cultural and environmental factors:

   "Our people have thrived here for generations, adapting to the challenges of our world and holding fast to our values."

4. Original Text Generation (100-150 words):
   Create a short text (2-3 sentences) in your conlang that would be culturally significant to the given society. Provide a translation into English and explain the cultural relevance.

5. Linguistic Analysis (150-200 words):
   Analyze how your conlang compares to natural human languages. Discuss any similarities to existing language families and explain how it might evolve over time given the cultural and environmental factors.

Ensure your conlang is consistent, reflects the given parameters, and demonstrates a deep understanding of linguistic principles and cultural adaptation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design is comprehensive and clearly reflects the given cultural and environmental parameters",
            "The grammar rules are well-defined and logically connected to the scenario",
            "The translation and original text generation demonstrate consistent application of the conlang's rules",
            "The linguistic analysis shows deep understanding of language structures and cultural influences",
            "The overall response demonstrates creativity, linguistic expertise, and cultural sensitivity"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
