import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        constructed_languages = [
            {
                "name": "Synesthesia",
                "feature": "Color-based grammar",
                "description": "A language where grammatical structures are represented by colors, and meaning can change based on the color combinations used."
            },
            {
                "name": "Chronos",
                "feature": "Time-dependent vocabulary",
                "description": "A language where words change meaning based on the time of day or year, reflecting a culture with a unique perception of time."
            },
            {
                "name": "Empathia",
                "feature": "Emotion-integrated syntax",
                "description": "A language where the emotional state of the speaker is mandatory in the sentence structure, affecting verb conjugations and noun declensions."
            }
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(constructed_languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-based language acquisition system that mimics human cognitive processes in learning languages, then apply it to the constructed language '{t['name']}' with its unique feature of {t['feature']}. Your response should include:

1. Cognitive Model Design (300-350 words):
   a) Describe the key components of your AI language acquisition system, explaining how they parallel human cognitive processes.
   b) Detail how your system incorporates theories of language acquisition (e.g., statistical learning, rule-based learning, social learning).
   c) Explain how your model accounts for different aspects of language learning (phonology, morphology, syntax, semantics, pragmatics).

2. Implementation Approach (250-300 words):
   a) Outline the main algorithms or computational techniques your system would use.
   b) Explain how your system would handle the unique feature of {t['feature']} in {t['name']}.
   c) Describe how you would measure and evaluate the system's language acquisition progress.
   d) Provide a short pseudocode snippet (10-15 lines) illustrating a crucial part of your implementation.

3. Learning Process Simulation (200-250 words):
   a) Describe a step-by-step scenario of how your AI system would learn {t['name']}.
   b) Explain how the system would overcome challenges posed by the language's unique feature.
   c) Predict potential errors or misconceptions the AI might develop and how they would be corrected.

4. Comparative Analysis (200-250 words):
   a) Compare your AI system's approach to language acquisition with typical human language learning processes.
   b) Discuss potential insights about human cognition that could be gained from this AI system.
   c) Propose how this system could be used to enhance human language learning methods.

5. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of developing AI systems that can rapidly acquire languages.
   b) Address potential societal impacts, both positive and negative.
   c) Propose guidelines for responsible development and use of such AI language acquisition systems.

6. Future Research Directions (100-150 words):
   a) Suggest potential improvements or extensions to your system.
   b) Propose a novel research question that arises from your design.
   c) Briefly describe an experiment that could further explore the intersection of AI, cognitive science, and linguistics based on your system.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an AI-based language acquisition system that credibly mimics human cognitive processes.",
            f"The system should be specifically applied to the constructed language '{t['name']}' with its unique feature of {t['feature']}.",
            "The implementation approach should include realistic algorithms or computational techniques.",
            "The learning process simulation should provide a plausible step-by-step scenario for acquiring the given constructed language.",
            "The comparative analysis should offer insightful comparisons between the AI system and human language learning processes.",
            "Ethical considerations must be thoughtfully addressed, including potential societal impacts.",
            "The response should demonstrate a high level of interdisciplinary knowledge in cognitive science, linguistics, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
