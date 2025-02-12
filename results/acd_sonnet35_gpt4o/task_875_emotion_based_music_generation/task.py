import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'emotion': 'Nostalgic melancholy',
                'musical_style': 'Contemporary classical'
            },
            {
                'emotion': 'Exhilarating anticipation',
                'musical_style': 'Electronic dance music'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates {t['musical_style']} music based on the complex emotional state of {t['emotion']}. Your system should incorporate principles from music theory, cognitive science, and artificial intelligence. Provide your response in the following format:

1. Emotional Analysis (150-200 words):
   a) Define and analyze the emotional state of {t['emotion']}.
   b) Describe how this emotion might be expressed in music, considering elements like melody, harmony, rhythm, and timbre.
   c) Explain how cognitive science informs your understanding of this emotion and its musical expression.

2. System Architecture (200-250 words):
   a) Describe the key components of your AI system for emotion-based music generation.
   b) Explain how your system integrates music theory principles, emotional mapping, and AI algorithms.
   c) Detail how your system would generate music in the {t['musical_style']} style.

3. Emotional-Musical Mapping (150-200 words):
   a) Create a specific mapping between aspects of {t['emotion']} and musical elements.
   b) Explain how your system translates emotional intensities or nuances into musical parameters.
   c) Provide an example of how a particular aspect of the emotion would be represented musically.

4. AI Algorithm Design (200-250 words):
   a) Describe the AI algorithms or models your system uses for music generation.
   b) Explain how these algorithms incorporate both emotional input and musical style constraints.
   c) Discuss any novel approaches or adaptations in your AI design for this specific task.

5. Training and Data (100-150 words):
   a) Describe the type and sources of data your system would require for training.
   b) Explain how you would curate or generate a dataset that captures both {t['emotion']} and {t['musical_style']}.
   c) Discuss any challenges in data acquisition or representation for this task.

6. Evaluation Method (100-150 words):
   a) Propose a method to evaluate the effectiveness of your system in generating emotionally appropriate music.
   b) Describe both quantitative and qualitative measures you would use.
   c) Explain how you would validate the emotional impact of the generated music.

7. Ethical Considerations and Limitations (100-150 words):
   a) Discuss potential ethical implications or challenges in using AI for emotion-based music generation.
   b) Address limitations of your approach and areas where human expertise would still be necessary.
   c) Suggest future improvements or extensions to your system.

Ensure your response demonstrates a deep understanding of music theory, emotional psychology, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered exactly as above. Your total response should be between 1000-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, emotional psychology, and artificial intelligence.",
            "The system architecture effectively integrates principles from music theory, cognitive science, and AI.",
            "The emotional-musical mapping is detailed, creative, and plausible.",
            "The AI algorithm design is innovative and appropriate for the task.",
            "The training and data section addresses the unique challenges of this task.",
            "The evaluation method is comprehensive, including both quantitative and qualitative measures.",
            "Ethical considerations and limitations are thoughtfully discussed.",
            "The response is well-structured, following the specified format and word count guidelines.",
            "The proposed system is creative and novel while maintaining scientific plausibility.",
            "The response effectively addresses the specific emotion and musical style given in the task."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
