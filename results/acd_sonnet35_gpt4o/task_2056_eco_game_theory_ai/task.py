import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = ['Coral Reef', 'Rainforest', 'Arctic Tundra', 'Savanna', 'Wetland']
        game_theory_concepts = ['Nash Equilibrium', 'Evolutionary Stable Strategy', 'Pareto Optimality', 'Shapley Value', 'Stackelberg Competition']
        conservation_goals = ['Biodiversity Preservation', 'Carbon Sequestration', 'Water Resource Management', 'Invasive Species Control', 'Sustainable Resource Extraction']
        
        return {
            "1": {
                "ecosystem": random.choice(ecosystems),
                "game_theory_concept": random.choice(game_theory_concepts),
                "conservation_goal": random.choice(conservation_goals)
            },
            "2": {
                "ecosystem": random.choice(ecosystems),
                "game_theory_concept": random.choice(game_theory_concepts),
                "conservation_goal": random.choice(conservation_goals)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses game theory to model and manage complex ecological interactions in a {t['ecosystem']} ecosystem. Your system should incorporate the game theory concept of {t['game_theory_concept']} and focus on the conservation goal of {t['conservation_goal']}. Then, analyze its potential for environmental conservation and resource management. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for ecological modeling and management.
   b) Explain how your system integrates game theory, ecological principles, and machine learning algorithms.
   c) Detail how the system is tailored to the specified ecosystem, game theory concept, and conservation goal.
   d) Include a brief diagram or flowchart of your system's architecture (describe it textually).

2. Game Theory Model (250-300 words):
   a) Explain how you apply the specified game theory concept to model ecological interactions in the given ecosystem.
   b) Provide an example of how your model represents a specific ecological scenario or interaction.
   c) Discuss how your model captures the complexities and dynamics of the ecosystem.

3. AI Decision-Making Process (250-300 words):
   a) Describe how your AI system makes decisions to achieve the specified conservation goal.
   b) Explain how the system balances competing interests and optimizes for long-term sustainability.
   c) Discuss any learning mechanisms or adaptive strategies incorporated into your system.

4. Data Requirements and Collection (200-250 words):
   a) Outline the types of data your system requires to function effectively.
   b) Propose innovative methods for collecting and integrating ecological data into your system.
   c) Address challenges in data acquisition and how your system handles uncertainty or incomplete information.

5. Simulation and Prediction (200-250 words):
   a) Describe how your system simulates future ecological scenarios and predicts outcomes.
   b) Explain how these simulations inform conservation strategies and resource management decisions.
   c) Discuss the limitations and potential biases in your simulation approach.

6. Practical Applications and Impact (200-250 words):
   a) Propose two specific applications of your system in real-world conservation efforts.
   b) Analyze the potential impact of your system on environmental policy and decision-making.
   c) Discuss how your approach could be scaled or adapted to other ecosystems or conservation challenges.

7. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues or unintended consequences of implementing your system.
   b) Discuss how these ethical considerations might be addressed or mitigated.
   c) Acknowledge limitations of your approach and areas where human expertise remains crucial.

Ensure your response demonstrates a deep understanding of ecology, game theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and ecological soundness.

Format your response with clear headings for each section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['ecosystem']} ecosystem and its ecological interactions.",
            f"The game theory concept of {t['game_theory_concept']} is accurately applied and well-integrated into the AI system design.",
            f"The AI system effectively addresses the conservation goal of {t['conservation_goal']}.",
            "The system architecture is well-explained and integrates ecological principles, game theory, and AI algorithms coherently.",
            "The response includes creative and plausible solutions for data collection, simulation, and real-world application of the system.",
            "Ethical considerations and limitations of the approach are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
