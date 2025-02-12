import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "quantum_principle": "Quantum entanglement",
                "brain_region": "Prefrontal cortex",
                "ai_capability": "Natural language processing",
                "cognitive_enhancement": "Decision-making"
            },
            {
                "quantum_principle": "Quantum superposition",
                "brain_region": "Hippocampus",
                "ai_capability": "Pattern recognition",
                "cognitive_enhancement": "Memory formation and recall"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-based neural interface system that connects human brains to advanced AI systems, focusing on the following parameters:

- Quantum Principle: {t['quantum_principle']}
- Brain Region: {t['brain_region']}
- AI Capability: {t['ai_capability']}
- Cognitive Enhancement Target: {t['cognitive_enhancement']}

Then, analyze its potential impact on human cognition and the nature of consciousness. Your response should include the following sections:

1. Quantum Neural Interface Design (300-350 words):
   a) Describe the key components of your quantum-based neural interface system.
   b) Explain how it leverages {t['quantum_principle']} to interface with the {t['brain_region']}.
   c) Detail how your system integrates with AI systems, particularly for {t['ai_capability']}.
   d) Discuss any novel quantum-biological mechanisms proposed in your design.
   e) Include a simple diagram or flowchart of your system architecture (using ASCII art or a clear textual description).

2. Cognitive Enhancement Mechanism (250-300 words):
   a) Explain how your system aims to enhance {t['cognitive_enhancement']}.
   b) Describe the hypothetical neurophysiological changes induced by your quantum neural interface.
   c) Discuss potential limitations or side effects of this cognitive enhancement.

3. AI-Brain Interaction (200-250 words):
   a) Detail how information is exchanged between the human brain and the AI system.
   b) Explain how {t['ai_capability']} is integrated with human cognition.
   c) Discuss potential emergent properties of this human-AI cognitive hybrid.

4. Consciousness Implications (250-300 words):
   a) Analyze how your quantum neural interface might affect human consciousness.
   b) Discuss philosophical implications of a quantum basis for consciousness.
   c) Explore how AI integration might alter the nature of human experience and self-awareness.

5. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues arising from this technology.
   b) Discuss implications for human autonomy, privacy, and identity.
   c) Propose guidelines for responsible development and use of quantum neural interfaces.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your quantum neural interface system.
   b) Propose a research question that could further our understanding of quantum effects in cognition.
   c) Discuss how this technology might evolve in the next few decades.

Ensure your response demonstrates a deep understanding of quantum physics, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the quantum principle of {t['quantum_principle']}, the brain region {t['brain_region']}, the AI capability of {t['ai_capability']}, and the cognitive enhancement target of {t['cognitive_enhancement']}.",
            "The proposed quantum neural interface system must be logically coherent and demonstrate a clear understanding of how quantum physics, neuroscience, and AI could theoretically work together.",
            "The response must include all six required sections as specified in the instructions, with each section adequately addressing its respective topics.",
            "The submission must demonstrate creativity and propose novel ideas while remaining grounded in current scientific understanding.",
            "The analysis of consciousness implications and ethical considerations must be thoughtful and demonstrate an understanding of the complex philosophical and societal issues involved.",
            "The response must show a clear integration of concepts from quantum physics, neuroscience, and AI, explaining how these fields intersect in the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
