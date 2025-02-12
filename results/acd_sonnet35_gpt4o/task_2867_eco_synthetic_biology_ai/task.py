import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ecosystem_type": "marine",
                "environmental_challenge": "ocean acidification",
                "synthetic_biology_approach": "engineered coral symbionts",
                "ai_technique": "reinforcement learning"
            },
            {
                "ecosystem_type": "terrestrial",
                "environmental_challenge": "soil degradation",
                "synthetic_biology_approach": "designer microbiomes",
                "ai_technique": "evolutionary algorithms"
            },
            {
                "ecosystem_type": "freshwater",
                "environmental_challenge": "eutrophication",
                "synthetic_biology_approach": "engineered algae",
                "ai_technique": "deep learning"
            },
            {
                "ecosystem_type": "urban",
                "environmental_challenge": "air pollution",
                "synthetic_biology_approach": "bioengineered plants",
                "ai_technique": "multi-agent systems"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that integrates synthetic biology principles to create and optimize artificial ecosystems, then use it to propose solutions for environmental challenges. Focus on a {t['ecosystem_type']} ecosystem, addressing the challenge of {t['environmental_challenge']} using {t['synthetic_biology_approach']} and {t['ai_technique']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for designing and optimizing artificial ecosystems.
   b) Explain how your system integrates synthetic biology principles with {t['ai_technique']}.
   c) Detail how the system models and simulates {t['ecosystem_type']} ecosystems.
   d) Discuss any novel algorithms or approaches used in your system.

2. Synthetic Biology Integration (250-300 words):
   a) Explain how your system incorporates {t['synthetic_biology_approach']} to address {t['environmental_challenge']}.
   b) Describe the genetic engineering techniques your system would use or simulate.
   c) Discuss how your system predicts and optimizes the behavior of synthetic biological components in the ecosystem.

3. Environmental Challenge Solution (300-350 words):
   a) Propose a detailed solution to {t['environmental_challenge']} using your AI-driven synthetic biology approach.
   b) Explain how your solution leverages the strengths of both {t['ai_technique']} and {t['synthetic_biology_approach']}.
   c) Discuss potential risks and mitigation strategies for your proposed solution.
   d) Compare your approach to traditional methods of addressing this environmental challenge.

4. Simulation and Optimization Process (250-300 words):
   a) Describe how your AI system simulates the impact of synthetic biological interventions on the {t['ecosystem_type']} ecosystem.
   b) Explain how {t['ai_technique']} is used to optimize the synthetic biology designs and their deployment.
   c) Propose a method to validate your system's predictions and optimizations.

5. Ethical and Ecological Considerations (200-250 words):
   a) Discuss the ethical implications of using AI-driven synthetic biology to modify ecosystems.
   b) Address potential unintended consequences of your approach on biodiversity and ecosystem balance.
   c) Propose guidelines for responsible development and deployment of your technology.

6. Future Implications and Research Directions (150-200 words):
   a) Speculate on how your system could be extended to address other environmental challenges.
   b) Discuss potential long-term impacts of AI-driven synthetic biology on environmental conservation and restoration.
   c) Suggest areas for future research to enhance the integration of AI, synthetic biology, and environmental science.

Ensure your response demonstrates a deep understanding of synthetic biology, artificial intelligence, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. When using technical terms, briefly define or explain them to demonstrate your understanding. Be innovative in your approach while maintaining scientific plausibility and considering ethical implications.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, artificial intelligence, and environmental science.",
            "The proposed system effectively integrates AI techniques with synthetic biology principles.",
            "The solution addresses the given environmental challenge in a creative and plausible manner.",
            "The response considers ethical implications and potential risks of the proposed technology.",
            "The submission is well-structured, following the specified format and word count guidelines.",
            "Technical terms are used appropriately and explained when necessary."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
