import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = ['Fibonacci sequence', 'fractal geometry', 'chaos theory', 'group theory']
        cognitive_models = ['auditory scene analysis', 'gestalt principles', 'predictive coding', 'tonal hierarchies']
        musical_elements = ['rhythm', 'harmony', 'timbre', 'form']
        
        return {
            "1": {
                "math_concept": random.choice(mathematical_concepts),
                "cognitive_model": random.choice(cognitive_models),
                "musical_element": random.choice(musical_elements)
            },
            "2": {
                "math_concept": random.choice(mathematical_concepts),
                "cognitive_model": random.choice(cognitive_models),
                "musical_element": random.choice(musical_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical composition system that integrates the mathematical concept of {t['math_concept']}, the cognitive model of {t['cognitive_model']}, and focuses on the musical element of {t['musical_element']}. Then, use this system to create and analyze a short musical piece. Your response should include:

1. System Design (300-350 words):
   a) Explain how your composition system incorporates the given mathematical concept and cognitive model.
   b) Describe how it specifically addresses the focal musical element.
   c) Outline the key components and rules of your system.
   d) Provide a specific example of how the mathematical concept is applied in your system.

2. Composition Creation (200-250 words):
   a) Using your system, create a short musical piece (you may describe it in words or use a simplified notation).
   b) Explain how each aspect of your composition reflects the mathematical concept, cognitive model, and musical element.

3. Analysis (200-250 words):
   a) Analyze your composition in terms of its mathematical structure.
   b) Discuss how it might be perceived according to the specified cognitive model.
   c) Evaluate its effectiveness in showcasing the focal musical element.

4. Cognitive Impact (150-200 words):
   a) Hypothesize how your composition system might influence listeners' cognitive processing of music.
   b) Propose an experiment to test this hypothesis.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss potential applications of your system in music education or music therapy.
   b) Explore how this approach might inform AI-generated music or music recommendation systems.

6. Limitations and Future Work (100-150 words):
   a) Reflect on potential limitations of your designed system.
   b) Suggest areas for future research or improvement.

Ensure your response demonstrates a deep understanding of music theory, the specified mathematical concept, and the cognitive model of auditory perception. Be creative in your approach while maintaining scientific and musical plausibility. Adhere to the word limits for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The composition system effectively incorporates the mathematical concept of {t['math_concept']}, the cognitive model of {t['cognitive_model']}, and focuses on the musical element of {t['musical_element']}.",
            "The system design is clearly explained and logically consistent, with a specific example of how the mathematical concept is applied.",
            "A short musical piece is created using the designed system and adequately described or notated.",
            "The composition is analyzed in terms of its mathematical structure and potential cognitive perception.",
            "The response includes a hypothesis about the cognitive impact of the composition system and a proposed experiment to test it.",
            "Potential applications in music education, therapy, AI-generated music, or music recommendation systems are discussed.",
            "Limitations of the designed system are reflected upon, and areas for future research are suggested.",
            "The overall response demonstrates creativity, interdisciplinary knowledge integration, and a deep understanding of music theory, mathematics, and cognitive science.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
