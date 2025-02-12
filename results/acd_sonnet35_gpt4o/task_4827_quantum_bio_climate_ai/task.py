import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "ecosystem": "Coral reefs",
                "biological_process": "Coral bleaching resistance",
                "climate_challenge": "Ocean acidification and warming"
            },
            {
                "ecosystem": "Boreal forests",
                "biological_process": "Tree species migration",
                "climate_challenge": "Shifting temperature zones"
            }
        ]
        return {
            "1": random.choice(ecosystems),
            "2": random.choice(ecosystems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system that models and predicts complex biological processes to enhance climate change adaptation strategies for ecosystems. Focus on the {t['ecosystem']} ecosystem, specifically modeling the process of {t['biological_process']} in response to the climate challenge of {t['climate_challenge']}. Your response should include the following sections:

1. Quantum Biology Foundation (250-300 words):
   a) Explain the relevance of quantum effects in the chosen biological process.
   b) Describe how these quantum effects might influence the ecosystem's response to climate change.
   c) Discuss current limitations in modeling these quantum biological phenomena.
   d) Provide a specific example of a quantum effect observed in {t['ecosystem']}.

2. Quantum-Inspired AI Architecture (300-350 words):
   a) Outline the key components of your quantum-inspired AI system.
   b) Explain how your system incorporates quantum principles into its architecture.
   c) Describe the data inputs and outputs of your system.
   d) Discuss any novel algorithms or approaches used in your design.
   e) Include a text-based diagram or flowchart illustrating your system's architecture.

3. Biological Process Modeling (250-300 words):
   a) Detail how your AI system models the specified biological process.
   b) Explain how quantum-inspired computations enhance the accuracy of your model.
   c) Describe how your system accounts for environmental variables and climate change factors.
   d) Discuss the temporal and spatial scales considered in your model.
   e) Provide a hypothetical scenario demonstrating your model's application.

4. Climate Adaptation Predictions (200-250 words):
   a) Explain how your system generates predictions for ecosystem adaptation.
   b) Describe the types of adaptation strategies your system might propose.
   c) Discuss how these predictions could inform conservation efforts and policy-making.
   d) Provide an example scenario of how your system's predictions could be applied.

5. Comparison with Classical Approaches (200-250 words):
   a) Compare your quantum-inspired system to classical AI approaches for ecosystem modeling.
   b) Discuss potential advantages and limitations of your approach.
   c) Describe a specific scenario where your system might outperform classical methods.

6. Validation and Uncertainty (200-250 words):
   a) Propose methods for validating your system's predictions.
   b) Discuss how your system quantifies and communicates uncertainty in its models and predictions.
   c) Explain how your system could be updated with new data and findings in quantum biology and climate science.

7. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns related to using AI for ecosystem management decisions.
   b) Discuss limitations of your approach and potential unintended consequences.
   c) Propose guidelines for the responsible use of your system in conservation efforts.

Ensure your response demonstrates a deep understanding of quantum biology, artificial intelligence, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Include the word count for each section in parentheses at the end of the section. Your total response should be between 1550-1900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of quantum biology, artificial intelligence, and climate science.",
            "The quantum-inspired AI system design is innovative, scientifically plausible, and clearly explained.",
            f"The biological process of {t['biological_process']} is accurately modeled and connected to specific quantum effects in {t['ecosystem']}.",
            f"The system effectively addresses the climate challenge of {t['climate_challenge']} for {t['ecosystem']} with concrete examples and scenarios.",
            "The response includes a thorough comparison between the quantum-inspired approach and classical methods, with a clear example of potential advantages.",
            "The proposed system's limitations, ethical considerations, and validation methods are thoughtfully discussed with specific examples.",
            "The response adheres to the specified format, including word counts for each section, and falls within the overall word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
