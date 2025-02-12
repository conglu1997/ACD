import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Quantum interference"
        ]
        linguistic_phenomena = [
            "Polysemy",
            "Homonymy",
            "Garden path sentences",
            "Lexical ambiguity"
        ]
        nlp_tasks = [
            "Word sense disambiguation",
            "Machine translation",
            "Sentiment analysis",
            "Named entity recognition"
        ]
        tasks = {
            "1": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "nlp_task": random.choice(nlp_tasks)
            },
            "2": {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_phenomenon": random.choice(linguistic_phenomena),
                "nlp_task": random.choice(nlp_tasks)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing model that simulates linguistic cognition, focusing on the phenomenon of semantic ambiguity resolution. Your model should incorporate the quantum concept of {t['quantum_concept']}, address the linguistic phenomenon of {t['linguistic_phenomenon']}, and be applied to the NLP task of {t['nlp_task']}. Your response should include the following sections:

1. Theoretical Foundation (250-300 words):
   a) Explain the relevance of {t['quantum_concept']} to linguistic cognition.
   b) Describe how {t['linguistic_phenomenon']} manifests in natural language processing.
   c) Discuss the cognitive processes involved in semantic ambiguity resolution.

2. Quantum Linguistic Model (300-350 words):
   a) Design a quantum computing model that simulates the cognitive processes of semantic ambiguity resolution.
   b) Explain how your model incorporates {t['quantum_concept']} to represent linguistic structures and processes.
   c) Describe the mathematical formalism of your model, including key equations or algorithms.
   d) Provide a diagram or pseudocode snippet illustrating a core component of your model.

3. Application to NLP (250-300 words):
   a) Apply your quantum linguistic cognition model to the task of {t['nlp_task']}.
   b) Explain how your model addresses the challenges posed by {t['linguistic_phenomenon']} in this task.
   c) Describe the potential advantages of your quantum approach over classical NLP methods for this task.

4. Empirical Predictions (200-250 words):
   a) Formulate at least two testable predictions derived from your model.
   b) Describe an experimental setup to validate these predictions.
   c) Discuss potential implications of your model for our understanding of human language processing.

5. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in implementing your quantum linguistic cognition model.
   b) Propose future research directions to address these limitations or extend the model's capabilities.
   c) Discuss the broader implications of quantum approaches to cognitive modeling and artificial intelligence.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words, not including the diagram or pseudocode.

Cite at least 3 relevant scientific papers or resources to support your model design and theoretical foundations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response incorporates the quantum concept of {t['quantum_concept']} in a meaningful way",
            f"The model addresses the linguistic phenomenon of {t['linguistic_phenomenon']} effectively",
            f"The application to the NLP task of {t['nlp_task']} is well-explained and plausible",
            "The quantum linguistic cognition model is innovative and scientifically grounded",
            "The response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science",
            "The empirical predictions and experimental setup are well-formulated and testable",
            "The limitations and future directions are thoughtfully considered",
            "At least 3 relevant scientific papers or resources are cited"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
