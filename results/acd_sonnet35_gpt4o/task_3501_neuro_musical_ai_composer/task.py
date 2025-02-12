import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            {
                'region': 'prefrontal cortex',
                'musical_element': 'melody',
                'emotional_state': 'joy'
            },
            {
                'region': 'amygdala',
                'musical_element': 'rhythm',
                'emotional_state': 'fear'
            },
            {
                'region': 'hippocampus',
                'musical_element': 'harmony',
                'emotional_state': 'nostalgia'
            }
        ]
        return {str(i+1): region for i, region in enumerate(random.sample(brain_regions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates brain activity patterns into musical compositions, focusing on the {t['region']} and its relationship to {t['musical_element']}. Your system should aim to evoke or represent the emotional state of {t['emotional_state']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for translating brain activity to music.
   b) Explain how your system processes neural signals from the {t['region']}.
   c) Detail how your system generates {t['musical_element']} based on these signals.
   d) Discuss how your system incorporates or represents the emotional state of {t['emotional_state']}.

2. Neuroscience-Music Interface (250-300 words):
   a) Explain the neurophysiological basis for your chosen brain-to-music mapping.
   b) Describe how you handle the complexity and variability of brain signals.
   c) Discuss any novel algorithms or techniques used in your system.

3. Musical Output Analysis (250-300 words):
   a) Describe the expected characteristics of the musical compositions produced by your system.
   b) Explain how these characteristics relate to the activity in the {t['region']}.
   c) Discuss how the {t['musical_element']} in your compositions might reflect or induce {t['emotional_state']}.

4. Potential Applications (200-250 words):
   a) Propose two potential applications of your system in neuroscience research.
   b) Suggest two ways your system could be used in music therapy.
   c) Discuss any potential benefits or insights these applications might provide.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of translating brain activity into music.
   b) Address privacy concerns related to 'reading' and interpreting brain activity.
   c) Propose guidelines for the responsible development and use of such technology.

6. Future Directions (200-250 words):
   a) Suggest two potential improvements or extensions to your system.
   b) Discuss how these improvements could enhance our understanding of the brain-music relationship.
   c) Propose an experiment to test the effectiveness or impact of your system.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words. Include a brief summary (50-100 words) at the end of your response.

Your response will be evaluated based on the depth of understanding shown, the innovation and plausibility of your system design, and the thoroughness of your analysis across all sections. A successful response will demonstrate comprehensive knowledge integration across neuroscience, music theory, and AI."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['region']} and its potential relationship to {t['musical_element']}.",
            f"The proposed system plausibly translates brain activity into {t['musical_element']} while considering the emotional state of {t['emotional_state']}.",
            "The system architecture and neuroscience-music interface are innovative yet scientifically grounded.",
            "The response shows creative problem-solving and interdisciplinary knowledge integration across neuroscience, music theory, and artificial intelligence.",
            "The potential applications and ethical considerations are thoughtfully discussed and relevant to the proposed system.",
            "The response follows the required format, including all specified sections and a brief summary."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
