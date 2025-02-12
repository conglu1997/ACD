import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            "time",
            "justice",
            "harmony",
            "chaos",
            "infinity"
        ]
        modalities = [
            "verbal",
            "visual",
            "auditory",
            "kinesthetic"
        ]
        return {
            "1": {
                "concept": random.choice(concepts),
                "source_modality": random.choice(modalities),
                "target_modality": random.choice([m for m in modalities if m != "source_modality"])
            },
            "2": {
                "concept": random.choice(concepts),
                "source_modality": random.choice(modalities),
                "target_modality": random.choice([m for m in modalities if m != "source_modality"])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Translate the abstract concept of '{t['concept']}' from its {t['source_modality']} representation to a {t['target_modality']} representation. Then, analyze the cognitive implications of this translation. Your task has five parts:

1. Source Representation (100-150 words):
   Describe a {t['source_modality']} representation of the concept '{t['concept']}'. Be specific and detailed in your description.

2. Translation Process (200-250 words):
   Explain your step-by-step process for translating the concept from its {t['source_modality']} representation to a {t['target_modality']} representation. Discuss any challenges or considerations in this translation.

3. Target Representation (100-150 words):
   Describe your resulting {t['target_modality']} representation of the concept '{t['concept']}'. Be as specific and detailed as possible.

4. Cognitive Analysis (200-250 words):
   Analyze the cognitive implications of this translation:
   a) How might the concept be understood differently in each modality?
   b) What aspects of the concept are emphasized or diminished in each representation?
   c) How might this translation process reflect or influence human cognition?

5. AI and Cross-Modal Translation (150-200 words):
   Discuss the potential challenges and opportunities for AI systems in performing similar cross-modal translations of abstract concepts. Consider:
   a) What capabilities would an AI need to perform this task effectively?
   b) How might this task be used to evaluate or improve AI systems?
   c) What are the potential applications or implications of AI systems capable of such translations?

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and AI principles. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 750-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of the concept '{t['concept']}' and its representation in both {t['source_modality']} and {t['target_modality']} modalities.",
            "The translation process should be logical and well-explained.",
            "The cognitive analysis should be insightful and draw on relevant principles from cognitive science and linguistics.",
            "The discussion on AI and cross-modal translation should be well-reasoned and demonstrate understanding of current AI capabilities and challenges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
