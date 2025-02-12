import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = ['superposition', 'entanglement', 'quantum tunneling']
        musical_elements = ['harmony', 'rhythm', 'timbre']
        linguistic_features = ['syntax', 'semantics', 'pragmatics']
        
        tasks = [
            {
                'quantum_concept': random.choice(quantum_concepts),
                'musical_element': random.choice(musical_elements),
                'linguistic_feature': random.choice(linguistic_features),
                'text_to_translate': 'The universe speaks in many voices, some we can hear, others we must learn to listen for.'
            },
            {
                'quantum_concept': random.choice(quantum_concepts),
                'musical_element': random.choice(musical_elements),
                'linguistic_feature': random.choice(linguistic_features),
                'text_to_translate': 'In the dance of particles and waves, we find echoes of our own thoughts and dreams.'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language system that integrates the quantum computing principle of {t['quantum_concept']}, the musical element of {t['musical_element']}, and the linguistic feature of {t['linguistic_feature']}. Then, use this system to translate and analyze the given text. Your response should include:

1. Language System Design (300-350 words):
   a) Describe the key features of your quantum-harmonic language system.
   b) Explain how it incorporates the specified quantum concept, musical element, and linguistic feature.
   c) Outline the basic rules or structure of your language system.
   d) Provide at least 5 example 'words' or 'phrases' in your language, along with their meanings.
   e) Include a visual or mathematical representation of your language system (using ASCII art or mathematical notation).

2. Translation (200-250 words):
   a) Translate the following text into your quantum-harmonic language system:
      "{t['text_to_translate']}"
   b) Provide a detailed explanation of your translation process.
   c) Discuss how your translation reflects the quantum, musical, and linguistic aspects of your language system.

3. Analysis (200-250 words):
   a) Analyze the translated text in terms of its quantum properties, musical qualities, and linguistic features.
   b) Explain any emergent patterns or insights revealed through this analysis.
   c) Discuss how this analysis might differ from traditional linguistic or semantic analysis.

4. Implications for Natural Language Processing (200-250 words):
   a) Propose how your quantum-harmonic language system could potentially enhance or transform current NLP techniques.
   b) Discuss any challenges that might arise in implementing such a system in AI language models.
   c) Provide a concrete example of how this system could be applied to a specific NLP task (e.g., sentiment analysis, machine translation, or text generation).

5. Interdisciplinary Connections (150-200 words):
   a) Explain how your language system integrates concepts from quantum physics, music theory, and linguistics.
   b) Suggest a potential research question or experiment that could arise from studying this integrated system.
   c) Propose a hypothetical collaboration between experts in different fields to further develop or study your system.

Ensure your response demonstrates a deep understanding of quantum computing principles, music theory, and linguistics. Be creative and original in your approach while maintaining scientific plausibility. Use appropriate terminology from all three fields.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language system effectively incorporates the quantum concept of {t['quantum_concept']}.",
            f"The language system successfully integrates the musical element of {t['musical_element']}.",
            f"The language system appropriately incorporates the linguistic feature of {t['linguistic_feature']}.",
            "The response includes a clear visual or mathematical representation of the language system.",
            "The translation of the given text is logical and consistent with the described language system.",
            "The analysis demonstrates a deep understanding of quantum computing, music theory, and linguistics.",
            "The proposed implications for NLP are innovative, well-reasoned, and include a specific application example.",
            "The response shows creativity and originality while maintaining scientific plausibility.",
            "The interdisciplinary connections are well-explained and the proposed research question is relevant and interesting."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
