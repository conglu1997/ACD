import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        signaling_pathways = [
            'MAPK/ERK pathway',
            'JAK-STAT pathway',
            'NF-κB pathway',
            'PI3K-Akt pathway',
            'Wnt signaling pathway'
        ]
        bioinformatics_problems = [
            'protein folding prediction',
            'gene regulatory network inference',
            'metagenomics analysis',
            'drug-target interaction prediction',
            'phylogenetic tree construction'
        ]
        return {
            '1': {
                'pathway': random.choice(signaling_pathways),
                'problem': random.choice(bioinformatics_problems)
            },
            '2': {
                'pathway': random.choice(signaling_pathways),
                'problem': random.choice(bioinformatics_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical biocomputing system that uses the {t['pathway']} to perform complex computations, then apply it to solve the bioinformatics problem of {t['problem']}. Your response should include:

1. Biocomputer Architecture (300-350 words):
   a) Describe the key components of your biocomputing system based on the {t['pathway']}.
   b) Explain how you map computational processes to biological mechanisms in this pathway.
   c) Discuss how your system handles input, processing, and output of information.
   d) Include a diagram or flowchart of your system architecture (describe it in words).

2. Information Encoding and Processing (250-300 words):
   a) Explain how information is encoded in your biocomputing system.
   b) Describe the basic computational operations your system can perform.
   c) Discuss how your system achieves parallelism or other advantages over traditional computing.

3. Application to {t['problem']} (250-300 words):
   a) Describe how you would apply your biocomputing system to address the problem of {t['problem']}.
   b) Explain the specific algorithms or processes your system would use.
   c) Discuss any advantages your approach might have over traditional computational methods for this problem.

4. Challenges and Limitations (150-200 words):
   a) Identify at least three major challenges in implementing your biocomputing system.
   b) Discuss any limitations of your approach compared to traditional computing methods.
   c) Propose potential solutions or future research directions to address these challenges.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to using biological systems for computation.
   b) Explore the broader societal implications of biocomputing technology.
   c) Propose guidelines for the responsible development and use of such systems.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how your biocomputing system integrates principles from biology, information theory, and AI.
   b) Discuss potential applications of your system in fields other than bioinformatics.
   c) Propose a future research direction that combines insights from your system with another scientific discipline.

Ensure your response demonstrates a deep understanding of cellular biology, information theory, and computational systems. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified cellular signaling pathway and its potential for computation.",
            "The biocomputing system design is innovative, scientifically plausible, and well-explained.",
            "The application to the given bioinformatics problem is clearly described and demonstrates potential advantages over traditional methods.",
            "The response addresses challenges, limitations, and ethical implications thoughtfully.",
            "The interdisciplinary connections are well-explored and demonstrate a broad understanding of multiple scientific fields.",
            "The response is well-structured and adheres to the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
