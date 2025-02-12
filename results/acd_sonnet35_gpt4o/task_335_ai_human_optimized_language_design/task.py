import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "context": "Space exploration mission control",
                "key_concepts": ["navigation", "resource management", "emergency protocols"],
                "communication_challenges": ["time delay", "limited bandwidth", "critical decision-making"]
            },
            {
                "context": "AI-assisted medical diagnosis",
                "key_concepts": ["symptom analysis", "treatment recommendations", "patient history"],
                "communication_challenges": ["medical jargon", "emotional sensitivity", "real-time updates"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language optimized for AI-human communication in the context of {t['context']}. Your language should facilitate efficient and accurate exchange of information between AI systems and human operators, considering the unique challenges of this environment. Your task has five parts:

1. Language Structure (250-300 words):
   a) Describe the basic elements of your language (e.g., phonemes, morphemes, syntax).
   b) Explain how these elements are optimized for both AI processing and human cognition.
   c) Discuss how your language handles the key concepts: {', '.join(t['key_concepts'])}.
   d) Provide examples of basic sentences or expressions in your language, with translations.

2. Cognitive Load Optimization (200-250 words):
   a) Explain how your language minimizes cognitive load for human users.
   b) Describe features that make it easy for humans to learn and use the language quickly.
   c) Discuss how the language balances precision (for AI) with intuitive understanding (for humans).

3. Disambiguation and Context (200-250 words):
   a) Describe how your language handles ambiguity and context-dependent meanings.
   b) Explain any special features that help clarify intent or resolve misunderstandings.
   c) Provide an example of how your language would handle a potentially ambiguous situation in the given context.

4. Cross-modal Representation (200-250 words):
   a) Explain how your language can be represented across different modalities (e.g., visual, auditory, tactile).
   b) Describe how these representations maintain consistency and meaning across modalities.
   c) Discuss how this cross-modal design helps address the communication challenges: {', '.join(t['communication_challenges'])}.

5. Implementation and Evaluation (150-200 words):
   a) Propose a method for implementing this language in an AI system.
   b) Suggest criteria for evaluating the effectiveness of your language in real-world use.
   c) Discuss potential limitations or areas for future improvement in your language design.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your design while maintaining scientific plausibility and addressing the specific challenges of the given context.

Please structure your response with clear headings for each of the five main sections, and use subheadings or bullet points where appropriate to organize your thoughts within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The language structure is well-defined and optimized for both AI processing and human cognition.",
            "The design effectively minimizes cognitive load for human users while maintaining precision.",
            "The language has clear mechanisms for handling ambiguity and context-dependent meanings.",
            "The cross-modal representation is well-thought-out and addresses the given communication challenges.",
            "The implementation and evaluation proposals are practical and well-reasoned.",
            "The overall design demonstrates creativity, interdisciplinary knowledge, and scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
