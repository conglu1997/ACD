import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy",
            "sadness",
            "anger",
            "fear",
            "surprise",
            "disgust",
            "anticipation",
            "trust",
            "nostalgia",
            "serenity"
        ]
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre",
            "dynamics",
            "tempo",
            "texture",
            "form",
            "articulation",
            "instrumentation"
        ]
        tasks = [
            {
                "emotion": random.choice(emotions),
                "musical_element": random.choice(musical_elements),
                "target_audience": random.choice(["children", "adults", "elderly", "teenagers", "cross-cultural"])
            } for _ in range(2)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate original music compositions to evoke the emotion of {t['emotion']}, with a particular focus on manipulating the musical element of {t['musical_element']}. The system should be optimized for a target audience of {t['target_audience']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI music generation system.
   b) Explain how your system integrates principles from music theory, cognitive science, and emotional psychology.
   c) Detail how the system processes and represents emotional states and musical elements.
   d) Discuss any novel approaches you've incorporated to handle the complexities of emotional music synthesis.

2. Emotion-Music Mapping (250-300 words):
   a) Explain how your system maps the emotion of {t['emotion']} to musical characteristics, particularly {t['musical_element']}.
   b) Provide specific examples of how different aspects of {t['musical_element']} might be manipulated to evoke {t['emotion']}.
   c) Discuss how your system accounts for cultural differences in emotional responses to music.

3. Target Audience Considerations (200-250 words):
   a) Describe how your system adapts its output for the target audience of {t['target_audience']}.
   b) Explain any specific cognitive or emotional factors considered for this age group.
   c) Discuss potential challenges in creating emotionally resonant music for this audience.

4. Music Generation Process (200-250 words):
   a) Outline the step-by-step process your AI system would use to generate a composition.
   b) Explain how the system ensures musical coherence while maintaining emotional resonance.
   c) Describe any constraints or guidelines built into the system to produce pleasing music.

5. Sample Output Description (150-200 words):
   a) Provide a detailed description of a hypothetical piece of music your system might generate for the given emotion, musical element, and target audience.
   b) Explain how specific aspects of this composition reflect the system's design and goals.

6. Evaluation Metrics (150-200 words):
   a) Propose specific metrics to evaluate the emotional effectiveness of the generated music.
   b) Describe how you would measure the system's success in evoking the intended emotion.
   c) Discuss the challenges in objectively evaluating emotional responses to music.

7. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to AI systems that can manipulate emotions through music.
   b) Consider the societal implications of such technology, both positive and negative.
   c) Propose guidelines for the responsible development and use of emotional music synthesis systems.

8. Future Research Directions (100-150 words):
   a) Suggest two potential areas for further research to advance emotional music synthesis.
   b) Explain how these research directions could address current limitations or open up new possibilities.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1500-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the relationship between music, particularly {t['musical_element']}, and the emotion of {t['emotion']}.",
            f"The system design effectively considers the target audience of {t['target_audience']} in its approach to emotional music synthesis.",
            "The proposed AI system integrates principles from music theory, cognitive science, and emotional psychology in a coherent and innovative way.",
            "The sample output description provides a clear and plausible example of the system's capabilities.",
            "The response addresses ethical implications and proposes responsible guidelines for the development and use of emotional music synthesis technology.",
            "The suggested future research directions are insightful and have the potential to advance the field significantly."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
