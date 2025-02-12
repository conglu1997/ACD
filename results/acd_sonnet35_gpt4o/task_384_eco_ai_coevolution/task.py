import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ecosystem": "Coral Reef",
                "ai_role": "Pollution Mitigation",
                "key_species": "Coral Polyps"
            },
            {
                "ecosystem": "Temperate Forest",
                "ai_role": "Fire Management",
                "key_species": "Coniferous Trees"
            },
            {
                "ecosystem": "Arctic Tundra",
                "ai_role": "Climate Adaptation",
                "key_species": "Polar Bears"
            },
            {
                "ecosystem": "Savanna Grassland",
                "ai_role": "Grazing Optimization",
                "key_species": "Acacia Trees"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a simulated ecosystem where AI agents and biological species coevolve in a {t['ecosystem']} environment. The AI's primary role is {t['ai_role']}, and a key species in this ecosystem is {t['key_species']}. Your task is to create a detailed proposal for this eco-AI coevolution simulation, addressing the following points:

1. Ecosystem Design (200-250 words):
   - Describe the key components and interactions in your {t['ecosystem']} ecosystem.
   - Explain the role and behavior of the {t['key_species']} in this ecosystem.
   - Outline how the AI agents are integrated into the ecosystem for {t['ai_role']}.

2. Coevolution Mechanics (250-300 words):
   - Detail the mechanisms by which the AI agents and biological species (especially {t['key_species']}) coevolve.
   - Explain how the AI learns and adapts its {t['ai_role']} strategies over time.
   - Describe how the biological species evolve in response to the AI's actions.
   - Include at least one specific example of a potential coevolutionary pathway.

3. Game Theory Analysis (200-250 words):
   - Identify the key players (AI and biological) and their potential strategies.
   - Analyze the potential equilibria that might emerge in this system.
   - Discuss how the payoff structure for different strategies might change over time due to coevolution.

4. Long-term Consequences (200-250 words):
   - Predict potential long-term outcomes of this coevolution (consider timeframes of 50, 100, and 500 years).
   - Discuss possible unintended consequences of the AI's {t['ai_role']} role.
   - Analyze how this coevolution might affect biodiversity and ecosystem stability.

5. Ethical Implications (150-200 words):
   - Discuss the ethical considerations of integrating AI into natural ecosystems for {t['ai_role']}.
   - Propose guidelines for responsible development and deployment of such AI systems in ecological contexts.

6. Simulation Proposal (150-200 words):
   - Outline a computational approach to simulate this eco-AI coevolution.
   - Describe key variables, processes, and outputs of your proposed simulation.
   - Explain how you would validate the simulation results.

Ensure your response demonstrates a deep understanding of ecological principles, game theory, AI behavior, and complex systems dynamics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of ecosystem dynamics, AI behavior, and coevolutionary processes.",
            f"The ecosystem design effectively incorporates the {t['ecosystem']} environment, the role of {t['key_species']}, and the AI's {t['ai_role']} function.",
            "The coevolution mechanics are well-explained and plausible, with a clear example provided.",
            "The game theory analysis identifies relevant players, strategies, and potential equilibria.",
            "Long-term consequences are thoughtfully considered across multiple timeframes.",
            "Ethical implications are thoroughly discussed with responsible guidelines proposed.",
            "The simulation proposal outlines a feasible computational approach with key variables and validation methods.",
            "The response maintains scientific rigor while showcasing creativity in system design and analysis.",
            "The response is well-structured and addresses all required points comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
