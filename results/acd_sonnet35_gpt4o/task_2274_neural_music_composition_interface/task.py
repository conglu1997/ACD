import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "brain_region": "auditory cortex",
                "musical_element": "melody",
                "compositional_style": "classical"
            },
            {
                "brain_region": "prefrontal cortex",
                "musical_element": "rhythm",
                "compositional_style": "jazz"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""
        Design a brain-computer interface system that translates neural activity patterns into musical compositions. Your system should focus on the {t['brain_region']}, primarily translating activity in this region into the musical element of {t['musical_element']}, and should aim to produce compositions in the {t['compositional_style']} style. Your response should include:

        1. System Architecture (250-300 words):
           a) Describe the key components of your brain-computer interface system.
           b) Explain how these components interact to facilitate the translation of neural activity into music.
           c) Detail how your system incorporates current understanding of the specified brain region and its role in music processing or generation.

        2. Neural Signal Processing (200-250 words):
           a) Explain how your system processes and interprets neural signals from the specified brain region.
           b) Discuss challenges specific to decoding activity related to the given musical element and how your system addresses them.
           c) Propose a method for filtering relevant neural activity from background noise.

        3. Music Generation Mechanism (200-250 words):
           a) Describe how your system translates processed neural signals into the specified musical element.
           b) Explain how it ensures the generated music aligns with principles of music theory and the given compositional style.
           c) Discuss any AI or machine learning techniques used in this translation process.

        4. Adaptive Learning and Personalization (150-200 words):
           a) Explain how your system adapts to individual users' brain patterns over time.
           b) Describe any personalization features that tailor the music generation to user preferences or emotional states.
           c) Discuss how the system maintains a balance between user input and adherence to music theory principles.

        5. Example Composition Process (150-200 words):
           Provide a specific example of how your system might generate a short musical phrase, including:
           a) A description of the input neural activity pattern.
           b) The step-by-step process of translating this activity into music.
           c) The resulting musical output (described in musical terms or notation).

        6. Ethical and Practical Considerations (150-200 words):
           a) Discuss potential therapeutic applications of your system (e.g., in music therapy or neurological rehabilitation).
           b) Address privacy concerns related to decoding and interpreting neural activity.
           c) Consider potential impacts on creativity and the nature of musical composition.

        7. Future Directions and Challenges (100-150 words):
           a) Identify potential limitations of your proposed system.
           b) Suggest areas for future research or improvement.
           c) Discuss how emerging technologies might enhance your system's capabilities.

        Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

        Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately addresses the translation of neural activity from the {t['brain_region']} into {t['musical_element']}, focusing on {t['compositional_style']} style.",
            "The system architecture and neural signal processing methods are innovative yet scientifically plausible.",
            "The music generation mechanism demonstrates a deep understanding of both neuroscience and music theory.",
            "The example composition process is clear, detailed, and aligns with the specified parameters.",
            "Ethical and practical considerations are thoroughly analyzed.",
            "The response shows a high level of interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
