import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_phenomena = [
            'Quantum Entanglement',
            'Quantum Superposition',
            'Quantum Tunneling',
            'Wave-Particle Duality'
        ]
        language_families = [
            'Sino-Tibetan',
            'Austronesian',
            'Niger-Congo',
            'Afroasiatic'
        ]
        tasks = [
            {
                'quantum_phenomenon': random.choice(quantum_phenomena),
                'language_family': random.choice(language_families)
            },
            {
                'quantum_phenomenon': random.choice(quantum_phenomena),
                'language_family': random.choice(language_families)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that interprets and translates quantum phenomena into natural language descriptions, then use it to generate a novel quantum-inspired conlang (constructed language). Focus on the quantum phenomenon of {t['quantum_phenomenon']} and draw inspiration from the {t['language_family']} language family. Your response should include the following sections:

1. Quantum-Linguistic AI System Design (300-350 words):
   a) Describe the architecture of your AI system for interpreting quantum phenomena and translating them into natural language.
   b) Explain how your system integrates quantum physics concepts with linguistic structures.
   c) Detail any novel algorithms or techniques used in your model.
   d) Include a brief diagram or flowchart describing your system's key components and their interactions.

2. Quantum Phenomenon Analysis (200-250 words):
   a) Provide a clear explanation of {t['quantum_phenomenon']} in layman's terms.
   b) Describe how your AI system would represent and process this phenomenon.
   c) Give an example of how your system would translate a specific aspect of this phenomenon into natural language.

3. Language Family Integration (200-250 words):
   a) Briefly describe the key features of the {t['language_family']} language family.
   b) Explain how your AI system incorporates these features into its language processing and generation.
   c) Discuss any challenges in reconciling quantum concepts with this language family's structures.

4. Quantum-Inspired Conlang Design (250-300 words):
   a) Present the basic structure and key features of your quantum-inspired constructed language.
   b) Explain how it incorporates both quantum concepts and linguistic elements from the {t['language_family']} family.
   c) Provide examples of unique words or grammatical structures in your conlang that reflect quantum principles.
   d) Describe how your conlang represents the specific phenomenon of {t['quantum_phenomenon']}.

5. Sample Translation (150-200 words):
   a) Provide a short paragraph (3-4 sentences) in English describing an aspect of {t['quantum_phenomenon']}.
   b) Translate this paragraph into your quantum-inspired conlang.
   c) Explain key features of your translation, highlighting how it captures both quantum and linguistic elements.

6. Potential Applications (200-250 words):
   a) Discuss potential applications of your quantum-linguistic AI system and conlang in scientific communication or education.
   b) Explore how this system might enhance our understanding of quantum phenomena or language evolution.
   c) Propose an experiment to test the effectiveness of your conlang in describing quantum concepts.

7. Limitations and Future Work (150-200 words):
   a) Identify potential limitations or challenges in your current system and conlang design.
   b) Suggest areas for future research or improvement.
   c) Discuss any ethical considerations related to developing AI systems that bridge quantum physics and linguistics.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of an AI system that interprets and translates quantum phenomena, focusing on {t['quantum_phenomenon']} and drawing inspiration from the {t['language_family']} language family.",
            "The quantum-linguistic AI system design is thoroughly explained, including its architecture, integration of quantum physics and linguistics, and novel techniques.",
            f"The quantum phenomenon ({t['quantum_phenomenon']}) is clearly explained and its representation in the AI system is described.",
            f"The key features of the {t['language_family']} language family are described and integrated into the AI system's language processing.",
            "A quantum-inspired conlang is presented with clear structure and features, incorporating both quantum concepts and linguistic elements from the specified language family.",
            "A sample translation is provided, demonstrating the conlang's ability to represent quantum concepts.",
            "Potential applications of the quantum-linguistic AI system and conlang are discussed, including an experimental proposal.",
            "Limitations, future work, and ethical considerations are addressed.",
            "The response demonstrates a deep understanding of quantum physics, linguistics, and artificial intelligence, using appropriate technical terminology.",
            "The proposed system and conlang are innovative while maintaining scientific plausibility.",
            "The response adheres to the specified word count limits for each section and the overall word count range of 1450-1800 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
