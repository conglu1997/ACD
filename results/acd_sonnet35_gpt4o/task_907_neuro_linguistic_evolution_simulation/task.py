import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "phonological inventory",
            "morphological complexity",
            "syntactic structure",
            "semantic network"
        ]
        neural_mechanisms = [
            "hebbian learning",
            "predictive coding",
            "neural plasticity",
            "hierarchical processing"
        ]
        return {
            "1": {
                "linguistic_feature": random.choice(linguistic_features),
                "neural_mechanism": random.choice(neural_mechanisms)
            },
            "2": {
                "linguistic_feature": random.choice(linguistic_features),
                "neural_mechanism": random.choice(neural_mechanisms)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a simulated language evolution process that focuses on the development of {t['linguistic_feature']}, incorporating the neural mechanism of {t['neural_mechanism']}. Your task has the following components:

1. Evolutionary Model Design (250-300 words):
   a) Describe your model for simulating the evolution of {t['linguistic_feature']} over time.
   b) Explain how you incorporate {t['neural_mechanism']} into your model.
   c) Outline the key parameters and variables in your simulation.
   d) Discuss how your model accounts for environmental and social factors in language evolution.

2. Simulation Process (200-250 words):
   a) Provide a step-by-step explanation of how your simulation would run.
   b) Describe the initial state of the language feature and how it changes over time.
   c) Explain how you would measure and quantify the evolution of the language feature.

3. Neural Correlates (200-250 words):
   a) Describe the hypothetical neural changes that would correspond to the simulated language evolution.
   b) Explain how {t['neural_mechanism']} contributes to these changes.
   c) Discuss any predictions your model makes about brain structure or function related to language.

4. AI Integration (150-200 words):
   a) Explain how you would use AI language models in your simulation.
   b) Discuss the potential advantages and limitations of using AI in this context.
   c) Propose a method for validating the AI's performance against human language data.

5. Comparative Analysis (150-200 words):
   a) Compare your simulated language evolution to known historical language changes.
   b) Discuss any insights your model provides into the origins and development of human language.
   c) Explain how your findings might inform theories of language acquisition or linguistic universals.

6. Ethical Considerations (100-150 words):
   a) Discuss potential ethical issues in simulating language evolution and using AI in this context.
   b) Propose guidelines for responsible use of this technology in linguistics and cognitive science.

Ensure your response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, neuroscience, and artificial intelligence",
            "The evolutionary model design is innovative and scientifically plausible",
            "The simulation process is clearly explained and accounts for the specified linguistic feature and neural mechanism",
            "The neural correlates section provides insightful hypotheses about brain structure and function",
            "The AI integration is well-thought-out and addresses both advantages and limitations",
            "The comparative analysis draws meaningful connections to real-world language evolution",
            "Ethical considerations are thoughtfully addressed",
            "The response is well-structured and adheres to the specified word limits"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
