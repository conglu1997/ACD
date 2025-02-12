import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'linguistic_concept': 'Syntactic trees',
                'biological_process': 'Gene expression regulation',
                'information_theory_principle': 'Mutual information',
                'genomic_sequence': 'ATCG GTTA CCTA GGAC TAAT CGGA'
            },
            '2': {
                'linguistic_concept': 'Morphological analysis',
                'biological_process': 'Protein folding',
                'information_theory_principle': 'Kolmogorov complexity',
                'genomic_sequence': 'CGAT TGCA AATC GGTT ACCT GAAC'
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biolinguistic framework for analyzing genomic sequences by integrating the following concepts:

1. Linguistic concept: {t['linguistic_concept']}
2. Biological process: {t['biological_process']}
3. Information theory principle: {t['information_theory_principle']}

Your task is to create a novel approach that applies linguistic and information theory principles to genetic data analysis. Provide your response in the following format:

1. Conceptual Framework (300-350 words):
   a) Explain how you will integrate the given linguistic concept, biological process, and information theory principle.
   b) Describe the key components of your biolinguistic framework and how they interact.
   c) Discuss how your approach differs from traditional methods of genomic analysis.

2. Methodology (250-300 words):
   a) Outline the steps involved in applying your framework to genomic data.
   b) Explain how genetic information is represented and processed in your system.
   c) Describe any novel algorithms or data structures you've developed for this framework.

3. Application Example (250-300 words):
   a) Apply your framework to analyze the following genomic sequence: {t['genomic_sequence']}
   b) Walk through the analysis process, highlighting how each component of your framework contributes.
   c) Explain the insights or results that your approach yields for this specific sequence.
   d) Include a visual representation (using ASCII art) of how your framework interprets this sequence.

4. Comparative Analysis (200-250 words):
   a) Compare your biolinguistic framework to existing methods in genomics and bioinformatics.
   b) Discuss potential advantages and limitations of your approach.
   c) Explain how your framework might complement or challenge current understanding in genetics.

5. Implications and Future Directions (200-250 words):
   a) Discuss the broader implications of your biolinguistic framework for genetics and linguistics.
   b) Propose two potential applications of your framework in genetic research or biotechnology.
   c) Suggest future research directions or extensions of your framework.

Ensure your response demonstrates a deep understanding of linguistics, genetics, and information theory. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology from all relevant fields and provide clear explanations for complex concepts.

Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given linguistic concept, biological process, and information theory principle.",
            "The biolinguistic framework is innovative and integrates concepts from multiple disciplines coherently.",
            "The methodology is clearly explained and scientifically plausible.",
            "The application example effectively analyzes the given genomic sequence using the proposed framework.",
            "The response includes an ASCII art representation of the framework's interpretation of the sequence.",
            "The comparative analysis shows critical thinking and awareness of existing methods.",
            "The implications and future directions are insightful and demonstrate the broader potential of the framework.",
            "The response is well-structured and adheres to the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
