import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "protein_type": "membrane protein",
                "medical_application": "drug delivery"
            },
            {
                "protein_type": "enzyme",
                "medical_application": "gene therapy"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an evolutionary algorithm to optimize protein folding predictions for {t['protein_type']}s, then analyze its potential applications in {t['medical_application']} and the associated ethical implications. Your response should include:

1. Evolutionary Algorithm Design (300-350 words):
   a) Describe the key components of your evolutionary algorithm for protein folding prediction.
   b) Explain how your algorithm incorporates specific features of {t['protein_type']}s.
   c) Discuss any novel elements in your design that differ from traditional evolutionary algorithms.
   d) Provide a high-level pseudocode (10-15 lines) illustrating the main steps of your algorithm.

2. Bioinformatics Integration (250-300 words):
   a) Explain how your algorithm integrates existing bioinformatics data and tools.
   b) Describe the data structures you would use to represent protein structures and folding states.
   c) Discuss how your algorithm handles the complexities and uncertainties in protein folding prediction.

3. Performance Evaluation (200-250 words):
   a) Propose metrics to evaluate the performance of your algorithm.
   b) Describe how you would validate your algorithm's predictions experimentally.
   c) Discuss potential limitations of your approach and how they might be addressed.

4. Application in {t['medical_application']} (250-300 words):
   a) Explain how your optimized protein folding predictions could be applied to {t['medical_application']}.
   b) Describe potential benefits and challenges of using this approach in personalized medicine.
   c) Discuss how this application might impact current medical practices and patient outcomes.

5. Ethical Implications (250-300 words):
   a) Identify potential ethical issues related to using AI-optimized protein folding predictions in {t['medical_application']}.
   b) Discuss privacy concerns and potential for misuse of genetic information.
   c) Propose guidelines for responsible development and use of this technology in medicine.
   d) Analyze how this technology might exacerbate or alleviate existing healthcare inequalities.

6. Future Directions (150-200 words):
   a) Propose two potential research projects that could extend or improve your approach.
   b) Speculate on how widespread adoption of AI-driven protein folding prediction might influence drug discovery and personalized medicine in the long term.

Ensure your response demonstrates a deep understanding of evolutionary algorithms, protein biology, and bioethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The evolutionary algorithm design is well-explained and scientifically grounded.",
            "The bioinformatics integration is thorough and appropriate.",
            "The performance evaluation approach is well-thought-out and comprehensive.",
            f"The application in {t['medical_application']} is clearly explained and plausible.",
            "Ethical implications are thoughtfully addressed and analyzed.",
            "The response demonstrates strong interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
