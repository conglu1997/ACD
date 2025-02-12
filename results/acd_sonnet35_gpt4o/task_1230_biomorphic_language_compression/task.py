import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "bio_mechanism": "Codon optimization",
                "text_type": "Scientific abstract",
                "compression_goal": "Maximize information density"
            },
            {
                "bio_mechanism": "Intron splicing",
                "text_type": "Legal document",
                "compression_goal": "Preserve key semantic content"
            },
            {
                "bio_mechanism": "Repetitive element condensation",
                "text_type": "Poetry",
                "compression_goal": "Maintain rhythmic structure"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a language compression algorithm inspired by the biological DNA compression mechanism of {t['bio_mechanism']} and apply it to compress a {t['text_type']}. Your algorithm should {t['compression_goal']}.

Your task consists of the following parts:

1. Biological Mechanism Explanation (100-150 words):
   Explain the {t['bio_mechanism']} mechanism in DNA and how it contributes to genetic information compression.

2. Algorithm Design (250-300 words):
   a) Describe your language compression algorithm inspired by {t['bio_mechanism']}.
   b) Explain how it mimics or adapts the biological process for text compression.
   c) Discuss how your algorithm addresses the goal to {t['compression_goal']}.
   d) Provide a step-by-step breakdown of how your algorithm would process and compress text.

3. Application to {t['text_type']} (200-250 words):
   a) Provide a short sample {t['text_type']} (50-75 words).
   b) Apply your algorithm to this sample, showing the compression process and result.
   c) Explain how the compressed version maintains the key characteristics of a {t['text_type']}.

4. Efficiency Analysis (150-200 words):
   a) Discuss the potential compression ratio achieved by your algorithm.
   b) Compare its efficiency to standard text compression methods.
   c) Analyze any trade-offs between compression efficiency and maintaining text integrity.

5. Linguistic Implications (150-200 words):
   a) Discuss how your algorithm might reveal patterns or structures in language similar to those in genetic sequences.
   b) Explore potential applications of your approach in linguistic analysis or natural language processing.

Ensure your response demonstrates a deep understanding of both the biological mechanism and linguistic principles. Use appropriate terminology from biology, linguistics, and information theory. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 850-1100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should accurately explain the {t['bio_mechanism']} mechanism in DNA",
            f"The algorithm design should clearly mimic or adapt {t['bio_mechanism']} for text compression",
            f"The algorithm should address the goal to {t['compression_goal']}",
            f"The application should demonstrate the algorithm's use on a {t['text_type']} of 50-75 words",
            "The efficiency analysis should compare the algorithm to standard text compression methods",
            "The response should explore linguistic implications and potential applications",
            "The answer should demonstrate interdisciplinary knowledge of biology, linguistics, and information theory",
            "The proposed algorithm should be creative yet scientifically plausible"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
