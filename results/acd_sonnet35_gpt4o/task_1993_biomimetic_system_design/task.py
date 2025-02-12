import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                'challenge': 'Sustainable urban water management',
                'organism1': 'Namibian desert beetle',
                'organism2': 'Mangrove trees'
            },
            {
                'challenge': 'Noise reduction in high-speed transportation',
                'organism1': 'Owl feathers',
                'organism2': 'Dolphin skin'
            }
        ]
        return {str(i+1): task for i, task in enumerate(challenges)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic system to address the challenge of {t['challenge']} by drawing inspiration from {t['organism1']} and {t['organism2']}. Your response should include:

1. Biological Analysis (200-250 words):
   a) Describe the relevant mechanisms or properties of {t['organism1']} and {t['organism2']}.
   b) Explain how these biological features help the organisms in their natural environments.
   c) Identify the key principles that could be applied to the human challenge.

2. Biomimetic System Design (250-300 words):
   a) Propose a system that addresses {t['challenge']} using principles derived from both organisms.
   b) Explain how your design incorporates and adapts the biological mechanisms.
   c) Describe the key components and processes of your biomimetic system.
   d) Include a simple diagram or sketch of your proposed system.

3. Performance Analysis (150-200 words):
   a) Discuss the potential benefits of your biomimetic system compared to conventional solutions.
   b) Analyze any limitations or challenges in implementing your design.
   c) Propose metrics to evaluate the effectiveness of your system.

4. Interdisciplinary Connections (150-200 words):
   a) Explain how your design integrates knowledge from biology, engineering, and other relevant fields.
   b) Discuss how this biomimetic approach might lead to new insights in the contributing disciplines.

5. Ethical and Sustainability Considerations (100-150 words):
   a) Analyze the environmental impact of your proposed system.
   b) Discuss any ethical implications of mimicking biological systems for human use.
   c) Propose guidelines for responsible development and implementation of biomimetic technologies.

Ensure your response demonstrates a deep understanding of the biological mechanisms, creative application of these principles to the human challenge, and critical analysis of the proposed solution. Use appropriate technical terminology and provide clear explanations for complex concepts.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a thorough understanding of the biological mechanisms in {t['organism1']} and {t['organism2']}.",
            f"The proposed biomimetic system effectively addresses the challenge of {t['challenge']} by creatively applying principles from both organisms.",
            "The design is innovative, scientifically plausible, and well-explained.",
            "The analysis shows critical thinking about the system's performance, limitations, and broader implications.",
            "The response integrates knowledge from multiple disciplines and considers ethical and sustainability aspects."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
