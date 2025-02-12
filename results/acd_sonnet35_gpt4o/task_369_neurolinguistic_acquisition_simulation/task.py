import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'language_feature': 'Syntax',
                'age_group': 'Early childhood (2-7 years)'
            },
            {
                'language_feature': 'Phonology',
                'age_group': 'Infancy (0-2 years)'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates the acquisition of {t['language_feature']} in {t['age_group']}, considering the critical period hypothesis. Your task has the following parts:

1. Neuroscientific Foundation (150-200 words):
   Explain the key neural mechanisms involved in language acquisition during {t['age_group']}, focusing on {t['language_feature']}. Discuss how the critical period hypothesis applies to this specific aspect of language learning.

2. Computational Model Design (250-300 words):
   a) Describe the architecture of your computational model, including its main components and how they interact.
   b) Explain how your model incorporates principles of neural plasticity and the critical period hypothesis.
   c) Detail how your model simulates the acquisition of {t['language_feature']}.
   d) Discuss how your model accounts for individual differences in language acquisition rates and outcomes.

3. Learning Algorithm (150-200 words):
   Propose a specific learning algorithm or approach that your model would use to acquire {t['language_feature']}. Explain how this algorithm reflects current understanding of brain function and language acquisition processes.

4. Model Evaluation (150-200 words):
   a) Describe how you would evaluate the performance and accuracy of your model.
   b) Propose specific metrics or benchmarks that could be used to compare your model's 'language acquisition' to that of human children.
   c) Discuss potential limitations of your evaluation method.

5. Predictions and Implications (200-250 words):
   a) Describe two specific, testable predictions that your model makes about language acquisition in children.
   b) Discuss how these predictions might be tested in real-world studies with children.
   c) Explain how your model and its predictions might inform our understanding of language disorders or delays.

6. Ethical Considerations (100-150 words):
   Discuss potential ethical implications of using such a model in research or clinical applications. Consider issues such as privacy, consent, and potential misuse or misinterpretation of results.

7. Future Directions (100-150 words):
   Propose two ways your model could be extended or improved in future research. Consider both technological advancements and new findings in neurolinguistics.

Ensure your response demonstrates a deep understanding of neurolinguistics, developmental psychology, and AI principles. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, exactly as numbered above. Begin each section with the heading (e.g., '1. Neuroscientific Foundation:') on a new line, followed by your response for that section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The neuroscientific foundation is accurate and relevant to the specified language feature and age group.",
            "The computational model design is comprehensive, innovative, and grounded in current neuroscientific understanding.",
            "The proposed learning algorithm reflects current theories of brain function and language acquisition.",
            "The model evaluation approach is well-thought-out and includes appropriate metrics for comparison with human language acquisition.",
            "The predictions are specific, testable, and logically derived from the model.",
            "The discussion of ethical considerations shows awareness of potential issues in applying such models.",
            "The proposed future directions are innovative and build meaningfully on the presented model.",
            "The overall response demonstrates a deep understanding of neurolinguistics, developmental psychology, and AI principles.",
            "The response shows originality and creativity while maintaining scientific plausibility.",
            "The response follows the required format with clear headings for each section as specified in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
