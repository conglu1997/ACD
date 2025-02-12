import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "swarm_type": "Foraging ants",
                "environment": "2D grid with scattered food sources",
                "collective_goal": "Optimize food collection efficiency",
                "evolutionary_pressure": "Resource scarcity"
            },
            {
                "swarm_type": "Schooling fish",
                "environment": "3D ocean with predators",
                "collective_goal": "Enhance group survival rate",
                "evolutionary_pressure": "Predation"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a computational model that simulates the emergence of collective intelligence in artificial swarms, integrating principles from complex systems theory, evolutionary biology, and artificial intelligence. Focus on {t['swarm_type']} in a {t['environment']} with the collective goal of {t['collective_goal']}, considering the evolutionary pressure of {t['evolutionary_pressure']}. Your response should include:

1. Model Design (300-350 words):
   a) Describe the key components of your swarm intelligence model, including individual agent properties and behaviors.
   b) Explain how your model incorporates principles from complex systems theory and evolutionary biology.
   c) Detail the mechanisms for agent interaction and information sharing within the swarm.
   d) Describe how the model simulates the evolutionary pressure and its effect on the swarm.
   e) Include a simple pseudocode or algorithm outlining the core logic of your model.

2. Emergence of Collective Intelligence (250-300 words):
   a) Explain how collective intelligence emerges from individual agent behaviors in your model.
   b) Discuss the role of self-organization and adaptation in this process.
   c) Describe any novel or unexpected behaviors that might emerge from the system.
   d) Analyze how the collective goal is achieved through emergent behaviors.

3. Mathematical Framework (200-250 words):
   a) Provide a mathematical representation of key aspects of your model (e.g., agent decision-making, swarm dynamics).
   b) Explain how your mathematical framework captures the emergence of collective intelligence.
   c) Include at least one equation or formula central to your model's functioning.

4. Simulation and Analysis (250-300 words):
   a) Describe how you would implement and run a simulation of your model.
   b) Explain the key parameters and variables you would measure or observe.
   c) Discuss how you would analyze the simulation results to evaluate the emergence of collective intelligence.
   d) Propose a method to quantify the efficiency or success of the swarm in achieving its collective goal.

5. Implications and Applications (200-250 words):
   a) Discuss potential real-world applications of your swarm intelligence model.
   b) Analyze how insights from your model might contribute to our understanding of natural swarm systems.
   c) Explore potential implications for designing artificial swarm systems (e.g., robot swarms, distributed AI systems).

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss any ethical considerations in applying swarm intelligence principles to artificial systems.
   b) Identify potential limitations or challenges of your model.
   c) Propose future research directions to address these limitations or extend the model.

Ensure your response demonstrates a deep understanding of complex systems theory, evolutionary biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of complex systems theory, evolutionary biology, and artificial intelligence.",
            "The model design is comprehensive, incorporating principles from all required fields and addressing all specified components.",
            "The explanation of emergent collective intelligence is clear and well-reasoned.",
            "The mathematical framework is appropriate and well-explained.",
            "The simulation and analysis section provides a clear and feasible approach to implementing and evaluating the model.",
            "The discussion of implications, applications, and ethical considerations is thoughtful and insightful.",
            "The response is creative and innovative while maintaining scientific plausibility.",
            f"The model appropriately addresses the specific scenario of {t['swarm_type']} in a {t['environment']} with the goal of {t['collective_goal']} and evolutionary pressure of {t['evolutionary_pressure']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
