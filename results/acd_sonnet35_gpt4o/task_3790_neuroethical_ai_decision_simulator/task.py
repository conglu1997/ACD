import random
from typing import List, Optional

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "Autonomous vehicle accident dilemma",
            "AI-assisted medical triage in a pandemic",
            "Predictive policing and racial bias",
            "AI-driven resource allocation in climate disasters"
        ]
        return {
            "1": {"scenario": random.choice(scenarios)},
            "2": {"scenario": random.choice(scenarios)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates human-like ethical decision-making based on neural network models of moral cognition, then apply it to the scenario: {t['scenario']}. Your response should include:\n\n1. Neural Network Architecture (300-350 words):\n   a) Describe the key components of your neural network model for ethical decision-making.\n   b) Explain how your model incorporates different ethical frameworks (e.g., deontological, consequentialist).\n   c) Detail how the model processes moral dilemmas and generates decisions.\n   d) Include a diagram or pseudocode snippet illustrating a key aspect of your neural network.\n\n2. Ethical Framework Integration (250-300 words):\n   a) Explain how your system integrates multiple ethical frameworks.\n   b) Describe the process of encoding ethical principles into the neural network.\n   c) Discuss how your system handles conflicts between different ethical considerations.\n\n3. Decision-Making Process (250-300 words):\n   a) Outline the step-by-step process your AI system uses to make ethical decisions.\n   b) Explain how the system weighs different factors and stakeholder interests.\n   c) Describe how uncertainty and probabilistic outcomes are incorporated into the decision-making process.\n\n4. Application to the Scenario (300-350 words):\n   a) Apply your AI system to the given scenario: {t['scenario']}.\n   b) Describe the ethical considerations involved and how your system processes them.\n   c) Provide the decision or recommendation made by your AI system.\n   d) Analyze the potential consequences of this decision.\n\n5. Comparative Analysis (200-250 words):\n   a) Compare your AI system's decision to potential human decisions in the same scenario.\n   b) Discuss the advantages and limitations of using AI for ethical decision-making in this context.\n\n6. Societal Implications (200-250 words):\n   a) Discuss the broader implications of using AI systems for ethical decision-making in society.\n   b) Address potential concerns about AI bias, accountability, and transparency.\n   c) Propose guidelines for the responsible development and use of ethical AI decision-making systems.\n\nEnsure your response demonstrates a deep understanding of neuroscience, artificial intelligence, ethics, and decision theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing practical and ethical concerns.\n\nFormat your response with clear headings for each section. Your total response should be between 1500-1800 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of neural network architectures and their application to ethical decision-making.",
            "The AI system design effectively integrates multiple ethical frameworks and handles conflicts between different ethical considerations.",
            "The decision-making process is clearly explained and incorporates uncertainty and probabilistic outcomes.",
            "The application to the given scenario is thorough, considering relevant ethical factors and potential consequences.",
            "The comparative analysis between AI and human decision-making is insightful and balanced.",
            "The discussion of societal implications is thoughtful and addresses key concerns about AI ethics.",
            "The response is innovative while maintaining scientific plausibility and addressing practical concerns.",
            "The writing is clear, well-structured, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
