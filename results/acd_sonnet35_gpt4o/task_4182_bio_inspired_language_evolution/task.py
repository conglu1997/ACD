import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'biological_principle': 'Genetic drift',
                'linguistic_feature': 'Phonological changes'
            },
            {
                'biological_principle': 'Natural selection',
                'linguistic_feature': 'Syntactic structures'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired computational model that simulates the evolution of language, focusing on the biological principle of {t['biological_principle']} and its impact on {t['linguistic_feature']}. Your response should include:

1. Model Architecture (250-300 words):
   a) Describe the key components of your bio-inspired language evolution model.
   b) Explain how you integrate the principles of {t['biological_principle']} into your model.
   c) Detail how your model represents and evolves {t['linguistic_feature']}.
   d) Discuss any novel algorithms or data structures used in your implementation.

2. Evolutionary Mechanisms (200-250 words):
   a) Explain how your model simulates language change over time.
   b) Describe the specific mechanisms that drive the evolution of {t['linguistic_feature']}.
   c) Discuss how you incorporate randomness and selection pressures in your model.

3. Linguistic Representation (200-250 words):
   a) Detail how you represent language elements, particularly {t['linguistic_feature']}, in your model.
   b) Explain how this representation allows for evolutionary changes.
   c) Discuss any trade-offs or limitations in your chosen representation.

4. Simulation and Analysis (250-300 words):
   a) Describe a hypothetical simulation run using your model.
   b) Explain how you would analyze the results to track changes in {t['linguistic_feature']}.
   c) Propose metrics to quantify the evolutionary changes in your simulation.
   d) Suggest how you might validate your model against real-world language evolution data.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss how your model might inform or challenge current theories in linguistics or evolutionary biology.
   b) Propose a novel hypothesis about language evolution that your model could help investigate.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical implications or misuses of your language evolution model.
   b) Discuss limitations of your approach and areas for future improvement.
   c) Propose guidelines for the responsible development and use of bio-inspired language evolution models.

Ensure your response demonstrates a deep understanding of genetics, evolutionary biology, and computational linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biological_principle']} and its potential impact on {t['linguistic_feature']}.",
            "The model architecture is innovative, plausible, and clearly integrates biological and linguistic principles.",
            "The evolutionary mechanisms and linguistic representations are well-explained and scientifically grounded.",
            "The simulation and analysis section provides a clear and plausible example of the model's application.",
            "The response addresses interdisciplinary implications and ethical considerations thoughtfully.",
            "The response maintains scientific accuracy while showcasing creativity and interdisciplinary knowledge integration.",
            "The response follows the specified format with clear section headings and appropriate word counts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
