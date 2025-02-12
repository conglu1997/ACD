import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'linguistic_feature': 'Syntax',
                'cognitive_bias': 'Mutual exclusivity bias',
                'learning_paradigm': 'Reinforcement learning'
            },
            {
                'linguistic_feature': 'Phonology',
                'cognitive_bias': 'Shape bias',
                'learning_paradigm': 'Unsupervised learning'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a computational model that simulates language acquisition in children and language evolution over generations, focusing on the following parameters:

Linguistic Feature: {t['linguistic_feature']}
Cognitive Bias: {t['cognitive_bias']}
Learning Paradigm: {t['learning_paradigm']}

Your task has the following components:

1. Model Architecture (250-300 words):
   a) Describe the overall architecture of your computational model.
   b) Explain how it incorporates the given linguistic feature, cognitive bias, and learning paradigm.
   c) Discuss how your model simulates both individual language acquisition and generational language evolution.
   d) Include a diagram or pseudo-code snippet illustrating a key component of your model.
   e) Provide a concrete example of how your model would process a specific linguistic input.

2. Acquisition Simulation (200-250 words):
   a) Explain how your model simulates the process of language acquisition in children.
   b) Describe the input data and learning mechanisms used in your model.
   c) Discuss how the specified cognitive bias influences the acquisition process in your model.
   d) Provide an example scenario demonstrating the acquisition process in your model.

3. Evolution Simulation (200-250 words):
   a) Describe how your model simulates language evolution over multiple generations.
   b) Explain how individual acquisition in your model contributes to language change over time.
   c) Discuss any emergent properties or unexpected outcomes in the evolutionary process.
   d) Illustrate with a specific example of how a linguistic feature might evolve in your model.

4. Model Evaluation (150-200 words):
   a) Propose methods to evaluate the accuracy and realism of your model's simulations.
   b) Describe potential experiments or tests to validate your model against real-world data.
   c) Discuss the limitations of your model and how they might be addressed.
   d) Suggest potential improvements or extensions to overcome these limitations.

5. Interdisciplinary Implications (200-250 words):
   a) Analyze how your model contributes to our understanding of language acquisition and evolution.
   b) Discuss potential applications of your model in fields such as linguistics, cognitive science, and artificial intelligence.
   c) Propose a novel research question that could be explored using your model.
   d) Describe a hypothetical experiment using your model to address this research question.

6. Ethical Considerations (100-150 words):
   a) Discuss any ethical implications of using computational models to study language acquisition and evolution.
   b) Address potential concerns about applying insights from your model to real-world language policies or educational practices.
   c) Propose guidelines for the responsible use and interpretation of results from your model.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and machine learning principles. Be creative in your model design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts. Include concrete examples and illustrations where appropriate to demonstrate your understanding.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The model architecture is well-designed and clearly incorporates the given linguistic feature, cognitive bias, and learning paradigm.",
            "The acquisition simulation demonstrates a deep understanding of language acquisition processes and cognitive biases.",
            "The evolution simulation effectively models language change over generations and identifies emergent properties.",
            "The proposed evaluation methods are rigorous and appropriate for validating the model.",
            "The interdisciplinary implications are insightful and demonstrate the model's potential impact on multiple fields.",
            "The ethical considerations show a nuanced understanding of the potential real-world impacts of the model.",
            "The response includes concrete examples and illustrations that effectively demonstrate understanding of the concepts.",
            "The limitations and potential improvements of the model are thoroughly discussed and addressed.",
            "The overall response demonstrates creativity, interdisciplinary knowledge integration, and clear articulation of complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
