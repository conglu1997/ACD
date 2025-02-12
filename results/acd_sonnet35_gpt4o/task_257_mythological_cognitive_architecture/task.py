import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mythologies = [
            {
                "mythology": "Norse",
                "being": "Odin",
                "problem": "preventing Ragnarök"
            },
            {
                "mythology": "Greek",
                "being": "Zeus",
                "problem": "maintaining balance between gods and humans"
            }
        ]
        return {
            "1": random.choice(mythologies),
            "2": random.choice(mythologies)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive architecture for {t['being']} from {t['mythology']} mythology, then apply it to solve the problem of {t['problem']}. Follow these steps:

1. Cognitive Architecture Design (200-250 words):
   a) Describe the key components of your cognitive architecture for {t['being']}.
   b) Explain how these components interact to process information and make decisions.
   c) Incorporate at least one unique feature inspired by {t['mythology']} mythology.

2. Mythological Basis (150-200 words):
   a) Explain how your cognitive architecture reflects {t['being']}'s characteristics and abilities in {t['mythology']} mythology.
   b) Discuss any conflicts or synergies between traditional mythology and your cognitive science-based approach.

3. Problem-Solving Application (250-300 words):
   a) Apply your cognitive architecture to the problem of {t['problem']}.
   b) Provide a step-by-step breakdown of how {t['being']} would approach and solve this problem using the designed cognitive architecture.
   c) Explain any unique insights or solutions that emerge from this approach.

4. Comparative Analysis (150-200 words):
   Compare your mythological cognitive architecture to a well-known artificial intelligence cognitive architecture (e.g., ACT-R, SOAR, or CLARION). Discuss similarities, differences, and potential advantages of each approach.

5. Ethical and Narrative Implications (100-150 words):
   a) Discuss the ethical implications of your cognitive architecture in the context of {t['mythology']} mythology.
   b) Explain how this cognitive architecture might influence storytelling and character development in modern adaptations of {t['mythology']} myths.

Ensure your response demonstrates a deep understanding of cognitive science principles, mythology, and creative problem-solving. Be innovative in your approach while maintaining logical consistency and mythological authenticity."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The cognitive architecture design is well-explained and incorporates unique features inspired by {t['mythology']} mythology.",
            f"The problem-solving application demonstrates a logical and creative approach to {t['problem']} using the designed cognitive architecture.",
            "The comparative analysis shows a deep understanding of both mythological and AI cognitive architectures.",
            "The response demonstrates creativity, interdisciplinary knowledge application, and analytical thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
