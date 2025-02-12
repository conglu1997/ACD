import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            "Japanese",
            "Nigerian",
            "Brazilian",
            "Russian"
        ]
        contexts = [
            "business negotiations",
            "social media communication",
            "literary translation",
            "diplomatic exchanges"
        ]
        challenges = [
            "idioms and proverbs",
            "humor and sarcasm",
            "politeness levels",
            "cultural taboos"
        ]
        
        tasks = [
            {
                "source_culture": culture1,
                "target_culture": culture2,
                "context": context,
                "challenge": challenge
            }
            for culture1 in cultures
            for culture2 in cultures if culture1 != culture2
            for context in contexts
            for challenge in challenges
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate not just words, but cultural context and nuances from {t['source_culture']} culture to {t['target_culture']} culture. Focus on the context of {t['context']} and address the specific challenge of translating {t['challenge']}. Your response should include the following sections:

1. Cultural Analysis (250-300 words):
   a) Compare and contrast the relevant aspects of {t['source_culture']} and {t['target_culture']} cultures, focusing on {t['context']}.
   b) Explain the specific challenges in translating {t['challenge']} between these cultures.
   c) Identify key cultural elements that your AI system needs to understand and process.

2. AI System Architecture (300-350 words):
   a) Describe the main components of your AI system for cultural translation.
   b) Explain how your system integrates linguistic knowledge with cultural understanding.
   c) Detail the data sources and training approach for your AI model.
   d) Discuss any novel algorithms or techniques used in your system.

3. Translation Process (250-300 words):
   a) Outline step-by-step how your AI system would approach a translation task.
   b) Explain how it handles the specific challenge of {t['challenge']}.
   c) Provide an example of how a specific phrase or concept would be translated, considering cultural nuances.

4. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the cultural accuracy of your AI system's translations.
   b) Describe how you would validate the system's performance across different contexts.
   c) Discuss potential biases in your system and how you would address them.

5. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI for cultural translation.
   b) Address potential issues of cultural appropriation or misrepresentation.
   c) Propose guidelines for responsible development and use of such systems.

6. Future Developments (150-200 words):
   a) Suggest two potential improvements or extensions to your AI system.
   b) Discuss how this technology could evolve to handle more complex cultural translations.

Ensure your response demonstrates a deep understanding of linguistics, cultural anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both the source and target cultures.",
            "The AI system architecture effectively integrates linguistic and cultural knowledge.",
            "The translation process adequately addresses the specific challenge mentioned in the prompt.",
            "The evaluation methods are appropriate and consider cultural accuracy.",
            "Ethical considerations are thoughtfully addressed.",
            "The proposed future developments are innovative and relevant.",
            "The response is well-structured and within the specified word count.",
            "The writing demonstrates interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0