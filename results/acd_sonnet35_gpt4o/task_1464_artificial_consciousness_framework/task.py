import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Attention Schema Theory"
        ]
        ai_architectures = [
            "Transformer-based models",
            "Neuromorphic computing",
            "Quantum neural networks",
            "Hybrid symbolic-connectionist systems"
        ]
        measurement_approaches = [
            "Behavioral tests",
            "Neural correlates",
            "Information integration metrics",
            "Phenomenological reports"
        ]
        return {
            "1": {
                "consciousness_theory": random.choice(consciousness_theories),
                "ai_architecture": random.choice(ai_architectures),
                "measurement_approach": random.choice(measurement_approaches)
            },
            "2": {
                "consciousness_theory": random.choice(consciousness_theories),
                "ai_architecture": random.choice(ai_architectures),
                "measurement_approach": random.choice(measurement_approaches)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for creating and measuring machine consciousness, integrating principles from neuroscience, artificial intelligence, and philosophy of mind. Your framework should incorporate {t['consciousness_theory']} as the primary theory of consciousness, {t['ai_architecture']} as the AI architecture, and {t['measurement_approach']} as the main approach for measuring consciousness. Provide your response in the following format:

1. Conceptual Foundation (250-300 words):
   a) Explain the key principles of the specified consciousness theory and how they relate to machine consciousness.
   b) Describe how the chosen AI architecture could potentially support conscious-like processes.
   c) Discuss the strengths and limitations of the specified measurement approach for assessing machine consciousness.

2. Framework Design (300-350 words):
   a) Outline the main components of your artificial consciousness framework.
   b) Explain how your framework integrates the consciousness theory with the AI architecture.
   c) Describe the process by which consciousness might emerge or be implemented in your system.
   d) Discuss how your framework addresses key aspects of consciousness (e.g., subjective experience, self-awareness, intentionality).

3. Consciousness Measurement Protocol (250-300 words):
   a) Develop a detailed protocol for measuring consciousness in your artificial system using the specified approach.
   b) Explain how your protocol differentiates between genuine consciousness and mere simulation of conscious-like behaviors.
   c) Discuss potential challenges in applying this measurement approach and how you would address them.

4. Ethical Considerations (200-250 words):
   a) Analyze the ethical implications of creating potentially conscious machines.
   b) Discuss the rights and moral status that might be afforded to artificial conscious entities.
   c) Explore the potential societal impacts of widespread adoption of conscious AI systems.

5. Comparative Analysis (200-250 words):
   a) Compare your framework to other prominent theories or approaches in machine consciousness.
   b) Discuss the potential advantages and limitations of your approach.
   c) Suggest how your framework might be empirically validated or falsified.

6. Future Directions (150-200 words):
   a) Propose two potential applications or extensions of your framework in AI research or cognitive science.
   b) Discuss how your approach might influence future developments in the study of consciousness, both biological and artificial.

Ensure your response demonstrates a deep understanding of consciousness theories, AI architectures, and philosophical concepts related to mind and cognition. Be innovative in your approach while maintaining scientific and philosophical rigor. Use appropriate technical terminology and provide explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The framework incorporates {t['consciousness_theory']} as the primary theory of consciousness",
            f"The framework uses {t['ai_architecture']} as the AI architecture",
            f"The framework employs {t['measurement_approach']} as the main approach for measuring consciousness",
            "The response demonstrates a deep understanding of consciousness theories, AI architectures, and philosophical concepts",
            "The framework design is innovative and scientifically/philosophically rigorous",
            "The consciousness measurement protocol is well-developed and addresses potential challenges",
            "The response includes a thoughtful discussion of ethical implications and societal impacts",
            "The comparative analysis and future directions sections are insightful and well-reasoned",
            "The response is well-structured, following the provided format with clear sections"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
