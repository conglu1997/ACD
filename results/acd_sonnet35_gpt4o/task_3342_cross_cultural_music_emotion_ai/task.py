import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "source_culture": "Western classical",
                "target_culture": "Traditional Chinese",
                "emotional_intent": "Melancholy"
            },
            {
                "source_culture": "Indian classical (Hindustani)",
                "target_culture": "West African (Yoruba)",
                "emotional_intent": "Joy"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of translating the emotional intent of '{t['emotional_intent']}' from {t['source_culture']} music to {t['target_culture']} music. Your response should include:

1. Cultural and Musical Analysis (250-300 words):
   a) Compare and contrast how '{t['emotional_intent']}' is expressed in {t['source_culture']} and {t['target_culture']} music.
   b) Analyze the key musical elements (e.g., rhythm, melody, harmony, timbre) used to convey this emotion in each culture.
   c) Discuss any cultural-specific contexts or associations related to this emotion in both musical traditions.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI system for emotional translation in music.
   b) Explain how your system processes and analyzes input from the source culture's music.
   c) Describe the methods used to map emotional content across cultures.
   d) Detail how the system generates output in the target culture's musical style.

3. Machine Learning Approach (200-250 words):
   a) Propose a machine learning model or combination of models suitable for this task.
   b) Explain how you would collect and preprocess training data for your system.
   c) Discuss any novel techniques or adaptations needed for cross-cultural music emotion translation.

4. Emotional Mapping Process (200-250 words):
   a) Describe the step-by-step process your AI uses to translate the emotional intent.
   b) Explain how your system handles nuances and subtleties in emotional expression.
   c) Discuss how cultural context is incorporated into the translation process.

5. Output Generation and Evaluation (200-250 words):
   a) Explain how your system generates music in the target culture's style.
   b) Propose methods to evaluate the accuracy and authenticity of the emotional translation.
   c) Discuss potential challenges in maintaining both emotional fidelity and cultural authenticity.

6. Ethical Considerations and Limitations (150-200 words):
   a) Discuss ethical implications of AI-driven cross-cultural music translation.
   b) Address concerns about cultural appropriation or misrepresentation.
   c) Acknowledge limitations of your approach and areas for future improvement.

Ensure your response demonstrates a deep understanding of musicology, cultural studies, emotion theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both musical traditions and their cultural contexts.",
            "The AI system design is innovative, detailed, and scientifically plausible.",
            "The machine learning approach is well-explained and appropriate for the task.",
            "The emotional mapping process is logical, comprehensive, and culturally sensitive.",
            "The output generation and evaluation methods are well-thought-out and address key challenges.",
            "Ethical considerations are thoroughly discussed, showing awareness of potential issues.",
            "The response maintains coherence and relevance throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
