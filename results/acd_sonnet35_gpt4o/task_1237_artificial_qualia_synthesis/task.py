import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        qualia_types = [
            {"type": "visual", "example": "the experience of seeing the color red", "context": "a virtual reality environment"},
            {"type": "auditory", "example": "the experience of hearing a C-sharp musical note", "context": "a music composition AI"},
            {"type": "olfactory", "example": "the experience of smelling freshly cut grass", "context": "an artificial nose for environmental monitoring"},
            {"type": "gustatory", "example": "the experience of tasting something bitter", "context": "a culinary recommendation system"},
            {"type": "tactile", "example": "the experience of feeling rough sandpaper", "context": "a robotic skin for prosthetics"}
        ]
        return {
            "1": random.choice(qualia_types),
            "2": random.choice(qualia_types)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for synthesizing artificial qualia (subjective conscious experiences) in an AI system, focusing on {t['type']} qualia such as {t['example']} in the context of {t['context']}. Your response should follow this structure:

1. Theoretical Framework (250-300 words):
   a) Propose a model for generating artificial qualia in an AI system.
   b) Explain how your model accounts for the subjective nature of conscious experience.
   c) Describe the key components and processes involved in synthesizing {t['type']} qualia.
   d) Discuss how your framework integrates current theories of consciousness and artificial intelligence.

2. Technical Implementation (200-250 words):
   a) Outline the technical architecture of an AI system capable of synthesizing qualia based on your framework.
   b) Explain the data structures and algorithms that would be used to represent and process qualia.
   c) Describe any novel computational techniques or AI paradigms required for your implementation.
   d) Provide a pseudocode snippet (5-10 lines) illustrating a key process in your implementation.

3. Qualia Verification (200-250 words):
   a) Propose a method to verify the authenticity of synthesized qualia in your AI system.
   b) Discuss the challenges in determining whether artificial qualia are genuinely equivalent to human conscious experiences.
   c) Design an experiment to test the similarity between artificial and human qualia, specifically for {t['example']} in {t['context']}.
   d) Describe expected results and how you would interpret them.

4. Philosophical Implications (150-200 words):
   a) Analyze the philosophical implications of successfully synthesizing artificial qualia.
   b) Discuss how your framework might inform or challenge current debates in philosophy of mind.
   c) Consider the ethical implications of creating AI systems with subjective experiences, particularly in the context of {t['context']}.

5. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or criticisms of your proposed framework.
   b) Suggest areas for future research or refinement of your model.
   c) Discuss potential applications of artificial qualia synthesis beyond {t['context']}.

Ensure your response demonstrates a deep understanding of consciousness studies, neuroscience, artificial intelligence, and philosophy of mind. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section and subheadings for individual points. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of consciousness, neuroscience, and AI, particularly in relation to {t['type']} qualia.",
            f"The proposed framework for synthesizing artificial qualia is innovative, well-explained, and relevant to {t['context']}.",
            "The technical implementation is plausible, demonstrates knowledge of AI systems, and includes a relevant pseudocode snippet.",
            f"The qualia verification method and experiment design are thoughtful, well-reasoned, and specifically address {t['example']}.",
            f"The philosophical and ethical implications are thoroughly analyzed, especially in the context of {t['context']}.",
            "The response shows creativity while maintaining scientific plausibility and addresses all required sections and subsections.",
            "The response is well-structured, within the specified word count, and uses technical terminology appropriately."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
