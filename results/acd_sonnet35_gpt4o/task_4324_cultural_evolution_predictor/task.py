import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultural_elements = [
            {"element": "cuisine", "factor": "globalization"},
            {"element": "social norms", "factor": "technological advancement"},
            {"element": "artistic expression", "factor": "environmental change"},
            {"element": "religious practices", "factor": "demographic shifts"},
            {"element": "language use", "factor": "economic transformations"}
        ]
        return {str(i+1): random.choice(cultural_elements) for i in range(2)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts cultural evolution, focusing on the cultural element of {t['element']} and considering the impact of {t['factor']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling cultural evolution.
   b) Explain how your system integrates anthropological, linguistic, and complex systems theory principles.
   c) Detail how your system models the evolution of {t['element']} over time.
   d) Discuss how your system incorporates the impact of {t['factor']} on cultural change.

2. Data Integration and Processing (250-300 words):
   a) Specify the types of data your system would use to model cultural evolution.
   b) Explain how your system processes and integrates diverse data sources.
   c) Describe any novel approaches to handling the complexity and uncertainty in cultural data.

3. Predictive Modeling (250-300 words):
   a) Detail the predictive modeling techniques used in your system.
   b) Explain how your system accounts for non-linear dynamics and emergent phenomena in cultural evolution.
   c) Discuss how your system balances short-term and long-term predictions.

4. Case Study: Evolution of {t['element']} (300-350 words):
   a) Present a specific scenario modeling the evolution of {t['element']} under the influence of {t['factor']}.
   b) Provide a step-by-step explanation of how your system would process this scenario.
   c) Include a sample prediction output, detailing potential changes in {t['element']} over a 50-year period.
   d) Analyze the key factors and dynamics identified by your system in this evolution.

5. Evaluation and Validation (200-250 words):
   a) Propose methods for evaluating the accuracy and reliability of your system's predictions.
   b) Discuss how you would validate your model against historical data and expert knowledge.
   c) Address potential biases or limitations in your approach and how you might mitigate them.

6. Ethical Considerations and Societal Impact (200-250 words):
   a) Discuss the ethical implications of using AI to predict cultural evolution.
   b) Consider potential misuses or unintended consequences of such a system.
   c) Propose guidelines for the responsible development and use of cultural evolution prediction systems.

7. Future Directions and Interdisciplinary Applications (150-200 words):
   a) Suggest potential improvements or extensions to your system.
   b) Explore how your system could be applied in fields such as policy-making, education, or business strategy.
   c) Discuss how this approach might contribute to our understanding of human societies and cultural dynamics.

Ensure your response demonstrates a deep understanding of anthropology, linguistics, complex systems theory, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1650-2000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cultural evolution, anthropology, linguistics, and complex systems theory.",
            "The proposed AI system is innovative, well-reasoned, and effectively integrates principles from multiple disciplines.",
            "The system architecture and data processing methods are clearly explained and appropriate for modeling cultural evolution.",
            "The predictive modeling approach is sophisticated and accounts for the complexity of cultural systems.",
            "The case study provides a detailed and plausible scenario for the evolution of the specified cultural element.",
            "The evaluation and validation methods are rigorous and address potential biases and limitations.",
            "Ethical considerations are thoroughly explored, with thoughtful guidelines proposed.",
            "The response is well-structured, follows the specified format, and falls within the given word count range.",
            "The proposed system demonstrates potential for practical applications and advancing our understanding of cultural dynamics."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
