import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Resource Competition",
                "agents": ["Cooperators", "Defectors", "Punishers"],
                "environment": "Finite, renewable resource pool"
            },
            {
                "name": "Information Sharing",
                "agents": ["Honest", "Deceptive", "Skeptical"],
                "environment": "Dynamic information landscape"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a multi-agent simulation based on evolutionary game theory principles, focusing on the emergence of cooperation in complex adaptive systems. Your task involves the following steps:

1. Simulation Design (300-350 words):
   a) Describe the key components of your multi-agent simulation for the scenario: {t['name']}
   b) Explain how you model the interactions between agent types: {', '.join(t['agents'])}
   c) Detail how you represent and update the {t['environment']}
   d) Describe your approach to modeling evolutionary dynamics in the system

2. Game Theoretical Framework (250-300 words):
   a) Define the payoff structure for interactions between agent types
   b) Explain how your model incorporates concepts from evolutionary game theory
   c) Describe any novel game theoretical concepts or extensions you've introduced

3. Implementation Details (200-250 words):
   a) Outline the algorithms used for agent decision-making and system evolution
   b) Describe how you handle stochasticity and uncertainty in the simulation
   c) Explain your approach to balancing computational efficiency and model complexity

4. Simulation Analysis (250-300 words):
   a) Describe the key metrics you use to analyze the simulation outcomes
   b) Present and interpret the results of a sample simulation run
   c) Discuss any emergent behaviors or unexpected outcomes observed
   d) Explain how your simulation demonstrates the emergence (or lack) of cooperation

5. Theoretical Implications (150-200 words):
   a) Discuss how your simulation results relate to existing theories of cooperation
   b) Propose a novel hypothesis or theoretical extension based on your findings
   c) Suggest how your model could be applied to real-world cooperative dilemmas

6. Limitations and Extensions (150-200 words):
   a) Identify potential limitations of your simulation model
   b) Propose two extensions or modifications to address these limitations
   c) Suggest one way your simulation could be adapted to study a different complex system

Ensure your response demonstrates a deep understanding of game theory, complex systems, and multi-agent simulations. Use appropriate terminology and provide explanations where necessary. Be creative in your approach while maintaining scientific rigor and plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of evolutionary game theory and complex systems in the context of the '{t['name']}' scenario.",
            "The simulation design is well-explained, creative, and addresses all required components, including agent types and environment.",
            "The game theoretical framework is sound and incorporates relevant concepts from evolutionary game theory.",
            "Implementation details are clear and demonstrate a balance between computational efficiency and model complexity.",
            "The simulation analysis is thorough, with meaningful interpretation of results and discussion of emergent behaviors.",
            "Theoretical implications are well-reasoned and demonstrate novel thinking about cooperation in complex systems.",
            "Limitations are honestly addressed, and proposed extensions show creative thinking about future applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
