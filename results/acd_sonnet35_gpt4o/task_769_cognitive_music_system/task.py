class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_principle": "Working memory capacity",
                "musical_element": "Harmonic progression",
                "emotion": "Nostalgia",
                "tempo_range": (60, 80)
            },
            "2": {
                "cognitive_principle": "Attentional blink",
                "musical_element": "Rhythmic structure",
                "emotion": "Anticipation",
                "tempo_range": (100, 120)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical system based on cognitive principles, then use it to compose and analyze music. Your task has the following components:

1. System Design (300-350 words):
   a) Create a musical system that incorporates the cognitive principle of {t['cognitive_principle']} into the musical element of {t['musical_element']}.
   b) Explain how your system reflects or exploits this cognitive principle.
   c) Describe the key components and rules of your musical system.
   d) Discuss how your system differs from traditional Western music theory.
   e) Provide a visual representation or notation system for your musical system (use ASCII art or Unicode characters).
   f) Include at least one mathematical formula or quantitative rule that governs an aspect of your system.

2. Composition (250-300 words):
   a) Using your musical system, compose a short piece (describe it in words) that aims to evoke the emotion of {t['emotion']}.
   b) Explain how specific elements of your composition relate to the cognitive principle and musical element.
   c) Describe how your system's unique features contribute to expressing the intended emotion.
   d) Specify a tempo within the range of {t['tempo_range']} BPM and justify your choice based on your system's principles.

3. Cognitive Analysis (250-300 words):
   a) Analyze how your musical system might affect listeners' cognitive processes, particularly in relation to {t['cognitive_principle']}.
   b) Propose a hypothesis about how repeated exposure to music in your system might influence perception or memory.
   c) Discuss potential cognitive advantages or challenges for musicians learning to compose in your system.
   d) Suggest an experiment design to test one of your hypotheses, including dependent and independent variables.

4. Cross-Cultural Perspective (200-250 words):
   a) Compare your system to a non-Western musical tradition of your choice.
   b) Discuss how cultural background might influence the perception and emotional impact of music created in your system.
   c) Propose how your system could be adapted to incorporate elements from diverse musical traditions.
   d) Provide a specific example of how a musical phrase might be interpreted differently across cultures.

5. AI Application (200-250 words):
   a) Describe how an AI could be trained to compose music using your system.
   b) Discuss potential challenges in teaching an AI to understand and generate emotionally evocative music in your system.
   c) Propose an experiment to test whether human listeners can distinguish between human-composed and AI-composed pieces in your musical system.
   d) Suggest a metric for evaluating the AI's performance in composing within your system.

6. Practical Application (150-200 words):
   a) Suggest a real-world application for your musical system (e.g., therapy, education, or entertainment).
   b) Describe how this application could be implemented and its potential benefits.
   c) Address potential criticisms or limitations of using your system in this context.
   d) Propose a method to quantitatively measure the effectiveness of your system in this application.

Ensure your response demonstrates a deep understanding of music theory, cognitive science, and creative composition. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your system design while maintaining scientific plausibility.

Format your response with clear headings for each section and use numbered or bulleted lists where appropriate. Your total response should be between 1350-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response provides a detailed and coherent description of a novel musical system that incorporates the specified cognitive principle and musical element.",
            "The system design includes a clear visual representation and at least one mathematical formula or quantitative rule.",
            "The composition demonstrates a clear application of the musical system, effectively targets the specified emotion, and justifies the chosen tempo.",
            "The cognitive analysis shows a deep understanding of the relationship between music and cognitive processes and includes a well-designed experiment proposal.",
            "The cross-cultural perspective demonstrates an awareness of diverse musical traditions and provides a specific example of cross-cultural interpretation.",
            "The AI application proposal is well-reasoned, addresses relevant challenges, and suggests a meaningful evaluation metric.",
            "The practical application suggestion is creative, well-justified, and includes a quantitative measurement method.",
            "The overall response shows creativity, scientific plausibility, and a deep understanding of music theory and cognitive science.",
            "The response adheres to the specified word count range and uses appropriate formatting."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
