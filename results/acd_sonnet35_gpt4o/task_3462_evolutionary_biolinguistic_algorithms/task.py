import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        organisms = ['marine invertebrates', 'social insects', 'arboreal mammals']
        communication_features = ['chemical signaling', 'bioluminescence', 'vocalizations']
        return {
            "1": {"organism": random.choice(organisms),
                   "communication_feature": random.choice(communication_features)},
            "2": {"organism": random.choice(organisms),
                   "communication_feature": random.choice(communication_features)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an evolutionary algorithm that simulates the co-evolution of {t['organism']} and their communication systems, focusing on {t['communication_feature']}. Then, use this algorithm to predict potential future developments in both the organisms' biology and their communication methods. Your response should include:

1. Algorithm Design (300-350 words):
   a) Describe the key components of your evolutionary algorithm.
   b) Explain how it models the co-evolution of biological traits and communication systems.
   c) Detail how you incorporate {t['communication_feature']} into the model.
   d) Provide a pseudocode representation of your algorithm (at least 15 lines long) with comments explaining key steps.
   e) Give two specific examples of how biological traits are encoded in your algorithm (e.g., gene representation).

2. Biological-Linguistic Interface (250-300 words):
   a) Explain how your algorithm translates between biological traits and communication features.
   b) Describe the fitness function(s) used to evaluate evolutionary success.
   c) Discuss how environmental factors are incorporated into the model.
   d) Provide a mathematical formula for at least one aspect of your model (e.g., fitness calculation).

3. Simulation Results (250-300 words):
   a) Describe a simulated run of your algorithm over 1000 generations.
   b) Highlight key evolutionary changes observed in both biology and communication.
   c) Explain any unexpected or emergent properties that arose during the simulation.
   d) Include a graph or table representing a key aspect of your simulation results.

4. Future Predictions (200-250 words):
   a) Based on your simulation, predict three potential future developments in the biology of {t['organism']}.
   b) Predict three potential future developments in their {t['communication_feature']} systems.
   c) Discuss the potential ecological and evolutionary implications of these changes.
   d) Rank your predictions in order of likelihood and explain your reasoning.

5. Comparative Analysis (200-250 words):
   a) Compare your algorithm's predictions to current evolutionary theories about {t['organism']}.
   b) Discuss how your model might inform or challenge existing ideas in biolinguistics.
   c) Propose an experiment to test one of your algorithm's predictions in real-world conditions.
   d) Discuss potential limitations or biases in your evolutionary algorithm and how they might affect the results.

6. Ethical and Practical Implications (150-200 words):
   a) Discuss potential applications of your algorithm in conservation biology or linguistics.
   b) Address any ethical considerations in using predictive evolutionary models.
   c) Propose guidelines for the responsible use of such algorithms in scientific research.
   d) Suggest a method for validating the accuracy of long-term evolutionary predictions.

Ensure your response demonstrates a deep understanding of evolutionary biology, linguistics, and computer science. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of evolutionary biology, linguistics, and computer science.",
            "The proposed algorithm creatively and plausibly models the co-evolution of biological traits and communication systems.",
            f"The algorithm and simulation specifically address {t['organism']} and {t['communication_feature']}.",
            "The answer covers all required sections with appropriate detail and word count.",
            "The response shows clear interdisciplinary thinking and novel approaches to complex scientific challenges.",
            "The proposed future predictions and comparative analysis are insightful and well-reasoned.",
            "The response includes a clear pseudocode representation of the algorithm with at least 15 lines and explanatory comments.",
            "The response provides specific examples of how biological traits are encoded in the algorithm.",
            "The response includes a mathematical formula for at least one aspect of the model.",
            "The response includes a graph or table representing a key aspect of the simulation results.",
            "The response discusses potential limitations or biases in the evolutionary algorithm.",
            "The response suggests a method for validating the accuracy of long-term evolutionary predictions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
