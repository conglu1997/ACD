import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        conceptual_domains = [
            {
                "domain1": "Music",
                "domain2": "Mathematics",
                "target_capability": "Creative Problem Solving"
            },
            {
                "domain1": "Quantum Mechanics",
                "domain2": "Cognitive Psychology",
                "target_capability": "Decision Making"
            },
            {
                "domain1": "Ecology",
                "domain2": "Economics",
                "target_capability": "Resource Management"
            },
            {
                "domain1": "Neurobiology",
                "domain2": "Computer Networks",
                "target_capability": "Information Processing"
            }
        ]
        return {
            "1": random.choice(conceptual_domains),
            "2": random.choice(conceptual_domains)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and apply the theory of conceptual blending to design a novel AI architecture that combines principles from {t['domain1']} and {t['domain2']} to enhance the AI's capabilities in {t['target_capability']}. Then, evaluate the potential impact of this architecture on AI capabilities and human-AI interaction.

Provide your response in the following format:

1. Conceptual Analysis (200-250 words):
   a) Briefly explain the key principles or concepts from both {t['domain1']} and {t['domain2']} that you will use in your conceptual blend.
   b) Describe how these concepts might interact or complement each other in the context of {t['target_capability']}.
   c) Identify any potential challenges or conflicts in blending these domains.

2. Blended AI Architecture Design (300-350 words):
   a) Present your novel AI architecture that combines elements from both domains.
   b) Explain how this architecture incorporates the key concepts identified earlier.
   c) Describe the main components or processes of your blended AI system.
   d) Discuss how your architecture specifically enhances the AI's capabilities in {t['target_capability']}.

3. Technical Feasibility (200-250 words):
   a) Analyze the technical feasibility of implementing your blended AI architecture.
   b) Discuss any new algorithms, data structures, or computational approaches required.
   c) Identify potential technical challenges and propose ways to overcome them.

4. Impact Analysis (200-250 words):
   a) Evaluate the potential impact of your blended AI architecture on overall AI capabilities.
   b) Discuss how this architecture might influence human-AI interaction and collaboration.
   c) Explore any ethical considerations or potential risks associated with your design.

5. Future Implications (150-200 words):
   a) Propose two potential applications of your blended AI architecture in fields beyond the original domains.
   b) Discuss how this approach to AI design might influence future research directions in artificial intelligence and cognitive science.

Ensure your response demonstrates a deep understanding of conceptual blending theory, the chosen conceptual domains, and artificial intelligence principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and technical plausibility.

Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of conceptual blending theory and its application to AI design.",
            "The blended AI architecture is innovative, well-explained, and effectively combines principles from both specified domains.",
            "The proposed architecture clearly addresses the enhancement of the specified target capability.",
            "The technical feasibility analysis is thorough and considers relevant challenges and potential solutions.",
            "The impact analysis provides meaningful insights into the effects on AI capabilities and human-AI interaction.",
            "The discussion of future implications is insightful and considers broader applications and research directions.",
            "The submission is well-structured with clear sections as requested in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
