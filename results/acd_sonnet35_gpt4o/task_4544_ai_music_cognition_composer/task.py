import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "music_style": "Jazz",
                "cognitive_aspect": "Improvisation",
                "target_emotion": "Joy"
            },
            {
                "music_style": "Classical",
                "cognitive_aspect": "Structural perception",
                "target_emotion": "Melancholy"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that models human music cognition, focusing on {t['cognitive_aspect']}, and uses this model to compose original {t['music_style']} music that evokes {t['target_emotion']}. Then, analyze its implications for creativity and copyright. Your response should include:\n\n1. Cognitive Model Design (300-350 words):\n   a) Describe the key components of your AI system's cognitive model for music perception and creation.\n   b) Explain how it integrates {t['cognitive_aspect']} in the context of {t['music_style']} music.\n   c) Discuss how your model accounts for emotional responses, particularly {t['target_emotion']}.\n   d) Include a high-level diagram or flowchart of your model (describe it textually).\n\n2. AI Composition Process (250-300 words):\n   a) Explain how your AI system uses the cognitive model to compose original music.\n   b) Describe the specific techniques or algorithms used in the composition process.\n   c) Discuss how your system ensures the music evokes {t['target_emotion']}.\n   d) Explain how your system maintains the stylistic elements of {t['music_style']}.\n\n3. Music Theory Integration (200-250 words):\n   a) Describe how your system incorporates fundamental music theory concepts.\n   b) Explain how it handles specific elements of {t['music_style']} (e.g., harmony, rhythm, form).\n   c) Discuss any novel approaches your system takes in applying music theory.\n\n4. Evaluation and Validation (200-250 words):\n   a) Propose methods to evaluate the quality and originality of the AI-composed music.\n   b) Describe how you would validate the cognitive model's accuracy in representing human music perception.\n   c) Suggest experiments to test if the composed music effectively evokes {t['target_emotion']}.\n\n5. Creativity Analysis (200-250 words):\n   a) Discuss the implications of your AI system for our understanding of musical creativity.\n   b) Analyze whether the AI's compositions can be considered truly 'creative'.\n   c) Explore the potential impact of such AI systems on human musicians and composers.\n\n6. Copyright and Ethical Considerations (200-250 words):\n   a) Discuss the copyright status of music created by your AI system.\n   b) Analyze potential ethical issues related to AI-generated music.\n   c) Propose guidelines for the responsible development and use of music cognition AI systems.\n\n7. Future Directions (150-200 words):\n   a) Suggest two potential improvements or extensions to your system.\n   b) Discuss how this technology might evolve and its potential applications beyond music composition.\n\nEnsure your response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence.",
            f"The cognitive model effectively integrates {t['cognitive_aspect']} in the context of {t['music_style']} music.",
            f"The AI composition process is well-explained and addresses how it evokes {t['target_emotion']}.",
            "The music theory integration is thorough and specific to the given music style.",
            "The evaluation and validation methods are well-thought-out and appropriate.",
            "The creativity analysis is insightful and considers multiple perspectives.",
            "The copyright and ethical considerations are comprehensive and propose meaningful guidelines.",
            "The response is well-structured, clear, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
