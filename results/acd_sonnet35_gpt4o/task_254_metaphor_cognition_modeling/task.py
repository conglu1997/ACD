class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "source_domain": "Ocean",
                "target_domain": "Mind",
                "cultural_context": "Western philosophy"
            },
            "2": {
                "source_domain": "Fire",
                "target_domain": "Emotion",
                "cultural_context": "Japanese poetry"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Model the cognitive process of metaphor comprehension and generation, then apply it to create and explain a novel metaphor. Your task has four parts:

1. Cognitive Model (200-250 words):
   Propose a cognitive model for how the human mind processes and generates metaphors. Include key components such as conceptual mapping, neural activation patterns, and cultural influence. Explain how this model would work for comprehending an existing metaphor and generating a new one.

2. AI Implementation (150-200 words):
   Describe how you would implement this cognitive model in an AI system. What kind of neural network architecture would you use? How would you train it? What data would you need?

3. Novel Metaphor Generation (100-150 words):
   Using your cognitive model, generate a novel metaphor that maps the source domain of '{t['source_domain']}' onto the target domain of '{t['target_domain']}'. Your metaphor should be appropriate for the cultural context of {t['cultural_context']}. Provide the metaphor and a brief explanation of its meaning.

4. Explanation of Metaphor Generation Process (200-250 words):
   Explain step-by-step how your cognitive model and AI implementation would have generated this metaphor. Include details on conceptual mapping, cultural considerations, and any creative leaps made by the system.

Ensure your response demonstrates a deep understanding of cognitive science, metaphor theory, and AI. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a plausible cognitive model for metaphor processing and generation.",
            "The AI implementation description is technically sound and feasible.",
            "The generated metaphor is novel, appropriate for the given domains and cultural context.",
            "The explanation of the metaphor generation process is clear, detailed, and consistent with the proposed cognitive model."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
