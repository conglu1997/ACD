import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "emotion_pair": ("joy", "sorrow"),
                "context": "A bittersweet reunion",
                "target_emotion": "Nostalgic happiness with underlying sadness"
            },
            {
                "emotion_pair": ("anger", "fear"),
                "context": "A confrontation with a powerful adversary",
                "target_emotion": "Defiant courage masking deep-seated fear"
            },
            {
                "emotion_pair": ("disgust", "surprise"),
                "context": "An unexpected plot twist in a story",
                "target_emotion": "Shocked revulsion turning into fascination"
            },
            {
                "emotion_pair": ("trust", "anticipation"),
                "context": "Preparing for a life-changing event",
                "target_emotion": "Excited confidence tinged with nervous energy"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a language system based on an emotional spectrum between {t['emotion_pair'][0]} and {t['emotion_pair'][1]}. Then use this system to generate a short text (50-75 words) that conveys the following emotional state in the given context:\n\n" \
               f"Context: {t['context']}\n" \
               f"Target Emotion: {t['target_emotion']}\n\n" \
               f"Your response should include:\n\n" \
               f"1. Emotion Spectrum Design (100-150 words):\n" \
               f"   Describe your language system, explaining how it represents the spectrum between {t['emotion_pair'][0]} and {t['emotion_pair'][1]}. Include at least three linguistic features (e.g., syntax, phonology, morphology) that vary along this spectrum.\n\n" \
               f"2. Language Sample (50-75 words):\n" \
               f"   Generate a short text using your designed language system that conveys the target emotion in the given context. Ensure that your text demonstrates the linguistic features you described.\n\n" \
               f"3. Analysis (100-150 words):\n" \
               f"   Explain how your generated text conveys the target emotion using your language system. Discuss specific linguistic choices and their emotional implications.\n\n" \
               f"4. Potential Applications (50-75 words):\n" \
               f"   Briefly describe a potential real-world application of your emotion-based language system in fields such as AI, psychology, or communication."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language system design clearly explains how it represents the spectrum between {t['emotion_pair'][0]} and {t['emotion_pair'][1]}.",
            "The design includes at least three distinct linguistic features that vary along the emotional spectrum.",
            f"The generated text effectively conveys the target emotion: {t['target_emotion']}.",
            "The analysis provides a clear explanation of how the linguistic choices in the generated text convey the target emotion.",
            "The proposed real-world application is innovative and relevant to the emotion-based language system.",
            "The overall response demonstrates creativity, coherence, and a deep understanding of the relationship between language and emotions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
