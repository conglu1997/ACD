import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_concepts = [
            {"concept": "Fibonacci sequence", "cognitive_aspect": "pattern recognition"},
            {"concept": "Golden ratio", "cognitive_aspect": "aesthetic perception"},
            {"concept": "Fractal geometry", "cognitive_aspect": "self-similarity processing"},
            {"concept": "Prime number intervals", "cognitive_aspect": "numerical cognition"}
        ]
        return {
            "1": random.choice(musical_concepts),
            "2": random.choice(musical_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and create a novel musical structure based on the mathematical concept of {t['concept']}, and explore its cognitive implications related to {t['cognitive_aspect']}. Your response should include the following sections and be approximately 1000-1200 words in total:

1. Mathematical-Musical Mapping (200-250 words):
   a) Explain how the {t['concept']} can be mapped onto musical elements (e.g., pitch, rhythm, harmony).
   b) Provide a specific example of this mapping, using musical notation or a clear description.
   c) Discuss how this mapping preserves or transforms the mathematical properties of the concept.

2. Novel Musical Structure (200-250 words):
   a) Design a new musical structure or composition technique based on your mapping.
   b) Explain the rules or principles of your musical structure.
   c) Provide a short example (4-8 measures) of music created using your structure, described in musical terms or notation.

3. Cognitive Analysis (200-250 words):
   a) Analyze how your musical structure might engage {t['cognitive_aspect']}.
   b) Discuss potential effects on music perception and cognition.
   c) Propose a hypothesis about how this structure might influence musical memory or learning.

4. Comparative Analysis (150-200 words):
   a) Compare your mathematical-musical mapping to traditional music theory concepts.
   b) Discuss similarities and differences in cognitive processing between your structure and conventional musical forms.

5. Experimental Design (150-200 words):
   a) Propose an experiment to test the cognitive effects of your musical structure.
   b) Describe the methodology, including participant selection, stimuli, and measurements.
   c) Explain how the results could contribute to our understanding of music cognition.

6. Limitations and Challenges (100-150 words):
   a) Discuss potential limitations or challenges of your proposed musical structure.
   b) Suggest possible ways to address or mitigate these limitations.

Ensure your response demonstrates a deep understanding of music theory, mathematical principles, and cognitive science. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and theoretical plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the given mathematical concept and its application to music.",
            "The novel musical structure is well-explained and creatively applies the mathematical-musical mapping.",
            "The cognitive analysis shows a deep understanding of the specified cognitive aspect and its relation to music perception.",
            "The comparative analysis effectively contrasts the novel structure with traditional music theory.",
            "The proposed experiment is well-designed and relevant to testing the cognitive effects of the musical structure.",
            "The response uses appropriate terminology from music theory, mathematics, and cognitive science.",
            "The limitations and challenges of the proposed musical structure are thoughtfully considered.",
            "The response demonstrates creativity and originality in the proposed musical structure and its analysis.",
            "All sections of the response are complete and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
