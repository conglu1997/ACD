import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            'Amygdala',
            'Prefrontal Cortex'
        ]
        emotional_states = [
            'Joy',
            'Sadness',
            'Anger',
            'Fear'
        ]
        musical_styles = [
            'Classical',
            'Jazz',
            'Electronic'
        ]
        
        tasks = [
            {
                'brain_region': random.choice(brain_regions),
                'emotional_state': random.choice(emotional_states),
                'musical_style': random.choice(musical_styles)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that interprets human emotional states from brain activity in the {t['brain_region']} and composes music in real-time to reflect and potentially modulate those emotions. Focus on the emotional state of {t['emotional_state']} and the musical style of {t['musical_style']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system, including neural signal processing, emotion interpretation, and music generation modules.
   b) Explain how these components interact to create a cohesive system.
   c) Detail how your system incorporates neurofeedback to modulate emotional states.

2. Neural Signal Processing (200-250 words):
   a) Explain how your system processes neural signals from the {t['brain_region']}.
   b) Describe the techniques used to isolate and interpret emotional states, particularly {t['emotional_state']}.
   c) Discuss any challenges in real-time processing of neural data and how your system addresses them.

3. Emotion-to-Music Translation (200-250 words):
   a) Describe your system's approach to translating emotional states into musical elements.
   b) Explain how it captures the nuances of {t['emotional_state']} in the {t['musical_style']} genre.
   c) Discuss how your system ensures musical coherence while reflecting real-time emotional changes.

4. AI Composition Techniques (200-250 words):
   a) Detail the AI techniques or algorithms used for real-time music composition.
   b) Explain how your system balances adherence to {t['musical_style']} with emotional expression.
   c) Describe any novel AI approaches you've incorporated for this specific task.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI to interpret and potentially influence human emotions.
   b) Address privacy concerns related to reading and responding to brain activity.
   c) Propose guidelines for the responsible development and use of such technology.

6. Potential Applications and Future Directions (150-200 words):
   a) Suggest potential therapeutic or artistic applications of your system.
   b) Discuss how this technology could advance our understanding of the relationship between music and emotions.
   c) Propose two directions for future research or expansion of this system.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence.",
            f"The system design clearly incorporates neural signal processing from the {t['brain_region']}, interpretation of {t['emotional_state']}, and composition in the {t['musical_style']} genre.",
            "The emotion-to-music translation process is well-explained and scientifically plausible.",
            "The AI composition techniques are coherent and innovative.",
            "Ethical considerations are thoughtfully discussed, including privacy concerns and responsible use guidelines.",
            "Potential applications and future research directions are creatively explored.",
            "The response is well-structured, using appropriate technical terminology and clear explanations.",
            "The proposed system is creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
