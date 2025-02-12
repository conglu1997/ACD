import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        resources = ['freshwater', 'forests', 'fisheries', 'clean air']
        economic_systems = ['cap-and-trade', 'global tax', 'tradable quotas', 'international fund']
        return {
            "1": {
                "resource": random.choice(resources),
                "economic_system": random.choice(economic_systems)
            },
            "2": {
                "resource": random.choice(resources),
                "economic_system": random.choice(economic_systems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a global eco-economic system for managing {t['resource']} using a {t['economic_system']} approach. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components and mechanisms of your {t['economic_system']} system for managing {t['resource']}.
   b) Explain how your system incorporates principles from game theory and environmental science.
   c) Detail how the system incentivizes sustainable use of {t['resource']} while balancing economic growth.
   d) Address potential challenges in implementing this system on a global scale.

2. Mathematical Model (250-300 words):
   a) Develop a simple mathematical model that captures the core dynamics of your system.
   b) Define key variables and their relationships.
   c) Provide at least one equation or formula that represents a critical aspect of your system.
   d) Explain how your model accounts for factors such as resource regeneration, economic utility, and environmental impact.

3. Stakeholder Analysis (200-250 words):
   a) Identify key stakeholders in your global eco-economic system.
   b) Analyze how different stakeholders might respond to the system.
   c) Discuss potential strategies for addressing conflicting interests.

4. Long-term Projections (200-250 words):
   a) Use your model to project the long-term (50-100 years) outcomes of implementing your system.
   b) Discuss potential environmental and economic impacts.
   c) Identify key uncertainties or variables that could significantly affect outcomes.

5. Comparative Analysis (150-200 words):
   a) Compare your proposed system to current approaches for managing {t['resource']}.
   b) Discuss potential advantages and limitations of your system.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of your global eco-economic system.
   b) Address issues of equity, intergenerational justice, and potential unintended consequences.

Ensure your response demonstrates a deep understanding of economics, game theory, and environmental science. Use appropriate terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific and economic plausibility.

Your total response should be between 1250-1550 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of the {t['economic_system']} approach and its application to managing {t['resource']}.",
            "The mathematical model should be coherent and relevant to the proposed system.",
            "The analysis should show a deep understanding of game theory principles and their application to environmental resource management.",
            "The response should demonstrate creative problem-solving in addressing potential challenges and conflicts.",
            "The long-term projections should be logical and based on the proposed model.",
            "The comparative analysis should show a good understanding of current resource management approaches.",
            "The response should address ethical considerations thoughtfully and comprehensively.",
            "The overall response must demonstrate strong interdisciplinary knowledge integration and analytical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
