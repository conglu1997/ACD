import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotional_states = [
            "anxiety",
            "depression",
            "stress",
            "anger",
            "grief"
        ]
        music_elements = [
            "rhythm",
            "harmony",
            "melody",
            "timbre",
            "dynamics"
        ]
        return {
            "1": {
                "emotional_state": random.choice(emotional_states),
                "music_element": random.choice(music_elements)
            },
            "2": {
                "emotional_state": random.choice(emotional_states),
                "music_element": random.choice(music_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates personalized music to regulate emotions based on real-time neurophysiological data and music theory principles. Your system should focus on addressing the emotional state of {t['emotional_state']} and emphasize the musical element of {t['music_element']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they interact.
   b) Explain how your system processes neurophysiological data to infer emotional states.
   c) Detail how music theory principles are incorporated into the generation process.
   d) Discuss any novel algorithms or techniques used in your emotion-music mapping.

2. Neurophysiological-Musical Mapping (250-300 words):
   a) Explain how your system maps neurophysiological indicators to musical parameters.
   b) Describe how you handle the complexity of emotional states and their musical representations.
   c) Discuss how you ensure personalization in the music generation process.

3. Music Generation Process (250-300 words):
   a) Provide a step-by-step explanation of how your system generates music for the given emotional state.
   b) Explain how you emphasize the specified musical element in the generation process.
   c) Describe how your system ensures musical coherence and aesthetic quality.

4. Emotional Regulation Strategy (200-250 words):
   a) Explain your system's strategy for regulating the specified emotional state through music.
   b) Discuss how you balance immediate emotional impact with long-term therapeutic effects.
   c) Describe how your system adapts to changes in the user's emotional state over time.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the effectiveness of your system in regulating emotions.
   b) Describe how you would validate the musical quality and appropriateness of the generated pieces.
   c) Discuss potential challenges in evaluating such a system and how you'd address them.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using AI for emotional regulation through music.
   b) Propose guidelines for responsible development and use of such systems.
   c) Suggest potential improvements or extensions to your system for future research.

Ensure your response demonstrates a deep understanding of music theory, neuroscience, emotional psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all required sections with appropriate content and word counts.",
            f"The system design effectively addresses the emotional state of {t['emotional_state']}.",
            f"The music generation process emphasizes the musical element of {t['music_element']}.",
            "The response demonstrates a deep understanding of music theory, neuroscience, and emotional psychology.",
            "The proposed AI system is innovative and scientifically plausible.",
            "The response includes a thoughtful discussion of ethical considerations and future directions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
