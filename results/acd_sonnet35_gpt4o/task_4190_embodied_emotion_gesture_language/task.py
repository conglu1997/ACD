import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = [
            "contentment",
            "anticipation",
            "nostalgia",
            "awe",
            "melancholy",
            "ambivalence"
        ]
        body_parts = [
            "hands",
            "face",
            "torso",
            "legs",
            "eyes",
            "shoulders"
        ]
        contexts = [
            "professional setting",
            "intimate relationship",
            "public space",
            "nature environment",
            "artistic performance",
            "virtual reality"
        ]
        return {
            "1": {
                "emotion": random.choice(emotions),
                "primary_body_part": random.choice(body_parts),
                "context": random.choice(contexts)
            },
            "2": {
                "emotion": random.choice(emotions),
                "primary_body_part": random.choice(body_parts),
                "context": random.choice(contexts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that creates and interprets a gesture-based language for expressing complex emotions, incorporating principles of embodied cognition and non-verbal communication. Your system should focus on the emotion of {t['emotion']}, primarily using the {t['primary_body_part']} for expression, and be suitable for use in a {t['context']}. Your response should include:

1. Gesture Language Design (300-350 words):
   a) Describe the key components and principles of your gesture-based emotional language.
   b) Explain how your language incorporates embodied cognition principles.
   c) Detail how the {t['primary_body_part']} is used to express {t['emotion']}.
   d) Discuss how context ({t['context']}) influences the gesture language.

2. AI System Architecture (250-300 words):
   a) Outline the main components of your AI system for creating and interpreting the gesture language.
   b) Explain how your system learns and generates new gestures.
   c) Describe the algorithms or models used for gesture recognition and interpretation.
   d) Discuss how your system handles ambiguity and context-dependence in gesture interpretation.

3. Emotional Complexity (200-250 words):
   a) Explain how your system represents and processes the complexity of {t['emotion']}.
   b) Describe how subtle variations in gesture can convey different intensities or nuances of {t['emotion']}.
   c) Discuss how your system handles the potential cultural variations in expressing {t['emotion']}.

4. Gesture Sequence Example (200-250 words):
   a) Provide a detailed example of a gesture sequence that expresses {t['emotion']} in the given context.
   b) Explain how each component of the sequence contributes to the overall emotional expression.
   c) Describe how your AI system would interpret this sequence.
   d) Include at least three distinct gestures in your sequence, explaining their individual and combined significance.

5. Application and Evaluation (200-250 words):
   a) Propose a specific application of your system in the given context ({t['context']}).
   b) Describe how you would evaluate the effectiveness of your gesture language and AI system.
   c) Discuss potential challenges in implementing your system and how you'd address them.
   d) Identify and explain at least two limitations of your proposed system.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss potential ethical implications of an AI system interpreting and generating emotional gestures.
   b) Explore how your system might impact human non-verbal communication.
   c) Suggest two potential extensions or improvements to your system.

Ensure your response demonstrates a deep understanding of embodied cognition, emotional intelligence, and non-verbal communication. Use technical terminology appropriately and provide explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Adhere strictly to the word count for each section. Your total response should be between 1300-1600 words. Include a word count at the end of each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs an AI system for creating and interpreting a gesture-based language for expressing {t['emotion']}, primarily using the {t['primary_body_part']} and suitable for a {t['context']}.",
            "The gesture language design and AI system architecture are well-explained, innovative, and grounded in principles of embodied cognition and non-verbal communication.",
            "The response demonstrates a deep understanding of emotional complexity and cultural variations in expressing emotions through gestures.",
            "The gesture sequence example is detailed, relevant, and clearly explained in terms of both expression and AI interpretation, including at least three distinct gestures.",
            "The proposed application and evaluation methods are practical and well-thought-out, with at least two limitations identified and explained.",
            "The response addresses ethical considerations and future directions thoughtfully.",
            "The response is creative, demonstrates sophisticated understanding of the relevant fields, and maintains scientific plausibility.",
            "The response follows the specified format and adheres to the word limit guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
