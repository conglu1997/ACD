import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "superposition",
            "entanglement",
            "interference"
        ]
        ambiguity_types = [
            "lexical ambiguity",
            "syntactic ambiguity",
            "semantic ambiguity",
            "pragmatic ambiguity"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "ambiguity_type": random.choice(ambiguity_types)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "ambiguity_type": random.choice(ambiguity_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired language model capable of capturing and resolving {t['ambiguity_type']} in natural language using the quantum principle of {t['quantum_principle']}. Your response should include the following sections:

1. Conceptual Framework (250-300 words):
   a) Explain the chosen quantum principle and its relevance to language processing.
   b) Describe the nature of the specified type of linguistic ambiguity.
   c) Propose a novel conceptual framework that integrates these quantum and linguistic concepts.

2. Model Architecture (300-350 words):
   a) Design the architecture of your quantum-inspired language model.
   b) Explain how your model incorporates the specified quantum principle.
   c) Detail how your model captures and represents linguistic ambiguities.
   d) Describe the process by which your model resolves ambiguities.

3. Mathematical Formulation (200-250 words):
   a) Provide a mathematical representation of your model's key components.
   b) Explain how your formulation captures both quantum and linguistic aspects.
   c) Include at least one equation or algorithm that demonstrates ambiguity resolution.

4. Example Scenario (200-250 words):
   a) Present a specific example of {t['ambiguity_type']} in a sentence or short text.
   b) Walk through how your model would process and resolve this ambiguity.
   c) Contrast your model's approach with traditional NLP methods.

5. Cognitive Implications (150-200 words):
   a) Discuss how your model relates to theories of human language processing.
   b) Propose an experiment to test if human cognition exhibits quantum-like properties in language understanding.

6. Practical Applications and Limitations (150-200 words):
   a) Suggest two potential real-world applications of your quantum-inspired language model.
   b) Discuss current technological limitations in implementing your model.
   c) Propose future research directions to overcome these limitations.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified quantum principle and its potential application to language processing.",
            "The proposed model architecture effectively integrates quantum concepts with linguistic theory to address the given type of ambiguity.",
            "The mathematical formulation is sound and clearly represents the integration of quantum and linguistic concepts.",
            "The example scenario effectively illustrates how the model would resolve the specified type of ambiguity.",
            "The discussion of cognitive implications and proposed experiment are scientifically plausible and insightful.",
            "The suggested practical applications are innovative and the analysis of limitations is thoughtful.",
            "The response is well-structured, coherent, and adheres to the specified format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
