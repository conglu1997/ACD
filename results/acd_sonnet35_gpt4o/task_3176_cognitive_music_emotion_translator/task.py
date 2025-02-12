import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotion_complexity = [
            {
                "complexity": "basic",
                "example": "joy",
                "musical_element": "melody"
            },
            {
                "complexity": "complex",
                "example": "bittersweet nostalgia",
                "musical_element": "harmony"
            }
        ]
        return {
            "1": random.choice(emotion_complexity),
            "2": random.choice(emotion_complexity)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that translates {t['complexity']} emotional states (e.g., {t['example']}) into musical compositions, focusing primarily on the musical element of {t['musical_element']}. Your system should be based on principles of cognitive science and music theory. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system incorporates cognitive science principles related to emotion and music perception.
   c) Detail how the system processes emotional input and generates musical output.
   d) Include a simple ASCII diagram or flowchart of your system architecture.

2. Emotion-to-Music Translation Mechanism (200-250 words):
   a) Explain the process of translating emotional states into musical elements, focusing on {t['musical_element']}.
   b) Describe how your system handles the complexity of {t['complexity']} emotions like {t['example']}.
   c) Discuss any novel algorithms or data structures required for this translation.

3. Cognitive-Musical Mapping (200-250 words):
   a) Propose a framework for mapping between emotional states and musical structures.
   b) Explain how your system addresses the subjective nature of emotional experiences in this mapping.
   c) Discuss how your approach might provide insights into the relationship between cognition, emotion, and music.

4. AI and Music Theory Integration (150-200 words):
   a) Describe how artificial intelligence is utilized in your system to apply music theory principles.
   b) Explain the role of machine learning in improving the quality and emotional accuracy of compositions over time.
   c) Discuss any potential for emergent musical creativity in the AI component.

5. Evaluation and Feedback (150-200 words):
   a) Propose methods for evaluating the emotional effectiveness of the generated compositions.
   b) Explain how your system could incorporate human feedback to improve its translations.
   c) Discuss potential challenges in objectively assessing the system's performance.

6. Ethical and Philosophical Implications (150-200 words):
   a) Analyze the ethical considerations of an AI system that translates human emotions into music.
   b) Discuss the philosophical implications of algorithmically generated emotional music.
   c) Consider potential societal impacts of this technology, both positive and negative.

7. Limitations and Future Directions (100-150 words):
   a) Identify potential limitations or challenges in implementing your system.
   b) Propose future research directions to overcome these limitations or expand the system's capabilities.
   c) Speculate on how this technology might evolve and impact the fields of music, therapy, and human-computer interaction.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1200-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence.",
            f"The system effectively translates {t['complexity']} emotional states into musical compositions, focusing on {t['musical_element']}.",
            "The proposed architecture and translation mechanism are innovative yet scientifically plausible.",
            "The response addresses all required sections with appropriate depth and clarity.",
            "The ethical and philosophical implications are thoughtfully considered.",
            "The response is well-structured, coherent, and within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
