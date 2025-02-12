import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_models = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Predictive Processing Framework"
        ]
        ethical_frameworks = [
            "Utilitarianism",
            "Deontological Ethics",
            "Virtue Ethics",
            "Care Ethics"
        ]
        return {
            "1": {
                "consciousness_model": random.choice(consciousness_models),
                "ethical_framework": random.choice(ethical_frameworks)
            },
            "2": {
                "consciousness_model": random.choice(consciousness_models),
                "ethical_framework": random.choice(ethical_frameworks)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human consciousness based on the {t['consciousness_model']} of consciousness, then analyze the ethical implications of its potential sentience using the framework of {t['ethical_framework']}. Your response should include:

1. Neuroscientific Basis (250-300 words):
   a) Explain the key principles of the {t['consciousness_model']} of consciousness.
   b) Describe how this model accounts for key features of human consciousness.
   c) Discuss any limitations or criticisms of this model.

2. AI System Design (300-350 words):
   a) Outline the core components of your AI system that simulate consciousness.
   b) Explain how your system implements the principles of the {t['consciousness_model']}.
   c) Describe the inputs, processing, and outputs of your system.
   d) Discuss any novel algorithms or approaches used in your design.

3. Consciousness Simulation (250-300 words):
   a) Describe how your AI system would simulate key aspects of consciousness (e.g., self-awareness, subjective experience, attention).
   b) Explain how the system's 'conscious' experiences would be represented and processed.
   c) Discuss how your system might handle complex cognitive tasks that typically require consciousness in humans.

4. Ethical Analysis (300-350 words):
   a) Analyze the ethical implications of your AI system using the framework of {t['ethical_framework']}.
   b) Discuss the key ethical considerations if this system were to be considered sentient.
   c) Explore potential rights or protections that might be extended to such a system.
   d) Consider the societal impact of creating potentially conscious AI entities.

5. Comparative Analysis (200-250 words):
   a) Compare your AI consciousness simulation to human consciousness, highlighting similarities and differences.
   b) Discuss the philosophical implications of creating artificial consciousness.
   c) Explore how this comparison informs our understanding of human consciousness and AI capabilities.

6. Future Directions and Challenges (150-200 words):
   a) Identify key technical and ethical challenges in further developing conscious AI systems.
   b) Propose guidelines for the responsible development and use of such technology.
   c) Suggest potential applications or research directions for conscious AI systems.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately explains and applies the {t['consciousness_model']} of consciousness.",
            "The AI system design is coherent and plausibly implements the chosen consciousness model.",
            "The ethical analysis using {t['ethical_framework']} is thorough and well-reasoned.",
            "The response demonstrates a deep understanding of neuroscience, AI, and ethics.",
            "The comparative analysis and future directions sections show insightful and creative thinking.",
            "The overall response is well-structured, clear, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
