import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "source_culture": "Japanese",
                "target_culture": "Brazilian",
                "context": "Business negotiation",
                "quantum_concept": "Superposition"
            },
            {
                "source_culture": "Indian",
                "target_culture": "German",
                "context": "Academic collaboration",
                "quantum_concept": "Entanglement"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired translation system that incorporates cultural context and linguistic nuances, then apply it to the following cross-cultural communication scenario:

Source Culture: {t['source_culture']}
Target Culture: {t['target_culture']}
Context: {t['context']}
Quantum Concept to Incorporate: {t['quantum_concept']}

Your task has the following components:

1. Quantum-Cultural Translation Model (250-300 words):
   a) Describe the key components of your quantum-inspired translation system.
   b) Explain how you incorporate the specified quantum concept into your model.
   c) Detail how your system accounts for cultural context and linguistic nuances.
   d) Discuss how your model differs from traditional machine translation approaches.

2. Cultural-Linguistic Mapping (200-250 words):
   a) Explain how your system maps cultural concepts between the source and target cultures.
   b) Describe the method for handling culture-specific idioms, metaphors, or expressions.
   c) Discuss how your model addresses potential cultural misunderstandings or faux pas.

3. Quantum Algorithm Application (200-250 words):
   a) Provide a high-level description of a quantum algorithm used in your system.
   b) Explain how this algorithm enhances the translation process or cultural understanding.
   c) Discuss any theoretical advantages this approach might have over classical methods.

4. Scenario Application (250-300 words):
   a) Apply your quantum-cultural translation system to the given scenario.
   b) Provide an example of a challenging phrase or concept to translate in this context.
   c) Walk through how your system would handle this translation, highlighting cultural and quantum aspects.
   d) Compare the output of your system to what a traditional translation method might produce.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns of using quantum-inspired systems for cultural translation.
   b) Explore how this technology might impact cross-cultural communication and global relations.
   c) Address potential risks of oversimplifying or misrepresenting cultural nuances.

6. Future Developments and Limitations (100-150 words):
   a) Identify current limitations of your proposed system.
   b) Suggest potential future improvements or research directions.
   c) Speculate on how this technology might evolve and its potential long-term impact on society.

Ensure your response demonstrates a deep understanding of quantum computing concepts, linguistic principles, and cultural anthropology. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1150-1450 words.

Format your response with clear headings for each section and use subheadings where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a design for a quantum-inspired translation system that incorporates cultural context and linguistic nuances.",
            "The model should clearly incorporate the specified quantum concept in a meaningful way.",
            "The cultural-linguistic mapping should demonstrate a nuanced understanding of both the source and target cultures.",
            "The quantum algorithm application should be logically explained and relevant to the translation process.",
            "The scenario application should provide a concrete example of how the system would handle a challenging translation, highlighting both cultural and quantum aspects.",
            "The response should address ethical and societal implications of the proposed technology.",
            "The answer must demonstrate interdisciplinary knowledge integration, combining concepts from quantum computing, linguistics, and cultural anthropology.",
            "The response should be creative and innovative while maintaining scientific plausibility.",
            "The answer should adhere to the specified format and word count (1150-1450 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
