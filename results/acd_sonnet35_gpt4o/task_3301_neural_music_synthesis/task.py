import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "prefrontal cortex",
            "hippocampus",
            "amygdala",
            "motor cortex"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre"
        ]
        neural_recording_methods = [
            "EEG",
            "fMRI",
            "single-unit recording",
            "calcium imaging"
        ]
        return {
            "1": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "recording_method": random.choice(neural_recording_methods)
            },
            "2": {
                "brain_region": random.choice(brain_regions),
                "musical_element": random.choice(musical_elements),
                "recording_method": random.choice(neural_recording_methods)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates real-time neural activity into musical compositions, focusing on the {t['brain_region']} and its relationship to the musical element of {t['musical_element']}. Your system should use {t['recording_method']} for neural data acquisition. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your neural music synthesis system.
   b) Explain how neural data is acquired, processed, and translated into musical parameters.
   c) Detail how you map neural activity from the {t['brain_region']} to {t['musical_element']}.
   d) Discuss any AI or machine learning techniques used in your system.

2. Neural-Musical Mapping (250-300 words):
   a) Provide a detailed explanation of how specific neural patterns are translated into musical features.
   b) Describe how your system ensures musical coherence and aesthetic quality.
   c) Explain how you handle the temporal aspects of both neural activity and music.

3. Real-time Processing and Performance (200-250 words):
   a) Describe how your system processes neural data in real-time.
   b) Explain any techniques used to minimize latency between neural activity and musical output.
   c) Discuss how the system could be used in a live performance setting.

4. Neuroscientific Insights (200-250 words):
   a) Explain how your system could be used to gain new insights into brain function, particularly in the {t['brain_region']}.
   b) Discuss potential experiments that could be conducted using your system.
   c) Describe how your system might contribute to our understanding of the neural basis of music perception and creation.

5. Artistic Applications (150-200 words):
   a) Propose novel artistic applications of your neural music synthesis system.
   b) Discuss how this technology might influence the future of music composition and performance.
   c) Address any ethical considerations related to using neural activity for artistic expression.

6. Technical Challenges and Future Directions (150-200 words):
   a) Identify the main technical challenges in implementing your system.
   b) Propose solutions or areas for future research to address these challenges.
   c) Suggest potential improvements or extensions to your system.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, particularly regarding the specified brain region and recording method.",
            "The system design shows a clear and plausible mapping between neural activity and the specified musical element.",
            "The response includes innovative ideas for both scientific and artistic applications of the system.",
            "The technical challenges and future directions are thoughtfully considered and addressed.",
            "The overall response is well-structured, coherent, and demonstrates interdisciplinary knowledge integration and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
