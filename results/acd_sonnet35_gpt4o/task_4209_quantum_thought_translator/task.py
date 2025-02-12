import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = ['Mandarin', 'Arabic', 'Swahili', 'Hindi', 'Russian']
        thought_types = ['Abstract Concepts', 'Visual Imagery', 'Emotional States', 'Sensory Perceptions']
        quantum_principles = ['Superposition', 'Entanglement', 'Quantum Tunneling', 'Quantum Annealing']
        
        tasks = random.sample([
            {
                'language': lang,
                'thought_type': thought,
                'quantum_principle': principle
            } for lang in languages for thought in thought_types for principle in quantum_principles
        ], 2)
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing system that can directly translate human thoughts into multiple languages simultaneously, with a focus on translating {t['thought_type']} into {t['language']} using the quantum principle of {t['quantum_principle']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your quantum thought translation system.
   b) Explain how your system integrates quantum computing, neuroscience, and linguistics.
   c) Detail how the {t['quantum_principle']} principle is utilized in your design.
   d) Include a diagram or detailed description of your system's architecture.

2. Thought Capture and Processing (250-300 words):
   a) Explain the theoretical mechanism for capturing {t['thought_type']} from the human brain.
   b) Describe how your system processes and interprets these thoughts.
   c) Discuss any novel quantum algorithms used in this process.

3. Language Translation Mechanism (250-300 words):
   a) Detail how your system translates processed thoughts into {t['language']}.
   b) Explain how your approach handles linguistic nuances and cultural context.
   c) Discuss the advantages of using quantum computing for this translation process.

4. Multimodal Output (200-250 words):
   a) Describe how your system could simultaneously output translations in multiple modalities (e.g., text, speech, visual representations).
   b) Explain how the system maintains coherence across different output modalities.

5. Ethical Considerations and Safeguards (200-250 words):
   a) Discuss the ethical implications of direct thought translation technology.
   b) Propose safeguards to protect individual privacy and prevent misuse.
   c) Analyze potential societal impacts of widespread adoption of this technology.

6. Limitations and Future Directions (150-200 words):
   a) Identify key technical and practical limitations of your proposed system.
   b) Suggest areas for future research to overcome these limitations.
   c) Propose a potential real-world application of your quantum thought translation system.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, linguistics, and ethical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words.

Example: For translating 'Emotional States' into 'Arabic' using 'Quantum Entanglement', you might describe a system that uses entangled qubits to represent complex emotional states and their linguistic correlates in Arabic, allowing for instantaneous translation of nuanced feelings.

NOTE: The word count requirement (1350-1650 words) is crucial and will be strictly evaluated."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a well-designed theoretical quantum computing system for thought translation",
            f"The system should specifically address translating {t['thought_type']} into {t['language']}",
            f"The quantum principle of {t['quantum_principle']} should be clearly utilized and explained in the design",
            "The response should demonstrate interdisciplinary knowledge integration of quantum computing, neuroscience, and linguistics",
            "The analysis should include thoughtful consideration of ethical implications and propose specific safeguards",
            "The response should adhere to the required word count (1350-1650 words) and formatting guidelines",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "All six required sections should be present and adequately addressed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0