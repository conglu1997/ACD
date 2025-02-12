import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_language": "English",
                "target_language": "Mandarin Chinese",
                "cognitive_bias": "Availability heuristic",
                "cultural_factor": "Technological advancement"
            },
            {
                "source_language": "Spanish",
                "target_language": "Japanese",
                "cognitive_bias": "Confirmation bias",
                "cultural_factor": "Collectivism vs. Individualism"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""
        Design an AI system that models the evolution of idiomatic expressions from {t['source_language']} to {t['target_language']}, considering the influence of the {t['cognitive_bias']} and the cultural factor of {t['cultural_factor']}. Your response should include:

        1. System Architecture (300-350 words):
           a) Outline the key components of your AI system for modeling idiomatic expression evolution.
           b) Explain how your system incorporates the specified cognitive bias and cultural factor.
           c) Describe the data structures and algorithms used to represent and process idiomatic expressions.
           d) Discuss how your system accounts for linguistic and cultural differences between the source and target languages.

        2. Idiomatic Expression Analysis (250-300 words):
           a) Choose an idiomatic expression in the source language and explain its meaning and cultural context.
           b) Analyze how this expression might evolve when transferred to the target language culture.
           c) Discuss the role of the specified cognitive bias in this evolution process.
           d) Explain how the cultural factor might influence the adoption or adaptation of the expression.

        3. Evolution Simulation (250-300 words):
           a) Describe the step-by-step process your AI system would use to simulate the evolution of the chosen idiomatic expression.
           b) Explain how your system models the interaction between linguistic, cognitive, and cultural factors.
           c) Provide a hypothetical timeline of the expression's evolution, including intermediate forms or variations.
           d) Discuss any challenges in simulating this evolution and how your system addresses them.

        4. Predictive Analysis (200-250 words):
           a) Based on your simulation, predict the final form of the evolved idiomatic expression in the target language.
           b) Explain the reasoning behind your prediction, linking it to the cognitive bias and cultural factor.
           c) Discuss potential alternative outcomes and why your system favors the predicted result.
           d) Describe how your system quantifies or measures the degree of evolution in idiomatic expressions.

        5. Validation and Testing (200-250 words):
           a) Propose a method to validate the accuracy of your AI system's predictions.
           b) Describe an experiment to test the influence of the specified cognitive bias on idiomatic expression evolution.
           c) Discuss the challenges in testing and validating models of idiomatic expression evolution across cultures.
           d) Suggest metrics for evaluating the performance of your system.

        6. Ethical and Cultural Considerations (150-200 words):
           a) Identify potential ethical concerns related to modeling and predicting cultural linguistic evolution.
           b) Discuss how your system ensures cultural sensitivity and avoids perpetuating stereotypes.
           c) Consider the implications of accurate idiomatic expression evolution predictions on intercultural communication.
           d) Propose guidelines for the responsible use of such AI systems in linguistics and cultural studies.

        7. Future Directions and Applications (150-200 words):
           a) Suggest two potential improvements or extensions to your AI system.
           b) Discuss how your approach could contribute to our understanding of cultural exchange and linguistic globalization.
           c) Propose an interdisciplinary research project that could build upon your work.
           d) Describe a potential real-world application of your system beyond theoretical linguistics.

        Ensure your response demonstrates a deep understanding of computational linguistics, cognitive science, and cultural studies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

        Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the evolution of idiomatic expressions from {t['source_language']} to {t['target_language']}.",
            f"The system incorporates the {t['cognitive_bias']} and the cultural factor of {t['cultural_factor']} in a meaningful way.",
            "The proposed AI system is innovative yet scientifically plausible.",
            "The response demonstrates a deep understanding of computational linguistics, cognitive science, and cultural studies.",
            "The ethical and cultural considerations are thoroughly analyzed.",
            "The response shows a high level of interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
