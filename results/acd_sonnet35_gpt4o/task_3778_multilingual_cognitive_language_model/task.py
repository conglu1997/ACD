class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "language_pair": "Mandarin Chinese and Spanish",
                "cognitive_process": "working memory",
                "acquisition_stage": "early childhood (ages 3-5)"
            },
            "2": {
                "language_pair": "Arabic and English",
                "cognitive_process": "executive function",
                "acquisition_stage": "adolescence (ages 13-17)"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts language acquisition and use in multilingual environments, focusing on how different languages shape cognitive processes. Your system should address the language pair {t['language_pair']}, the cognitive process of {t['cognitive_process']}, and the acquisition stage of {t['acquisition_stage']}. Your response should include the following sections:

        1. System Architecture (300-350 words):
           a) Describe the key components of your AI system for modeling multilingual language acquisition and use.
           b) Explain how your system integrates neurolinguistic principles and computational models.
           c) Detail how your system accounts for the interaction between the specified languages and cognitive process.
           d) Include a visual representation of your system's architecture using ASCII art or a text-based diagram. The diagram should be at least 10 lines long and use characters such as |, -, +, >, <, and ^ to represent components and their relationships.

        2. Language Acquisition Modeling (250-300 words):
           a) Explain how your system models the acquisition of the specified language pair.
           b) Describe how it accounts for the specified acquisition stage and its unique challenges.
           c) Discuss how your model handles cross-linguistic influences and transfer.
           d) Explain how your system models the development of the specified cognitive process in relation to language acquisition.
           e) Describe how your system handles code-switching or language mixing, which is common in multilingual environments.

        3. Cognitive Process Simulation (200-250 words):
           a) Detail how your system simulates the specified cognitive process.
           b) Explain how this simulation interacts with the language acquisition model.
           c) Discuss any novel insights your system might provide about the relationship between multilingualism and the specified cognitive process.

        4. Predictive Capabilities (200-250 words):
           a) Describe the types of predictions your system can make about language use and cognitive development.
           b) Explain how these predictions account for individual differences and environmental factors.
           c) Provide an example of a specific prediction your system might make, along with its potential implications.

        5. Data Requirements and Ethical Considerations (150-200 words):
           a) Specify the types and sources of data your system would require.
           b) Discuss potential ethical issues in collecting and using this data, especially considering the age group involved.
           c) Propose guidelines for responsible development and use of your system.

        6. Validation and Testing (150-200 words):
           a) Propose methods to validate your system's predictions and models.
           b) Describe potential experiments or studies that could test your system's accuracy.
           c) Discuss the challenges in validating such a complex system and how you would address them.

        7. Practical Applications and Societal Impact (200-250 words):
           a) Suggest potential applications of your system in education, cognitive science, or clinical settings.
           b) Discuss how your system might influence our understanding of multilingualism and cognitive development.
           c) Consider potential societal impacts, both positive and negative, of widespread use of such a system.

        8. Future Directions (100-150 words):
           a) Propose two potential improvements or extensions to your system.
           b) Suggest a novel research question that arises from your work.

        Throughout your response, cite at least three relevant research papers or theories to support your system design and predictions.

        Ensure your response demonstrates a deep understanding of neurolinguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section. Your total response should be between 1550-1950 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all eight required sections with appropriate content and adheres to the specified word counts.",
            f"The system architecture clearly addresses the language pair {t['language_pair']}, the cognitive process of {t['cognitive_process']}, and the acquisition stage of {t['acquisition_stage']}.",
            "The ASCII diagram of the system architecture is at least 10 lines long and uses the specified characters.",
            "The language acquisition modeling section effectively explains how the system models the acquisition of the specified language pair and cognitive process, including how it handles code-switching or language mixing.",
            "The cognitive process simulation section provides a detailed explanation of how the system simulates the specified cognitive process and its interaction with language acquisition.",
            "The predictive capabilities section describes concrete and plausible predictions the system can make.",
            "The response addresses ethical considerations and proposes guidelines for responsible development and use.",
            "The validation and testing section proposes feasible methods to validate the system's predictions and models.",
            "The practical applications and societal impact section suggests realistic applications and considers both positive and negative impacts.",
            "The response demonstrates a deep understanding of neurolinguistics, cognitive science, and artificial intelligence, using appropriate terminology.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "The response cites at least three relevant research papers or theories to support the system design and predictions.",
            "The response stays within the overall word limit of 1550-1950 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
