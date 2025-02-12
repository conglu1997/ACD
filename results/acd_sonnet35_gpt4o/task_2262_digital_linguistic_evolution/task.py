import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "linguistic_feature": "phonological rules",
                "evolutionary_pressure": "information density",
                "computational_constraint": "limited memory"
            },
            "2": {
                "linguistic_feature": "syntactic structures",
                "evolutionary_pressure": "energy efficiency",
                "computational_constraint": "processing speed"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a digital ecosystem that simulates the evolution of language, focusing on the linguistic feature of {t['linguistic_feature']}. Your ecosystem should incorporate evolutionary pressure towards {t['evolutionary_pressure']} and operate under the computational constraint of {t['computational_constraint']}. Your response should include:

1. Ecosystem Design (300-350 words):
   a) Describe the key components of your digital linguistic ecosystem.
   b) Explain how you model {t['linguistic_feature']} in your digital environment.
   c) Discuss how the evolutionary pressure of {t['evolutionary_pressure']} is implemented.
   d) Explain how the computational constraint of {t['computational_constraint']} affects your system.
   e) Provide a simple pseudocode or flowchart representation of your ecosystem's main algorithm.

2. Linguistic Model (250-300 words):
   a) Describe how language is represented and processed in your digital ecosystem.
   b) Explain the mechanisms for language change and evolution in your model.
   c) Discuss how your model accounts for the interaction between different linguistic features.
   d) Provide an example of how a specific language feature might evolve in your system.

3. Evolutionary Dynamics (250-300 words):
   a) Explain the evolutionary mechanisms in your ecosystem (e.g., selection, mutation, drift).
   b) Describe how {t['evolutionary_pressure']} drives language change in your model.
   c) Discuss any emergent properties or unexpected behaviors you anticipate in your system.
   d) Propose a hypothesis about the long-term evolutionary trajectory of language in your ecosystem.

4. Computational Implementation (200-250 words):
   a) Describe the data structures and algorithms used to implement your ecosystem.
   b) Explain how you address the constraint of {t['computational_constraint']}.
   c) Discuss any trade-offs or optimizations in your implementation.
   d) Propose a method for visualizing or analyzing the language evolution in your system.

5. Implications and Applications (150-200 words):
   a) Discuss the potential insights your model could provide about real-world language evolution.
   b) Propose two novel applications of your digital linguistic ecosystem.
   c) Explore how your model might inform or challenge current theories in linguistics or evolutionary biology.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical implications of simulating language evolution.
   b) Discuss any biases that might be present in your model and how to address them.
   c) Propose guidelines for the responsible use and interpretation of results from your ecosystem.

7. Future Directions (100-150 words):
   a) Suggest two potential extensions or modifications to your digital linguistic ecosystem.
   b) Describe how these extensions could enhance our understanding of language evolution or improve the system's applicability.

Ensure your response demonstrates a deep understanding of linguistics, evolutionary biology, and computer science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of linguistics, evolutionary biology, and computer science, particularly in relation to {t['linguistic_feature']}, {t['evolutionary_pressure']}, and {t['computational_constraint']}.",
            "The digital ecosystem design is innovative, coherent, and scientifically plausible.",
            "The linguistic model and evolutionary dynamics are well-explained and logically consistent.",
            "The computational implementation addresses the given constraint effectively.",
            "The response includes thoughtful discussions on implications, ethics, and future directions.",
            "The overall response is well-structured, clear, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
