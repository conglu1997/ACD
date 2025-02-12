import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum interference",
            "quantum tunneling"
        ]
        cultural_aspects = [
            "idiomatic expressions",
            "cultural values",
            "social norms",
            "historical context"
        ]
        language_pairs = [
            ("English", "Mandarin Chinese"),
            ("Arabic", "Japanese"),
            ("Hindi", "Spanish"),
            ("Swahili", "Russian")
        ]
        return {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "cultural_aspect": random.choice(cultural_aspects),
                "language_pair": random.choice(language_pairs)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "cultural_aspect": random.choice(cultural_aspects),
                "language_pair": random.choice(language_pairs)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm for cross-cultural natural language understanding and generation, focusing on preserving cultural nuances and idioms. Your algorithm should incorporate the quantum concept of {t['quantum_concept']} and address the cultural aspect of {t['cultural_aspect']} for the language pair {t['language_pair'][0]} and {t['language_pair'][1]}. Your response should include the following sections:

1. Quantum Algorithm Design (300-350 words):
   a) Describe the overall structure and key components of your quantum algorithm.
   b) Explain how you incorporate {t['quantum_concept']} into your algorithm design.
   c) Detail how your algorithm processes and generates language while preserving {t['cultural_aspect']}.
   d) Include a high-level quantum circuit diagram or pseudocode snippet illustrating a key part of your algorithm.

2. Linguistic and Cultural Model Integration (250-300 words):
   a) Explain how your quantum algorithm interfaces with classical natural language processing and cultural knowledge bases.
   b) Describe the method for encoding linguistic and cultural information into quantum states.
   c) Discuss how your algorithm handles the complexity of preserving {t['cultural_aspect']} across the {t['language_pair'][0]}-{t['language_pair'][1]} language pair.

3. Translation and Generation Process (250-300 words):
   a) Provide a step-by-step explanation of how your algorithm translates a culturally-nuanced phrase from {t['language_pair'][0]} to {t['language_pair'][1]}.
   b) Describe the process by which your algorithm generates culturally appropriate responses in the target language.
   c) Explain how the quantum nature of your algorithm enhances cross-cultural communication compared to classical approaches.

4. Example Output (150-200 words):
   a) Provide an example of a challenging {t['cultural_aspect']} in {t['language_pair'][0]} and its quantum-generated translation in {t['language_pair'][1]}.
   b) Explain the quantum operations that led to this output.
   c) Analyze the cultural and linguistic accuracy of the translation.

5. Theoretical Advantages and Limitations (200-250 words):
   a) Discuss the theoretical improvements offered by your quantum approach in cross-cultural communication.
   b) Identify potential limitations or challenges in implementing your algorithm on current or near-term quantum hardware.
   c) Propose potential solutions or areas for future research to address these limitations.

6. Societal Implications (150-200 words):
   a) Explore how your quantum cultural translation algorithm might impact fields such as international relations, global business, or cultural exchange programs.
   b) Discuss potential ethical considerations and safeguards needed for responsible use of this technology.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic theories, cultural studies, and natural language processing. Be innovative in your approach while maintaining scientific and theoretical plausibility. Use appropriate terminology from quantum physics, linguistics, and cultural studies throughout your answer.

Format your response with clear headings for each section and adhere to the specified word counts. Your total response should be between 1300-1600 words. Include a word count at the end of each section.

Remember to balance creativity with scientific plausibility in your design. While we encourage innovative thinking, ensure that your proposed quantum algorithm maintains a foundation in current scientific understanding."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum computing and cross-cultural communication challenges.",
            f"The quantum concept of {t['quantum_concept']} is effectively incorporated into the algorithm design.",
            f"The algorithm addresses the preservation of {t['cultural_aspect']} in a novel and plausible way.",
            f"The example output shows a nuanced understanding of both {t['language_pair'][0]} and {t['language_pair'][1]} cultures.",
            "The societal implications and ethical considerations are thoughtfully analyzed.",
            "The response adheres to the specified word count requirements for each section.",
            "The proposed quantum algorithm maintains a balance between innovation and scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
