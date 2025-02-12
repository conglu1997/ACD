import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = [
            {"emotion": "Joy", "motif": "Rising major third followed by two staccato notes"},
            {"emotion": "Melancholy", "motif": "Descending minor second followed by a long note"},
            {"emotion": "Anger", "motif": "Repeated sharp staccato notes in a syncopated rhythm"},
            {"emotion": "Serenity", "motif": "Gentle ascending and descending major scale fragments"},
            {"emotion": "Anxiety", "motif": "Rapid alternation between two dissonant notes"},
            {"emotion": "Love", "motif": "Slow, lyrical melody with wide intervals"},
            {"emotion": "Nostalgia", "motif": "Descending perfect fourth followed by a rising major second"},
            {"emotion": "Awe", "motif": "Ascending perfect fifth followed by a sustained high note"}
        ]
        musical_styles = [
            "Classical",
            "Jazz",
            "Electronic",
            "Folk",
            "Avant-garde"
        ]
        return {
            "1": {"emotion": random.choice(emotional_states), "style": random.choice(musical_styles)},
            "2": {"emotion": random.choice(emotional_states), "style": random.choice(musical_styles)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural-inspired AI system for music composition that mimics human creativity and emotional expression, then use it to compose a piece of music expressing the emotion of {t['emotion']['emotion']} in the style of {t['style']} music. The emotional motif associated with this emotion is: {t['emotion']['motif']}. Your response should include the following sections:

1. Neural-AI Music Composition System (300-350 words):
   a) Describe the architecture of your neural-inspired AI system for music composition.
   b) Explain how your system incorporates principles from neuroscience, particularly those related to creativity and emotional processing.
   c) Detail the AI algorithms and techniques used in your system.
   d) Discuss how your system integrates music theory and compositional techniques.
   e) Include a diagram or flowchart illustrating the key components and processes of your system (describe it textually).

2. Emotion-to-Music Mapping (200-250 words):
   a) Explain how your system translates emotional states into musical elements (e.g., melody, harmony, rhythm, timbre).
   b) Describe the specific musical features your system associates with {t['emotion']['emotion']}.
   c) Discuss how your system incorporates the given emotional motif: {t['emotion']['motif']}.
   d) Address any challenges in representing complex emotions through music and how your system overcomes them.

3. Style Integration (200-250 words):
   a) Describe how your system incorporates the characteristics of {t['style']} music.
   b) Explain how it balances adhering to stylistic conventions with generating novel compositions.
   c) Discuss any techniques used to ensure stylistic coherence while expressing the target emotion.

4. Composition Process (250-300 words):
   a) Walk through the step-by-step process your system follows to compose a piece expressing {t['emotion']['emotion']} in the {t['style']} style.
   b) Highlight key decision points and how the system resolves them.
   c) Explain how the system ensures musical coherence and emotional continuity throughout the piece.
   d) Provide a sample output of your system by describing a 30-second segment of the composed piece. Include details on melody, harmony, rhythm, and instrumentation.

5. Evaluation and Analysis (200-250 words):
   a) Propose specific, measurable methods to evaluate the emotional expressiveness and musical quality of your system's compositions.
   b) Discuss how you would compare your system's output to human-composed music expressing similar emotions.
   c) Analyze potential biases or limitations in your system's approach to emotional expression in music.

6. Ethical and Artistic Implications (150-200 words):
   a) Discuss the ethical considerations of using AI for creative tasks traditionally performed by humans.
   b) Explore the potential impact of your system on the music industry and human composers.
   c) Consider the philosophical question of whether AI-generated music can truly convey human emotions.

7. Future Developments (100-150 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how advancements in neuroscience or AI might enhance music composition systems in the future.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neuroscience, AI, and music theory.",
            "The neural-inspired AI system for music composition is well-designed and scientifically plausible.",
            "The emotion-to-music mapping incorporates the given emotional motif and is thoroughly explained.",
            "The style integration for the specified musical style is clearly described and justified.",
            "The composition process is detailed, with a plausible 30-second sample output provided.",
            "The evaluation methods are specific and measurable.",
            "Ethical implications and future developments are thoughtfully discussed.",
            "The response shows creativity and innovation while maintaining scientific rigor.",
            "Technical terminology is used appropriately and complex concepts are explained clearly.",
            "The response adheres to the specified word count and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
