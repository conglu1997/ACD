import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"emotion": "Joy", "musical_element": "Rhythm"},
            {"emotion": "Sadness", "musical_element": "Harmony"},
            {"emotion": "Anger", "musical_element": "Timbre"},
            {"emotion": "Fear", "musical_element": "Melody"}
        ]
        return {str(i+1): emotion for i, emotion in enumerate(random.sample(emotions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding emotional states and composing music that expresses or evokes specific emotions, based on theories of music cognition and affective computing. Focus on the emotion of {t['emotion']} and the musical element of {t['musical_element']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain key theories from music cognition and affective computing relevant to emotion-based music composition.
   b) Describe how these theories apply to the relationship between {t['emotion']} and {t['musical_element']}.
   c) Discuss any unique challenges or opportunities in computationally representing and manipulating {t['musical_element']} to express {t['emotion']}.

2. System Architecture (300-350 words):
   a) Describe the main components of your AI system and how they interact.
   b) Explain how your system processes emotional input and translates it into musical parameters.
   c) Detail how your system generates and manipulates {t['musical_element']} to express {t['emotion']}.
   d) Provide a visual representation of your system architecture (describe it textually, using ASCII art if helpful).

3. Composition Process (250-300 words):
   a) Provide a step-by-step example of how your system would compose a short musical piece expressing {t['emotion']} through {t['musical_element']}.
   b) Explain how this process incorporates principles from music cognition and affective computing.
   c) Describe how your system ensures musical coherence and aesthetic quality.
   d) Include a pseudocode snippet (5-10 lines) illustrating a key algorithm in your composition process.

4. Evaluation Methods (200-250 words):
   a) Propose quantitative and qualitative methods to evaluate your system's ability to express {t['emotion']} through music.
   b) Describe how you would compare your system's compositions to those of human composers.
   c) Suggest a novel metric for measuring the emotional impact of the generated music.

5. Ethical Considerations and Future Directions (200-250 words):
   a) Discuss potential ethical issues related to AI-generated emotional music.
   b) Address any limitations of your approach, particularly in capturing the nuances of human emotion in music.
   c) Propose guidelines for the responsible development and use of emotion-based AI music composition systems.
   d) Suggest potential applications of your system beyond music composition.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, affective computing, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include all required sections with appropriate word counts",
            "The system design should demonstrate a clear understanding of music cognition and affective computing theories",
            f"The system must specifically address how it handles the emotion of {t['emotion']} and the musical element of {t['musical_element']}",
            "The architecture should be clearly explained and include a visual representation",
            "The composition process should be logically described with a relevant pseudocode snippet",
            "Evaluation methods should be well-thought-out and include a novel metric",
            "Ethical considerations and limitations should be thoroughly discussed",
            "The response should demonstrate creativity and innovation while maintaining scientific plausibility",
            "Appropriate terminology from music theory, cognitive science, and AI should be used throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
