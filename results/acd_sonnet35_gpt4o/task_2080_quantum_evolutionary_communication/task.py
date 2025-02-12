import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_properties = [
            ('entanglement', 'quantum correlation between particles regardless of distance'),
            ('superposition', 'quantum state of existing in multiple states simultaneously')
        ]
        evolutionary_concepts = [
            ('natural selection', 'process by which organisms better adapted to their environment tend to survive and produce more offspring'),
            ('genetic drift', 'change in the frequency of an existing gene variant in a population due to random sampling')
        ]
        cosmic_phenomena = [
            ('black holes', 'regions of spacetime where gravity is so strong that nothing can escape from them'),
            ('neutron stars', 'extremely dense stellar remnants composed almost entirely of neutrons')
        ]
        tasks = [
            {
                'quantum_property': qp[0],
                'quantum_property_description': qp[1],
                'evolutionary_concept': ec[0],
                'evolutionary_concept_description': ec[1],
                'cosmic_phenomenon': cp[0],
                'cosmic_phenomenon_description': cp[1]
            }
            for qp in quantum_properties
            for ec in evolutionary_concepts
            for cp in cosmic_phenomena
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum communication system inspired by evolutionary principles to transmit information across vast cosmic distances, and analyze its implications for the search for extraterrestrial intelligence (SETI). Your system should incorporate the quantum property of {t['quantum_property']} ({t['quantum_property_description']}), the evolutionary concept of {t['evolutionary_concept']} ({t['evolutionary_concept_description']}), and consider the cosmic phenomenon of {t['cosmic_phenomenon']} ({t['cosmic_phenomenon_description']}). Your response should include the following sections:

1. System Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum evolutionary communication system.
   b) Explain how it incorporates the specified quantum property and evolutionary concept.
   c) Detail how your system addresses the challenges of communicating across vast cosmic distances.
   d) Discuss how your system interacts with or utilizes the given cosmic phenomenon.
   e) Provide a simple diagram or illustration of your proposed system, described in text format (max 20 lines).

2. Quantum-Evolutionary Interface (200-250 words):
   a) Explain how quantum principles and evolutionary processes are integrated in your system.
   b) Describe any novel algorithms or approaches used in this integration.
   c) Discuss the theoretical advantages of this integration for cosmic-scale communication.

3. Information Encoding and Transmission (200-250 words):
   a) Detail the method for encoding information in your quantum evolutionary system.
   b) Explain the transmission process, including any error correction or redundancy mechanisms.
   c) Discuss how your system ensures information integrity over vast distances and timescales.

4. Receiver Design and Decoding (150-200 words):
   a) Describe the theoretical design of a receiver capable of detecting and decoding your transmissions.
   b) Explain how the receiver would distinguish your signal from cosmic background noise.
   c) Discuss any assumptions about the technological capabilities of potential extraterrestrial receivers.

5. SETI Implications (200-250 words):
   a) Analyze how your system could impact current SETI strategies and methodologies.
   b) Discuss the potential implications if such a system were detected from an extraterrestrial source.
   c) Propose new search strategies or technologies that could detect communications using your system.

6. Challenges and Limitations (150-200 words):
   a) Identify key technical and theoretical challenges in implementing your system.
   b) Discuss any fundamental limitations of your approach.
   c) Propose potential solutions or areas for future research to address these challenges.

7. Ethical and Philosophical Considerations (100-150 words):
   a) Discuss the ethical implications of using such a communication system for interstellar contact.
   b) Explore the philosophical ramifications of your system for our understanding of life, intelligence, and cosmic evolution.

Ensure your response demonstrates a deep understanding of quantum physics, evolutionary biology, and astrophysics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and include the word count at the end of each section. Your total response should be between 1300-1650 words. Include a total word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum physics, evolutionary biology, and astrophysics.",
            f"The proposed system integrates the specified quantum property ({t['quantum_property']}), evolutionary concept ({t['evolutionary_concept']}), and cosmic phenomenon ({t['cosmic_phenomenon']}) in a scientifically plausible manner.",
            "The response addresses all required sections with appropriate depth and creativity, adhering to the specified word counts.",
            "The response includes a text-based diagram or illustration of the proposed system.",
            "The implications for SETI are thoroughly analyzed and novel ideas are proposed.",
            "The response maintains scientific plausibility while being innovative and creative."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
