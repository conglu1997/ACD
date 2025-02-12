import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sadness', 'anger', 'fear', 'love']
        musical_styles = ['classical', 'jazz', 'rock', 'electronic', 'folk']
        return {
            "1": {"emotion": random.choice(emotions), "style": random.choice(musical_styles)},
            "2": {"emotion": random.choice(emotions), "style": random.choice(musical_styles)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates harmonized musical compositions based on the emotional content and linguistic structure of song lyrics, using principles from neuroscience and music theory. Your system should focus on the emotion of {t['emotion']} and compose in the {t['style']} style. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system, including modules for lyric analysis, emotion recognition, and music generation.
   b) Explain how your system integrates neuroscientific principles of emotion processing with music theory concepts.
   c) Detail the process of how your system translates lyrical and emotional content into musical elements.
   d) Discuss any novel approaches or technologies your system employs.
   e) Include a text-based diagram or flowchart illustrating the system's architecture (use ASCII characters or simple text formatting).

2. Lyric Analysis and Emotion Recognition (250-300 words):
   a) Explain how your system analyzes the linguistic structure and semantic content of lyrics.
   b) Describe the methods used to recognize and quantify emotional content in the lyrics.
   c) Discuss how your system handles ambiguity or multiple emotions in the lyrics.
   d) Provide an example of how your system would analyze a short lyric excerpt related to {t['emotion']}.

3. Neural-Musical Translation (250-300 words):
   a) Detail how your system translates identified emotions and linguistic structures into musical elements (e.g., melody, harmony, rhythm).
   b) Explain how neuroscientific understanding of emotion processing influences this translation.
   c) Describe how your system ensures the generated music aligns with the {t['style']} style.
   d) Discuss any challenges in combining emotion-based composition with this particular style.

4. Composition Process (200-250 words):
   a) Provide a step-by-step explanation of how your AI system would compose a piece based on a given set of lyrics.
   b) Include at least one specific musical example (you can describe it in words, no need for actual notation).
   c) Explain how your system handles aspects like musical form, development, and coherence.

5. Evaluation and Refinement (200-250 words):
   a) Propose methods for evaluating the emotional congruence between the lyrics and the generated music.
   b) Discuss how your system could learn and improve from feedback.
   c) Suggest potential applications of your AI system in music therapy, composition, or emotion research.

6. Ethical Implications and Future Directions (150-200 words):
   a) Identify potential ethical concerns or misuses of an AI system that generates emotion-based music.
   b) Discuss the limitations of your system and areas for future improvement.
   c) Propose one novel research question that arises from your system design.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and natural language processing. Use appropriate terminology from all fields and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and musical plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses all 6 required sections with appropriate word counts.",
            f"The system design effectively integrates principles from neuroscience, music theory, and natural language processing.",
            f"The response demonstrates creativity and innovation while maintaining scientific plausibility.",
            f"The system architecture and processes are clearly explained and illustrated with a text-based diagram or flowchart.",
            f"The response includes specific examples of lyric analysis and musical composition for the emotion {t['emotion']} in the {t['style']} style.",
            f"The ethical implications and limitations of the system are thoughtfully discussed, with at least one novel research question proposed.",
            f"The response uses appropriate terminology from neuroscience, music theory, and NLP, providing clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
