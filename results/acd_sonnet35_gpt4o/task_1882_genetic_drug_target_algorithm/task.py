import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'genetic_focus': 'Protein-coding regions',
                'ml_technique': 'Convolutional Neural Networks',
                'pharmacological_property': 'Binding affinity'
            },
            {
                'genetic_focus': 'Non-coding regulatory elements',
                'ml_technique': 'Recurrent Neural Networks',
                'pharmacological_property': 'Toxicity prediction'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel bioinformatics algorithm to identify potential drug targets in genetic sequences, focusing on {t['genetic_focus']} and incorporating {t['ml_technique']} for {t['pharmacological_property']} analysis. Your task has six parts:

1. Algorithm Overview (200-250 words):
   a) Provide a name for your algorithm and explain its primary purpose.
   b) Describe how it integrates genomics, machine learning, and pharmacology principles.
   c) Outline the key steps of your algorithm, from input to output.

2. Genomic Analysis Component (200-250 words):
   a) Explain how your algorithm analyzes {t['genetic_focus']}.
   b) Describe any novel genomic features or patterns your algorithm identifies.
   c) Discuss how your approach differs from existing methods in the field.

3. Machine Learning Integration (200-250 words):
   a) Detail how you incorporate {t['ml_technique']} into your algorithm.
   b) Explain how this ML technique enhances the identification of potential drug targets.
   c) Describe your proposed training data and how you would validate the ML model.

4. Pharmacological Considerations (150-200 words):
   a) Explain how your algorithm assesses {t['pharmacological_property']}.
   b) Discuss how this assessment contributes to identifying viable drug targets.
   c) Address potential limitations or challenges in predicting this property.

5. Pseudocode Representation (100-150 words):
   Provide a simple pseudocode representation of a key part of your algorithm, focusing on either the genomic analysis or machine learning component.

6. Comparative Analysis and Implications (200-250 words):
   a) Compare your algorithm to two existing methods in the field, highlighting key differences and potential advantages.
   b) Propose a method for validating your algorithm's predictions experimentally.
   c) Discuss potential applications of your algorithm in drug discovery pipelines.
   d) Address ethical considerations and potential misuses of your algorithm.

Ensure your response demonstrates a deep understanding of genomics, machine learning, and pharmacology. Be innovative in your approach while maintaining scientific plausibility and addressing potential limitations. Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The algorithm design is novel and integrates principles from genomics, machine learning, and pharmacology effectively.",
            f"The genomic analysis component demonstrates a clear understanding of {t['genetic_focus']} and proposes innovative methods for their analysis.",
            f"The machine learning integration effectively incorporates {t['ml_technique']} and provides a plausible approach for enhancing drug target identification.",
            f"The pharmacological considerations show a thorough understanding of {t['pharmacological_property']} and its relevance to drug target identification.",
            "The pseudocode representation accurately reflects a key part of the algorithm and is logically consistent.",
            "The comparative analysis demonstrates a good understanding of existing methods and provides insightful discussion on validation, applications, and ethical considerations.",
            "The overall response demonstrates strong interdisciplinary thinking and creative problem-solving in bioinformatics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
