import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "dream_state": "Lucid dreaming",
                "quantum_approach": "Quantum entanglement",
                "consciousness_aspect": "Self-awareness",
                "brain_wave": "Gamma waves (30-100 Hz)",
                "constraint": "Minimize decoherence"
            },
            {
                "dream_state": "Deep sleep",
                "quantum_approach": "Quantum superposition",
                "consciousness_aspect": "Unconscious processing",
                "brain_wave": "Delta waves (0.5-4 Hz)",
                "constraint": "Maximize coherence time"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system that analyzes human {t['dream_state']} and models consciousness, focusing on the aspect of {t['consciousness_aspect']}. Your system should utilize the quantum approach of {t['quantum_approach']} and account for {t['brain_wave']} activity, while adhering to the constraint: {t['constraint']}. Then, use this system to explore the nature of subjective experience and propose novel theories of mind. Your response should include:

1. Quantum-Neural Interface (300-350 words):
   a) Describe the key components of your quantum computing system for analyzing {t['dream_state']}.
   b) Explain how your system integrates {t['quantum_approach']} with neural data processing of {t['brain_wave']}.
   c) Detail how the system captures and interprets brain activity during {t['dream_state']}.
   d) Propose a novel quantum algorithm that models {t['consciousness_aspect']} using {t['quantum_approach']}, addressing the constraint to {t['constraint']}.

2. Consciousness Modeling (250-300 words):
   a) Explain how your system represents {t['consciousness_aspect']} using quantum states.
   b) Describe a mathematical framework that links {t['quantum_approach']} to {t['consciousness_aspect']}.
   c) Discuss how your model accounts for the subjective nature of conscious experience in {t['dream_state']}.
   d) Propose a specific experiment to validate your consciousness model using {t['brain_wave']} data.

3. Dream Analysis Process (200-250 words):
   a) Outline a step-by-step process your system uses to analyze {t['dream_state']}.
   b) Explain how {t['quantum_approach']} enhances the analysis of dream content and structures.
   c) Describe a method to differentiate between levels of consciousness within {t['dream_state']} using quantum measurements.

4. Novel Theory of Mind (250-300 words):
   a) Propose a new theory of mind based on your quantum-enhanced analysis of {t['dream_state']}.
   b) Explain how this theory incorporates {t['quantum_approach']} and {t['consciousness_aspect']}.
   c) Address a specific existing paradox in consciousness studies using your theory.
   d) Predict three testable phenomena that would support your theory.

5. Ethical Implications (200-250 words):
   a) Discuss three potential misuses of quantum dream analysis technology.
   b) Propose five specific guidelines for the ethical development of quantum consciousness analysis.
   c) Analyze the potential impact of this technology on personal privacy and mental health.

6. Future Research Directions (150-200 words):
   a) Suggest three potential applications of your quantum dream consciousness analyzer in fields other than neuroscience.
   b) Identify two key technical challenges in developing this technology and propose approaches to address them.
   c) Discuss how your system might contribute to resolving the hard problem of consciousness.

Ensure your response demonstrates a deep understanding of quantum computing, neuroscience, and consciousness studies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Remember that your proposed system and theories should be grounded in current scientific understanding while pushing the boundaries of what's possible.

Format your response with clear headings for each section and use bullet points or numbered lists where appropriate. Include at least two relevant equations or formulas in your response. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must specifically address the dream state of {t['dream_state']} and incorporate {t['brain_wave']} activity in the system design and analysis.",
            f"The quantum approach of {t['quantum_approach']} must be effectively integrated into the system, with at least one specific algorithm or mathematical framework proposed that addresses the constraint to {t['constraint']}.",
            f"The aspect of consciousness, {t['consciousness_aspect']}, should be central to the model and proposed theory, with clear links to quantum states.",
            "The response must include all six required elements as specified in the instructions, with each section adequately addressing its respective topics.",
            "The proposed theory of mind must be novel, well-reasoned, and include three specific, testable predictions.",
            "The response must include at least two relevant equations or formulas related to quantum computing or consciousness modeling.",
            "The ethical implications section must discuss three potential misuses and propose five specific guidelines.",
            "The response must be within the specified word count (1350-1650 words) and include a word count at the end.",
            "The proposed system and theories should be innovative while remaining grounded in current scientific understanding and maintaining plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
