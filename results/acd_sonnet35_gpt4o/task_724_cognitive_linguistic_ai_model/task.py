import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_theories = [
            "Dual-process theory",
            "Embodied cognition",
            "Predictive processing",
            "Connectionism"
        ]
        linguistic_universals = [
            "Recursion",
            "Compositionality",
            "Phonological rules",
            "Syntactic categories"
        ]
        return {
            "1": {
                "cognitive_theory": random.choice(cognitive_theories),
                "linguistic_universal": random.choice(linguistic_universals)
            },
            "2": {
                "cognitive_theory": random.choice(cognitive_theories),
                "linguistic_universal": random.choice(linguistic_universals)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel language model inspired by the cognitive theory of {t['cognitive_theory']} and the linguistic universal of {t['linguistic_universal']}. Then, propose experiments to test its capabilities. Your response should include:

1. Theoretical Foundation (200-250 words):
   a) Explain the key concepts of {t['cognitive_theory']} and how they relate to language processing.
   b) Describe the linguistic universal of {t['linguistic_universal']} and its importance in human language.
   c) Discuss how these two concepts might interact or complement each other in a language model.

2. Model Architecture (250-300 words):
   a) Describe the overall structure of your language model, including its main components and their interactions.
   b) Explain how your model incorporates principles from {t['cognitive_theory']}.
   c) Detail how your model accounts for the linguistic universal of {t['linguistic_universal']}.
   d) Include a high-level diagram or pseudocode to illustrate your model's architecture.

3. Learning and Processing (200-250 words):
   a) Explain how your model would learn language, referencing relevant aspects of {t['cognitive_theory']}.
   b) Describe how your model would process and generate language, particularly in relation to {t['linguistic_universal']}.
   c) Discuss any novel features or mechanisms in your model that differ from traditional language models.

4. Experimental Design (250-300 words):
   Propose two experiments to test your model's capabilities:
   a) Experiment 1: Design an experiment to test how well your model captures the principles of {t['cognitive_theory']} in language processing.
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would validate (or invalidate) your model's approach.
   b) Experiment 2: Design an experiment to evaluate your model's handling of {t['linguistic_universal']}.
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would demonstrate your model's proficiency with this linguistic universal.

5. Implications and Future Directions (150-200 words):
   a) Discuss the potential implications of your model for our understanding of human language processing and AI language models.
   b) Explore how your model might be extended or applied to other areas of cognitive science or linguistics.
   c) Propose two directions for future research based on your model.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and AI principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['cognitive_theory']} and its relevance to language processing.",
            f"The model design must effectively incorporate principles from {t['cognitive_theory']} and account for the linguistic universal of {t['linguistic_universal']}.",
            "The proposed experiments must be well-designed and directly test the model's key features and capabilities.",
            "The response must show creativity and originality in the model design while maintaining scientific plausibility.",
            "The discussion of implications and future directions must demonstrate a broad understanding of cognitive science, linguistics, and AI.",
            "The overall response must exhibit strong interdisciplinary knowledge integration and advanced reasoning in cognitive linguistics and AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
