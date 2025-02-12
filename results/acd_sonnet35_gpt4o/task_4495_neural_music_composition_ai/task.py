import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'brain_region': 'prefrontal cortex',
                'musical_element': 'melody',
                'emotional_state': 'joy'
            },
            {
                'brain_region': 'amygdala',
                'musical_element': 'rhythm',
                'emotional_state': 'fear'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on real-time neural activity, integrating neuroscience, music theory, and artificial intelligence. Your system should focus on the {t['brain_region']} for neural input, primarily influence the {t['musical_element']} in the composition, and aim to evoke or reflect the emotional state of {t['emotional_state']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for neural music composition.
   b) Explain how your system integrates neural data, music theory, and AI algorithms.
   c) Detail the mechanisms used for translating neural activity into musical elements.
   d) Discuss how your system handles real-time processing and composition.

2. Neural-Musical Mapping (250-300 words):
   a) Explain how you map neural activity from the {t['brain_region']} to musical parameters, focusing on {t['musical_element']}.
   b) Describe the techniques used to extract relevant features from the neural data.
   c) Discuss how your model accounts for individual differences in brain activity and musical perception.

3. Emotion and Music Generation (200-250 words):
   a) Describe how your system incorporates the target emotional state of {t['emotional_state']} into the composition process.
   b) Explain the musical theory principles you use to evoke or reflect this emotion.
   c) Discuss any challenges in creating a consistent emotional tone in the generated music.

4. AI and Composition Techniques (250-300 words):
   a) Detail the AI algorithms and techniques used in your music composition system.
   b) Explain how these algorithms interact with the neural input and musical theory components.
   c) Describe any novel approaches you've developed for this specific application.

5. Real-time Adaptation and Feedback (200-250 words):
   a) Explain how your system adapts to changes in neural activity in real-time.
   b) Describe any feedback mechanisms between the generated music and the neural input.
   c) Discuss how you balance responsiveness with musical coherence and quality.

6. Evaluation and Validation (150-200 words):
   a) Propose methods for evaluating the quality and emotional efficacy of the generated music.
   b) Describe how you would validate the relationship between the neural input and musical output.
   c) Discuss the challenges in creating a 'ground truth' for neural-based music composition.

7. Ethical Considerations and Applications (150-200 words):
   a) Identify potential ethical issues related to neural-based music composition.
   b) Discuss possible applications of your system in fields such as therapy, entertainment, or neuroscience research.
   c) Propose guidelines for the responsible development and use of such technology.

8. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your neural music composition system.
   b) Discuss how these enhancements could advance our understanding of the brain-music relationship.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical considerations.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1600-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence.",
            "The system design effectively integrates neural data, music theory, and AI algorithms.",
            "The neural-musical mapping is well-explained and scientifically plausible.",
            "The approach to emotion and music generation is creative and grounded in musical theory.",
            "The AI and composition techniques are well-detailed and appropriate for the task.",
            "The system's real-time adaptation and feedback mechanisms are clearly explained.",
            "The evaluation and validation methods proposed are comprehensive and appropriate.",
            "Ethical considerations are thoroughly addressed, and responsible guidelines are proposed.",
            "The suggested future directions are innovative and relevant to advancing the field.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
