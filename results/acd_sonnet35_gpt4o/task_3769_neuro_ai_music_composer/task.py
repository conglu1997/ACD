import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre",
            "dynamics"
        ]
        neural_processes = [
            "working memory",
            "auditory processing",
            "emotional regulation",
            "pattern recognition",
            "motor planning"
        ]
        musical_genres = [
            "classical",
            "jazz",
            "electronic",
            "world music",
            "avant-garde"
        ]
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "neural_process": random.choice(neural_processes),
                "musical_genre": random.choice(musical_genres)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "neural_process": random.choice(neural_processes),
                "musical_genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that composes music by mimicking and enhancing human neural processes associated with musical creativity and emotion. Focus on the following scenario:\n\nMusical element: {t['musical_element']}\nNeural process: {t['neural_process']}\nMusical genre: {t['musical_genre']}\n\nYour response should include the following sections:\n\n1. System Architecture (300-350 words):\n   a) Describe the key components of your AI music composition system.\n   b) Explain how your system models and enhances the specified neural process.\n   c) Detail how the system generates and manipulates the given musical element.\n   d) Discuss how your system captures the essence of the specified musical genre.\n\n2. Neural-Music Interface (250-300 words):\n   a) Explain how your system translates neural activity into musical parameters.\n   b) Describe any novel algorithms or techniques used in this translation process.\n   c) Discuss how your system accounts for individual differences in neural processing of music.\n\n3. Emotional and Aesthetic Considerations (200-250 words):\n   a) Describe how your system incorporates emotional expression into its compositions.\n   b) Explain how it balances human-like creativity with machine precision.\n   c) Discuss how your system evaluates the aesthetic quality of its compositions.\n\n4. Learning and Adaptation (200-250 words):\n   a) Explain how your system learns from existing music and human feedback.\n   b) Describe how it adapts its composition style over time.\n   c) Discuss any potential biases in the learning process and how you address them.\n\n5. Practical Application and User Interaction (150-200 words):\n   a) Propose a practical application for your AI music composition system.\n   b) Describe how users would interact with the system.\n   c) Discuss potential benefits and challenges of implementing this system.\n\n6. Ethical Considerations and Future Directions (150-200 words):\n   a) Address ethical implications of AI-generated music, including issues of authorship and creativity.\n   b) Suggest two potential areas for future research or improvement of your system.\n   c) Discuss how this technology might impact the music industry and human musicians.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, music theory, and cognitive psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1250-1550 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections and subsections.",
            "The system design demonstrates a deep understanding of neuroscience, AI, music theory, and cognitive psychology.",
            "The proposed AI system effectively integrates the specified musical element, neural process, and musical genre.",
            "The response includes innovative ideas while maintaining scientific plausibility.",
            "The proposed system balances creativity with technical feasibility and scientific accuracy.",
            "The ethical considerations and future directions are thoughtfully addressed.",
            "The response is well-structured, clear, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
