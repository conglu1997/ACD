import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'surprise', 'disgust']
        brain_regions = ['amygdala', 'hippocampus', 'prefrontal cortex', 'insula']
        musical_elements = ['rhythm', 'melody', 'harmony', 'timbre']
        
        tasks = {
            "1": {
                "emotion": random.choice(emotions),
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "emotion": random.choice(emotions),
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on neural activity patterns associated with different emotions, focusing on the emotion of {t['emotion']}, the brain region {t['brain_region']}, and the musical element of {t['musical_element']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system models neural activity patterns associated with {t['emotion']}.
   c) Detail how your system translates these patterns into musical compositions, particularly focusing on {t['musical_element']}.
   d) Propose a novel feature that enhances the system's ability to generate emotionally evocative music.

2. Neuroscientific Basis (200-250 words):
   a) Explain the role of the {t['brain_region']} in processing the emotion of {t['emotion']}.
   b) Describe how neural activity patterns in this region might be mapped to musical parameters, especially {t['musical_element']}.
   c) Discuss any challenges in accurately interpreting and translating neural activity to music.

3. Music Generation Process (200-250 words):
   a) Outline the step-by-step process your AI uses to create a musical piece expressing {t['emotion']}.
   b) Explain how your algorithm balances neuroscientific accuracy with musical creativity and coherence.
   c) Describe how your system ensures the generated music effectively conveys the intended emotion.

4. Sample Composition Analysis (150-200 words):
   a) Provide a detailed description of a short musical piece that your AI might generate for {t['emotion']}.
   b) Analyze how specific elements of this composition, especially {t['musical_element']}, relate to the neural activity patterns associated with {t['emotion']}.
   c) Discuss the potential emotional impact and musical merit of this generated piece.

5. Applications and Implications (150-200 words):
   a) Propose potential applications of this system in fields such as music therapy, emotional regulation, or brain-computer interfaces.
   b) Discuss how this technology might advance our understanding of the relationship between brain activity, emotions, and music.
   c) Explore potential uses in creative industries or personal emotional expression.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI to generate emotion-based music, particularly regarding privacy and emotional manipulation.
   b) Consider potential misuses of this technology and propose safeguards against them.
   c) Explore philosophical questions about creativity, consciousness, and the nature of emotions that this system might raise.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and artistic integrity.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-defined AI system design that composes music based on neural activity patterns associated with {t['emotion']}, focusing on the {t['brain_region']} and the musical element of {t['musical_element']}.",
            "The system architecture should be clearly described, including a novel feature for generating emotionally evocative music.",
            f"The neuroscientific basis should accurately explain the role of the {t['brain_region']} in processing {t['emotion']} and how neural patterns might be mapped to music.",
            f"The music generation process should be detailed, explaining how it creates a piece expressing {t['emotion']} while balancing neuroscientific accuracy and musical creativity.",
            f"A sample composition should be described and analyzed, showing how it relates to neural activity patterns associated with {t['emotion']}.",
            "Potential applications, implications, and ethical considerations of the technology should be thoroughly discussed.",
            "The response should demonstrate interdisciplinary knowledge integration, creative problem-solving, and ethical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
