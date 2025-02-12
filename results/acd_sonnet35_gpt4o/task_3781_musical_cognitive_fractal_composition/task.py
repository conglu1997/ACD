import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "fractal_type": "Mandelbrot set",
                "cognitive_model": "Tonal Pitch Space",
                "musical_genre": "Classical",
                "target_emotion": "Serenity"
            },
            {
                "fractal_type": "Julia set",
                "cognitive_model": "Generative Theory of Tonal Music",
                "musical_genre": "Jazz",
                "target_emotion": "Excitement"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that generates musical compositions based on the {t['fractal_type']} fractal pattern and the {t['cognitive_model']} cognitive model of musical perception. Your system should create {t['musical_genre']} music aimed at evoking a sense of {t['target_emotion']}. 

Brief explanations:
- {t['fractal_type']}: A mathematical set of points that displays self-similar patterns at every scale.
- {t['cognitive_model']}: A theoretical framework for understanding how humans perceive and process musical structures.

Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your musical cognitive fractal composition system.
   b) Explain how your system integrates fractal mathematics, cognitive models, and music theory.
   c) Detail any novel approaches or algorithms used in your design.
   d) Provide a visual representation or detailed textual description of your system architecture.

2. Fractal-Music Mapping (200-250 words):
   a) Explain how you map the {t['fractal_type']} to musical elements (e.g., pitch, rhythm, harmony).
   b) Describe how this mapping preserves the self-similarity and complexity of the fractal structure.
   c) Discuss how you ensure the resulting music adheres to {t['musical_genre']} conventions.

3. Cognitive Model Integration (200-250 words):
   a) Describe how you incorporate the {t['cognitive_model']} into your composition process.
   b) Explain how this cognitive model influences the generated music's structure and emotional impact.
   c) Discuss any challenges in aligning fractal patterns with cognitive models of music perception.

4. Emotional Targeting (150-200 words):
   a) Detail the strategies your system uses to evoke a sense of {t['target_emotion']} in the listener.
   b) Explain how you balance emotional targeting with fractal structure and cognitive models.
   c) Describe any techniques used to evaluate the emotional impact of the generated compositions.

5. Potential Applications (200-250 words):
   a) Propose two potential applications of your system in music therapy or cognitive enhancement.
   b) Explain the theoretical basis for these applications and their potential benefits.
   c) Discuss any limitations or ethical considerations for using fractal-based music in these contexts.

6. Evaluation and Future Work (150-200 words):
   a) Suggest methods to evaluate the musical quality and cognitive effects of your system's compositions.
   b) Propose two directions for future research that could enhance your system or extend its applications.
   c) Discuss potential interdisciplinary collaborations that could arise from this work.

Ensure your response demonstrates a deep understanding of fractal mathematics, music theory, cognitive science, and generative music systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and artistic plausibility.

Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['fractal_type']} and its application to music generation.",
            f"The system effectively incorporates the {t['cognitive_model']} into the composition process.",
            f"The proposed system convincingly generates {t['musical_genre']} music aimed at evoking {t['target_emotion']}.",
            "The response shows innovative integration of fractal mathematics, cognitive science, and music theory.",
            "The potential applications in music therapy or cognitive enhancement are well-reasoned and plausible.",
            "The evaluation methods and future research directions are insightful and relevant.",
            "The response adheres to the specified word count and formatting requirements.",
            "The system architecture is clearly described and includes novel approaches or algorithms.",
            "The fractal-music mapping preserves self-similarity and complexity while adhering to genre conventions.",
            "The emotional targeting strategies are well-explained and balanced with fractal and cognitive elements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
