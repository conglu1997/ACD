import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        societies = [
            {
                "name": "Aquaterra",
                "description": "A society living in floating cities on a water-covered planet, with bioluminescent flora and fauna."
            },
            {
                "name": "Zephyria",
                "description": "A culture of nomadic wind-riders living in a world of floating islands and constant aerial currents."
            }
        ]
        texts = [
            "As the sun sets, we gather to share stories of our ancestors and dream of future voyages.",
            "In harmony with the elements, we forge our path through the ever-changing landscape."
        ]
        return {
            str(i+1): {
                "society": society,
                "text": text
            } for i, (society, text) in enumerate(zip(random.sample(societies, 2), texts))
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) for the fictional society of {t['society']['name']}: {t['society']['description']}. Then, use your conlang to translate the following text while preserving its cultural nuances: "{t['text']}"

Your response should include the following sections:

1. Language Design (300-350 words):
   a) Describe the phonology, morphology, and syntax of your conlang.
   b) Explain how the language reflects the society's culture, environment, and worldview.
   c) Provide examples of unique features or innovations in your conlang.
   d) Include a sample vocabulary of at least 10 words with their meanings and cultural significance.

2. Writing System (150-200 words):
   a) Design a writing system for your conlang.
   b) Explain how it reflects the society's culture and environment.
   c) Provide a visual representation or description of at least 5 characters or symbols.

3. Translation (200-250 words):
   a) Translate the given text into your conlang.
   b) Provide a word-for-word gloss and a free translation back into English.
   c) Explain any cultural adaptations or nuances in your translation.

4. Cultural Analysis (200-250 words):
   a) Analyze how your conlang reflects and shapes the worldview of its speakers.
   b) Discuss potential challenges or unique aspects of communication in this language.
   c) Explain how the language might evolve as the society develops or faces new challenges.

5. Linguistic Implications (150-200 words):
   a) Discuss how your conlang challenges or supports existing linguistic theories.
   b) Propose a hypothesis about human language based on your conlang design.
   c) Suggest potential applications of your conlang in fields such as cognitive science or anthropology.

Ensure your response demonstrates a deep understanding of linguistics, anthropology, and creative language design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining plausibility within the given cultural and environmental context.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design demonstrates a deep understanding of linguistic principles and creativity",
            "The language effectively reflects the given society's culture, environment, and worldview",
            "The writing system is innovative and culturally appropriate",
            "The translation preserves the original text's meaning while adapting to the conlang's cultural context",
            "The cultural and linguistic analyses show insight and originality"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
