import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        emotions = ['joy', 'sorrow', 'anger', 'fear', 'surprise', 'disgust']
        musical_elements = ['melody', 'harmony', 'rhythm', 'timbre']
        linguistic_elements = ['metaphor', 'syntax', 'phonology', 'semantics']
        
        return {
            "1": {
                "emotion": random.choice(emotions),
                "musical_element": random.choice(musical_elements),
                "linguistic_element": random.choice(linguistic_elements)
            },
            "2": {
                "emotion": random.choice(emotions),
                "musical_element": random.choice(musical_elements),
                "linguistic_element": random.choice(linguistic_elements)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that synthesizes musical compositions, linguistic expressions, and emotional states, then use it to translate a complex emotional narrative across these modalities. Your system should focus on the emotion of {t['emotion']}, the musical element of {t['musical_element']}, and the linguistic element of {t['linguistic_element']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for synthesizing music, language, and emotion.
   b) Explain how your system integrates and processes information across these modalities.
   c) Detail the methods used for representing and manipulating emotional states within the system.
   d) Discuss any novel techniques or algorithms used in your design, particularly for cross-modal translation.

2. Emotional-Musical-Linguistic Mapping (250-300 words):
   a) Explain how your system maps the emotion of {t['emotion']} to musical features, focusing on {t['musical_element']}.
   b) Describe how the system represents {t['emotion']} using the linguistic element of {t['linguistic_element']}.
   c) Discuss how these mappings interact and influence each other in your system.
   d) Provide an example of how a specific emotional state would be represented across all three modalities.

3. Narrative Translation Process (250-300 words):
   a) Detail the step-by-step process your system uses to translate an emotional narrative from one modality to another.
   b) Explain how your system maintains emotional coherence across modalities during translation.
   c) Discuss any challenges in preserving emotional nuances when translating between music and language.
   d) Provide a specific example of translating a short emotional narrative between two modalities.

4. Evaluation and Analysis (200-250 words):
   a) Propose methods for evaluating the effectiveness and accuracy of your system's emotional translations.
   b) Discuss potential biases or limitations in your approach and how they might be addressed.
   c) Analyze how your system's translations might differ from human-generated emotional expressions.

5. Cognitive and Neuroscientific Implications (150-200 words):
   a) Discuss how your system's approach relates to current theories of emotion processing in the brain.
   b) Explore potential insights your system might provide into the relationship between music, language, and emotion in human cognition.
   c) Propose a neuroscientific experiment inspired by your system's design or outputs.

6. Ethical Considerations and Applications (150-200 words):
   a) Identify potential ethical concerns related to AI systems that manipulate and generate emotional content.
   b) Propose guidelines for the responsible development and use of emotion-synthesizing AI systems.
   c) Suggest two novel applications of your system in fields such as therapy, education, or artistic expression.

Ensure your response demonstrates a deep understanding of music theory, linguistics, and affective science. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the integration of music, language, and emotion, particularly focusing on {t['emotion']}, {t['musical_element']}, and {t['linguistic_element']}.",
            "The proposed AI system architecture is well-explained, innovative, and plausible.",
            "The emotional-musical-linguistic mapping is clearly described and grounded in relevant theories.",
            "The narrative translation process is detailed and addresses challenges in cross-modal emotional expression.",
            "The response includes thoughtful evaluation methods, cognitive implications, and ethical considerations.",
            "The response is well-structured, coherent, and demonstrates creativity while maintaining scientific rigor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
