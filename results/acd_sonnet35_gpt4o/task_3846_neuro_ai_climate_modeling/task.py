import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {"neural_mechanism_1": "predictive coding", "neural_mechanism_2": "hebbian learning", "climate_feature": "ocean circulation patterns"},
            "2": {"neural_mechanism_1": "hebbian learning", "neural_mechanism_2": "predictive coding", "climate_feature": "atmospheric carbon cycle"}
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-inspired AI system for climate modeling and ecosystem prediction. Your system should incorporate and compare the neural mechanisms of {t['neural_mechanism_1']} and {t['neural_mechanism_2']}, focusing on modeling {t['climate_feature']}. Consider the following scenario: A coastal city is facing increased flooding risks due to changing ocean currents and rising sea levels. Your task is to design an AI system that can model these changes and predict their impact on the local ecosystem.

Your response should include the following sections:

1. Neuroscientific Basis (250-300 words):
   a) Explain both neural mechanisms and their roles in brain function.
   b) Compare and contrast how these mechanisms could be applied to climate modeling.
   c) Describe analogies between brain processes and climate systems that inform your design.
   d) Propose a quantitative metric to evaluate the effectiveness of each mechanism in climate modeling.

2. AI Architecture Design (300-350 words):
   a) Design an AI system that implements both neural mechanisms for climate modeling.
   b) Describe the key components of your system and how they interact.
   c) Explain how your system models the specified climate feature.
   d) Include a high-level diagram or pseudocode to illustrate your architecture.
   e) Propose an algorithm that combines both neural mechanisms for improved prediction accuracy.

3. Data Integration and Processing (200-250 words):
   a) Describe the types of climate data your system would use, including at least one novel data source.
   b) Explain how your system would integrate and process diverse data sources.
   c) Discuss any novel approaches to data handling inspired by brain function.
   d) Propose a method to handle potential biases or inconsistencies in the data.

4. Prediction and Modeling Capabilities (250-300 words):
   a) Describe the specific predictions or models your system could generate for the coastal city scenario.
   b) Explain how each neural mechanism enhances these capabilities.
   c) Discuss potential advantages over traditional climate modeling approaches.
   d) Propose a quantitative method to evaluate the accuracy of your system's predictions.

5. Ecosystem Impact Assessment (200-250 words):
   a) Explain how your system would assess the impact of climate changes on the coastal ecosystem.
   b) Describe a specific example of how it might model the effect of changing ocean currents on a particular species.
   c) Discuss how the brain-inspired approach might provide unique insights into ecosystem dynamics.
   d) Propose a method to validate your system's ecosystem impact predictions.

6. Ethical Considerations and Future Directions (200-250 words):
   a) Discuss any ethical implications of using brain-inspired AI for climate modeling.
   b) Address potential biases or limitations in your approach.
   c) Suggest one area for future research to enhance the capabilities of your system.
   d) Propose a framework for ensuring transparency and interpretability of your AI system's decisions.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and climate science. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Your response will be evaluated based on:
1. Correct incorporation and comparison of the specified neural mechanisms.
2. Demonstration of interdisciplinary knowledge and creative problem-solving.
3. Scientific plausibility and innovation in system design.
4. Comprehensive coverage of all required sections, including quantitative elements.
5. Thoughtful consideration of ethical implications and future directions.
6. Relevance to the coastal city scenario throughout the response.

Strive for a balance between creativity and scientific accuracy in your response.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response incorporates and compares the neural mechanisms of {t['neural_mechanism_1']} and {t['neural_mechanism_2']} in the AI system design.",
            f"The system focuses on modeling {t['climate_feature']} as specified, with relevance to the coastal city scenario.",
            "The design demonstrates a clear understanding of neuroscience, AI, and climate science principles, including quantitative elements.",
            "The response includes all required sections with appropriate content and word count.",
            "The proposed system is creative yet scientifically plausible, with novel approaches to data handling and prediction.",
            "The response addresses ethical considerations, potential biases, and future research directions comprehensively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
