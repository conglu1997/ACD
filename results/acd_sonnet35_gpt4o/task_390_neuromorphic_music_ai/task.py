import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        music_genres = [
            {
                'genre': 'Jazz',
                'key_features': 'Improvisation, syncopation, swing rhythm',
                'example_piece': 'Take Five by Dave Brubeck'
            },
            {
                'genre': 'Classical',
                'key_features': 'Complex harmonies, structured composition, orchestral instruments',
                'example_piece': 'Symphony No. 5 by Beethoven'
            },
            {
                'genre': 'Electronic Dance Music (EDM)',
                'key_features': 'Synthesized sounds, repetitive beats, build-ups and drops',
                'example_piece': 'Strobe by Deadmau5'
            },
            {
                'genre': 'Folk',
                'key_features': 'Acoustic instruments, storytelling lyrics, simple melodies',
                'example_piece': 'Blowin\' in the Wind by Bob Dylan'
            }
        ]
        return {str(i+1): genre for i, genre in enumerate(random.sample(music_genres, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuromorphic AI system inspired by the human auditory cortex for music composition and analysis, with a focus on the {t['genre']} genre. Your response should include the following sections:

1. Neuromorphic Architecture (250-300 words):
   a) Describe the key components of your AI system and how they correspond to structures in the human auditory cortex.
   b) Explain how your system processes and represents musical features (e.g., pitch, rhythm, timbre).
   c) Discuss how your architecture incorporates principles of neural plasticity and learning.
   d) Include a simple diagram or flowchart of your system's architecture.

2. Music Analysis Capabilities (200-250 words):
   a) Explain how your system would analyze and identify key features of {t['genre']} music ({t['key_features']}).
   b) Describe the algorithms or neural network structures used for this analysis.
   c) Discuss how your system could identify patterns and structures specific to this genre.
   d) Provide a brief analysis of how your system would process the example piece: {t['example_piece']}.

3. Composition Process (200-250 words):
   a) Outline the step-by-step process your system would use to compose a new piece in the {t['genre']} style.
   b) Explain how it would incorporate learned patterns and structures from the analysis phase.
   c) Describe any generative algorithms or techniques used in the composition process.

4. Training and Learning (150-200 words):
   a) Propose a method for training your neuromorphic AI system.
   b) Discuss the type and amount of data required for effective learning.
   c) Explain how your system would continue to learn and improve over time.

5. Evaluation and Comparison (150-200 words):
   a) Suggest criteria for evaluating the quality and authenticity of the AI-generated music.
   b) Compare your neuromorphic approach to traditional deep learning methods for music generation.
   c) Discuss potential advantages and limitations of your bio-inspired system.

6. Cognitive and Artistic Implications (150-200 words):
   a) Discuss what your system's performance might reveal about human music cognition and creativity.
   b) Explore the potential impact of such technology on the music industry and artistic expression.
   c) Address any ethical considerations related to AI-generated music.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response using clear headings for each section (e.g., '1. Neuromorphic Architecture', '2. Music Analysis Capabilities', etc.). Your total response should be between 1100-1400 words, not including the headings."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, AI, and music theory, particularly in relation to the {t['genre']} genre.",
            "The neuromorphic architecture is well-explained and clearly inspired by the human auditory cortex.",
            f"The music analysis capabilities are appropriate for the {t['genre']} genre and include a brief analysis of the example piece ({t['example_piece']}).",
            f"The composition process is logically described and appropriate for creating music in the {t['genre']} style.",
            "The training and learning approach is feasible and well-reasoned.",
            "The evaluation criteria and comparison to traditional methods are thoughtfully addressed.",
            "The discussion of cognitive and artistic implications is insightful and considers ethical aspects.",
            "The overall design is creative while maintaining scientific plausibility.",
            "The response is well-formatted with clear headings and adheres to the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
