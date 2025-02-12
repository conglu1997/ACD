import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "dilemma": "Tragedy of the Commons",
                "resource": "shared water supply",
                "behavior": "cooperation",
                "evolutionary_factor": "climate change"
            },
            {
                "dilemma": "Public Goods Game",
                "resource": "community fund",
                "behavior": "free-riding",
                "evolutionary_factor": "technological advancement"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a multi-agent simulation of an evolving social dilemma, incorporating principles from game theory, evolutionary psychology, and behavioral economics. Your task involves the following steps:

1. Simulation Design (300-350 words):
   a) Describe the key components of your multi-agent simulation for the {t['dilemma']} scenario.
   b) Explain how you model individual agents, their decision-making processes, and interactions.
   c) Detail how you incorporate the {t['resource']} as the central resource in your simulation.
   d) Describe how you implement evolutionary mechanisms to allow strategies to adapt over time.

2. Game Theory Integration (200-250 words):
   a) Explain how you apply game theory principles to model the {t['dilemma']} scenario.
   b) Describe the payoff structure for different agent behaviors, particularly {t['behavior']}.
   c) Discuss how you handle imperfect information and bounded rationality in your model.

3. Evolutionary Dynamics (250-300 words):
   a) Describe how agent strategies evolve over multiple generations in your simulation.
   b) Explain how you model the impact of {t['evolutionary_factor']} on the evolutionary process.
   c) Discuss any emergent behaviors or equilibria you expect to observe, and why.

4. Behavioral Economics Factors (200-250 words):
   a) Identify key behavioral economics principles you incorporate into your simulation.
   b) Explain how these factors influence agent decision-making and overall system dynamics.
   c) Discuss how your model accounts for cognitive biases and heuristics.

5. Simulation Analysis (250-300 words):
   a) Describe the key metrics and methods you would use to analyze the simulation results.
   b) Explain how you would validate your model against real-world data or existing theories.
   c) Discuss potential insights your simulation might provide about human behavior in social dilemmas.

6. Ethical Considerations and Applications (150-200 words):
   a) Discuss ethical implications of using such simulations to understand and potentially influence human behavior.
   b) Propose two potential real-world applications of your simulation, beyond academic research.
   c) Address any concerns about the potential misuse of insights gained from your model.

Ensure your response demonstrates a deep understanding of game theory, evolutionary psychology, and behavioral economics. Use appropriate terminology from these fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Simulation Design section must clearly explain how the {t['dilemma']} scenario is modeled and how the {t['resource']} is incorporated as the central resource.",
            f"The Game Theory Integration section should establish a clear payoff structure that addresses the {t['behavior']} behavior.",
            f"The Evolutionary Dynamics section must explain how agent strategies evolve over time and how {t['evolutionary_factor']} impacts this process.",
            "The Behavioral Economics Factors section should identify and explain relevant principles and how they influence agent decision-making.",
            "The Simulation Analysis section must propose valid metrics and methods for analyzing and validating the simulation results.",
            "The response must adhere to the specified word counts for each section, with a total word count between 1350-1650 words.",
            "The overall response must demonstrate interdisciplinary knowledge, creativity, and critical thinking in the domains of game theory, evolutionary psychology, and behavioral economics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
