import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            "Rhythm",
            "Harmony",
            "Melody",
            "Timbre",
            "Dynamics",
            "Texture"
        ]
        cognitive_processes = [
            "Attention",
            "Emotion regulation",
            "Working memory",
            "Decision making",
            "Pattern recognition",
            "Sensory integration"
        ]
        musical_genres = [
            "Classical",
            "Jazz",
            "Electronic",
            "Rock",
            "World music",
            "Ambient"
        ]
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "musical_genre": random.choice(musical_genres)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "cognitive_process": random.choice(cognitive_processes),
                "musical_genre": random.choice(musical_genres)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that synthesizes music based on real-time neural activity and emotional states, focusing on the musical element of {t['musical_element']}, the cognitive process of {t['cognitive_process']}, and the musical genre of {t['musical_genre']}. Your response should include the following sections:\n\n1. System Architecture (300-350 words):\n   a) Describe the overall structure and components of your AI system.\n   b) Explain how it integrates neural activity data, emotional state analysis, and music generation.\n   c) Detail how the system specifically handles the given musical element, cognitive process, and musical genre.\n   d) Discuss any novel algorithms or approaches used in your design.\n\n2. Neural-Musical Mapping (250-300 words):\n   a) Explain how your system maps neural activity and emotional states to musical parameters.\n   b) Describe the specific neural correlates used for the given cognitive process.\n   c) Detail how these mappings are used to influence the specified musical element.\n   d) Discuss how your system ensures musical coherence and adherence to the given genre.\n\n3. Real-time Processing and Adaptation (250-300 words):\n   a) Describe how your system processes neural and emotional data in real-time.\n   b) Explain how it adapts to changes in cognitive states and emotional fluctuations.\n   c) Discuss any techniques used to minimize latency and ensure a smooth musical output.\n   d) Provide an example scenario of how the system would respond to a specific change in neural activity or emotional state.\n\n4. Music Theory Integration (200-250 words):\n   a) Explain how your system incorporates principles of music theory.\n   b) Describe how it maintains musical structure and coherence within the specified genre.\n   c) Discuss any challenges in balancing adherence to music theory with neural-driven generation.\n\n5. Evaluation and Validation (200-250 words):\n   a) Propose methods to evaluate the effectiveness of your system in translating neural activity to music.\n   b) Suggest experiments to validate the system's ability to capture and express emotional states musically.\n   c) Discuss how you would assess the musical quality and emotional congruence of the generated output.\n\n6. Ethical Considerations and Applications (200-250 words):\n   a) Discuss potential ethical issues related to brain-computer interfaces for creative expression.\n   b) Address privacy concerns regarding the use of neural and emotional data.\n   c) Propose guidelines for responsible development and use of such systems.\n   d) Suggest potential therapeutic or artistic applications of your neurocognitive music synthesis system.\n\nEnsure your response demonstrates a deep understanding of music theory, cognitive neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1400-1700 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, cognitive neuroscience, and artificial intelligence.",
            "The proposed system architecture is innovative, coherent, and plausibly integrates neural activity, emotional states, and music generation.",
            "The neural-musical mapping is well-explained and scientifically grounded.",
            "The system's real-time processing and adaptation capabilities are clearly described and technically feasible.",
            "The integration of music theory principles is well-explained and appropriate for the given musical genre.",
            "The evaluation methods and ethical considerations are thoughtfully addressed.",
            "The response is well-structured, uses appropriate technical terminology, and provides clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
