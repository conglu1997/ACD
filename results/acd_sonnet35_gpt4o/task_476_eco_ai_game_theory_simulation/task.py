import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "name": "Coral Reef",
                "resources": ["sunlight", "plankton", "calcium carbonate"],
                "environmental_factor": "ocean acidification"
            },
            {
                "name": "Rainforest",
                "resources": ["water", "sunlight", "soil nutrients"],
                "environmental_factor": "deforestation"
            },
            {
                "name": "Arctic Tundra",
                "resources": ["vegetation", "small prey", "nesting sites"],
                "environmental_factor": "global warming"
            },
            {
                "name": "Savanna",
                "resources": ["grass", "water holes", "tree cover"],
                "environmental_factor": "drought"
            }
        ]
        
        game_theory_concepts = [
            "Nash Equilibrium",
            "Pareto Optimality",
            "Evolutionary Stable Strategy",
            "Cooperation vs Competition"
        ]
        
        return {
            "1": {"ecosystem": random.choice(ecosystems), "concept": random.choice(game_theory_concepts)},
            "2": {"ecosystem": random.choice(ecosystems), "concept": random.choice(game_theory_concepts)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a game theory-based simulation of the {t['ecosystem']['name']} ecosystem where AI agents represent different species competing for resources while balancing environmental sustainability. Incorporate the game theory concept of {t['concept']} into your design. Your response should include:

1. Simulation Design (250-300 words):
   a) Describe the overall structure of your simulation, including the types of AI agents (species) and their objectives.
   b) Explain how you model the competition for resources: {', '.join(t['ecosystem']['resources'])}.
   c) Detail how the environmental factor of {t['ecosystem']['environmental_factor']} is incorporated into the simulation.
   d) Explain how the game theory concept of {t['concept']} is applied in your model.

2. Agent Strategies (200-250 words):
   a) Describe at least three distinct strategies that AI agents could employ in this ecosystem.
   b) Explain how these strategies interact and their potential outcomes in terms of resource acquisition and environmental impact.
   c) Discuss how the chosen game theory concept influences the development or selection of these strategies.

3. Sustainability Mechanics (200-250 words):
   a) Explain how your simulation models environmental sustainability.
   b) Describe the trade-offs between individual agent success and overall ecosystem health.
   c) Propose a mechanism for agents to learn and adapt their strategies based on environmental feedback.

4. Simulation Outcomes (150-200 words):
   a) Predict potential equilibrium states or long-term outcomes of your simulation.
   b) Discuss how these outcomes might change under different initial conditions or perturbations.
   c) Explain how these outcomes relate to real-world ecological phenomena in the chosen ecosystem.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using such a simulation for ecological modeling or decision-making.
   b) Address any potential biases or limitations in your model and how they might be mitigated.

Ensure your response demonstrates a deep understanding of game theory, ecological principles, and artificial intelligence. Be creative in your approach while maintaining scientific plausibility and rigor. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should clearly incorporate principles from game theory, ecology, and artificial intelligence, specifically modeling the {t['ecosystem']['name']} ecosystem.",
            f"The simulation design should effectively integrate the game theory concept of {t['concept']}.",
            f"The response should address competition for the specified resources: {', '.join(t['ecosystem']['resources'])}.",
            f"The environmental factor of {t['ecosystem']['environmental_factor']} should be meaningfully incorporated into the simulation design.",
            "The proposed AI agent strategies should be diverse, well-reasoned, and demonstrate an understanding of ecological interactions.",
            "The sustainability mechanics should present a clear trade-off between individual agent success and overall ecosystem health.",
            "The predicted simulation outcomes should be plausible and relate to real-world ecological phenomena.",
            "The response should demonstrate creativity and interdisciplinary thinking while maintaining scientific plausibility.",
            "All five requested sections should be present and adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
