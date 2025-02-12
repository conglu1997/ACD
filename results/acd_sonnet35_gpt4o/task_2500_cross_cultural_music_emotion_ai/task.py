import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        cultures = ['Western', 'East Asian', 'African', 'Middle Eastern', 'South Asian', 'Latin American']
        task1 = {"emotion": random.choice(emotions), "culture1": random.choice(cultures), "culture2": random.choice(cultures)}
        while task1["culture1"] == task1["culture2"]:
            task1["culture2"] = random.choice(cultures)
        task2 = {"emotion": random.choice(emotions), "culture1": random.choice(cultures), "culture2": random.choice(cultures)}
        while task2["culture1"] == task2["culture2"]:
            task2["culture2"] = random.choice(cultures)
        return {"1": task1, "2": task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating music to evoke the emotion of {t['emotion']} across {t['culture1']} and {t['culture2']} cultural contexts. Then, evaluate its performance in cross-cultural scenarios. Your response should include:

1. Theoretical Framework (250-300 words):
   a) Explain the key principles of music theory and emotion psychology relevant to your AI system.
   b) Discuss how cultural background influences emotional perception of music.
   c) Describe how these principles can be integrated into an AI system.

2. AI System Architecture (300-350 words):
   a) Outline the overall architecture of your AI system.
   b) Explain how it incorporates cultural knowledge, music theory, and emotion psychology.
   c) Describe the main components and their interactions.
   d) Discuss any novel algorithms or approaches used in your design.

3. Music Analysis Process (200-250 words):
   a) Explain how your system would analyze music to identify emotional content.
   b) Provide a specific example of how it would analyze a piece of music from {t['culture1']} culture intended to evoke {t['emotion']}, including at least two concrete musical elements (e.g., tempo, key, rhythm patterns).
   c) Describe how the system accounts for cultural context in its analysis.

4. Music Generation Process (200-250 words):
   a) Describe how your system would generate music to evoke {t['emotion']} in {t['culture2']} culture.
   b) Explain how the system ensures cultural authenticity while maintaining the intended emotional impact.
   c) Provide an example of a musical motif or structure your system might generate, describing at least two specific musical elements.

5. Cross-Cultural Evaluation (250-300 words):
   a) Propose a method to evaluate your system's performance in evoking {t['emotion']} across {t['culture1']} and {t['culture2']} cultures.
   b) Discuss potential challenges in cross-cultural emotion perception and how your system addresses them.
   c) Describe an experiment to test the effectiveness of your system's cross-cultural capabilities.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI to analyze and generate culturally-specific emotional music.
   b) Address concerns about cultural appropriation or misrepresentation in your system.
   c) Identify limitations of your approach and propose ways to address them.
   d) Discuss potential biases in AI systems when dealing with cultural and emotional content in music.

7. Future Applications and Implications (150-200 words):
   a) Explore potential applications of your AI system in fields such as music therapy, cross-cultural communication, or AI-assisted composition.
   b) Discuss how this technology could contribute to our understanding of music, emotion, and culture.
   c) Speculate on future developments in AI systems for emotional and cultural modeling in music.

Ensure your response demonstrates a deep understanding of music theory, emotion psychology, cultural anthropology, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section, adhering strictly to the word limits provided. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address all seven required sections within the specified word limits.",
            f"The AI system design must clearly incorporate principles from music theory, emotion psychology, and cultural anthropology.",
            f"The response must demonstrate how the AI system analyzes and generates music to evoke {t['emotion']} in both {t['culture1']} and {t['culture2']} cultures, providing specific examples of musical elements.",
            f"The cross-cultural evaluation method must be well-defined and address potential challenges.",
            "The response should show creativity and innovation in AI system design while maintaining scientific plausibility.",
            "Ethical considerations, limitations, and potential biases must be thoughtfully addressed.",
            "The response must adhere to the specified word limits for each section and the overall word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
