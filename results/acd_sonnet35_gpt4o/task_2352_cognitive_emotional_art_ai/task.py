import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "emotion": "existential dread",
                "cognitive_state": "temporal dissonance",
                "context": "facing mortality"
            },
            {
                "emotion": "transcendent joy",
                "cognitive_state": "expanded consciousness",
                "context": "spiritual awakening"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting abstract conceptual art based on complex emotional and cognitive states. Then, use your system to analyze and create artwork for the following psychological scenario:

Emotion: {t['emotion']}
Cognitive State: {t['cognitive_state']}
Context: {t['context']}

Your response should include:

1. AI System Design (300-350 words):
   a) Describe the architecture of your AI system, including its main components and how they interact.
   b) Explain how your system models and processes complex emotions and cognitive states.
   c) Detail the mechanisms for generating and interpreting abstract conceptual art.
   d) Discuss any novel features or approaches in your system design.
   e) Provide a brief example of pseudocode or a code snippet illustrating a key component of your system.

2. Artistic Generation Process (250-300 words):
   a) Explain how your AI system would approach creating art for the given scenario.
   b) Describe the key elements, symbols, or techniques it might employ.
   c) Provide a detailed textual description of the artwork your AI would generate, including specific visual elements, colors, shapes, and composition.
   d) Explain how this artwork reflects the specified emotion, cognitive state, and context.

3. Interpretation and Analysis (200-250 words):
   a) Describe how your AI system would interpret its own generated artwork.
   b) Explain the key insights or meanings it would extract from the piece.
   c) Compare this AI interpretation to potential human interpretations of the same work.

4. Cognitive-Emotional Mapping (200-250 words):
   a) Analyze how your AI system maps complex emotional and cognitive states to visual elements.
   b) Discuss any challenges in representing abstract psychological concepts in art.
   c) Explain how your system's approach might differ from human artists tackling similar themes.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of AI-generated emotional and cognitive art.
   b) Explore the philosophical questions raised by machines interpreting and creating art about human experiences.
   c) Propose guidelines for responsible development and use of such AI systems in artistic and therapeutic contexts.

Ensure your response demonstrates a deep understanding of cognitive science, emotional processing, artistic theory, and AI systems. Be creative and innovative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section and use subheadings (a, b, c, etc.) as outlined above. Your total response should be between 1100-1350 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, emotional processing, artistic theory, and AI systems",
            "The proposed AI system is innovative and plausibly incorporates methods for processing complex emotions and cognitive states",
            "The explanation of the artistic generation process is clear, creative, and aligns with the given psychological scenario",
            "The response includes a detailed textual description of the generated artwork with specific visual elements",
            "The response provides a brief example of pseudocode or code snippet for a key component of the AI system",
            "The discussion of ethical and philosophical implications is thoughtful and considers multiple perspectives",
            "The response addresses all required sections comprehensively, uses the specified format, and meets the word count requirement"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
