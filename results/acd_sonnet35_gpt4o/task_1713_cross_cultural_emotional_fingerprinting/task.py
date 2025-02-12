class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_language": "Japanese",
                "target_language": "Swahili",
                "emotion": "nostalgia",
                "context": "childhood memories"
            },
            "2": {
                "source_language": "Arabic",
                "target_language": "Finnish",
                "emotion": "contentment",
                "context": "daily routines"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing 'emotional fingerprints' in language, focusing on the emotion of {t['emotion']} in the context of {t['context']}. Your system should be able to compare and translate these emotional fingerprints between {t['source_language']} and {t['target_language']}. Your response should include:

        1. System Architecture (250-300 words):
           a) Describe the key components of your AI system for emotional fingerprinting.
           b) Explain how your system integrates linguistic analysis, cultural knowledge, and emotion recognition.
           c) Discuss how your system handles the challenges of cross-cultural and cross-linguistic emotion analysis.
           d) Include a simple diagram or flowchart of your system architecture using ASCII art or Unicode characters.

        2. Emotional Fingerprint Generation (200-250 words):
           a) Explain the process of generating an emotional fingerprint for {t['emotion']} in {t['source_language']}.
           b) Describe the linguistic and cultural features your system considers when creating this fingerprint.
           c) Provide an example of what an emotional fingerprint might look like in your system.

        3. Cross-Cultural Analysis (200-250 words):
           a) Describe how your system would compare the emotional fingerprint of {t['emotion']} between {t['source_language']} and {t['target_language']}.
           b) Discuss the challenges in translating {t['emotion']} across these two cultures and languages.
           c) Explain how your system accounts for cultural differences in emotional expression and interpretation.

        4. AI Model and Training (200-250 words):
           a) Propose a specific AI model or combination of models for your emotional fingerprinting system.
           b) Describe the training data and process you would use for this specific emotion and language pair.
           c) Explain how your model handles ambiguity and context-dependence in emotional expressions.

        5. Evaluation and Validation (150-200 words):
           a) Suggest methods to evaluate the accuracy and cultural sensitivity of your system.
           b) Propose an experiment to validate your system's performance in analyzing {t['emotion']} across {t['source_language']} and {t['target_language']}.
           c) Discuss potential biases in your system and how you would address them.

        6. Ethical Considerations (150-200 words):
           a) Discuss the ethical implications of using AI to analyze and translate emotions across cultures.
           b) Address privacy concerns related to emotional fingerprinting.
           c) Propose guidelines for the responsible development and use of cross-cultural emotion AI systems.

        7. Potential Applications (100-150 words):
           a) Suggest two potential applications of your emotional fingerprinting system.
           b) Briefly explain how each application could benefit from cross-cultural emotion analysis.

        Ensure your response demonstrates a deep understanding of linguistics, cultural studies, emotion theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

        Format your answer with clear headings for each section, numbered as above. Your total response should be between 1250-1600 words. Stay within the specified word count for each section.

        For the system architecture diagram, use ASCII art or Unicode characters to create a clear and informative representation. The diagram should be no larger than 20 lines by 80 characters.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all seven required sections with appropriate content and adheres to the specified word counts.",
            "The system architecture is well-described and includes a clear ASCII art or Unicode diagram (max 20 lines by 80 characters).",
            f"The emotional fingerprint generation process for {t['emotion']} in {t['source_language']} is thoroughly explained and considers relevant linguistic and cultural features.",
            f"The cross-cultural analysis demonstrates a deep understanding of the challenges in translating {t['emotion']} between {t['source_language']} and {t['target_language']}.",
            "The proposed AI model and training process are well-suited for the task of cross-cultural emotional fingerprinting.",
            "The evaluation and validation methods are appropriate and address potential biases in the system.",
            "Ethical considerations are thoroughly discussed with appropriate guidelines proposed for responsible development and use.",
            "The potential applications are creative, relevant, and clearly benefit from cross-cultural emotion analysis.",
            "The overall response shows deep understanding and integration of linguistics, cultural studies, emotion theory, and AI concepts, using appropriate technical terminology.",
            "The response stays within the overall word limit of 1250-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
