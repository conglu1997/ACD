class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            {"emotion": "joy", "characteristics": "upbeat, major key, fast tempo"},
            {"emotion": "sadness", "characteristics": "slow tempo, minor key, legato articulation"},
            {"emotion": "anger", "characteristics": "loud dynamics, dissonant harmonies, irregular rhythms"},
            {"emotion": "fear", "characteristics": "sudden changes, low register, minor key"},
            {"emotion": "surprise", "characteristics": "unexpected harmonies, sudden dynamic changes, unique timbres"}
        ]
        import random
        selected_emotions = random.sample(emotions, 2)
        return {
            "1": selected_emotions[0],
            "2": selected_emotions[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can compose music to evoke the emotion of {t['emotion']}. Your system should incorporate principles of music theory and emotional psychology to generate compositions with the following characteristics: {t['characteristics']}.

        Provide your response in the following format:

        1. System Architecture (100-150 words):
           Describe the key components of your AI system, including how it processes emotional input, applies music theory principles, and generates compositions.

        2. Emotion-Music Mapping (100-150 words):
           Explain how your system maps the given emotion to specific musical elements (e.g., key, tempo, rhythm, harmony). Provide concrete examples.

        3. Music Generation Process (100-150 words):
           Detail the step-by-step process your AI uses to compose a piece of music, from initial emotion input to final composition.

        4. Evaluation Mechanism (75-100 words):
           Propose a method for evaluating the effectiveness of your AI's compositions in evoking the intended emotion.

        5. Ethical Considerations (75-100 words):
           Discuss potential ethical implications of using AI to manipulate emotions through music, and how your system might address these concerns.

        6. Sample Output (50-75 words):
           Describe a short musical phrase or motif that your AI might generate for the given emotion, explaining how it embodies the emotion's characteristics.

        Ensure your response demonstrates a deep understanding of music theory, emotional psychology, and AI system design. Be creative in your approach while maintaining scientific plausibility.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of music theory, emotional psychology, and AI system design.",
            "The system architecture is well-defined and integrates all necessary components for emotion-driven music composition.",
            "The emotion-music mapping is detailed and provides concrete examples of how musical elements correspond to the given emotion.",
            "The music generation process is clearly explained and logically sound.",
            "The evaluation mechanism is feasible and appropriate for assessing the AI's effectiveness in evoking emotions.",
            "Ethical considerations are thoughtfully addressed.",
            "The sample output description is creative and accurately reflects the given emotion's characteristics.",
            "The overall response is well-structured, coherent, and adheres to the specified word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
