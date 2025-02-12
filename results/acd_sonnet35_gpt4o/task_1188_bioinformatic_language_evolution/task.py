import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        genetic_principles = [
            "mutation",
            "recombination",
            "selection",
            "drift"
        ]
        information_theory_concepts = [
            "entropy",
            "compression",
            "channel capacity",
            "error correction"
        ]
        language_features = [
            "phonology",
            "morphology",
            "syntax",
            "semantics"
        ]
        return {
            "1": {
                "genetic_principle": random.choice(genetic_principles),
                "info_theory_concept": random.choice(information_theory_concepts),
                "language_feature": random.choice(language_features)
            },
            "2": {
                "genetic_principle": random.choice(genetic_principles),
                "info_theory_concept": random.choice(information_theory_concepts),
                "language_feature": random.choice(language_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language evolution simulator based on principles of genetics and information theory, then use it to analyze the development of a constructed language. Your task has the following components:

1. Simulator Design (300-350 words):
   a) Explain how your simulator incorporates the genetic principle of {t['genetic_principle']} and the information theory concept of {t['info_theory_concept']}.
   b) Describe how these principles are applied to model the evolution of {t['language_feature']} in your simulated language.
   c) Outline the key components and rules of your simulator, including any mathematical or algorithmic representations.
   d) Explain how your simulator handles the balance between randomness and determinism in language evolution.

2. Constructed Language Creation (200-250 words):
   a) Create a basic constructed language with 10-15 example words or phrases.
   b) Briefly describe the initial {t['language_feature']} of your constructed language.
   c) Explain how this language serves as a starting point for your simulation.

3. Simulation and Analysis (250-300 words):
   a) Run a simulated evolution of your constructed language using your simulator. Describe the parameters and duration of the simulation.
   b) Analyze how the {t['language_feature']} of your language changed over the course of the simulation.
   c) Explain how the changes reflect the genetic principle and information theory concept you incorporated.
   d) Provide 3-5 examples of evolved words or structures, comparing them to their original forms.

4. Theoretical Implications (200-250 words):
   a) Discuss how your simulation results might inform our understanding of natural language evolution.
   b) Explore potential applications of your approach in historical linguistics or language preservation efforts.
   c) Hypothesize how different initial conditions or parameters might affect language evolution in your model.

5. Limitations and Future Work (150-200 words):
   a) Identify potential limitations of your simulator and approach.
   b) Propose ways to expand or improve your model in future iterations.
   c) Suggest an experiment to validate your simulator against real-world language evolution data.

Ensure your response demonstrates a deep understanding of genetics, information theory, and linguistics. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The simulator design clearly incorporates the genetic principle of {t['genetic_principle']} and the information theory concept of {t['info_theory_concept']}.",
            f"The simulation and analysis effectively demonstrate the evolution of {t['language_feature']} in the constructed language.",
            "The response shows a deep understanding and creative application of concepts from genetics, information theory, and linguistics.",
            "The theoretical implications and limitations are thoughtfully discussed, with plausible suggestions for future work."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
