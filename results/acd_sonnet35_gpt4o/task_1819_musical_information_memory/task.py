import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_elements = [
            "melody",
            "harmony",
            "rhythm",
            "timbre",
            "dynamics"
        ]
        information_types = [
            "historical dates",
            "scientific formulas",
            "language vocabulary",
            "geographical locations",
            "mathematical sequences"
        ]
        cognitive_principles = [
            "chunking",
            "elaborative rehearsal",
            "mnemonic devices",
            "spaced repetition",
            "dual coding theory"
        ]
        return {
            "1": {
                "musical_element": random.choice(musical_elements),
                "information_type": random.choice(information_types),
                "cognitive_principle": random.choice(cognitive_principles)
            },
            "2": {
                "musical_element": random.choice(musical_elements),
                "information_type": random.choice(information_types),
                "cognitive_principle": random.choice(cognitive_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that encodes {t['information_type']} using {t['musical_element']} as the primary musical structure, and analyze its effectiveness as a memory aid based on the cognitive psychology principle of {t['cognitive_principle']}. Your response should include:

1. System Design (250-300 words):
   a) Explain how you will use {t['musical_element']} to encode {t['information_type']}.
   b) Provide a detailed example of how a specific piece of information would be encoded.
   c) Describe how the encoded information would be presented or performed.
   d) Explain how your system incorporates the principle of {t['cognitive_principle']}.

2. Information Theory Analysis (200-250 words):
   a) Discuss the information capacity of your musical encoding system.
   b) Analyze potential sources of noise or error in the encoding and decoding process.
   c) Compare the efficiency of your system to a traditional method of encoding the same information.

3. Cognitive Psychology Evaluation (200-250 words):
   a) Explain how the principle of {t['cognitive_principle']} enhances memory in your system.
   b) Discuss potential limitations or challenges of using this system for memory enhancement.
   c) Propose a method to empirically test the effectiveness of your system compared to traditional memorization techniques.

4. Musical Analysis (150-200 words):
   a) Discuss how your encoding system relates to existing musical structures or compositions.
   b) Analyze potential aesthetic qualities or challenges of the resulting musical pieces.
   c) Explain how a musician might interpret or perform these information-encoded compositions.

5. Practical Applications and Ethical Considerations (200-250 words):
   a) Propose at least two practical applications for your musical information encoding system.
   b) Discuss any potential benefits or risks of using music as a memory aid in these contexts.
   c) Address any ethical considerations related to encoding information in music, such as privacy concerns or potential for subliminal messaging.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your system might contribute to our understanding of the relationship between music, memory, and information processing.
   b) Propose a research question that could be explored using your system, bridging music theory, information theory, and cognitive psychology.
   c) Speculate on how this approach might influence future developments in fields such as education, AI, or neuroscience.

Ensure your response demonstrates a deep understanding of music theory, information theory, and cognitive psychology. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology from each field and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of how {t['musical_element']} can be used to encode {t['information_type']}.",
            f"The system design should effectively incorporate the cognitive psychology principle of {t['cognitive_principle']}.",
            "The information theory analysis should be sound and demonstrate an understanding of key concepts.",
            "The cognitive psychology evaluation should be well-reasoned and scientifically plausible.",
            "The musical analysis should show an understanding of musical structures and composition.",
            "The practical applications and ethical considerations should be thoughtful and relevant.",
            "The interdisciplinary implications should demonstrate an ability to synthesize concepts from multiple fields."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
