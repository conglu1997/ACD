import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        language_features = [
            "grammatical gender",
            "evidentiality markers",
            "ergative-absolutive alignment",
            "tonal distinctions",
            "click consonants"
        ]
        cognitive_constraints = [
            "working memory limitations",
            "pattern recognition abilities",
            "social learning capacities",
            "neural plasticity",
            "attentional bottlenecks"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "language_feature": random.choice(language_features),
                "cognitive_constraint": random.choice(cognitive_constraints)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates both the evolution of language over time and individual language acquisition, focusing on the development of {t['language_feature']} while considering {t['cognitive_constraint']}. Your response should include:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your AI system for modeling language evolution and acquisition.\n   b) Explain how these components interact to simulate both population-level language change and individual learning.\n   c) Discuss how your design incorporates principles from historical linguistics and developmental psychology.\n\n2. Evolutionary Simulation (200-250 words):\n   a) Detail how your system models the emergence and development of {t['language_feature']} over time.\n   b) Explain how social and environmental factors are incorporated into the evolutionary process.\n   c) Describe how your system handles variation and selection in language features.\n\n3. Acquisition Modeling (200-250 words):\n   a) Explain how your system simulates individual language acquisition, particularly for {t['language_feature']}.\n   b) Discuss how {t['cognitive_constraint']} is modeled and its impact on the acquisition process.\n   c) Describe any critical periods or stages in your acquisition model.\n\n4. Integration and Interaction (150-200 words):\n   a) Explain how the evolutionary and acquisition components of your system interact.\n   b) Discuss how individual acquisition processes might influence population-level language change in your model.\n\n5. Hypothetical Scenario (200-250 words):\n   a) Present a specific scenario for the evolution and acquisition of {t['language_feature']} using your system.\n   b) Describe the initial conditions, key stages of development, and final state of the feature.\n   c) Explain how {t['cognitive_constraint']} influences the outcome in your scenario.\n\n6. Evaluation and Implications (150-200 words):\n   a) Propose methods for evaluating the accuracy and plausibility of your system's simulations.\n   b) Discuss the potential implications of your model for our understanding of language evolution and acquisition.\n   c) Suggest how your system could be used to generate and test hypotheses in linguistics and cognitive science.\n\nEnsure your response demonstrates a deep understanding of linguistics, neuroscience, developmental psychology, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response using clear headings for each section. Your total response should be between 1150-1450 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['language_feature']} and how it might evolve and be acquired",
            f"The proposed AI system presents a plausible and creative approach to simulating language evolution and acquisition while considering {t['cognitive_constraint']}",
            "The system architecture effectively integrates evolutionary and acquisition processes",
            "The hypothetical scenario is well-developed and illustrates the system's capabilities",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
