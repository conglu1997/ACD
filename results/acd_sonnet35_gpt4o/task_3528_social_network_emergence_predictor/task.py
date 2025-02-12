import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        network_types = [
            "Online social media platform",
            "Professional networking site",
            "Decentralized social network",
            "Multiplayer online game community"
        ]
        emergent_phenomena = [
            "Information cascades",
            "Opinion polarization",
            "Community formation",
            "Viral content spread"
        ]
        return {
            "1": {"network": random.choice(network_types), "phenomenon": random.choice(emergent_phenomena)},
            "2": {"network": random.choice(network_types), "phenomenon": random.choice(emergent_phenomena)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts emergent behaviors in large-scale social networks, focusing on {t['phenomenon']} within a {t['network']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for modeling and predicting emergent social behaviors.
   b) Explain how your system incorporates principles from complex systems theory, network science, and sociology.
   c) Detail how the system processes and analyzes social network data.
   d) Discuss any novel algorithms or techniques used in your system.

2. Network Modeling (200-250 words):
   a) Explain how your system models the structure and dynamics of the {t['network']}.
   b) Describe the key variables and parameters considered in your model.
   c) Discuss how your system handles the scale and complexity of large social networks.

3. Emergent Behavior Prediction (250-300 words):
   a) Detail the specific methods your system uses to predict {t['phenomenon']}.
   b) Explain how your system identifies early signs or precursors of this emergent behavior.
   c) Describe any machine learning or statistical techniques employed for prediction.
   d) Discuss how your system accounts for the non-linear and often unpredictable nature of social dynamics.

4. Data Requirements and Ethics (150-200 words):
   a) Specify the types and sources of data your system would require.
   b) Address potential privacy concerns and ethical considerations in data collection and analysis.
   c) Propose guidelines for responsible use of your system.

5. Validation and Performance Metrics (200-250 words):
   a) Describe how you would validate your system's predictions.
   b) Propose specific metrics to evaluate the accuracy and reliability of your system.
   c) Discuss the challenges in measuring performance for complex social phenomena prediction.

6. Potential Applications and Implications (150-200 words):
   a) Suggest potential applications of your system in research, policy-making, or business.
   b) Discuss the broader implications of being able to predict {t['phenomenon']} in {t['network']}.
   c) Address any potential risks or negative consequences of such predictive capabilities.

7. Future Directions (100-150 words):
   a) Propose one way to extend or improve your system.
   b) Suggest a related research question that could be explored using your system.

Ensure your response demonstrates a deep understanding of complex systems theory, network science, and sociology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specific network type ({t['network']}) and emergent phenomenon ({t['phenomenon']}) given in the task.",
            "The system design must incorporate principles from complex systems theory, network science, and sociology.",
            "The response must include all seven required sections with appropriate content and depth.",
            "The proposed system must be innovative yet scientifically plausible.",
            "The response must demonstrate a deep understanding of modeling and predicting emergent behaviors in social networks.",
            "The ethical considerations and potential implications of the system must be thoroughly addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
