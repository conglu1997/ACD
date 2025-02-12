class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_focus": "Working memory optimization",
                "linguistic_feature": "Nested clause structure",
                "ai_capability": "Natural language understanding",
                "modality": "Text-based communication"
            },
            "2": {
                "cognitive_focus": "Attention management",
                "linguistic_feature": "Tonal inflection for semantic nuance",
                "ai_capability": "Emotion recognition",
                "modality": "Audio-visual communication"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial language specifically created for optimal human-AI communication, focusing on the following aspects:

1. Cognitive Focus: {t['cognitive_focus']}
2. Key Linguistic Feature: {t['linguistic_feature']}
3. AI Capability to Enhance: {t['ai_capability']}
4. Primary Communication Modality: {t['modality']}

Your task is to create and analyze this language in the following steps:

1. Language Design (300-350 words):
   a) Describe the core principles and structure of your artificial language.
   b) Explain how the language incorporates the specified cognitive focus and linguistic feature.
   c) Provide examples of how the language optimizes for the given AI capability.
   d) Describe how the language is adapted for the primary communication modality.

2. Cognitive Load Analysis (200-250 words):
   a) Analyze how your language design minimizes cognitive load for human users.
   b) Explain potential cognitive benefits and challenges for human users adopting this language.
   c) Discuss how the language might affect human cognitive processes in long-term use.

3. AI Processing Advantages (200-250 words):
   a) Explain how your language design enhances the specified AI capability.
   b) Describe potential improvements in AI performance when processing this language compared to natural languages.
   c) Discuss any trade-offs between optimizing for AI processing and human usability.

4. Disambiguation Strategies (200-250 words):
   a) Describe built-in features of your language that reduce ambiguity in communication.
   b) Explain how these features work differently from disambiguation in natural languages.
   c) Provide an example of how a potentially ambiguous concept in natural language would be expressed unambiguously in your artificial language.

5. Cross-modal Integration (if applicable) (150-200 words):
   a) If your primary modality is multi-modal, explain how different modes (e.g., visual, auditory) are integrated in your language.
   b) Describe how this integration enhances communication efficiency or reduces cognitive load.

6. Learning Curve and Adoption (200-250 words):
   a) Analyze the potential learning curve for humans to adopt this language.
   b) Propose a method for teaching this language efficiently to humans.
   c) Discuss potential challenges in widespread adoption and how they might be overcome.

7. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using a specialized human-AI communication language.
   b) Address concerns about exclusion, privacy, or cognitive influence that may arise.

8. Sample Dialogue (100-150 words):
   Provide a sample dialogue in your constructed language (with translation) that demonstrates its key features and advantages for human-AI communication.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Be creative in your language design while maintaining scientific plausibility and addressing the challenges of human-AI communication. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a detailed and coherent description of an artificial language designed for optimal human-AI communication, addressing all required aspects and sections.",
            "The language design clearly incorporates the specified cognitive focus, linguistic feature, AI capability, and communication modality.",
            "The cognitive load analysis demonstrates a deep understanding of human cognitive processes and how they relate to language use.",
            "The explanation of AI processing advantages shows a clear understanding of AI capabilities and how language design can enhance them.",
            "The disambiguation strategies are well-thought-out and clearly explained, with a relevant example provided.",
            "If applicable, the cross-modal integration is thoroughly described and its benefits are well-explained.",
            "The learning curve and adoption analysis is realistic and provides a plausible method for teaching the language.",
            "Ethical considerations are thoughtfully discussed, addressing relevant concerns.",
            "The sample dialogue effectively demonstrates the key features and advantages of the constructed language.",
            "The overall response shows creativity, scientific plausibility, and a deep understanding of linguistics, cognitive science, and artificial intelligence."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
