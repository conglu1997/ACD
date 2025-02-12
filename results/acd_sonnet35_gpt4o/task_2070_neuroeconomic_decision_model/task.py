import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'context': 'Electric Vehicle Purchase',
                'uncertainty_factor': 'Future Fuel Prices',
                'behavioral_bias': 'Present Bias'
            },
            {
                'context': 'Sustainable Fashion Choices',
                'uncertainty_factor': 'Product Longevity',
                'behavioral_bias': 'Social Influence'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuroeconomic model of decision-making under uncertainty and apply it to analyze consumer behavior in the context of sustainable product choices. Focus on {t['context']} with {t['uncertainty_factor']} as the primary uncertainty factor and {t['behavioral_bias']} as a key behavioral bias to consider. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Outline the key components of your neuroeconomic model, integrating concepts from neuroscience, economics, and psychology.
   b) Explain how your model accounts for decision-making under uncertainty.
   c) Describe how you incorporate the specified behavioral bias into your model.
   d) Discuss the neurological bases for the decision-making processes in your model.

2. Model Formalization (200-250 words):
   a) Present a mathematical or computational formalization of your model.
   b) Explain the variables, parameters, and relationships in your formalization.
   c) Describe how your model quantifies and integrates the uncertainty factor and behavioral bias.

3. Application to Sustainable Product Choices (250-300 words):
   a) Apply your model to analyze consumer behavior in the given context.
   b) Explain how the uncertainty factor influences decision-making in this scenario.
   c) Discuss the role of the specified behavioral bias in consumer choices.
   d) Provide a hypothetical example of how a consumer might make a decision based on your model.

4. Predictions and Implications (200-250 words):
   a) Generate at least three testable predictions from your model about consumer behavior in sustainable product choices.
   b) Discuss the potential implications of your model for marketing strategies, policy-making, or consumer education in promoting sustainable choices.
   c) Explain how your model might inform the design of choice architectures to promote more sustainable decision-making.

5. Model Evaluation and Limitations (150-200 words):
   a) Propose methods to empirically validate your model, including potential experiments or data collection strategies.
   b) Discuss the limitations of your model and potential areas for future refinement or expansion.
   c) Compare your neuroeconomic approach to traditional economic models of consumer choice.

6. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using neuroeconomic models to influence consumer behavior.
   b) Address potential concerns about privacy, manipulation, or unintended consequences.
   c) Propose guidelines for the responsible use of such models in real-world applications.

Ensure your response demonstrates a deep understanding of neuroeconomics, decision theory, and sustainability issues. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing real-world constraints. Your total response should be between 1200-1500 words.

Format your response with clear headings for each section and number your paragraphs within each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroeconomics, integrating concepts from neuroscience, economics, and psychology.",
            "The model effectively incorporates decision-making under uncertainty and the specified behavioral bias.",
            "The mathematical or computational formalization of the model is clear and well-explained.",
            "The application of the model to the given sustainable product choice scenario is thorough and insightful.",
            "The predictions and implications derived from the model are logical and relevant to real-world scenarios.",
            "The proposed evaluation methods and discussion of limitations show critical thinking and scientific rigor.",
            "The ethical considerations are thoughtfully addressed, demonstrating awareness of potential issues in applying such models."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
