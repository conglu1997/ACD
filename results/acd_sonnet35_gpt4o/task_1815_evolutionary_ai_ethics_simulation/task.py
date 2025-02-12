import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_dilemmas = [
            "Trolley Problem",
            "Prisoner's Dilemma",
            "Tragedy of the Commons",
            "Altruism vs. Self-interest"
        ]
        evolutionary_mechanisms = [
            "Natural Selection",
            "Genetic Drift",
            "Gene Flow",
            "Mutation"
        ]
        ai_architectures = [
            "Neural Networks",
            "Genetic Algorithms",
            "Reinforcement Learning",
            "Rule-based Systems"
        ]
        return {
            "1": {
                "ethical_dilemma": random.choice(ethical_dilemmas),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms),
                "ai_architecture": random.choice(ai_architectures)
            },
            "2": {
                "ethical_dilemma": random.choice(ethical_dilemmas),
                "evolutionary_mechanism": random.choice(evolutionary_mechanisms),
                "ai_architecture": random.choice(ai_architectures)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze an artificial life simulation that explores the emergence of ethical behavior in evolving AI agents, focusing on the {t['ethical_dilemma']} as the central ethical challenge. Your simulation should incorporate {t['evolutionary_mechanism']} as the primary evolutionary mechanism and use {t['ai_architecture']} as the foundation for the AI agents. Your response should follow this structure:\n\n1. Simulation Design (200-250 words):\n   1.1 Overall Structure: Describe the basic components and how they interact.\n   1.2 Implementation of Ethical Dilemma: Explain how the {t['ethical_dilemma']} is represented in the simulation.\n   1.3 AI Agent Representation: Detail how agents make decisions and interact.\n   1.4 Evolutionary Mechanism: Describe how {t['evolutionary_mechanism']} is implemented.\n\n2. Ethical Behavior Emergence (150-200 words):\n   2.1 Hypothesis: Propose how ethical behavior might emerge over time.\n   2.2 Evolutionary Pressures: Identify factors that could influence ethical or unethical behaviors.\n   2.3 AI Architecture Influence: Explain how {t['ai_architecture']} might affect ethical decision-making.\n\n3. Simulation Analysis (150-200 words):\n   3.1 Metrics: Propose at least two ways to measure ethical behavior in your simulation.\n   3.2 Expected Patterns: Describe potential trends or phenomena you might observe.\n   3.3 Validation: Suggest how to distinguish true ethical behavior from simple optimization.\n\n4. Philosophical Implications (100-150 words):\n   4.1 Ethics Understanding: Discuss how your simulation might inform our understanding of ethics.\n   4.2 Machine Ethics: Consider implications for developing ethical AI systems.\n\n5. Limitations and Future Work (100-150 words):\n   5.1 Limitations: Identify at least two potential shortcomings of your simulation.\n   5.2 Extensions: Propose one or two ways to improve or expand your simulation in future work.\n\nEnsure your response demonstrates understanding of evolutionary biology, artificial intelligence, and moral philosophy. Be creative while maintaining scientific plausibility and ethical responsibility. Use appropriate terminology and provide clear explanations.\n\nYour total response should be between 700-950 words. Responses outside this range will not be considered valid."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        word_count = len(submission.split())
        if word_count < 650 or word_count > 1000:  # Allowing for some tolerance
            return 0.0
        criteria = [
            f"The simulation design incorporates the {t['ethical_dilemma']}, {t['evolutionary_mechanism']}, and {t['ai_architecture']}.",
            "The response proposes a plausible mechanism for the emergence of ethical behavior in AI agents.",
            "At least two metrics for measuring ethical behavior in the simulation are proposed.",
            "The response discusses potential implications for understanding ethics or developing ethical AI systems.",
            "At least two limitations of the proposed simulation are identified.",
            "The response demonstrates basic understanding of evolutionary biology, artificial intelligence, and moral philosophy concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
