import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        composers = [
            {
                "name": "Johann Sebastian Bach",
                "period": "Baroque",
                "signature_element": "Counterpoint",
                "emotional_theme": "Reverence"
            },
            {
                "name": "Wolfgang Amadeus Mozart",
                "period": "Classical",
                "signature_element": "Clarity and balance",
                "emotional_theme": "Joy"
            },
            {
                "name": "Ludwig van Beethoven",
                "period": "Classical/Romantic",
                "signature_element": "Dramatic contrast",
                "emotional_theme": "Heroism"
            },
            {
                "name": "Claude Debussy",
                "period": "Impressionist",
                "signature_element": "Tonal ambiguity",
                "emotional_theme": "Dreamlike atmosphere"
            }
        ]
        return {
            "1": random.choice(composers),
            "2": random.choice(composers)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of composing music in the style of {t['name']} from the {t['period']} period. Your system should incorporate the composer's signature element of {t['signature_element']} and convey the emotional theme of {t['emotional_theme']}. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI music composition system.
   b) Explain how your system incorporates music theory principles.
   c) Detail how the system captures and replicates the composer's style.
   d) Discuss any novel algorithms or data structures used in your design.

2. Style Replication (200-250 words):
   a) Explain how your system replicates the signature element of {t['signature_element']}.
   b) Describe how the emotional theme of {t['emotional_theme']} is conveyed in the compositions.
   c) Discuss how your system handles the cultural and historical context of the {t['period']} period.

3. Composition Process (200-250 words):
   a) Outline the step-by-step process your AI system follows to compose a piece of music.
   b) Explain how the system generates and develops musical ideas.
   c) Describe how your system ensures coherence and structure in the compositions.

4. Training and Data (150-200 words):
   a) Describe the training data and process for your AI system.
   b) Explain how you address potential issues of copyright and originality.
   c) Discuss any techniques used to prevent direct plagiarism of existing works.

5. Evaluation and Authenticity (200-250 words):
   a) Propose methods to evaluate the quality and authenticity of the AI-generated compositions.
   b) Suggest how music experts could be involved in the evaluation process.
   c) Discuss potential challenges in distinguishing AI-generated music from human-composed pieces.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of AI systems that can replicate human creativity.
   b) Address concerns about the impact on human composers and the music industry.
   c) Propose guidelines for the responsible development and use of AI in music composition.
   d) Suggest potential future enhancements or applications of your system.

Ensure your response demonstrates a deep understanding of music theory, AI technologies, and the specific composer's style. Use appropriate musical and technical terminology, providing explanations where necessary. Be innovative in your approach while maintaining musical authenticity and plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a comprehensive understanding of {t['name']}'s compositional style and the {t['period']} period.",
            f"The AI system effectively incorporates the signature element of {t['signature_element']} and conveys the emotional theme of {t['emotional_theme']}.",
            "The system architecture and composition process are well-explained and plausible.",
            "The response addresses ethical considerations and future directions thoughtfully.",
            "The proposed evaluation methods for AI-generated compositions are reasonable and comprehensive.",
            "The response maintains a balance between technical accuracy and creative innovation in AI music composition."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
