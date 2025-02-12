import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = ["auditory cortex", "prefrontal cortex", "hippocampus", "amygdala"]
        musical_elements = ["melody", "harmony", "rhythm", "timbre"]
        emotional_states = ["joy", "sadness", "excitement", "calmness"]
        
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "emotional_state": random.choice(emotional_states)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "emotional_state": random.choice(emotional_states)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that can generate and analyze music based on neural activity patterns, then use it to explore the relationship between brain states and musical creativity. Focus on the {t['brain_region']} for neural input, the musical element of {t['musical_element']}, and the emotional state of {t['emotional_state']}. Consider how neural oscillations, neurotransmitter levels, and connectivity patterns in the {t['brain_region']} might influence {t['musical_element']} and reflect the emotional state of {t['emotional_state']}.\n\nYour response should include the following sections:\n\n" \
               f"1. System Architecture (300-350 words):\n" \
               f"   a) Describe the key components of your AI system for neural music synthesis and analysis.\n" \
               f"   b) Explain how your system integrates neuroscientific data with music generation and analysis.\n" \
               f"   c) Detail how the AI processes neural input from the {t['brain_region']} and translates it into musical output.\n" \
               f"   d) Include a high-level diagram or flowchart of your AI system architecture.\n\n" \
               f"2. Neural-Musical Mapping (250-300 words):\n" \
               f"   a) Explain how your AI system maps neural activity patterns to musical elements, focusing on {t['musical_element']}.\n" \
               f"   b) Describe the methods used to correlate brain states with musical creativity.\n" \
               f"   c) Provide an example of how neural activity in the {t['brain_region']} might influence the generation of {t['musical_element']}.\n\n" \
               f"3. Emotional State Integration (200-250 words):\n" \
               f"   a) Describe how your system incorporates the emotional state of {t['emotional_state']} into music generation and analysis.\n" \
               f"   b) Explain the potential neural correlates of this emotional state and how they relate to musical expression.\n" \
               f"   c) Discuss how your system might differentiate between innate and learned emotional responses in music.\n\n" \
               f"4. Music Generation and Analysis (250-300 words):\n" \
               f"   a) Provide a detailed example of a musical piece your system might generate based on the given parameters.\n" \
               f"   b) Explain how your system would analyze this piece in terms of its neural origins and emotional content.\n" \
               f"   c) Discuss how your system could be used to study the relationship between brain states and musical creativity.\n\n" \
               f"5. Potential Applications and Implications (200-250 words):\n" \
               f"   a) Propose two potential applications of your system in fields such as music therapy, composition, or neuroscience.\n" \
               f"   b) Discuss the implications of your system for our understanding of music cognition and creativity.\n" \
               f"   c) Consider how your system might be used to generate personalized music based on an individual's brain activity.\n\n" \
               f"6. Ethical Considerations and Limitations (150-200 words):\n" \
               f"   a) Identify potential ethical issues in using neural data for music generation and analysis.\n" \
               f"   b) Discuss the limitations of your AI system and the reliability of its outputs.\n" \
               f"   c) Propose guidelines for the responsible development and use of neural music synthesis technology.\n\n" \
               f"Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section, numbered as above. Include the high-level diagram or flowchart of your AI system architecture as mentioned in section 1. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence, particularly in relation to the {t['brain_region']}, {t['musical_element']}, and the emotional state of {t['emotional_state']}.",
            "The AI system design is innovative, plausible, and well-explained, including a relevant high-level diagram or flowchart.",
            "The neural-musical mapping and emotional state integration are thoroughly described and scientifically grounded.",
            "The music generation and analysis example is detailed and clearly linked to the given parameters.",
            "The discussion of potential applications, implications, and ethical considerations is thoughtful and comprehensive.",
            "The response adheres to the specified format and word count (1350-1650 words).",
            "The response includes appropriate technical terminology and clear explanations for complex concepts.",
            "The proposed system maintains scientific plausibility while demonstrating creativity and innovation."
        ]
        
        # Check word count
        word_count = len(submission.split())
        if word_count < 1350 or word_count > 1650:
            return 0.0
        
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
