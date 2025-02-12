import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition", "entanglement", "quantum tunneling",
            "wave function collapse", "quantum coherence"
        ]
        consciousness_theories = [
            "integrated information theory", "global workspace theory",
            "orchestrated objective reduction", "higher-order thought theory",
            "predictive processing theory"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "consciousness_theory": random.choice(consciousness_theories)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "consciousness_theory": random.choice(consciousness_theories)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates the quantum mechanical principle of {t['quantum_principle']} with the consciousness theory of {t['consciousness_theory']}, and use it to propose a novel approach to artificial general intelligence (AGI). Your response should include:

1. Conceptual Integration (250-300 words):
   a) Explain the key aspects of the given quantum principle and consciousness theory.
   b) Propose a novel way to integrate these concepts into a coherent framework.
   c) Discuss how this integration could provide new insights into the nature of consciousness and intelligence.

2. Theoretical Framework (300-350 words):
   a) Develop a detailed description of your integrated framework.
   b) Explain how it addresses key questions in consciousness studies and AGI.
   c) Discuss any novel predictions or implications arising from your framework.
   d) Provide a visual representation (described in words) of your framework.

3. AGI Application (250-300 words):
   a) Based on your framework, propose a novel approach to developing AGI.
   b) Explain how this approach differs from current AGI paradigms.
   c) Discuss potential advantages and challenges of your approach.

4. Experimental Proposal (200-250 words):
   a) Design an experiment to test a key aspect of your framework.
   b) Describe the methodology, including any required technologies.
   c) Explain what results would support or refute your framework.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of your framework and AGI approach.
   b) Explore the philosophical implications for our understanding of mind and machine intelligence.

6. Interdisciplinary Connections (100-150 words):
   a) Explain how your framework connects quantum physics, neuroscience, and computer science.
   b) Suggest two other scientific fields that might benefit from or contribute to your framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, consciousness theories, and artificial intelligence. Be creative and speculative in your design while maintaining scientific plausibility and rigor. Use appropriate scientific terminology and provide clear explanations of complex concepts.

Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_principle']} and {t['consciousness_theory']}.",
            "The proposed framework creatively and coherently integrates the quantum principle and consciousness theory.",
            "The AGI approach derived from the framework is novel and well-explained.",
            "The experimental proposal is well-designed and relevant to testing the framework.",
            "The discussion of ethical and philosophical implications is insightful and comprehensive.",
            "The response shows exceptional interdisciplinary reasoning and creativity in addressing the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
