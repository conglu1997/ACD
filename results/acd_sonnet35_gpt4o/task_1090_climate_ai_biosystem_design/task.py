import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "climate_challenge": "Ocean acidification",
                "ecosystem": "Coral reefs",
                "ai_focus": "Predictive modeling"
            },
            {
                "climate_challenge": "Extreme weather events",
                "ecosystem": "Urban environments",
                "ai_focus": "Real-time adaptation"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven biosystem to mitigate the effects of {t['climate_challenge']} on {t['ecosystem']}, with a focus on {t['ai_focus']}. Your design should integrate synthetic biology, machine learning, and environmental science. Provide your response in the following format:

1. System Overview (250-300 words):
   a) Describe the key components of your AI-driven biosystem.
   b) Explain how these components interact to address the climate challenge.
   c) Outline how your system integrates synthetic biology, AI, and environmental science.

2. AI Architecture (200-250 words):
   a) Detail the AI architecture used in your system, focusing on {t['ai_focus']}.
   b) Explain how the AI component interacts with the biological elements.
   c) Discuss any novel machine learning approaches used in your design.

3. Synthetic Biology Design (200-250 words):
   a) Describe the engineered biological components in your system.
   b) Explain how these components are designed to mitigate {t['climate_challenge']}.
   c) Discuss any potential risks or challenges in implementing these biological designs.

4. Environmental Impact Analysis (150-200 words):
   a) Analyze the potential positive and negative impacts of your system on {t['ecosystem']}.
   b) Discuss how your system accounts for complex ecological interactions.
   c) Propose methods to monitor and mitigate any unintended consequences.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to your AI-driven biosystem.
   b) Discuss the implications of using synthetic biology to address climate change.
   c) Propose guidelines for responsible development and deployment of your system.

6. Scalability and Global Application (150-200 words):
   a) Explain how your system could be scaled up to address {t['climate_challenge']} globally.
   b) Discuss potential challenges in implementing your system in different regions.
   c) Propose a strategy for international cooperation in deploying your solution.

Ensure your response demonstrates a deep understanding of AI, synthetic biology, climate science, and their intersections. Be creative in your approach while maintaining scientific plausibility and addressing real-world challenges. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses the specific climate challenge of {t['climate_challenge']} in the context of {t['ecosystem']}.",
            f"The AI architecture focuses on {t['ai_focus']} and is well-integrated with the biological components.",
            "The synthetic biology design is creative, plausible, and directly addresses the climate challenge.",
            "The environmental impact analysis considers both positive and negative effects on the ecosystem.",
            "Ethical considerations are thoroughly discussed, including responsible development guidelines.",
            "The proposal for scalability and global application is realistic and considers international challenges.",
            "The response demonstrates a deep understanding of AI, synthetic biology, and climate science.",
            "The design is creative and innovative while maintaining scientific plausibility.",
            "The response is well-structured, following the specified format and word count (1100-1400 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
