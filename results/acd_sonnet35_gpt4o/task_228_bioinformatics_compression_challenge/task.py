import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'compression_goal': 'Maximize compression ratio',
                'biological_constraint': 'Preserve GC content',
                'application': 'Design of minimal synthetic genomes'
            },
            {
                'compression_goal': 'Optimize decompression speed',
                'biological_constraint': 'Maintain codon usage bias',
                'application': 'Rapid DNA sequencing and analysis'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a DNA compression algorithm inspired by information theory and propose its application in synthetic biology. Your task has four parts:

1. Algorithm Design (300-350 words):
Create a DNA compression algorithm that aims to {t['compression_goal']}. Your algorithm should:
a) Explain the core principle of your compression technique.
b) Describe how it leverages concepts from information theory.
c) Outline how the algorithm ensures {t['biological_constraint']}.
d) Provide a high-level pseudocode or flowchart of your algorithm.

2. Compression Analysis (200-250 words):
Analyze the performance of your algorithm, addressing:
a) Expected compression ratio and how it compares to existing methods.
b) Time and space complexity of compression and decompression.
c) How the algorithm handles different types of genomic sequences (e.g., coding vs. non-coding regions).

3. Biological Implications (200-250 words):
Discuss the biological implications of your compression algorithm, including:
a) How preserving {t['biological_constraint']} affects the biological functionality of the compressed DNA.
b) Potential effects on DNA replication, transcription, or translation processes.
c) Any limitations or constraints on the types of organisms or genomic regions where your algorithm could be applied.

4. Synthetic Biology Application (250-300 words):
Propose an application of your compression algorithm in {t['application']}. Include:
a) A specific scenario or use case for your compressed DNA in synthetic biology.
b) How your algorithm's properties (compression ratio, speed, biological constraints) benefit this application.
c) Potential challenges in implementing this application and proposed solutions.
d) One ethical consideration related to this application and a suggested guideline to address it.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and synthetic biology. Be creative in your approach while maintaining scientific plausibility.

Format your response using the following structure:

1. Algorithm Design:
   [Your explanation here]

2. Compression Analysis:
   [Your analysis here]

3. Biological Implications:
   [Your discussion here]

4. Synthetic Biology Application:
   [Your proposal here]

Your total response should be between 950-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The algorithm design clearly explains how it achieves {t['compression_goal']} while ensuring {t['biological_constraint']}.",
            "The compression analysis provides a thorough evaluation of the algorithm's performance and compares it to existing methods.",
            f"The biological implications section adequately discusses how preserving {t['biological_constraint']} affects DNA functionality.",
            f"The synthetic biology application proposes a plausible use case for {t['application']} and addresses potential challenges and ethical considerations.",
            "The response demonstrates a strong understanding of molecular biology, information theory, and synthetic biology concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
