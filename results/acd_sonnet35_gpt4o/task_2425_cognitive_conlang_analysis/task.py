import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            "parallel distributed processing",
            "symbolic computation",
            "bayesian inference",
            "embodied cognition",
            "predictive processing"
        ]
        linguistic_features = [
            "word order",
            "morphological complexity",
            "lexical ambiguity",
            "evidentiality",
            "conceptual metaphors"
        ]
        return {
            "1": {
                "architecture": random.choice(cognitive_architectures),
                "feature": random.choice(linguistic_features)
            },
            "2": {
                "architecture": random.choice(cognitive_architectures),
                "feature": random.choice(linguistic_features)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language (conlang) that reflects the cognitive architecture of {t['architecture']}, with a particular focus on the linguistic feature of {t['feature']}. Then, analyze how this language might influence or reflect thought processes. Your response should include:

1. Conlang Design (300-350 words):
   a) Describe the key features of your conlang, including its phonology, morphology, syntax, and semantics.
   b) Explain how the conlang incorporates principles from the {t['architecture']} cognitive architecture.
   c) Provide specific examples of how the linguistic feature of {t['feature']} is implemented in your conlang.
   d) Include a sample text in your conlang with an English translation (50-75 words).

2. Cognitive Architecture Analysis (250-300 words):
   a) Explain the key principles of the {t['architecture']} cognitive architecture.
   b) Discuss how these principles are reflected in your conlang's structure and use.
   c) Analyze potential cognitive implications of using this language.

3. Linguistic Feature Deep Dive (200-250 words):
   a) Provide a detailed explanation of the {t['feature']} feature in your conlang.
   b) Compare and contrast this implementation with how the feature appears in natural languages.
   c) Discuss how this feature might influence or reflect thought processes in speakers of your conlang.

4. Thought Experiment (200-250 words):
   a) Propose a specific cognitive task or problem-solving scenario.
   b) Describe how speakers of your conlang might approach this task differently from speakers of natural languages.
   c) Explain your reasoning, drawing connections between the language structure and cognitive processes.

5. Implications and Predictions (200-250 words):
   a) Discuss potential implications of your conlang for theories of linguistic relativity or cognitive science.
   b) Propose two testable predictions about cognitive processing in speakers of your conlang.
   c) Suggest an experimental design to test one of these predictions.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or criticisms of your conlang design or analysis.
   b) Propose future research directions or extensions of this work.
   c) Discuss how this approach could be applied to other cognitive architectures or linguistic features.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Be creative in your conlang design while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and word counts.",
            f"The conlang design clearly reflects principles from the {t['architecture']} cognitive architecture.",
            f"The linguistic feature of {t['feature']} is well-implemented and analyzed in the conlang.",
            "The conlang design is creative, detailed, and linguistically plausible.",
            "The analysis demonstrates a deep understanding of the relationship between language structure and cognitive processes.",
            "The thought experiment and predictions are logical and well-reasoned.",
            "The response effectively integrates concepts from cognitive science, linguistics, and artificial intelligence.",
            "The sample text in the conlang is provided with an English translation.",
            "The proposed experimental design is feasible and relevant to the predictions made.",
            "The discussion of limitations and future directions is thoughtful and insightful.",
            "The total word count is between 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
