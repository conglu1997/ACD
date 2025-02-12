import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_parameters = [
            {
                "parameter": "Non-linear time perception",
                "description": "A culture that perceives time as cyclical or branching rather than linear"
            },
            {
                "parameter": "Synesthesia-based communication",
                "description": "A culture where language is based on sensory associations across different modalities"
            },
            {
                "parameter": "Collective consciousness",
                "description": "A culture with a highly developed sense of shared thoughts and experiences"
            },
            {
                "parameter": "Quantum superposition thinking",
                "description": "A culture that can conceptualize multiple states simultaneously, inspired by quantum mechanics"
            }
        ]
        
        texts_to_translate = [
            "The future is a mystery, but we shape it with our actions in the present.",
            "In unity, we find strength and wisdom beyond individual capabilities.",
            "Change is the only constant, embracing it leads to growth and understanding.",
            "Knowledge is a journey without end, each discovery opens new paths."
        ]
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "cognitive_parameter": random.choice(cognitive_parameters),
                "text_to_translate": random.choice(texts_to_translate)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a constructed language (conlang) based on the cognitive parameter: {t['cognitive_parameter']['parameter']} - {t['cognitive_parameter']['description']}. Then, use this conlang to translate the following text: "{t['text_to_translate']}"

Your response should include the following sections:

1. Conlang Design (300-350 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how the language reflects the given cognitive parameter.
   c) Provide examples of basic words or phrases in your conlang, with their meanings.
   d) Discuss any unique grammatical structures or linguistic innovations in your conlang.

2. Cognitive Analysis (200-250 words):
   a) Analyze how your conlang might influence or be influenced by cognitive processes related to the given parameter.
   b) Discuss potential implications of using this language on thought patterns or cultural development.
   c) Compare your conlang to natural languages, highlighting similarities or differences in cognitive aspects.

3. Translation Process (150-200 words):
   a) Translate the given text into your conlang.
   b) Provide a word-for-word or morpheme-by-morpheme gloss of the translation.
   c) Explain any challenges in translating the text and how you addressed them.

4. Cultural Implications (150-200 words):
   a) Describe a hypothetical culture that might use this language.
   b) Explain how the language and cognitive parameter might shape this culture's worldview or social structures.
   c) Discuss potential advantages or disadvantages this culture might have in certain areas (e.g., science, art, diplomacy) due to their language and cognition.

5. Potential Applications (100-150 words):
   a) Suggest potential real-world applications or implications of studying this type of conlang.
   b) Discuss how insights from this exercise might contribute to fields such as cognitive science, linguistics, or AI development.

Ensure your response demonstrates a deep understanding of linguistic principles, cognitive science, and cultural anthropology. Be creative in your language design while maintaining logical consistency and plausibility. Use appropriate linguistic terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang design must clearly reflect the cognitive parameter: {t['cognitive_parameter']['parameter']}",
            "The conlang must have a logically consistent structure with defined phonology, morphology, and syntax",
            f"The translation of '{t['text_to_translate']}' must be provided and explained",
            "The response must include a thoughtful analysis of cognitive and cultural implications",
            "The response should demonstrate creativity and deep understanding of linguistics and cognitive science"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
