import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neural_oscillations = [
            "Delta waves",
            "Theta waves",
            "Alpha waves",
            "Beta waves",
            "Gamma waves"
        ]
        music_elements = [
            "Melody",
            "Harmony",
            "Rhythm",
            "Timbre"
        ]
        music_genres = [
            "Classical",
            "Jazz",
            "Electronic",
            "World Music"
        ]
        
        tasks = [
            {
                "neural_oscillation": random.choice(neural_oscillations),
                "music_element": random.choice(music_elements),
                "music_genre": random.choice(music_genres)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes and analyzes music based on neural oscillations and harmonic theory, focusing on {t['neural_oscillation']} and their relationship to {t['music_element']} in the context of {t['music_genre']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for neuro-harmonic music composition and analysis.
   b) Explain how your system integrates principles from neuroscience, music theory, and artificial intelligence.
   c) Detail how the system models the relationship between {t['neural_oscillation']} and {t['music_element']}.
   d) Discuss how your system incorporates the stylistic elements of {t['music_genre']}.

2. Neural-Musical Mapping (200-250 words):
   a) Explain the theoretical basis for mapping {t['neural_oscillation']} to {t['music_element']}.
   b) Describe the algorithms or models used to translate neural patterns into musical structures.
   c) Discuss any challenges in this mapping process and how you address them.
   d) Provide a specific example of how a neural pattern might be expressed in {t['music_genre']}.

3. Composition Process (200-250 words):
   a) Outline the steps your AI system takes to compose a piece of music.
   b) Explain how the system ensures musical coherence and adherence to {t['music_genre']} conventions.
   c) Describe any novel techniques your system uses to generate creative musical ideas.
   d) Discuss how your system balances neural fidelity with musical aesthetics.

4. Analysis Capabilities (200-250 words):
   a) Describe how your system analyzes existing music in terms of neural oscillations.
   b) Explain how this analysis could provide insights into the cognitive effects of music.
   c) Discuss potential applications of this analysis in fields such as music therapy or cognitive science.
   d) Propose a method to validate the accuracy of your system's musical-neural mappings.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI to compose music based on neural patterns.
   b) Address concerns about the authenticity and ownership of AI-generated music.
   c) Explore potential misuses of this technology and propose safeguards.
   d) Discuss how this technology might impact human musicians and the music industry.

6. Future Directions (150-200 words):
   a) Propose potential expansions or modifications to your system for other musical elements or genres.
   b) Discuss how advancements in neuroscience or AI might enhance your system in the future.
   c) Suggest a novel research question that arises from the intersection of neural oscillations, music theory, and AI.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should address the specific neural oscillation of {t['neural_oscillation']}, music element of {t['music_element']}, and music genre of {t['music_genre']}",
            "The design should clearly integrate principles from neuroscience, music theory, and artificial intelligence",
            "The response should include all required sections: System Architecture, Neural-Musical Mapping, Composition Process, Analysis Capabilities, Ethical Considerations, and Future Directions",
            "The proposed system should be innovative while maintaining scientific plausibility",
            "The response should demonstrate a deep understanding of neuroscience, music theory, and artificial intelligence",
            "The discussion should be creative while addressing potential challenges and ethical implications"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
