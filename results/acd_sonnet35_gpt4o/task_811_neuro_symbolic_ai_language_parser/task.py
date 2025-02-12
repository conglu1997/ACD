import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_phenomena = [
            {
                "phenomenon": "Garden path sentences",
                "example": "The horse raced past the barn fell.",
                "challenge": "Resolving structural ambiguity"
            },
            {
                "phenomenon": "Pragmatic implicatures",
                "example": "Some students passed the exam.",
                "challenge": "Inferring implied meaning"
            },
            {
                "phenomenon": "Anaphora resolution",
                "example": "The trophy doesn't fit in the suitcase because it's too big.",
                "challenge": "Resolving pronoun references"
            },
            {
                "phenomenon": "Metaphorical language",
                "example": "Life is a roller coaster.",
                "challenge": "Interpreting non-literal meanings"
            }
        ]
        return {
            "1": random.choice(linguistic_phenomena),
            "2": random.choice(linguistic_phenomena)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuro-symbolic AI system for parsing and understanding complex linguistic structures, with a focus on handling the linguistic phenomenon of {t['phenomenon']}. Your task has five parts:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your neuro-symbolic AI system for language understanding.
   b) Explain how it integrates neural networks with symbolic reasoning.
   c) Detail how the system specifically addresses the challenge of {t['challenge']}.
   d) Include a high-level diagram or pseudocode to illustrate your system's architecture.

2. Neural Component (200-250 words):
   a) Describe the neural network part of your system, including its type and structure.
   b) Explain how this neural component contributes to understanding {t['phenomenon']}.
   c) Discuss any novel features or mechanisms in your neural design.

3. Symbolic Component (200-250 words):
   a) Describe the symbolic reasoning part of your system.
   b) Explain how this symbolic component aids in handling {t['phenomenon']}.
   c) Discuss how the symbolic and neural components interact in your system.

4. Performance Analysis (250-300 words):
   a) Analyze how your system would perform on the example: "{t['example']}"
   b) Provide a step-by-step breakdown of how your system would process this example.
   c) Discuss any challenges your system might face with this or similar examples.
   d) Compare your system's approach to how humans might process the same linguistic phenomenon.

5. Evaluation and Future Directions (150-200 words):
   a) Propose a method to evaluate your system's performance on {t['phenomenon']}.
   b) Discuss the potential implications of your system for our understanding of human language processing.
   c) Suggest two directions for future research or improvements to your system.

Ensure your response demonstrates a deep understanding of AI architectures, linguistics, and cognitive science. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a comprehensive description of a neuro-symbolic AI system architecture that integrates neural networks with symbolic reasoning.",
            f"The system design specifically addresses the challenge of {t['challenge']} in the context of {t['phenomenon']}.",
            "The neural and symbolic components are clearly explained, including their interaction and contribution to language understanding.",
            f"The performance analysis provides a detailed breakdown of how the system would process the example: \"{t['example']}\"",
            "The response demonstrates a deep understanding of AI architectures, linguistics, and cognitive science principles.",
            "The proposed evaluation method and future research directions are relevant and insightful.",
            "The response is creative and innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
