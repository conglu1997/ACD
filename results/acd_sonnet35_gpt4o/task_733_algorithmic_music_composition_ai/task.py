import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        styles = [
            {
                'style': 'Baroque counterpoint',
                'key_features': 'polyphony, harmonic progression, motivic development'
            },
            {
                'style': 'Jazz improvisation',
                'key_features': 'chord progressions, rhythmic patterns, melodic motifs'
            },
            {
                'style': 'Minimalist composition',
                'key_features': 'repetition, gradual variation, phasing techniques'
            },
            {
                'style': 'Electronic dance music (EDM)',
                'key_features': 'beat patterns, synthesizer sounds, layered textures'
            }
        ]
        return {str(i+1): style for i, style in enumerate(random.sample(styles, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for algorithmic music composition in the style of {t['style']}. Your task is to create a novel approach to generating music that incorporates both musical theory and artificial intelligence concepts. Consider the key features of this style: {t['key_features']}.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI music composition system.
   b) Explain how your system integrates knowledge from music theory and AI.
   c) Discuss how your system models the key features of the given musical style.

2. Musical Representation (200-250 words):
   a) Explain how musical elements (e.g., pitch, rhythm, harmony) are represented in your system.
   b) Describe any novel data structures or algorithms used for musical representation.
   c) Discuss how your representation captures the nuances of the given style.

3. Composition Process (200-250 words):
   a) Outline the step-by-step process your AI system would use to generate a composition.
   b) Explain how your system ensures coherence and adherence to the stylistic norms.
   c) Describe any techniques used for maintaining long-term structure in the composition.

4. Learning and Adaptation (150-200 words):
   a) Explain how your system could learn from existing compositions in the given style.
   b) Describe any mechanisms for adapting or evolving the system's compositional style.
   c) Discuss how you would balance imitation of existing works with novel creation.

5. Evaluation Metrics (150-200 words):
   a) Propose methods for evaluating the quality and stylistic accuracy of the generated compositions.
   b) Describe both quantitative and qualitative approaches to assessment.
   c) Discuss the challenges in evaluating computer-generated music and how you'd address them.

6. Creative AI and Music Theory Implications (200-250 words):
   a) Analyze how your AI system's approach to composition relates to human creativity in music.
   b) Discuss any insights your system might provide into music theory or the nature of the given style.
   c) Explore potential applications of your system in music education or analysis.

7. Ethical Considerations and Limitations (100-150 words):
   a) Identify potential ethical concerns or limitations of using AI for music composition.
   b) Suggest ways to address these concerns in the development and use of such systems.

Ensure your response demonstrates a deep understanding of both music theory and AI principles. Be creative in your system design while maintaining musical and technical plausibility. Use appropriate terminology from both fields and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture effectively integrates concepts from music theory and AI, with a focus on {t['style']}.",
            f"The musical representation and composition process adequately capture the key features: {t['key_features']}.",
            "The response demonstrates creativity and innovation in the AI system design while maintaining musical plausibility.",
            "The evaluation metrics and creative AI implications are thoughtfully considered and well-reasoned.",
            "The response shows a high level of understanding in both music theory and AI concepts, using appropriate terminology from both fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
