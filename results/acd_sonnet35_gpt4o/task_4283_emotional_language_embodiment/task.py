import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'disgust', 'surprise']
        cultures = ['Japanese', 'Brazilian', 'Egyptian', 'Finnish']
        modalities = ['facial expression', 'body language', 'vocal intonation', 'linguistic description']
        
        tasks = {
            "1": {
                "emotion": random.choice(emotions),
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "source_modality": random.choice(modalities),
                "target_modality": random.choice(modalities)
            },
            "2": {
                "emotion": random.choice(emotions),
                "source_culture": random.choice(cultures),
                "target_culture": random.choice(cultures),
                "source_modality": random.choice(modalities),
                "target_modality": random.choice(modalities)
            }
        }
        
        # Ensure source and target cultures are different
        while tasks["2"]["source_culture"] == tasks["2"]["target_culture"]:
            tasks["2"]["target_culture"] = random.choice(cultures)
        
        # Ensure source and target modalities are different
        for task in tasks.values():
            while task["source_modality"] == task["target_modality"]:
                task["target_modality"] = random.choice(modalities)
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate emotional states into multimodal expressions across different cultures, and vice versa. For this task, focus on the following parameters:

Emotion: {t['emotion']}
Source Culture: {t['source_culture']}
Target Culture: {t['target_culture']}
Source Modality: {t['source_modality']}
Target Modality: {t['target_modality']}

Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for emotional translation and expression.
   b) Explain how your system integrates cultural knowledge, emotional models, and multimodal expression.
   c) Discuss any novel techniques or approaches used in your system design.
   d) Include a high-level diagram or flowchart of your AI system's architecture (describe it textually).

2. Emotional-Cultural Mapping (200-250 words):
   a) Explain how your system maps the given emotion between the source and target cultures.
   b) Describe the key parameters and variables considered in this mapping process.
   c) Discuss how your system accounts for cultural nuances and subtleties in emotional expression.

3. Multimodal Translation Process (250-300 words):
   a) Detail how your AI system translates the emotion from the source modality to the target modality.
   b) Explain any challenges in this translation process and how your system addresses them.
   c) Provide a specific example of how your system would translate the given emotion between the specified modalities and cultures.

4. Evaluation and Validation (200-250 words):
   a) Propose metrics for evaluating the accuracy and cultural appropriateness of your system's emotional translations.
   b) Describe an experiment to validate your system's performance across different emotions, cultures, and modalities.
   c) Discuss how you would compare your system's output to human performance in similar tasks.

5. Ethical Considerations and Potential Applications (150-200 words):
   a) Discuss the ethical implications of developing AI systems that can manipulate and translate emotional expressions.
   b) Propose two potential applications of your system in fields such as cross-cultural communication, mental health, or human-computer interaction.
   c) Address any potential risks or misuses of this technology and suggest safeguards.

6. Limitations and Future Directions (100-150 words):
   a) Identify the main limitations or challenges of your proposed system.
   b) Suggest approaches to address these limitations.
   c) Propose two directions for future research that could extend or improve your system.

Ensure your response demonstrates a deep understanding of emotional intelligence, cultural anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of emotional intelligence, cultural differences, and AI system design.",
            "The proposed system architecture is innovative, well-explained, and addresses the complexities of emotional translation across cultures and modalities.",
            "The emotional-cultural mapping and multimodal translation processes are clearly described and account for cultural nuances.",
            "The evaluation and validation methods are well-thought-out and appropriate for the task.",
            "Ethical considerations are thoroughly discussed, and potential applications are insightful and relevant.",
            "Limitations and future directions are clearly identified and addressed.",
            "The response is well-structured, within the specified word count, and uses appropriate technical terminology.",
            f"The response specifically addresses the given emotion ({t['emotion']}), source culture ({t['source_culture']}), target culture ({t['target_culture']}), source modality ({t['source_modality']}), and target modality ({t['target_modality']})."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
