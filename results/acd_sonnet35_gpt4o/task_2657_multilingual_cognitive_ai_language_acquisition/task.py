import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_pairs = [
            ("Mandarin", "English"),
            ("Spanish", "Arabic"),
            ("Hindi", "Japanese"),
            ("French", "Swahili")
        ]
        cognitive_principles = [
            "Statistical Learning",
            "Critical Period Hypothesis",
            "Connectionist Models",
            "Usage-Based Theory"
        ]
        linguistic_features = [
            "Phonological Awareness",
            "Syntactic Bootstrapping",
            "Lexical Acquisition",
            "Pragmatic Development"
        ]
        
        tasks = []
        for _ in range(2):
            task = {
                "language_pair": random.choice(language_pairs),
                "cognitive_principle": random.choice(cognitive_principles),
                "linguistic_feature": random.choice(linguistic_features)
            }
            tasks.append(task)
        
        return {"1": tasks[0], "2": tasks[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes language acquisition in a multilingual environment, focusing on the language pair {t['language_pair'][0]} and {t['language_pair'][1]}. Your system should incorporate the cognitive principle of {t['cognitive_principle']} and pay special attention to the linguistic feature of {t['linguistic_feature']}.

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI language acquisition system.
   b) Explain how your system models the simultaneous acquisition of {t['language_pair'][0]} and {t['language_pair'][1]}.
   c) Detail how you've incorporated the {t['cognitive_principle']} principle into your system's design.
   d) Discuss how your system specifically addresses the development of {t['linguistic_feature']}.

2. Cognitive-Linguistic Integration (200-250 words):
   a) Analyze how the {t['cognitive_principle']} principle relates to the acquisition of {t['language_pair'][0]} and {t['language_pair'][1]}.
   b) Explain how your system models this cognitive principle in its language learning process.
   c) Discuss any challenges in integrating this cognitive principle with the linguistic feature of {t['linguistic_feature']}.

3. Multilingual Acquisition Simulation (250-300 words):
   a) Describe a specific scenario of how your system would simulate a child acquiring both {t['language_pair'][0]} and {t['language_pair'][1]} simultaneously.
   b) Provide an example of how the system would model the development of {t['linguistic_feature']} in this bilingual context.
   c) Explain how your system accounts for language transfer or interference between the two languages.

4. Data Analysis and Insights (200-250 words):
   a) Describe the types of data your system would generate and analyze during the language acquisition process.
   b) Explain how your system would identify and interpret patterns related to {t['linguistic_feature']} in the bilingual acquisition of {t['language_pair'][0]} and {t['language_pair'][1]}.
   c) Discuss potential insights your system might provide about language acquisition that would be difficult to obtain through traditional research methods.

5. Comparative Analysis (150-200 words):
   a) Compare your AI system's approach to language acquisition with traditional theories or models in linguistics and cognitive science.
   b) Discuss potential advantages and limitations of using AI to model multilingual language acquisition.
   c) Analyze how this approach might provide new insights into both human language learning and AI language models.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical considerations in using AI to model child language acquisition.
   b) Propose potential improvements or expansions to your system for future research.
   c) Suggest how this technology could be applied in real-world language learning or clinical contexts.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and address all subpoints. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must thoroughly address the language pair {t['language_pair'][0]} and {t['language_pair'][1]}, the cognitive principle of {t['cognitive_principle']}, and the linguistic feature of {t['linguistic_feature']}",
            "The system architecture should be well-designed and clearly explained, integrating cognitive and linguistic principles",
            "The response should demonstrate a deep understanding of language acquisition in multilingual environments",
            "The simulation scenario should be detailed and plausible, showcasing how the system models bilingual language acquisition",
            "The data analysis section should propose insightful ways to interpret patterns in bilingual language acquisition",
            "The comparative analysis should thoughtfully discuss the advantages and limitations of the AI approach",
            "Ethical considerations should be addressed thoughtfully, and future directions should be innovative and relevant",
            "The response should be well-structured, following the given format with clear headings and subheadings",
            "The response should demonstrate interdisciplinary thinking by effectively connecting concepts from cognitive science, linguistics, and AI",
            "The proposed system should be innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
