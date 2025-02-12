import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "concept": "justice",
                "environment": "resource_scarcity",
                "generations": 100
            },
            "2": {
                "concept": "beauty",
                "environment": "rapid_technological_change",
                "generations": 150
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the evolution of the abstract concept '{t['concept']}' within a population of artificial agents over {t['generations']} generations. Your system should incorporate principles from memetics, cognitive science, and evolutionary algorithms. The simulation should take place in an environment characterized by {t['environment']}.

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating conceptual evolution.
   b) Explain how your system models individual agents and their cognitive processes.
   c) Discuss how concepts are represented and manipulated within the system.
   d) Outline the mechanisms for concept transmission, mutation, and selection.

2. Evolutionary Process (200-250 words):
   a) Detail how your system simulates the evolution of the given concept over multiple generations.
   b) Explain how the specified environment influences the evolutionary process.
   c) Describe any unique features of your evolutionary algorithm tailored to concept evolution.

3. Cognitive Model (200-250 words):
   a) Explain how your system models the cognitive processes involved in concept understanding and manipulation.
   b) Discuss how individual differences in cognitive abilities are represented and how they affect concept evolution.
   c) Describe how your model accounts for the formation of new conceptual connections or innovations.

4. Simulation and Analysis (250-300 words):
   a) Provide a detailed example of how the concept might evolve over several generations in your system.
   b) Describe the metrics and methods you would use to analyze the evolution of the concept.
   c) Discuss any emergent phenomena or unexpected results you might anticipate from the simulation.
   d) Explain how you would validate the results of your simulation against real-world conceptual evolution.

5. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your system for understanding cultural evolution and cognitive processes.
   b) Propose two novel applications of your conceptual evolution simulator in fields such as education, AI ethics, or social sciences.
   c) Address any ethical considerations or potential misuses of this technology.

Ensure your response demonstrates a deep understanding of memetics, cognitive science, and evolutionary algorithms. Use appropriate terminology and provide clear explanations. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1050-1300 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of memetics, cognitive science, and evolutionary algorithms.",
            "The system architecture is well-designed and incorporates all required elements.",
            "The evolutionary process is clearly explained and takes into account the specified environment.",
            "The cognitive model is sophisticated and accounts for individual differences and concept manipulation.",
            "The simulation and analysis section provides a detailed and plausible example of concept evolution.",
            "The implications and applications are thoughtfully considered and novel.",
            "The response is creative while maintaining scientific plausibility.",
            "The response addresses all required sections and stays within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0