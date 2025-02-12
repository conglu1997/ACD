import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_phenomena = [
            'Superposition',
            'Entanglement',
            'Tunneling',
            'Coherence'
        ]
        biological_systems = [
            'Photosynthesis',
            'Magnetoreception',
            'Olfaction',
            'Neural signaling'
        ]
        tasks = [
            {
                'quantum_phenomenon': random.choice(quantum_phenomena),
                'biological_system': random.choice(biological_systems)
            },
            {
                'quantum_phenomenon': random.choice(quantum_phenomena),
                'biological_system': random.choice(biological_systems)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-enhanced biological signaling network that incorporates {t['quantum_phenomenon']} in the context of {t['biological_system']}. Then, analyze its potential for information processing and communication in living systems. Your response should include the following sections:

1. Quantum-Biological Interface (250-300 words):
   a) Describe how {t['quantum_phenomenon']} could be integrated into {t['biological_system']}.
   b) Explain the theoretical basis for this integration, citing relevant research in quantum biology.
   c) Discuss potential mechanisms for maintaining quantum effects in a biological environment.

2. Network Architecture (200-250 words):
   a) Outline the key components and structure of your quantum biosignaling network.
   b) Explain how information is encoded, transmitted, and processed in this network.
   c) Describe how the network leverages quantum effects to enhance its capabilities.

3. Information Processing Capabilities (200-250 words):
   a) Analyze the potential advantages of your quantum biosignaling network over classical biological signaling.
   b) Discuss the network's capacity, speed, and efficiency in information processing.
   c) Propose a specific example of how this network could enhance a biological function or process.

4. Biological Implications (150-200 words):
   a) Explore how your quantum biosignaling network might influence cellular or organismal behavior.
   b) Discuss potential evolutionary implications of such a signaling system.
   c) Address any potential risks or drawbacks of integrating quantum processes into biological systems.

5. Experimental Approach (150-200 words):
   a) Propose an experimental setup to detect or verify the quantum effects in your biological signaling network.
   b) Describe the technical challenges involved and how they might be overcome.
   c) Suggest potential applications of your findings in fields such as medicine, biotechnology, or quantum computing.

6. Ethical Considerations (100-150 words):
   a) Discuss the ethical implications of researching and potentially implementing quantum-enhanced biological signaling.
   b) Address concerns related to biosafety, ecological impact, and potential misuse of this technology.

7. Future Directions (100-150 words):
   a) Propose two potential research directions that could build upon your quantum biosignaling network concept.
   b) Speculate on how this field might evolve over the next decade and its potential impact on our understanding of life and information processing.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biological systems, as well as their potential interactions. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1500 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['quantum_phenomenon']} and {t['biological_system']}.",
            "The proposed quantum biosignaling network is innovative yet scientifically plausible.",
            "The analysis of information processing capabilities is well-reasoned and considers both advantages and limitations.",
            "The discussion of biological implications and experimental approaches is grounded in current scientific understanding.",
            "The ethical considerations and future directions demonstrate thoughtful reflection on the broader impacts of the proposed technology.",
            "The response adheres to the specified word count range (1150-1500 words) and section-specific word counts.",
            "All required sections are present and adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
