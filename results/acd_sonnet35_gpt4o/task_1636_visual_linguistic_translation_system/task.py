import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        visual_elements = [
            "facial expressions",
            "body language",
            "color patterns",
            "abstract shapes"
        ]
        emotional_concepts = [
            "complex grief",
            "ambivalence",
            "serendipity",
            "nostalgia"
        ]
        return {
            "1": {
                "visual_element": random.choice(visual_elements),
                "emotion": random.choice(emotional_concepts)
            },
            "2": {
                "visual_element": random.choice(visual_elements),
                "emotion": random.choice(emotional_concepts)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can translate between visual perceptions and linguistic structures, focusing on the domain of emotional expressions. Specifically, your system should be able to translate {t['visual_element']} representing {t['emotion']} into linguistic descriptions and vice versa. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for visual-linguistic translation.
   b) Explain how the system processes visual input and generates linguistic output (and vice versa).
   c) Detail how your system incorporates knowledge from cognitive science, neuroscience, and linguistics.
   d) Include a simple diagram or pseudocode snippet illustrating a key aspect of your system.

2. Visual-Linguistic Mapping (200-250 words):
   a) Explain your approach to mapping between {t['visual_element']} and linguistic descriptions of {t['emotion']}.
   b) Discuss how your system handles the subjective and cultural aspects of emotional expression.
   c) Provide an example of how a specific aspect of {t['emotion']} would be translated between visual and linguistic forms.

3. Machine Learning Approach (200-250 words):
   a) Describe the machine learning techniques your system would use for this translation task.
   b) Explain how you would obtain and prepare training data for your system.
   c) Discuss potential challenges in training the system and how you would address them.

4. Cognitive Model Integration (150-200 words):
   a) Explain how your system incorporates current understanding of human cognitive processes in visual perception and language processing.
   b) Discuss how your system might inform or challenge existing cognitive models of emotion processing.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues or misuses of this technology.
   b) Discuss the limitations of your system, particularly in handling complex or culturally-specific emotions.
   c) Propose guidelines for the responsible development and use of visual-linguistic translation systems.

6. Future Research and Applications (100-150 words):
   a) Suggest potential improvements or extensions to your system.
   b) Propose novel applications of this technology in fields such as psychology, art, or human-computer interaction.
   c) Briefly describe an experiment that could further explore the relationship between visual perception, language, and emotion using your system.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system effectively translates between {t['visual_element']} and linguistic descriptions of {t['emotion']}",
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence",
            "The system architecture is well-described and incorporates knowledge from relevant fields",
            "The machine learning approach is appropriate and well-explained",
            "Ethical considerations and limitations are thoughtfully addressed",
            "The proposed system is innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
