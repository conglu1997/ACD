import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            {
                'name': 'Cognitive Dissonance',
                'definition': 'The mental discomfort experienced when holding contradictory beliefs or values'
            },
            {
                'name': 'Flow State',
                'definition': 'A mental state of complete absorption and focus in an activity'
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(phenomena)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and analyzes musical compositions based on emotional states and cognitive processes, then apply it to create a musical representation of {t['name']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for emotional-cognitive music generation and analysis.
   b) Explain how your system integrates cognitive science, music theory, and AI techniques.
   c) Detail how your system models emotional states and cognitive processes in musical terms.
   d) Provide a diagram or flowchart of your system's architecture (describe it textually).

2. Cognitive-Musical Mapping (250-300 words):
   a) Explain how your system maps {t['name']} to musical elements (e.g., melody, harmony, rhythm, timbre).
   b) Describe the specific musical features that represent different aspects of {t['name']}.
   c) Discuss how your system ensures the musical output is both psychologically accurate and aesthetically pleasing.

3. Composition Generation (250-300 words):
   a) Describe the process by which your AI system generates a musical composition representing {t['name']}.
   b) Explain how the system incorporates variability and creativity in its compositions.
   c) Provide a short musical score or detailed description of a generated composition for {t['name']}.

4. Analysis Capabilities (200-250 words):
   a) Explain how your system would analyze an existing musical piece to identify elements related to {t['name']}.
   b) Describe the metrics or methods your system uses to quantify the emotional and cognitive content of music.
   c) Propose an experiment to validate your system's analysis capabilities.

5. Psychological Implications (200-250 words):
   a) Discuss how your system's musical representations might enhance our understanding of {t['name']}.
   b) Explore potential applications of your system in psychology research or therapy.
   c) Address any ethical considerations in using AI-generated music to represent psychological phenomena.

6. Limitations and Future Directions (150-200 words):
   a) Discuss the limitations of your current system design.
   b) Propose two potential improvements or expansions to your system.
   c) Suggest how this approach could be applied to other psychological phenomena or cognitive processes.

Ensure your response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, music theory, and artificial intelligence.",
            f"The system architecture effectively integrates cognitive science, music theory, and AI techniques to represent {t['name']}.",
            f"The cognitive-musical mapping for {t['name']} is well-explained and psychologically plausible.",
            "The composition generation process is clearly described and incorporates creativity.",
            "The analysis capabilities are well-defined and a valid experiment is proposed.",
            "Psychological implications and ethical considerations are thoughtfully discussed.",
            "Limitations and future directions are insightfully explored."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
