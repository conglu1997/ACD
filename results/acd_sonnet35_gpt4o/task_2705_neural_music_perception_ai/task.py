import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_pieces = [
            ("Beethoven's Symphony No. 9", "Classical"),
            ("Miles Davis's 'So What'", "Jazz"),
            ("Pink Floyd's 'Comfortably Numb'", "Rock"),
            ("Steve Reich's 'Music for 18 Musicians'", "Minimalism"),
            ("Ravi Shankar's 'Raga Malgunji'", "Indian Classical")
        ]
        return {
            "1": {"piece": random.choice(musical_pieces)},
            "2": {"piece": random.choice(musical_pieces)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that mimics human neural processes in music perception and analysis, then use it to analyze {t['piece'][0]} ({t['piece'][1]} genre). Your response should include:\n\n1. Neural Architecture (250-300 words):\n   a) Describe the key components of your AI system and how they correspond to human neural structures involved in music perception.\n   b) Explain how your system processes auditory input, focusing on frequency analysis, rhythm detection, and harmonic processing.\n   c) Discuss how your model incorporates aspects of neural plasticity and learning in music perception.\n\n2. Music Theory Integration (200-250 words):\n   a) Explain how your system integrates music theory concepts (e.g., tonality, harmony, rhythm) with neural processing.\n   b) Describe how the AI distinguishes between different musical elements and structures.\n   c) Discuss any novel approaches in your system for handling complex musical features specific to the given genre.\n\n3. Emotional and Cognitive Processing (200-250 words):\n   a) Detail how your AI system models the emotional response to music, referencing relevant neuroscientific research.\n   b) Explain how the system accounts for cultural and individual differences in music perception.\n   c) Describe how your model handles the cognitive aspects of music perception, such as expectation and surprise.\n\n4. Analysis of the Given Piece (250-300 words):\n   a) Provide a detailed analysis of {t['piece'][0]} using your AI system.\n   b) Include insights on its structural, harmonic, and rhythmic elements.\n   c) Describe the emotional trajectory and cognitive engagement predicted by your model.\n   d) Compare your AI's analysis to known human perceptions of the piece, noting any interesting similarities or differences.\n\n5. Limitations and Future Directions (150-200 words):\n   a) Discuss potential limitations of your AI system in fully capturing human music perception.\n   b) Propose ideas for future research or improvements to your model.\n   c) Explore potential applications of your system beyond music analysis (e.g., in music therapy, composition, or cognitive science).\n\nEnsure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your system design while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1050-1300 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neural processes involved in music perception",
            "The AI system design effectively integrates concepts from neuroscience, music theory, and artificial intelligence",
            "The analysis of the given musical piece is detailed, insightful, and plausibly reflects human-like perception",
            "The explanation of emotional and cognitive processing in music is well-grounded in neuroscientific research",
            "The response shows creativity in system design while maintaining scientific plausibility",
            "Limitations and future directions are thoughtfully considered and discussed"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
