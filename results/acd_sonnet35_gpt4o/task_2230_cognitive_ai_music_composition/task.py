import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'cognitive_model': 'Dual-process theory',
                'emotion': 'Nostalgia',
                'musical_style': 'Minimalism',
                'application': 'Memory enhancement therapy'
            },
            {
                'cognitive_model': 'Predictive coding',
                'emotion': 'Awe',
                'musical_style': 'Spectral music',
                'application': 'Virtual reality experiences'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that composes music based on cognitive models of human emotion and perception, then analyze its output for artistic and therapeutic applications. Your system should incorporate the cognitive model of {t['cognitive_model']}, focus on the emotion of {t['emotion']}, compose in the style of {t['musical_style']}, and aim for application in {t['application']}.

Your response should include:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI music composition system.
   b) Explain how it incorporates the specified cognitive model in its design.
   c) Detail how the system models and generates the given emotion through music.
   d) Discuss how the system implements the specified musical style.
   e) Include a high-level diagram or flowchart of your system (describe it textually).

2. Cognitive-Musical Interface (250-300 words):
   a) Explain how your system translates the cognitive model into musical parameters.
   b) Describe how these parameters are used to evoke the specified emotion.
   c) Discuss any challenges in bridging cognitive science and music theory, and how you address them.
   d) Provide a specific example of how your system would compose a musical phrase based on the given inputs.

3. AI Composition Process (250-300 words):
   a) Detail the step-by-step process your AI system follows to compose a piece of music.
   b) Explain how the system ensures coherence and structure in the composition.
   c) Describe how the system balances creativity with adherence to the specified style.
   d) Discuss any machine learning techniques or algorithms used in the composition process.

4. Emotion and Perception Analysis (200-250 words):
   a) Propose a method for analyzing the emotional impact of the AI-generated music on listeners.
   b) Describe how you would measure the effectiveness of the music in evoking the intended emotion.
   c) Discuss potential differences in emotional perception across different listener groups.

5. Artistic and Therapeutic Applications (250-300 words):
   a) Explain how the AI-generated music could be used in the specified application.
   b) Discuss potential benefits and challenges of using AI-composed music in this context.
   c) Propose a study design to test the effectiveness of the music in the given application.
   d) Suggest two other potential applications for your AI music composition system.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using AI-generated music for emotional manipulation or therapy.
   b) Address concerns about AI replacing human composers or devaluing human creativity.
   c) Propose guidelines for the responsible development and use of emotion-based AI music systems.

7. Future Developments (150-200 words):
   a) Suggest potential improvements or extensions to your AI music composition system.
   b) Discuss how advancements in cognitive science or AI could enhance such systems in the future.
   c) Propose a novel research question that arises from the intersection of cognitive science, AI, and music theory.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and music theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, artificial intelligence, and music theory.",
            f"The system architecture effectively incorporates the cognitive model of {t['cognitive_model']}.",
            f"The AI composition process clearly focuses on evoking the emotion of {t['emotion']}.",
            f"The system convincingly implements the musical style of {t['musical_style']}.",
            f"The response provides a plausible application of the AI-generated music in {t['application']}.",
            "The cognitive-musical interface is well-explained and scientifically plausible.",
            "The emotion and perception analysis method is well-thought-out and feasible.",
            "The response addresses ethical considerations comprehensively.",
            "The proposed future developments and research questions are innovative and relevant.",
            "The overall response shows strong integration of knowledge from cognitive science, AI, and music theory.",
            "The response adheres to the specified word limits for each section and overall length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
