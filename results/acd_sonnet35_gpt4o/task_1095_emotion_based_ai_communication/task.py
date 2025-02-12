import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotion_theories = [
            "Plutchik's Wheel of Emotions",
            "Ekman's Basic Emotions",
            "Dimensional Theory of Emotion",
            "Constructionist Theory of Emotion"
        ]
        communication_contexts = [
            "AI-to-AI communication in a multi-agent system",
            "AI-human interaction in a customer service scenario"
        ]
        
        tasks = {
            "1": {
                "emotion_theory": random.choice(emotion_theories),
                "context": random.choice(communication_contexts)
            },
            "2": {
                "emotion_theory": random.choice(emotion_theories),
                "context": random.choice(communication_contexts)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI communication system based on {t['emotion_theory']} and analyze its potential impact on {t['context']}. Your response should include:

1. Emotion Theory Overview (100-200 words):
   Explain the key concepts of {t['emotion_theory']} and its relevance to AI communication. Include at least two core principles of the theory.

2. Communication System Design (250-350 words):
   a) Describe the components and functioning of your emotion-based AI communication system.
   b) Explain how it incorporates at least three principles from {t['emotion_theory']}.
   c) Provide a specific example of how an emotional state would be encoded and transmitted in your system.

3. Implementation in Context (200-300 words):
   Explain how your system would be implemented in the context of {t['context']}. Provide at least two specific examples of how it would function in this scenario.

4. Comparative Analysis (150-250 words):
   Compare your emotion-based system to traditional language-based AI communication. Discuss at least two potential advantages and two limitations.

5. Ethical Implications (150-250 words):
   Discuss at least three ethical considerations and potential societal impacts of implementing such an emotion-based AI communication system.

6. Future Developments (100-200 words):
   Propose at least two potential future enhancements or research directions for your emotion-based AI communication system.

7. Novel Insight (100-200 words):
   Provide a novel insight or application of {t['emotion_theory']} in AI communication that isn't commonly discussed in existing literature. This could be a new way of applying the theory, an unexpected benefit or challenge, or a unique integration with another field.

Ensure your response demonstrates a deep understanding of both emotion theory and AI systems. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, and number your paragraphs within each section for easy reference. Your total response should be between 1050-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        
        # Check word count with more flexibility
        word_count = len(submission.split())
        if word_count < 1000 or word_count > 1800:
            return 0.0
        
        criteria = [
            f"The response accurately explains at least two core principles of {t['emotion_theory']} and its relevance to AI communication.",
            f"The AI communication system design incorporates at least three principles from {t['emotion_theory']} and provides a specific example of emotional state encoding and transmission.",
            f"The implementation includes at least two specific examples relevant to the context of {t['context']}.",
            "The comparative analysis provides at least two potential advantages and two limitations of the emotion-based system compared to traditional language-based AI communication.",
            "At least three ethical considerations and potential societal impacts are thoroughly discussed.",
            "At least two potential future enhancements or research directions are proposed.",
            "The novel insight presents an original idea or application not commonly discussed in existing literature.",
            "The response demonstrates creativity and scientific plausibility throughout.",
            "The response is well-structured with clear headings and numbered paragraphs."
        ]
        
        # Evaluate each criterion separately
        score = 0.0
        for criterion in criteria:
            if eval_with_llm_judge(instructions, submission, [criterion]):
                score += 1.0 / len(criteria)
        
        return score
