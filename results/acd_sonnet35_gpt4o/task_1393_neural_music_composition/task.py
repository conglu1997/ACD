import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_areas = [
            "Auditory Cortex",
            "Motor Cortex",
            "Prefrontal Cortex",
            "Hippocampus"
        ]
        music_elements = [
            "Rhythm",
            "Melody",
            "Harmony",
            "Timbre"
        ]
        return {
            "1": {
                "brain_area": random.choice(brain_areas),
                "music_element": random.choice(music_elements)
            },
            "2": {
                "brain_area": random.choice(brain_areas),
                "music_element": random.choice(music_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on real-time neural activity patterns from the {t['brain_area']}, with a focus on the musical element of {t['music_element']}. Your response should include:

1. Neural Interface Design (200-250 words):
   a) Describe the method for capturing and processing neural signals from the specified brain area.
   b) Explain how you isolate and interpret the relevant neural patterns for music composition.
   c) Discuss any novel techniques or algorithms you incorporate for improved accuracy and resolution.

2. Music Generation Model (250-300 words):
   a) Detail the architecture of your AI music generation model.
   b) Explain how it translates neural activity into musical elements, focusing on the specified musical aspect.
   c) Describe any machine learning techniques or algorithms used in your model.
   d) Discuss how your model ensures musical coherence and aesthetic quality.

3. Neuroscience-Music Theory Integration (200-250 words):
   a) Analyze the relationship between the specified brain area and the musical element.
   b) Explain how your system maps neural patterns to musical features.
   c) Discuss any challenges in maintaining a meaningful connection between brain activity and generated music.

4. Real-time Performance and Adaptation (150-200 words):
   a) Describe how your system performs and adapts in real-time.
   b) Explain any feedback mechanisms between the generated music and ongoing neural activity.
   c) Discuss strategies for handling variability in neural signals and maintaining musical consistency.

5. Evaluation and Validation (150-200 words):
   a) Propose methods for evaluating the musical quality and neuroscientific validity of the system's output.
   b) Describe an experiment to test your system's performance across different mental states or musical genres.
   c) Discuss how you would validate that the composed music genuinely reflects the individual's neural activity.

6. Ethical Considerations and Applications (150-200 words):
   a) Discuss the ethical implications of a system that transforms thought patterns into music.
   b) Address potential privacy concerns and propose safeguards.
   c) Suggest two innovative applications of this technology beyond artistic expression.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your design while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering to the word limits provided."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence.",
            "The proposed system integrates neural activity and music generation in a scientifically plausible manner.",
            "The design is creative and innovative while maintaining scientific accuracy.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "Ethical considerations and potential applications are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
