import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            "Mandarin Chinese",
            "Arabic",
            "Pirahã",
            "American Sign Language",
            "Basque",
            "Hopi",
            "Klingon (constructed)"
        ]
        linguistic_features = [
            "Tonal system and its interaction with syntax",
            "Grammatical gender and its influence on spatial cognition",
            "Evidentiality markers and their impact on memory formation",
            "Spatial metaphors in abstract reasoning",
            "Kinship terminology and social cognition",
            "Color categorization and perceptual processing",
            "Time conceptualization and its effect on decision-making"
        ]
        tasks = {
            "1": {"language": random.choice(languages), "feature": random.choice(linguistic_features)},
            "2": {"language": random.choice(languages), "feature": random.choice(linguistic_features)}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an AI system that models cross-cultural variations in neurolinguistic processes, focusing on how {t['language']} influences brain activity during language processing, particularly in relation to its {t['feature']}. Your response should include the following sections:

1. Neurolinguistic Model Design (300-350 words):
   a) Describe the key components of your AI system for modeling neurolinguistic processes.
   b) Explain how your model incorporates the specific linguistic feature of {t['feature']} in {t['language']}.
   c) Detail how your system simulates brain activity during language processing.
   d) Provide a simple, original pseudocode snippet (5-10 lines) demonstrating a core function of your system.
   e) Include a textual description of a visual representation (e.g., a flowchart or diagram) of your AI system's architecture.

2. Cross-Cultural Analysis (250-300 words):
   a) Compare and contrast how your model would process {t['feature']} in {t['language']} versus English.
   b) Discuss potential differences in brain activity patterns between speakers of these languages.
   c) Explain how cultural context might influence these neurolinguistic processes.
   d) Address potential biases in your cross-cultural analysis and how you would mitigate them.

3. AI Implementation Challenges (200-250 words):
   a) Identify key challenges in implementing your neurolinguistic model in an AI system.
   b) Propose innovative solutions to overcome these challenges.
   c) Discuss how your system could adapt to or learn from exposure to new languages and cultures.

4. Potential Applications and Implications (200-250 words):
   a) Propose three potential applications of your cross-cultural neurolinguistic AI system.
   b) Discuss the ethical considerations and potential societal impacts of these applications.
   c) Explain how your system could contribute to our understanding of language, culture, and cognition.

5. Experimental Validation (150-200 words):
   a) Design an experiment to test the accuracy of your AI system's predictions about brain activity during language processing.
   b) Describe the methodology, including participant selection, data collection, and analysis techniques.
   c) Discuss potential challenges in conducting cross-cultural neurolinguistic research and how to address them.

6. Future Directions (100-150 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Discuss how your approach could be applied to other aspects of cognitive science or linguistics.
   c) Propose an interdisciplinary research project that could build upon your work.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, cultural anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate detail and adheres to the specified word count for each section.",
            f"The AI system design clearly incorporates the linguistic feature of {t['feature']} in {t['language']} and explains how it models neurolinguistic processes.",
            "The response includes a textual description of a visual representation of the AI system's architecture.",
            "The cross-cultural analysis demonstrates a deep understanding of linguistic and cultural differences in language processing and addresses potential biases.",
            "The AI implementation challenges and proposed solutions are well-reasoned and innovative.",
            "The potential applications and ethical implications are thoroughly considered.",
            "The experimental validation proposal is scientifically sound and addresses cross-cultural research challenges.",
            "The future directions suggest meaningful extensions of the work and interdisciplinary applications.",
            "The overall response shows creativity, scientific reasoning, and interdisciplinary knowledge integration across neuroscience, linguistics, cultural anthropology, and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
