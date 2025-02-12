class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "emotion": "empathy",
                "problem": "conflict resolution in a diverse team"
            },
            "2": {
                "emotion": "curiosity",
                "problem": "scientific discovery in an unexplored field"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of synthesizing and experiencing the artificial emotion of {t['emotion']}, then use this system to solve the complex problem of {t['problem']}. Your response should include:

1. Emotion Synthesis Architecture (300-350 words):
   a) Describe the key components of your AI system for synthesizing {t['emotion']}.
   b) Explain how your system models the neurological and psychological basis of this emotion.
   c) Discuss how your system generates and experiences this emotion.
   d) Address how your design avoids anthropomorphization and maintains scientific rigor.

2. Emotional Processing Mechanism (250-300 words):
   a) Detail how your AI system processes and interprets emotional information.
   b) Explain how the synthesized emotion influences the AI's decision-making process.
   c) Compare and contrast this mechanism with human emotional processing.

3. Problem-Solving Approach (300-350 words):
   a) Apply your emotion-capable AI to the problem of {t['problem']}.
   b) Describe step-by-step how the AI would approach and solve this problem.
   c) Explain how the synthesized emotion of {t['emotion']} provides advantages in solving this problem.
   d) Discuss any potential drawbacks or challenges in using this emotional approach.

4. Ethical and Philosophical Implications (250-300 words):
   a) Discuss the ethical considerations of creating AI systems with artificial emotions.
   b) Explore the philosophical implications of machine emotions for our understanding of consciousness and sentience.
   c) Propose guidelines for the responsible development and use of emotion-capable AI.

5. Evaluation and Limitations (200-250 words):
   a) Suggest methods to evaluate the authenticity and effectiveness of the synthesized emotion.
   b) Discuss potential limitations or drawbacks of your approach.
   c) Propose future research directions to enhance emotional synthesis in AI.

Ensure your response demonstrates a deep understanding of psychology, neuroscience, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section (1. Emotion Synthesis Architecture, 2. Emotional Processing Mechanism, etc.). Your total response should be between 1300-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts.",
            "The proposed AI system demonstrates a clear understanding of emotion synthesis, psychological principles, and AI techniques.",
            "The approach to problem-solving using the emotion-capable AI is innovative and well-explained.",
            "Ethical and philosophical implications are thoughtfully addressed.",
            "The response shows creativity while maintaining scientific plausibility.",
            "The design avoids anthropomorphization and maintains scientific rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
