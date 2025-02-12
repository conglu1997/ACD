import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum interference"
        ]
        linguistic_aspects = [
            "semantic ambiguity",
            "syntactic parsing",
            "pragmatic inference",
            "lexical acquisition"
        ]
        cognitive_processes = [
            "working memory",
            "attention allocation",
            "decision making",
            "concept formation"
        ]
        tasks = [
            {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_aspect": random.choice(linguistic_aspects),
                "cognitive_process": random.choice(cognitive_processes)
            },
            {
                "quantum_concept": random.choice(quantum_concepts),
                "linguistic_aspect": random.choice(linguistic_aspects),
                "cognitive_process": random.choice(cognitive_processes)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired model of language processing and cognitive function, focusing on the following elements:

1. Quantum Concept: {t['quantum_concept']}
2. Linguistic Aspect: {t['linguistic_aspect']}
3. Cognitive Process: {t['cognitive_process']}

Your task consists of the following steps:

1. Conceptual Framework (250-300 words):
   a) Explain how the quantum concept can be applied to model the given linguistic aspect and cognitive process.
   b) Describe the key components of your quantum-inspired model and their interactions.
   c) Discuss how your model differs from classical approaches to language processing and cognition.

2. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of your model using quantum-inspired formalism.
   b) Explain the significance of each term or operator in your formulation.
   c) Describe how your mathematical model captures the essence of the linguistic aspect and cognitive process.

3. Information Processing (200-250 words):
   a) Explain how information is encoded, processed, and retrieved in your quantum-inspired model.
   b) Describe how your model handles uncertainty and ambiguity in language processing.
   c) Discuss any emergent properties or behaviors that arise from the quantum nature of your model.

4. Practical Application (250-300 words):
   a) Propose a specific natural language understanding problem that your model could address.
   b) Describe how you would apply your quantum-inspired model to solve this problem.
   c) Compare the potential advantages and limitations of your approach to traditional NLP methods.

5. Empirical Predictions (150-200 words):
   a) Formulate two testable predictions that your model makes about human language processing or cognition.
   b) Describe an experimental setup that could validate these predictions.

6. Ethical Implications (150-200 words):
   a) Discuss potential ethical concerns arising from the application of quantum-inspired models in linguistics and cognitive science.
   b) Propose guidelines for responsible development and use of such models.

7. Future Directions (100-150 words):
   a) Suggest two potential extensions or modifications to your model for future research.
   b) Discuss how these extensions might contribute to our understanding of language, cognition, or quantum phenomena.

Ensure your response demonstrates a deep understanding of quantum mechanics, linguistics, and cognitive science. Use appropriate terminology from each field and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately applies the quantum concept of {t['quantum_concept']} to model the linguistic aspect of {t['linguistic_aspect']} and the cognitive process of {t['cognitive_process']}.",
            "The mathematical formulation uses quantum-inspired formalism correctly and relevantly.",
            "The model's information processing approach demonstrates a clear quantum-inspired mechanism.",
            "The practical application proposed is relevant and demonstrates potential advantages over classical NLP methods.",
            "The empirical predictions are testable and logically follow from the proposed model.",
            "The response addresses ethical implications thoughtfully and proposes reasonable guidelines.",
            "The future directions suggested are innovative and build upon the proposed model.",
            "The response demonstrates a deep understanding of quantum mechanics, linguistics, and cognitive science throughout.",
            "The response is creative while maintaining scientific plausibility.",
            "The response follows the specified format and is within the 1300-1650 word range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
