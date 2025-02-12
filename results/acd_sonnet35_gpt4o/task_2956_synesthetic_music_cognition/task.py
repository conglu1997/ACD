import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        visual_elements = ['color', 'shape', 'texture', 'composition', 'contrast']
        musical_elements = ['pitch', 'rhythm', 'harmony', 'timbre', 'dynamics']
        art_styles = ['Impressionism', 'Cubism', 'Abstract Expressionism', 'Surrealism', 'Pop Art']
        music_genres = ['Classical', 'Jazz', 'Electronic', 'World', 'Avant-garde']
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'visual_element': random.choice(visual_elements),
                'musical_element': random.choice(musical_elements),
                'art_style': random.choice(art_styles),
                'music_genre': random.choice(music_genres)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates visual art into music using principles of synesthesia and music theory, focusing on the translation of {t['visual_element']} into {t['musical_element']}. Your system should be capable of translating works from the {t['art_style']} style into the {t['music_genre']} genre. Then, analyze its cognitive and creative implications. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for translating visual art to music.
   b) Explain how your system integrates principles of synesthesia and music theory.
   c) Detail how the system processes the specified visual element and translates it into the given musical element.
   d) Discuss how your system accounts for the characteristics of the specified art style and music genre.
   e) Include a high-level diagram or pseudocode to illustrate your architecture.

2. Translation Process (250-300 words):
   a) Provide a step-by-step explanation of how your system translates a specific visual artwork into music.
   b) Describe how your system ensures coherence and aesthetic quality in the musical output.
   c) Explain how your system handles ambiguity or multiple possible interpretations.

3. Cognitive Model (200-250 words):
   a) Describe the cognitive model underlying your system's cross-modal translations.
   b) Explain how this model relates to current theories of synesthesia and music cognition.
   c) Discuss any novel hypotheses about cross-modal processing that your system suggests.

4. Creative Implications (200-250 words):
   a) Analyze the potential impact of your system on artistic creation and appreciation.
   b) Discuss how this technology might influence our understanding of creativity and artistic expression.
   c) Propose an experiment to test whether exposure to synesthesia-inspired art-music translations affects human creativity.

5. Ethical and Societal Considerations (150-200 words):
   a) Identify potential ethical concerns related to AI-generated art and music.
   b) Discuss the implications for copyright and authorship in AI-translated works.
   c) Propose guidelines for the responsible development and use of cross-modal AI creativity tools.

6. Future Directions (150-200 words):
   a) Suggest two potential extensions or improvements to your synesthetic music cognition system.
   b) Propose a novel application of this technology outside the realm of art and music.
   c) Speculate on how this research might influence our understanding of human perception and creativity.

Ensure your response demonstrates a deep understanding of music theory, cognitive neuroscience, and AI technologies. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively translates {t['visual_element']} into {t['musical_element']}.",
            f"The design adequately addresses the translation of {t['art_style']} style into {t['music_genre']} genre.",
            "The System Architecture demonstrates a clear understanding of synesthesia and music theory principles.",
            "The Translation Process is well-explained and logically sound.",
            "The Cognitive Model is grounded in current theories and presents novel hypotheses.",
            "The Creative Implications are insightful and well-reasoned.",
            "Ethical and Societal Considerations are thoughtfully addressed.",
            "Future Directions propose innovative extensions and applications of the technology.",
            "The response demonstrates deep interdisciplinary knowledge and creative problem-solving.",
            "The ideas presented are scientifically grounded and clearly explained.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
