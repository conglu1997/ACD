import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "neural_region": "primary auditory cortex",
                "music_element": "pitch perception",
                "composition_style": "classical"
            },
            {
                "neural_region": "superior temporal gyrus",
                "music_element": "rhythm processing",
                "composition_style": "jazz"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural-inspired artificial intelligence system for music composition and analysis, based on the structure and function of the human auditory cortex and music cognition processes. Focus on the {t['neural_region']} and its role in {t['music_element']}, with the goal of composing in the {t['composition_style']} style. Your response should include the following sections:

1. Neural-AI Architecture (300-350 words):
   a) Describe the key components of your AI system, explaining how they mirror the structure and function of the {t['neural_region']}.
   b) Explain how your system incorporates current understanding of {t['music_element']} in human auditory processing.
   c) Detail how you've adapted neural network architectures to reflect these biological processes.
   d) Include a high-level diagram or description of your system's architecture.

2. Music Theory Integration (250-300 words):
   a) Explain how your system incorporates fundamental principles of music theory, particularly those relevant to {t['composition_style']} music.
   b) Describe how your AI model represents and processes musical elements such as melody, harmony, and rhythm.
   c) Discuss any novel approaches you've developed to bridge neuroscience and music theory in your system.

3. Composition Process (250-300 words):
   a) Outline the step-by-step process your AI system would follow to compose a piece of {t['composition_style']} music.
   b) Explain how the system's understanding of {t['music_element']} influences the composition process.
   c) Describe any generative or analytical algorithms your system employs.

4. Analysis Capabilities (200-250 words):
   a) Describe how your system could be used to analyze existing pieces of {t['composition_style']} music.
   b) Explain what unique insights your neural-inspired approach might offer compared to traditional music analysis methods.
   c) Propose an experiment to test your system's analysis capabilities against human music theorists.

5. Evaluation and Validation (200-250 words):
   a) Propose methods to evaluate the quality and authenticity of the music composed by your system.
   b) Describe how you would validate that your system accurately reflects the functioning of the {t['neural_region']}.
   c) Discuss potential limitations of your approach and how they might be addressed in future iterations.

6. Ethical and Creative Implications (150-200 words):
   a) Discuss the ethical considerations of using AI for music composition, particularly in the context of {t['composition_style']} music.
   b) Explore how your system might impact our understanding of human creativity and musical cognition.
   c) Consider potential applications of your system beyond music composition and analysis.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all six required sections with appropriate content and length.",
            f"The neural-AI architecture accurately reflects the structure and function of the {t['neural_region']}.",
            f"The system demonstrates a clear understanding of {t['music_element']} and its role in music cognition.",
            f"The composition process and analysis capabilities are well-explained and plausible for {t['composition_style']} music.",
            "The response shows a deep understanding of neuroscience, AI, and music theory, with appropriate use of technical terminology.",
            "The proposed system is innovative while maintaining scientific plausibility.",
            "Ethical implications and potential applications are thoughtfully addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
