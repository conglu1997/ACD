import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        qft_principles = [
            {
                'principle': 'vacuum fluctuations',
                'info_theory_concept': 'entropy',
                'decision_making_aspect': 'uncertainty handling'
            },
            {
                'principle': 'quantum entanglement',
                'info_theory_concept': 'mutual information',
                'decision_making_aspect': 'multi-agent coordination'
            }
        ]
        return {str(i+1): principle for i, principle in enumerate(random.sample(qft_principles, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a speculative artificial general intelligence (AGI) architecture based on principles from quantum field theory and information theory, and analyze its potential implications for consciousness and decision-making. Your AGI architecture should incorporate the following elements:

- Quantum field theory principle: {t['principle']}
- Information theory concept: {t['info_theory_concept']}
- Decision-making aspect to focus on: {t['decision_making_aspect']}

Your response should include the following sections:

1. Theoretical Foundation (250-300 words):
   a) Explain the key aspects of the given quantum field theory principle and information theory concept.
   b) Discuss how these concepts could be relevant to AGI and consciousness.
   c) Propose a novel way to integrate these concepts into a coherent AGI framework.

2. AGI Architecture Design (300-350 words):
   a) Describe the key components of your quantum field theory-inspired AGI architecture.
   b) Explain how your architecture incorporates the given QFT principle and information theory concept.
   c) Detail how your design addresses the specified decision-making aspect.
   d) Provide a high-level diagram or pseudocode representing a key process in your AGI system (describe it textually).

3. Consciousness and Cognition Model (250-300 words):
   a) Propose how consciousness might emerge in your AGI architecture.
   b) Explain how your model accounts for key aspects of cognition (e.g., memory, learning, reasoning).
   c) Discuss any novel predictions your model makes about the nature of consciousness or intelligence.

4. Decision-Making Framework (200-250 words):
   a) Describe how your AGI architecture approaches the specified decision-making aspect.
   b) Explain how this approach differs from classical AI decision-making methods.
   c) Discuss potential advantages and challenges of your approach.

5. Ethical and Philosophical Implications (150-200 words):
   a) Analyze the ethical considerations of developing AGI based on quantum field theory principles.
   b) Discuss the philosophical implications of your model for our understanding of mind, consciousness, and reality.
   c) Propose guidelines for responsible development and use of such AGI systems.

6. Experimental Proposal (150-200 words):
   a) Design a hypothetical experiment to test a key aspect of your AGI architecture.
   b) Describe the methodology, including any required technologies (existing or speculative).
   c) Explain what results would support or refute your proposed model.

Ensure your response demonstrates a deep understanding of quantum field theory, information theory, and artificial intelligence. Be creative and speculative in your design while maintaining scientific plausibility and logical consistency. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your total response should be between 1300-1600 words. Format your answer with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['principle']} and {t['info_theory_concept']} in the context of AGI architecture design.",
            "The proposed AGI architecture is novel, coherent, and integrates quantum field theory principles with information theory concepts.",
            f"The decision-making framework effectively addresses {t['decision_making_aspect']} using the proposed architecture.",
            "The consciousness and cognition model is innovative and logically consistent with the proposed AGI architecture.",
            "The response shows critical thinking about the ethical and philosophical implications of the proposed AGI system.",
            "The experimental proposal is well-designed and relevant to testing the key aspects of the AGI architecture."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
