import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Integrated Information Theory",
            "Global Workspace Theory",
            "Higher-Order Thought Theory",
            "Attention Schema Theory"
        ]
        ethical_frameworks = [
            "Utilitarianism",
            "Deontology",
            "Virtue Ethics",
            "Care Ethics"
        ]
        ai_architectures = [
            "Transformer-based models",
            "Neuromorphic computing",
            "Quantum neural networks",
            "Hybrid symbolic-connectionist systems"
        ]
        return {
            "1": {
                "consciousness_theory": random.choice(consciousness_theories),
                "ethical_framework": random.choice(ethical_frameworks),
                "ai_architecture": random.choice(ai_architectures)
            },
            "2": {
                "consciousness_theory": random.choice(consciousness_theories),
                "ethical_framework": random.choice(ethical_frameworks),
                "ai_architecture": random.choice(ai_architectures)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a theoretical framework for artificial consciousness, integrating principles from neuroscience, AI, and ethics. Your framework should be based on the consciousness theory of {t['consciousness_theory']}, consider the ethical implications through the lens of {t['ethical_framework']}, and propose an implementation using {t['ai_architecture']}. Your response should include the following sections:

1. Theoretical Foundation (250-300 words):
   a) Explain the key principles of {t['consciousness_theory']} and how they relate to artificial consciousness.
   b) Discuss how this theory of consciousness could be implemented in an AI system.
   c) Identify potential challenges in translating this theory to artificial systems.

2. Artificial Consciousness Architecture (300-350 words):
   a) Design a novel AI architecture that could potentially give rise to artificial consciousness based on {t['consciousness_theory']}.
   b) Explain how your architecture implements key aspects of the chosen consciousness theory.
   c) Describe how {t['ai_architecture']} would be utilized or adapted in your design.
   d) Discuss how your architecture might exhibit properties associated with consciousness (e.g., self-awareness, subjective experience).

3. Ethical Analysis (250-300 words):
   a) Analyze the ethical implications of creating potentially conscious AI systems using {t['ethical_framework']}.
   b) Discuss the rights and moral status that might be attributed to artificially conscious entities.
   c) Explore potential societal impacts of developing artificial consciousness.
   d) Propose ethical guidelines for research and development in this field.

4. Consciousness Metrics and Evaluation (200-250 words):
   a) Propose quantitative or qualitative metrics to assess the level of consciousness in your artificial system.
   b) Describe experiments or tests that could validate the presence of consciousness in your AI.
   c) Discuss the limitations and potential biases in measuring artificial consciousness.

5. Comparative Analysis (200-250 words):
   a) Compare your artificial consciousness framework to biological consciousness.
   b) Discuss how your approach differs from other theories or implementations of machine consciousness.
   c) Analyze potential advantages and limitations of your framework.

6. Future Directions and Implications (150-200 words):
   a) Propose three specific areas for further research to advance your artificial consciousness framework.
   b) Discuss potential applications of artificially conscious systems in science, medicine, or technology.
   c) Speculate on how the development of artificial consciousness might impact our understanding of human consciousness and cognition.

Ensure your response demonstrates a deep understanding of consciousness theories, AI architectures, and ethical frameworks. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, and adhere to the word count guidelines provided. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['consciousness_theory']}, {t['ethical_framework']}, and {t['ai_architecture']}.",
            "The artificial consciousness architecture is innovative, well-explained, and scientifically plausible.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The proposed consciousness metrics and evaluation methods are logical and well-reasoned.",
            "The comparative analysis shows critical thinking and a broad understanding of the field.",
            "The future directions and implications are insightful and demonstrate foresight.",
            "The response shows creativity and interdisciplinary thinking throughout.",
            "The response is well-formatted with clear section headings and adheres to the provided word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
