import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "communication_type": "chemical signals",
                "civilization_type": "hive-mind insects"
            },
            {
                "communication_type": "gravitational waves",
                "civilization_type": "energy beings"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical universal translation system capable of decoding and translating any form of communication, including potential extraterrestrial languages, based on principles from information theory and linguistics. Your system should be able to handle {t['communication_type']} used by a civilization of {t['civilization_type']}. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the key components of your universal translation system.
   b) Explain how your system incorporates principles from information theory and linguistics.
   c) Detail how your system would approach decoding and translating the specified communication type.
   d) Discuss any novel mechanisms or algorithms specific to handling extraterrestrial languages.

2. Information Theory Application (200-250 words):
   a) Explain how concepts from information theory (e.g., entropy, mutual information) are used in your system.
   b) Describe how your system would quantify and analyze the information content of the alien signals.
   c) Discuss how your approach handles potential differences in information encoding between species.

3. Linguistic Analysis (200-250 words):
   a) Describe the linguistic principles and theories your system uses to analyze unknown languages.
   b) Explain how your system would identify and categorize linguistic elements (e.g., phonemes, morphemes, syntax) in the alien communication.
   c) Discuss how your system handles potential fundamental differences in language structure compared to human languages.

4. Translation Process (200-250 words):
   a) Provide a step-by-step explanation of how your system would translate a message from the specified alien civilization into a human language.
   b) Describe how your system ensures accuracy and maintains the original meaning and context.
   c) Explain how your system handles idioms, metaphors, or culture-specific concepts that might not have direct equivalents.

5. Ethical Considerations (150-200 words):
   a) Discuss potential ethical issues in developing and using a universal translation system.
   b) Address concerns about privacy, cultural preservation, and potential misuse of the technology.
   c) Propose guidelines for responsible development and use of universal translation systems.

6. Limitations and Future Improvements (150-200 words):
   a) Identify potential limitations or challenges in your current system design.
   b) Propose areas for future research or improvement in universal translation technology.
   c) Discuss how advancements in this field might impact interspecies communication and human understanding of language.

Ensure your response demonstrates a deep understanding of information theory, linguistics, and ethical considerations. Be creative in your approach while maintaining scientific plausibility. Use technical terminology appropriately and provide clear explanations for complex concepts.

Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of information theory, linguistics, and their application to universal translation.",
            "The proposed universal translation system is innovative, scientifically plausible, and effectively addresses the specified communication type and civilization.",
            "The system architecture and translation process are well-reasoned and consider both information theory and linguistic principles.",
            "The ethical considerations are thoroughly explored and demonstrate critical thinking about the implications of such technology.",
            "The limitations and future improvements section shows a realistic assessment of the challenges and potential advancements in the field.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
