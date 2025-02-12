import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_features = [
            "grammatical gender",
            "evidentiality markers",
            "color terminology",
            "spatial reference frames",
            "counterfactual expressions"
        ]
        cognitive_domains = [
            "spatial reasoning",
            "time perception",
            "causal reasoning",
            "memory recall",
            "decision making"
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                "linguistic_feature": random.choice(linguistic_features),
                "cognitive_domain": random.choice(cognitive_domains)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and tests the linguistic relativity hypothesis, focusing on how {t['linguistic_feature']} might influence {t['cognitive_domain']}. Your response should include the following sections:

1. Theoretical Framework (200-250 words):
   a) Explain the linguistic relativity hypothesis and its relevance to {t['linguistic_feature']} and {t['cognitive_domain']}.
   b) Discuss current research and debates surrounding this specific aspect of linguistic relativity.
   c) Propose a testable hypothesis about how {t['linguistic_feature']} might influence {t['cognitive_domain']}.

2. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for simulating linguistic relativity effects.
   b) Explain how your system models language processing and cognitive processes related to {t['cognitive_domain']}.
   c) Detail how the system incorporates {t['linguistic_feature']} into its language models.
   d) Discuss how your system simulates cognitive tasks related to {t['cognitive_domain']}.

3. Simulation and Testing Methodology (200-250 words):
   a) Outline the process for simulating language use and cognitive tasks in your AI system.
   b) Describe how you would design experiments to test your hypothesis about {t['linguistic_feature']} and {t['cognitive_domain']}.
   c) Explain how you would control for confounding variables in your simulations.
   d) Discuss how you would measure and analyze the results of your simulations.

4. Data Requirements and Ethical Considerations (150-200 words):
   a) Describe the types and sources of data needed to train and validate your AI system.
   b) Discuss potential biases in language data and how you would address them.
   c) Explain ethical considerations in simulating cognitive processes and testing linguistic relativity.
   d) Propose guidelines for responsible use and interpretation of your system's results.

5. Potential Applications and Implications (150-200 words):
   a) Discuss potential applications of your AI system in fields such as cognitive science, linguistics, or cross-cultural communication.
   b) Explain how your system could contribute to our understanding of language, thought, and culture.
   c) Speculate on potential implications of your findings for language policy, education, or AI development.

6. Limitations and Future Directions (100-150 words):
   a) Identify three major limitations or challenges of your proposed AI system.
   b) For each limitation, suggest a potential avenue for future research or system improvement.

Ensure your response demonstrates a deep understanding of linguistic theories, cognitive science principles, and AI modeling techniques. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a clear explanation of the linguistic relativity hypothesis and its relevance to {t['linguistic_feature']} and {t['cognitive_domain']}",
            "The AI system architecture should be described in detail, including how it models language processing and cognitive processes",
            "The simulation and testing methodology should be clearly outlined, including experiment design and analysis methods",
            "The response should address data requirements and ethical considerations in AI-based linguistic and cognitive simulations",
            "Potential applications and implications of the AI system should be discussed, showing interdisciplinary thinking",
            "Limitations and future directions should be identified, demonstrating critical analysis of the proposed system",
            "The response should demonstrate a deep understanding of linguistic theories, cognitive science principles, and AI modeling techniques",
            "The proposed AI system should be creative and innovative while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
