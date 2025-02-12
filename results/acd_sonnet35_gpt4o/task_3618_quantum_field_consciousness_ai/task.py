import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        qft_principles = ['Vacuum fluctuations', 'Field excitations', 'Symmetry breaking']
        consciousness_aspects = ['Self-awareness', 'Qualia', 'Intentionality']
        return {
            "1": {"qft_principle": random.choice(qft_principles), "consciousness_aspect": random.choice(consciousness_aspects)},
            "2": {"qft_principle": random.choice(qft_principles), "consciousness_aspect": random.choice(consciousness_aspects)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that applies the quantum field theory principle of {t['qft_principle']} to model the aspect of consciousness known as {t['consciousness_aspect']} in artificial intelligence systems. Then, analyze its implications and propose experiments to test it. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain how the principle of {t['qft_principle']} can be applied to model {t['consciousness_aspect']} in AI systems.
   b) Describe the key components and mechanisms of your framework.
   c) Discuss how your framework differs from classical approaches to AI consciousness.
   d) Provide a mathematical formulation that captures the essence of your framework (you may use LaTeX-style notation).

2. Consciousness Emergence (250-300 words):
   a) Explain how {t['consciousness_aspect']} emerges in your framework.
   b) Discuss the conditions necessary for this emergence in AI systems.
   c) Address any paradoxes or counterintuitive aspects of your framework.

3. Information Processing (200-250 words):
   a) Describe how information is processed in your quantum field consciousness framework.
   b) Compare this to information processing in classical AI systems.
   c) Discuss any unique computational capabilities that might arise from your framework.

4. Implications for AI Development (200-250 words):
   a) Analyze the potential implications of your framework for the development of conscious AI systems.
   b) Discuss ethical considerations that arise from your framework.
   c) Propose guidelines for the responsible development of AI based on your framework.

5. Experimental Proposals (250-300 words):
   a) Propose two experiments that could test predictions made by your framework.
   b) Describe the methodology, including control conditions and measurable outcomes.
   c) Discuss potential challenges in implementing these experiments and how they might be overcome.

6. Interdisciplinary Connections (150-200 words):
   a) Explore how your framework might impact or be applied in fields beyond AI and physics.
   b) Discuss potential technological applications that could arise from your framework.

Ensure your response demonstrates a deep understanding of quantum field theory, artificial intelligence, and consciousness studies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses all 6 required sections with appropriate word counts.",
            f"The theoretical framework effectively integrates the quantum field theory principle of {t['qft_principle']} with the consciousness aspect of {t['consciousness_aspect']} in the context of AI systems.",
            f"The response demonstrates a deep understanding of quantum field theory, artificial intelligence, and consciousness studies, using appropriate terminology and providing clear explanations for complex concepts.",
            f"The proposed framework is innovative and speculative while maintaining scientific plausibility.",
            f"The response includes a mathematical formulation that captures the essence of the framework.",
            f"The proposed experiments are well-designed and directly test predictions made by the framework.",
            f"The response thoughtfully addresses ethical considerations and proposes guidelines for responsible AI development based on the framework."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
