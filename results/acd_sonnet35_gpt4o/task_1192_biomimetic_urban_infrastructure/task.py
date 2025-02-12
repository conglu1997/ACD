import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                'ecosystem': 'coral reef',
                'environmental_challenge': 'water management and filtration',
                'future_technology': 'smart materials'
            },
            {
                'ecosystem': 'redwood forest',
                'environmental_challenge': 'air purification and carbon sequestration',
                'future_technology': 'distributed energy systems'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(ecosystems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic urban infrastructure system inspired by a {t['ecosystem']} ecosystem, addressing the environmental challenge of {t['environmental_challenge']} and integrating with {t['future_technology']}. Your response should include:

1. Ecosystem Analysis (200-250 words):
   a) Describe the key features and processes of the {t['ecosystem']} ecosystem relevant to urban infrastructure design.
   b) Explain how these features address or relate to {t['environmental_challenge']}.
   c) Identify at least three specific biological mechanisms or structures that could be emulated.

2. Biomimetic Infrastructure Design (250-300 words):
   a) Present your urban infrastructure design, clearly explaining how it mimics the selected ecosystem features.
   b) Describe how your design addresses {t['environmental_challenge']}.
   c) Explain the integration of {t['future_technology']} into your biomimetic design.
   d) Include a basic schematic or diagram of your design (describe it textually).

3. Materials and Construction (150-200 words):
   a) Propose innovative materials inspired by the {t['ecosystem']} for use in your infrastructure.
   b) Describe the properties of these materials and how they contribute to the design's functionality.
   c) Outline any novel construction or manufacturing processes required for your design.

4. System Efficiency and Sustainability (200-250 words):
   a) Analyze the energy and resource efficiency of your biomimetic infrastructure system.
   b) Compare its performance to conventional urban infrastructure in addressing {t['environmental_challenge']}.
   c) Discuss the long-term sustainability and adaptability of your design.

5. Societal and Economic Impact (150-200 words):
   a) Examine the potential societal benefits and challenges of implementing your design.
   b) Analyze the economic implications, including initial costs and long-term savings.
   c) Discuss how your design might influence urban planning and development policies.

6. Ethical Considerations and Future Research (150-200 words):
   a) Identify potential ethical issues related to your biomimetic infrastructure design.
   b) Propose guidelines to ensure responsible development and implementation.
   c) Suggest two future research directions to enhance or expand your design.

Ensure your response demonstrates a deep understanding of ecology, materials science, environmental engineering, and urban planning. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility and addressing potential limitations or challenges. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design clearly draws inspiration from the {t['ecosystem']} ecosystem and addresses {t['environmental_challenge']}.",
            f"The integration of {t['future_technology']} is well-explained and relevant to the biomimetic design.",
            "The response demonstrates a deep understanding of ecology, materials science, environmental engineering, and urban planning.",
            "The design is innovative yet scientifically plausible, with clear explanations of biological mechanisms being emulated.",
            "The analysis of system efficiency, sustainability, and societal impact is thorough and well-reasoned.",
            "Ethical considerations are thoughtfully addressed, and future research directions are insightful.",
            "The response shows a high level of interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
