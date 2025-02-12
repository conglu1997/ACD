import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        senses = ['visual', 'auditory', 'olfactory', 'gustatory', 'tactile']
        art_styles = ['abstract expressionism', 'surrealism', 'minimalism', 'pop art']
        
        tasks = [
            {
                'emotion': random.choice(emotions),
                'primary_sense': random.choice(senses),
                'secondary_sense': random.choice([s for s in senses if s != 'primary_sense']),
                'art_style': random.choice(art_styles)
            }
            for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a short story (250-300 words) that explores the emotion of {t['emotion']} by translating it into sensory experiences, primarily focusing on {t['primary_sense']} sensations, with secondary emphasis on {t['secondary_sense']} sensations. Your story should evoke the emotion without explicitly naming it.

After writing the story, imagine that an AI has generated an artwork in the style of {t['art_style']} based on your story. Analyze this hypothetical AI-generated artwork (200-250 words), discussing how it captures the emotion and sensory experiences from your story, and how the chosen art style contributes to the overall effect.

Finally, reflect on the process of translating emotions into sensory experiences and then into visual art (150-200 words). Discuss the challenges and potential insights gained from this form of emotional synesthesia storytelling.

Format your response as follows:

1. Story:
[Your 250-300 word story here]

2. Artwork Analysis:
[Your 200-250 word analysis here]

3. Reflection:
[Your 150-200 word reflection here]

Ensure that your response demonstrates a deep understanding of emotional nuances, sensory descriptions, and art analysis. Be creative in your approach while maintaining coherence across the story, artwork analysis, and reflection."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The story effectively conveys the emotion of {t['emotion']} without explicitly naming it",
            f"The story primarily focuses on {t['primary_sense']} sensations, with secondary emphasis on {t['secondary_sense']} sensations",
            f"The artwork analysis discusses an AI-generated piece in the style of {t['art_style']}",
            "The reflection demonstrates insight into the process of translating emotions across different modalities",
            "The response shows creativity and coherence across all three sections",
            "The word counts for each section are within the specified ranges"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
