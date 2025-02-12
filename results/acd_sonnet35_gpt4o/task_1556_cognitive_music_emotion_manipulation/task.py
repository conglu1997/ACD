import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "emotion": "joy",
                "target_emotion": "melancholy",
                "musical_element": "harmony"
            },
            {
                "emotion": "tension",
                "target_emotion": "serenity",
                "musical_element": "rhythm"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system to manipulate the perceived emotional content of music from {t['emotion']} to {t['target_emotion']} using mathematical transformations of {t['musical_element']}. Then, analyze the cognitive implications of these manipulations. Your response should include:

1. System Design (250-300 words):
   a) Describe the mathematical transformation you would apply to {t['musical_element']} to shift the perceived emotion.
   b) Explain how this transformation relates to cognitive models of music perception.
   c) Provide a specific example of how your system would transform a musical piece.

2. Cognitive Analysis (200-250 words):
   a) Analyze how the transformation might affect listeners' cognitive processing of the music.
   b) Discuss potential changes in brain activity or cognitive load during this emotional shift.
   c) Explain how your system accounts for individual differences in music perception.

3. Experimental Design (200-250 words):
   Propose an experiment to test the effectiveness of your system:
   a) Describe the experimental setup, including control and experimental groups.
   b) Explain how you would measure the emotional response and cognitive effects.
   c) Discuss potential confounding variables and how you would control for them.

4. Ethical Implications (150-200 words):
   a) Discuss the ethical considerations of manipulating emotional responses to music.
   b) Analyze potential applications and misuses of this technology.
   c) Propose guidelines for responsible use of emotion-manipulating music systems.

5. Interdisciplinary Connections (100-150 words):
   Draw connections between your system and another scientific field not yet mentioned.
   Explain how insights from that field could inform or enhance your approach.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and mathematical concepts. Use appropriate technical terminology and provide clear explanations for complex ideas. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed system for manipulating {t['musical_element']} to shift perceived emotion from {t['emotion']} to {t['target_emotion']}.",
            "The cognitive analysis demonstrates a deep understanding of music perception and brain function.",
            "The experimental design is well-thought-out, with clear measures and controls.",
            "Ethical implications are thoroughly discussed with responsible guidelines proposed.",
            "The interdisciplinary connection is relevant and insightful.",
            "The response demonstrates creativity and scientific plausibility throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
