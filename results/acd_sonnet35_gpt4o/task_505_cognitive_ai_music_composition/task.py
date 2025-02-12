import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "Auditory Scene Analysis",
            "Tonal Hierarchy Perception",
            "Rhythmic Grouping",
            "Melodic Expectation",
            "Harmonic Tension-Resolution"
        ]
        musical_elements = [
            "Melody",
            "Harmony",
            "Rhythm",
            "Timbre",
            "Form"
        ]
        musical_styles = [
            "Classical",
            "Jazz",
            "Electronic",
            "World Music",
            "Avant-Garde"
        ]
        return {
            "1": {
                "cognitive_process": random.choice(cognitive_processes),
                "musical_element": random.choice(musical_elements),
                "musical_style": random.choice(musical_styles)
            },
            "2": {
                "cognitive_process": random.choice(cognitive_processes),
                "musical_element": random.choice(musical_elements),
                "musical_style": random.choice(musical_styles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive architecture for AI music composition inspired by theories of human musical cognition and creativity. Your architecture should focus on the cognitive process of {t['cognitive_process']}, emphasize the musical element of {t['musical_element']}, and be capable of generating music in the style of {t['musical_style']}.

Your response should include the following sections:

1. Cognitive-Musical Framework (250-300 words):
   a) Explain the chosen cognitive process and its role in human music perception or creation.
   b) Describe how this process relates to the specified musical element.
   c) Discuss any unique considerations for applying this cognitive process to the given musical style.

2. AI Architecture Design (300-350 words):
   a) Design an AI system that implements the cognitive-musical framework for composition.
   b) Describe the key components of your system and how they interact.
   c) Explain how your system simulates or adapts the chosen cognitive process for AI music creation.
   d) Include a high-level diagram or pseudocode to illustrate your architecture.

3. Composition Process Simulation (200-250 words):
   a) Describe how your AI system would progress through the music composition process.
   b) Provide a specific example of how it would create a musical phrase or section in the given style.
   c) Explain how the system would use the specified musical element in its compositions.

4. Evaluation and Creativity Assessment (200-250 words):
   a) Propose a method to evaluate the musical output of your system.
   b) Discuss how you would assess the creativity of the AI's compositions.
   c) Compare your cognitive approach to traditional algorithmic composition methods.

5. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss any ethical implications of using cognitive-inspired AI for music composition.
   b) Propose two potential applications of your system beyond music creation.
   c) Suggest one area for future research to enhance the cognitive-musical capabilities of AI.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the cognitive process of {t['cognitive_process']}.",
            f"The AI architecture must emphasize the musical element of {t['musical_element']}.",
            f"The system should be capable of generating music in the style of {t['musical_style']}.",
            "The response must include all five required sections: Cognitive-Musical Framework, AI Architecture Design, Composition Process Simulation, Evaluation and Creativity Assessment, and Ethical Considerations and Future Directions.",
            "The AI architecture design must be innovative and demonstrate a clear integration of cognitive science principles with AI and music theory.",
            "The response should show a deep understanding of the chosen cognitive process and its application to music composition.",
            "The composition process simulation must provide a clear and plausible example of how the system would create music.",
            "The evaluation method and creativity assessment should be well-reasoned and specific to the proposed system.",
            "The ethical considerations should be thoughtful and relevant to AI music composition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
