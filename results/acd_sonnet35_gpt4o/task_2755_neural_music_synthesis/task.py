import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = ['prefrontal cortex', 'auditory cortex', 'motor cortex', 'hippocampus']
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre']
        ai_techniques = ['neural networks', 'generative models', 'reinforcement learning', 'evolutionary algorithms']
        
        tasks = {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "ai_technique": random.choice(ai_techniques)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates neural activity patterns from the {t['brain_region']} into musical compositions, focusing on the musical element of {t['musical_element']} and utilizing the AI technique of {t['ai_technique']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your neural music synthesis system.
   b) Explain how your system interfaces with brain activity data from the {t['brain_region']}.
   c) Detail how your system processes neural signals and converts them into musical elements, focusing on {t['musical_element']}.
   d) Discuss how you incorporate {t['ai_technique']} into your system's design and functionality.

2. Neuroscientific Basis (200-250 words):
   a) Explain the relevant functions and characteristics of the {t['brain_region']}.
   b) Discuss how activity in this region might relate to musical perception or creation, particularly regarding {t['musical_element']}.
   c) Describe any challenges in interpreting neural signals from this region and how your system addresses them.

3. Musical Theory Integration (200-250 words):
   a) Explain how your system incorporates music theory principles, focusing on {t['musical_element']}.
   b) Describe the rules or algorithms used to ensure musical coherence and aesthetics in the output.
   c) Discuss how your system balances faithfulness to neural activity with musical structure and appeal.

4. AI Implementation (200-250 words):
   a) Detail how you implement {t['ai_technique']} in your system.
   b) Explain how this AI technique enhances the translation of neural activity to music.
   c) Discuss any novel approaches or adaptations of the AI technique for this specific application.

5. Potential Applications and Implications (150-200 words):
   a) Explore potential applications of your neural music synthesis system in fields such as neuroscience, music therapy, or artistic expression.
   b) Discuss the implications of your system for our understanding of the relationship between brain activity and music.
   c) Address any ethical considerations related to the interpretation and use of neural data for creative purposes.

6. Limitations and Future Directions (100-150 words):
   a) Identify potential limitations or challenges in implementing and using your system.
   b) Propose future research directions or enhancements to your neural music synthesis approach.
   c) Suggest how your system could be extended to incorporate other brain regions or musical elements.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and theoretical plausibility.

Format your response using clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive explanation of the neural music synthesis system architecture, focusing on the {t['brain_region']} and {t['musical_element']}",
            f"The neuroscientific basis section accurately describes the functions of the {t['brain_region']} and its potential relation to music",
            f"The musical theory integration section effectively explains how {t['musical_element']} is incorporated into the system",
            f"The AI implementation section clearly describes how {t['ai_technique']} is used in the system",
            "The response demonstrates deep understanding of neuroscience, artificial intelligence, and music theory",
            "The proposed system is creative and innovative while remaining scientifically and theoretically plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
