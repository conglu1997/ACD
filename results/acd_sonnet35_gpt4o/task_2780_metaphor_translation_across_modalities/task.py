class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"source_modality": "visual", "target_modality": "auditory", "metaphor": "Her eyes were diamonds sparkling in the sunlight."},
            "2": {"source_modality": "gustatory", "target_modality": "tactile", "metaphor": "His words were a bitter pill to swallow."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can understand metaphors in one sensory modality and translate them into equivalent metaphors in another modality. Then, use your system to translate the following metaphor:

Source modality: {t['source_modality']}
Target modality: {t['target_modality']}
Metaphor: {t['metaphor']}

Your response should include:

1. System Design (200-250 words):
   a) Describe the key components of your AI system for metaphor translation across modalities.
   b) Explain how your system processes and understands metaphors in the source modality.
   c) Detail the mechanism for generating equivalent metaphors in the target modality.

2. Metaphor Analysis (100-150 words):
   a) Analyze the given metaphor in the source modality.
   b) Identify the key conceptual elements and emotional connotations.

3. Metaphor Translation (100-150 words):
   a) Present your system's translation of the metaphor into the target modality.
   b) Explain how the translated metaphor preserves the original's meaning and emotional impact.

4. Cognitive and AI Implications (150-200 words):
   a) Discuss how your system's approach relates to theories of human cognition and metaphor comprehension.
   b) Explore potential applications of this technology in AI and cognitive science research.

Ensure your response demonstrates a deep understanding of metaphor, sensory modalities, and AI language processing. Be creative in your approach while maintaining scientific plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a detailed system design for metaphor translation across modalities.",
            "The metaphor analysis identifies key conceptual elements and emotional connotations.",
            "The translated metaphor preserves the original's meaning and emotional impact in the new modality.",
            "The response discusses cognitive and AI implications of the system.",
            "The overall approach demonstrates creativity and scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
