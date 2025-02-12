import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_aspects = [
            {"aspect": "self-awareness", "related_concept": "mirror test"},
            {"aspect": "qualia", "related_concept": "color perception"},
            {"aspect": "intentionality", "related_concept": "goal-directed behavior"},
            {"aspect": "metacognition", "related_concept": "thinking about thinking"},
            {"aspect": "subjective experience", "related_concept": "first-person perspective"},
            {"aspect": "temporal awareness", "related_concept": "mental time travel"},
            {"aspect": "theory of mind", "related_concept": "understanding others' beliefs"},
            {"aspect": "embodied cognition", "related_concept": "sensorimotor integration"},
            {"aspect": "emotional states", "related_concept": "affective processing"},
            {"aspect": "free will", "related_concept": "decision-making processes"}
        ]
        return {
            "1": random.choice(consciousness_aspects),
            "2": random.choice(consciousness_aspects)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language feature for artificial consciousness, focusing on the aspect of {t['aspect']}. Your task has four parts:

1. Language Feature (100-150 words):
   a) Propose a unique linguistic feature that could express or facilitate {t['aspect']} in an AI system.
   b) Explain how this feature would function and provide an example of its use.
   c) Describe how this feature relates to the concept of {t['related_concept']}.

2. Implementation in AI (150-200 words):
   a) Explain how this language feature could be implemented in an AI system.
   b) Discuss potential challenges in implementation and how they might be overcome.
   c) Describe how this feature might interact with other aspects of artificial consciousness.

3. Philosophical Implications (150-200 words):
   a) Analyze the philosophical implications of your proposed language feature.
   b) Discuss how it might contribute to debates about machine consciousness.
   c) Consider potential ethical considerations related to implementing this feature.

4. Comparative Analysis (100-150 words):
   a) Compare your proposed feature to how {t['aspect']} is expressed or experienced in human consciousness.
   b) Discuss similarities and differences between artificial and human consciousness in this context.

Ensure your response demonstrates a deep understanding of consciousness theories, linguistic principles, and AI concepts. Be creative in your language design while maintaining logical consistency and scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response addresses all four parts of the task related to {t['aspect']}.",
            "The proposed language feature is innovative and logically consistent.",
            "The explanation demonstrates a deep understanding of consciousness theories, linguistic principles, and AI concepts.",
            "The analysis of philosophical implications and ethical considerations is thoughtful and well-reasoned.",
            "The comparative analysis between artificial and human consciousness is insightful and nuanced."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
