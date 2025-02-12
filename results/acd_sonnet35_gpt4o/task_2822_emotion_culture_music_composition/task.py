import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sorrow', 'anger', 'fear', 'love', 'excitement', 'calm', 'nostalgia']
        cultures = ['Western classical', 'Japanese traditional', 'West African', 'Indian classical', 'Latin American', 'Middle Eastern', 'Nordic folk', 'Chinese opera']
        musical_elements = ['melody', 'harmony', 'rhythm', 'tempo', 'dynamics', 'timbre', 'texture', 'form']
        
        task1 = {
            'emotion': random.choice(emotions),
            'culture': random.choice(cultures),
            'focus_element': random.choice(musical_elements)
        }
        
        task2 = {
            'emotion': random.choice(emotions),
            'culture': random.choice(cultures),
            'focus_element': random.choice(musical_elements)
        }
        
        return {
            "1": task1,
            "2": task2
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a musical composition that expresses the emotion of {t['emotion']} within the context of {t['culture']} musical tradition, with a particular focus on the musical element of {t['focus_element']}. Your task consists of the following parts:

1. Composition Description (200-250 words):
   a) Describe the key features of your musical composition, including its structure, instrumentation, and overall mood.
   b) Explain how you've incorporated the specified emotion into the composition.
   c) Detail how your composition reflects elements of the given cultural musical tradition.
   d) Elaborate on how you've emphasized the specified musical element in your composition.

2. Musical Analysis (250-300 words):
   a) Analyze how each musical element (melody, harmony, rhythm, etc.) contributes to expressing the given emotion.
   b) Explain the cultural significance of the musical choices you've made.
   c) Discuss how the emphasized musical element interacts with other elements to create the desired emotional effect.
   d) Compare your composition to traditional examples from the specified culture, noting similarities and differences.

3. Emotional and Cultural Impact (200-250 words):
   a) Predict how listeners from the specified culture might respond emotionally to your composition.
   b) Discuss how listeners from different cultural backgrounds might interpret the emotion in your piece.
   c) Analyze any potential cultural misunderstandings or misinterpretations that could arise from your composition.

4. Notational Representation (150-200 words):
   a) Provide a brief excerpt of your composition in musical notation, or if not possible, describe in detail how it would be notated.
   b) Explain any specific notational elements used to convey the emotion or cultural style.

5. Variations and Adaptations (150-200 words):
   a) Propose how you would modify your composition to express a contrasting emotion while maintaining the cultural style.
   b) Suggest how you could adapt the piece to fusion with a different cultural tradition while preserving the emotional content.

Ensure your response demonstrates a deep understanding of musical theory, emotional expression in music, and the specified cultural musical tradition. Use appropriate musical terminology and provide clear explanations for your creative and analytical choices. Be innovative in your approach while maintaining cultural authenticity and emotional resonance.

Format your response with clear headings for each section and use subheadings (a, b, c, d) as outlined above. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of musical theory and composition techniques.",
            f"The composition effectively expresses the emotion of {t['emotion']}.",
            f"The composition accurately reflects elements of {t['culture']} musical tradition.",
            f"The musical element of {t['focus_element']} is effectively emphasized and analyzed.",
            "The analysis shows insight into the interaction between musical elements, emotion, and cultural context.",
            "The response considers cultural implications and potential cross-cultural interpretations.",
            "The notational representation or description is clear and appropriate for the composition.",
            "The proposed variations and adaptations are creative and maintain the integrity of the original concept.",
            "The response uses appropriate musical terminology and provides clear explanations throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
