import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "joy", "sadness", "anger", "fear", "disgust",
            "surprise", "trust", "anticipation"
        ]
        cultures = [
            "Japanese", "Brazilian", "Nigerian", "Indian", "Russian",
            "Egyptian", "French", "Chinese", "Mexican", "Australian"
        ]
        challenges = [
            "diplomatic negotiation",
            "marketing campaign",
            "conflict resolution",
            "mental health support",
            "educational material design"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "emotion": random.choice(emotions),
                "culture1": random.choice(cultures),
                "culture2": random.choice([c for c in cultures if c != tasks.get(str(i-1), {}).get("culture1")]),
                "challenge": random.choice(challenges)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing and generating emotionally nuanced language across multiple cultures, focusing on the emotion of {t['emotion']}. Then, use this system to address a {t['challenge']} scenario between {t['culture1']} and {t['culture2']} cultures. Your response should include:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system.
   b) Explain how it processes and generates emotionally nuanced language.
   c) Detail how it accounts for cultural differences in emotional expression.
   d) Include a high-level diagram or pseudocode representing the system's workflow.

2. Emotion Analysis Module (150-200 words):
   a) Explain how your system detects and quantifies the emotion of {t['emotion']}.
   b) Describe any specific algorithms or models used for emotion recognition.
   c) Discuss how the system handles cultural variations in expressing {t['emotion']}.

3. Cross-Cultural Emotion Generation (150-200 words):
   a) Describe how your system generates emotionally appropriate content for different cultures.
   b) Explain any techniques used to ensure cultural sensitivity and accuracy.
   c) Provide a brief example of how the system might express {t['emotion']} differently in {t['culture1']} and {t['culture2']} cultures.

4. Application to {t['challenge']} (200-250 words):
   a) Outline a specific {t['challenge']} scenario between {t['culture1']} and {t['culture2']} cultures.
   b) Explain how your AI system would analyze the emotional context of the situation.
   c) Describe how it would generate appropriate responses or content to address the challenge.
   d) Discuss potential outcomes and benefits of using your system in this scenario.

5. Ethical Considerations (100-150 words):
   a) Discuss potential ethical implications of using AI for cross-cultural emotional analysis and communication.
   b) Address concerns related to privacy, cultural appropriation, or potential misuse.
   c) Propose guidelines for responsible development and use of such systems.

6. Evaluation and Future Improvements (100-150 words):
   a) Suggest methods to evaluate the effectiveness and accuracy of your system.
   b) Propose two potential improvements or expansions to enhance its capabilities.
   c) Discuss any limitations of your current design and how they might be addressed in future iterations.

Ensure your response demonstrates a deep understanding of emotions, cultural differences, linguistics, and AI technologies. Be creative in your approach while maintaining scientific and ethical plausibility. Format your response using clear headings for each section. Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the emotion {t['emotion']} and its cultural variations.",
            f"The AI system design effectively addresses the {t['challenge']} scenario between {t['culture1']} and {t['culture2']} cultures.",
            "The proposed system shows innovation in combining emotion analysis, cultural understanding, and AI technologies.",
            "The response adequately addresses ethical considerations and potential improvements.",
            "The overall solution is creative, scientifically plausible, and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
