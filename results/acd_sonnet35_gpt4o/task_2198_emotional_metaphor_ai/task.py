import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy", "sadness", "anger", "fear", "disgust",
            "surprise", "trust", "anticipation", "love", "guilt"
        ]
        cultures = [
            "Western", "East Asian", "Middle Eastern", "African",
            "Latin American", "South Asian", "Scandinavian", "Oceanian"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "emotion": random.choice(emotions),
                "culture1": random.choice(cultures),
                "culture2": random.choice(cultures)
            }
            while tasks[str(i+1)]["culture1"] == tasks[str(i+1)]["culture2"]:
                tasks[str(i+1)]["culture2"] = random.choice(cultures)
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and analyzing metaphors based on specific emotional states, then use it to explore cross-cultural emotional expressions. Focus on the emotion of {t['emotion']}, comparing metaphors between {t['culture1']} and {t['culture2']} cultures. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for metaphor generation and analysis.
   b) Explain how your system represents and processes emotional states.
   c) Detail the mechanisms for generating culturally-specific metaphors.
   d) Discuss how your system analyzes and compares metaphors across cultures.

2. Metaphor Generation Process (250-300 words):
   a) Provide a step-by-step explanation of how your system generates a metaphor for {t['emotion']}.
   b) Include an example metaphor for {t['emotion']} in both {t['culture1']} and {t['culture2']} cultures.
   c) Explain how cultural context influences the metaphor generation process.

3. Cross-Cultural Analysis (250-300 words):
   a) Compare and contrast the generated metaphors for {t['emotion']} in {t['culture1']} and {t['culture2']} cultures.
   b) Analyze the cultural factors that might contribute to differences in emotional expression.
   c) Discuss any universal elements in the metaphorical expression of {t['emotion']}.

4. Evaluation and Validation (200-250 words):
   a) Propose a method to evaluate the accuracy and cultural authenticity of generated metaphors.
   b) Describe potential metrics for assessing the system's cross-cultural understanding.
   c) Discuss how you would validate the system's emotional intelligence capabilities.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns or risks associated with AI-generated cultural metaphors.
   b) Discuss limitations of your system in understanding and representing diverse cultural perspectives.
   c) Propose guidelines for responsible development and use of such systems in cross-cultural communication.

Ensure your response demonstrates a deep understanding of emotions, metaphors, cultural differences, and AI technologies. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the emotion of {t['emotion']}.",
            f"The system effectively generates and compares metaphors for {t['culture1']} and {t['culture2']} cultures.",
            "The proposed AI system demonstrates a plausible approach to metaphor generation and analysis.",
            "The response shows a deep understanding of emotions, metaphors, cultural differences, and AI technologies.",
            "The ethical considerations and limitations are thoroughly discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
