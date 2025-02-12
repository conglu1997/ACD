import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "brain_region": random.choice(["hippocampus", "amygdala", "prefrontal cortex", "auditory cortex"]),
                "emotional_state": random.choice(["calm", "excited", "melancholic", "joyful"]),
                "musical_style": random.choice(["ambient", "classical", "jazz", "electronic dance music", "folk"])
            },
            "2": {
                "brain_region": random.choice(["hippocampus", "amygdala", "prefrontal cortex", "auditory cortex"]),
                "emotional_state": random.choice(["calm", "excited", "melancholic", "joyful"]),
                "musical_style": random.choice(["ambient", "classical", "jazz", "electronic dance music", "folk"])
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates music based on neural activity patterns, then analyze its output and potential applications in neuroscience and music therapy. Focus on the {t['brain_region']} and create {t['musical_style']} music that induces a {t['emotional_state']} emotional state. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI system for neural music synthesis.
   b) Explain how your system integrates knowledge from neuroscience, music theory, and AI.
   c) Detail how the system maps neural activity patterns to musical elements.

2. Neural-Musical Mapping (200-250 words):
   a) Explain how specific neural patterns from the {t['brain_region']} are translated into musical features.
   b) Describe the process of generating {t['musical_style']} music that induces a {t['emotional_state']} state.
   c) Discuss any challenges in maintaining musical coherence while faithfully representing neural activity.

3. Output Analysis (200-250 words):
   a) Describe the expected characteristics of the generated music.
   b) Explain how the output reflects both the neural patterns and the target emotional state.
   c) Discuss how you would evaluate the quality and effectiveness of the generated music.

4. Neuroscientific Implications (150-200 words):
   a) Analyze how this system could contribute to our understanding of the {t['brain_region']} and its role in emotional processing.
   b) Discuss potential insights into the neural basis of music perception and creation.

5. Music Therapy Applications (150-200 words):
   a) Propose two potential applications of your neural music synthesis system in music therapy.
   b) Explain how these applications could benefit patients or advance the field of music therapy.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns related to using AI-generated music based on neural patterns.
   b) Suggest guidelines for the responsible development and use of such systems in clinical or research settings.

Ensure your response demonstrates a deep understanding of neuroscience, music theory, and AI principles. Be creative in your system design while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, music theory, and AI principles.",
            "The system architecture is well-described and integrates knowledge from all relevant fields.",
            "The neural-musical mapping process is clearly explained and scientifically plausible.",
            "The output analysis shows a thoughtful consideration of both neural and musical aspects.",
            "The neuroscientific implications and music therapy applications are insightful and well-reasoned.",
            "Ethical considerations are thoroughly addressed with appropriate guidelines suggested.",
            "The response is creative while maintaining scientific accuracy and plausibility.",
            f"The response specifically addresses the {t['brain_region']}, {t['musical_style']} music, and {t['emotional_state']} emotional state.",
            "The response follows the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
