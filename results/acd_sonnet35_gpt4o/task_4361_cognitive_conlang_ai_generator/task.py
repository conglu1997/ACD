class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_bias": "Confirmation bias",
                "cultural_value": "Collectivism",
                "alien_physiology": "Telepathic abilities"
            },
            "2": {
                "cognitive_bias": "Availability heuristic",
                "cultural_value": "Individualism",
                "alien_physiology": "Multiple sensory organs"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes constructed languages (conlangs) based on specific cognitive and cultural parameters. Then, use your system to create a language for a hypothetical alien species with the following characteristics:

Cognitive bias: {t['cognitive_bias']}
Cultural value: {t['cultural_value']}
Alien physiology: {t['alien_physiology']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for conlang generation and analysis.
   b) Explain how your system incorporates cognitive biases and cultural values into language generation.
   c) Detail how the system ensures linguistic consistency and plausibility.
   d) Discuss any novel approaches or mechanisms in your design.

2. Cognitive-Linguistic Mapping (250-300 words):
   a) Explain how your system maps the specified cognitive bias to linguistic features.
   b) Describe how the given cultural value is reflected in the generated language's structure.
   c) Discuss how the alien physiology influences the language's phonology or modality.

3. Conlang Generation (300-350 words):
   a) Provide an overview of the generated alien language, including its name.
   b) Describe its phonology (or alternative communication mode), morphology, and syntax.
   c) Explain how the language's features reflect the specified cognitive bias, cultural value, and alien physiology.
   d) Include a sample sentence or expression in the language, with translation and grammatical breakdown.

4. Language Analysis (200-250 words):
   a) Describe how your AI system would analyze the generated language.
   b) Explain what insights about the hypothetical alien species could be inferred from the language structure.
   c) Discuss how this analysis could be used to predict alien behavior or thought patterns.

5. Evaluation and Validation (150-200 words):
   a) Propose a method to evaluate the plausibility and consistency of the generated language.
   b) Suggest an experiment to test whether the language accurately reflects the specified parameters.
   c) Discuss potential biases in your AI system and how they might be mitigated.

6. Implications and Ethics (150-200 words):
   a) Discuss the potential applications of your AI system in linguistics, cognitive science, and extraterrestrial communication.
   b) Address ethical considerations in using AI for language creation and analysis.
   c) Explore the implications of your system for understanding the relationship between language, cognition, and culture.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response fully addresses all 6 required sections.",
            "The AI system design demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence.",
            "The generated alien language coherently reflects the specified cognitive bias, cultural value, and alien physiology.",
            "The response provides innovative and plausible approaches to language generation and analysis.",
            "The answer is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
