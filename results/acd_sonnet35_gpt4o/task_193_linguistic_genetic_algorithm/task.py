import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            ("phonology", "syntax"),
            ("morphology", "semantics"),
            ("pragmatics", "orthography")
        ]
        applications = [
            "intergalactic communication",
            "enhancing human-AI interaction",
            "preserving endangered languages",
            "optimizing information density in data transmission"
        ]
        return {
            "1": {"features": random.choice(language_features), "application": random.choice(applications)},
            "2": {"features": random.choice(language_features), "application": random.choice(applications)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a genetic algorithm to simulate the evolution of a constructed language, focusing on the linguistic features of {t['features'][0]} and {t['features'][1]}. Then, analyze its potential application in {t['application']}.

Your response should include:

1. Genetic Algorithm Design (200-250 words):
   a) Describe the 'genome' representation for your language.
   b) Explain the fitness function used to evaluate language variants.
   c) Outline the mutation and crossover operations.
   d) Describe the selection process for each generation.

2. Language Evolution Simulation (150-200 words):
   a) Provide a brief narrative of how the language might evolve over 100 generations.
   b) Highlight key changes in {t['features'][0]} and {t['features'][1]}.
   c) Explain how these changes reflect real-world language evolution principles.

3. Linguistic Analysis (200-250 words):
   a) Analyze the final evolved language's {t['features'][0]} and {t['features'][1]}.
   b) Compare these features to those found in natural human languages.
   c) Discuss any unique or unexpected linguistic properties that emerged.

4. Application in {t['application']} (150-200 words):
   a) Explain how the evolved language could be applied to {t['application']}.
   b) Discuss potential benefits and challenges of using this language in this context.
   c) Propose a specific scenario or use case for the language in this application.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using genetically evolved languages.
   b) Address concerns related to linguistic diversity and cultural preservation.

Ensure your response demonstrates a deep understanding of genetic algorithms, linguistic principles, and the specified application domain. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a detailed design of a genetic algorithm for language evolution, focusing on {t['features'][0]} and {t['features'][1]}.",
            "The language evolution simulation should be coherent and reflect real-world language evolution principles.",
            f"The linguistic analysis should thoroughly examine the evolved language's {t['features'][0]} and {t['features'][1]}.",
            f"The application of the evolved language to {t['application']} should be creative and well-reasoned.",
            "The response should address ethical considerations related to genetically evolved languages.",
            "The overall response should demonstrate interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
