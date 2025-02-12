import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "amygdala",
                "emotion": "fear",
                "music_style": "classical"
            },
            {
                "brain_region": "hippocampus",
                "emotion": "nostalgia",
                "music_style": "jazz"
            },
            {
                "brain_region": "prefrontal cortex",
                "emotion": "decision-making",
                "music_style": "electronic"
            },
            {
                "brain_region": "cerebellum",
                "emotion": "motor control",
                "music_style": "rock"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that generates {t['music_style']} music based on brain activity patterns in the {t['brain_region']}, focusing on the neural correlates of {t['emotion']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the main components of your AI system and their functions.\n   b) Explain how your system integrates neuroscientific data, music theory, and AI algorithms.\n   c) Discuss any novel features that make your system particularly suited for translating brain activity to music.\n\n2. Neural-Musical Mapping (200-250 words):\n   a) Explain how your system maps neural activity in the {t['brain_region']} to musical elements (e.g., rhythm, melody, harmony).\n   b) Describe how you incorporate the neural correlates of {t['emotion']} into the music generation process.\n   c) Discuss how you ensure the generated music adheres to {t['music_style']} conventions while reflecting brain activity.\n\n3. AI Model and Training (200-250 words):\n   a) Describe the AI model(s) used in your system (e.g., neural networks, reinforcement learning).\n   b) Explain your training process, including the types of data used and how you handle the multimodal nature of the task.\n   c) Discuss strategies for ensuring the model generalizes well across different individuals and brain states.\n\n4. Ethical Considerations (150-200 words):\n   a) Discuss potential ethical implications of using brain activity for music generation.\n   b) Address privacy concerns related to the use of neural data.\n   c) Propose guidelines for the responsible development and use of such a system.\n\n5. Potential Applications and Future Directions (200-250 words):\n   a) Suggest two potential applications of your system outside of artistic creation.\n   b) Discuss how this technology might advance our understanding of the relationship between brain function and music.\n   c) Propose a future research direction that could extend or improve your system.\n\nEnsure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 1000-1250 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, particularly regarding the specified brain region and its role in the given emotion or function.",
            f"The system design effectively integrates principles of {t['music_style']} music theory with AI and neuroscience concepts.",
            "The proposed AI model and training process are well-explained and appropriate for the task.",
            "The neural-musical mapping is innovative yet plausible, clearly explaining how brain activity is translated into musical elements.",
            "Ethical considerations are thoughtfully addressed, with relevant guidelines proposed.",
            "Potential applications and future directions are creative and well-reasoned.",
            "The response uses appropriate terminology from neuroscience, music theory, and AI, providing clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
