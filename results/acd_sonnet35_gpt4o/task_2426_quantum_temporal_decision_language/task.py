import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        contexts = [
            "political speech",
            "emergency response",
            "creative writing",
            "academic discourse",
            "social media communication",
            "legal argumentation"
        ]
        quantum_concepts = [
            "superposition",
            "entanglement",
            "interference",
            "quantum tunneling",
            "decoherence"
        ]
        linguistic_features = [
            "lexical choice",
            "syntactic structure",
            "pragmatic implicature",
            "metaphorical expression",
            "discourse coherence"
        ]
        temporal_aspects = [
            "future prediction",
            "past inference",
            "present state estimation",
            "temporal ordering",
            "event duration"
        ]
        
        tasks = {
            "1": {
                "context": random.choice(contexts),
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_feature": random.choice(linguistic_features),
                "temporal_aspect": random.choice(temporal_aspects)
            },
            "2": {
                "context": random.choice(contexts),
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_feature": random.choice(linguistic_features),
                "temporal_aspect": random.choice(temporal_aspects)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired model of temporal decision-making in language processing, then apply it to analyze and predict linguistic choices in the context of {t['context']}. Your model should incorporate the quantum concept of {t['quantum_concept']}, focus on the linguistic feature of {t['linguistic_feature']}, and address the temporal aspect of {t['temporal_aspect']}. Provide your response in the following format:

1. Quantum Temporal Language Model (300-350 words):
   a) Describe the key components and mechanisms of your model.
   b) Explain how it incorporates the specified quantum concept into language processing.
   c) Detail how your model represents and processes temporal information.
   d) Discuss how your model simulates decision-making in language production or comprehension.

2. Mathematical Formulation (250-300 words):
   a) Provide a mathematical description of your quantum temporal language model.
   b) Include key equations or formalisms that capture the integration of quantum principles, temporal aspects, and linguistic features.
   c) Explain how your mathematical framework relates to established models in quantum cognition or psycholinguistics.

3. Contextual Analysis and Prediction (250-300 words):
   a) Apply your model to analyze the specified linguistic feature in the given context.
   b) Provide an example of how your model would predict language choices or interpret linguistic data.
   c) Explain how the quantum and temporal aspects of your model enhance this analysis compared to classical approaches.

4. Empirical Validation (200-250 words):
   a) Propose an experiment to test the predictions of your model in the given context.
   b) Describe the data you would collect and how you would analyze it.
   c) Discuss potential challenges in empirically validating your quantum temporal language model.

5. Implications and Extensions (200-250 words):
   a) Discuss the implications of your model for our understanding of language, cognition, and decision-making.
   b) Propose two potential applications of your model in fields such as natural language processing, cognitive science, or artificial intelligence.
   c) Suggest an extension of your model to address a related linguistic or cognitive phenomenon.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, cognitive science, and temporal reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed description of a quantum-inspired model for temporal decision-making in language processing.",
            f"The model effectively incorporates the quantum concept of {t['quantum_concept']}.",
            f"The analysis focuses on the linguistic feature of {t['linguistic_feature']} in the context of {t['context']}.",
            f"The model addresses the temporal aspect of {t['temporal_aspect']}.",
            "The mathematical formulation is sound and relevant to the proposed model.",
            "The proposed experiment for empirical validation is well-designed and feasible.",
            "The response demonstrates a deep understanding of quantum mechanics, linguistics, cognitive science, and temporal reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
