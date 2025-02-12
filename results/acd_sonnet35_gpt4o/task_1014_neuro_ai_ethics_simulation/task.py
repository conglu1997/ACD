import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_functions = [
            "memory formation and retrieval",
            "emotional processing",
            "decision-making and reasoning",
            "language comprehension and production",
            "sensory perception integration"
        ]
        application_domains = [
            "healthcare",
            "education",
            "criminal justice",
            "social media",
            "autonomous systems"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "brain_function": random.choice(brain_functions),
                "application_domain": random.choice(application_domains)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates the human brain function of {t['brain_function']} for application in the domain of {t['application_domain']}. Then, analyze its ethical implications and potential societal impacts. Your response should include the following sections:\n\n1. AI System Design (250-300 words):\n   a) Describe the key components and architecture of your AI system.\n   b) Explain how it simulates the specified brain function.\n   c) Discuss how it would be applied in the given domain.\n   d) Highlight any novel features or approaches in your design.\n\n2. Neuroscientific Basis (200-250 words):\n   a) Explain the current understanding of the specified brain function.\n   b) Discuss how your AI system models or deviates from biological processes.\n   c) Identify any simplifications or assumptions made in your model.\n\n3. Ethical Implications (200-250 words):\n   a) Analyze at least three potential ethical issues arising from your system.\n   b) Discuss how these issues might be addressed or mitigated.\n   c) Consider both short-term and long-term ethical consequences.\n\n4. Societal Impact (200-250 words):\n   a) Predict potential positive and negative societal impacts of your system.\n   b) Discuss how it might change current practices in the specified domain.\n   c) Consider potential misuses or unintended consequences.\n\n5. Comparative Analysis (150-200 words):\n   a) Compare your AI system to existing technologies in the field.\n   b) Discuss how your approach differs from or improves upon current methods.\n\n6. Future Developments and Safeguards (150-200 words):\n   a) Propose future research directions to enhance your system.\n   b) Suggest potential safeguards or regulations to ensure responsible use.\n\nEnsure your response demonstrates a deep understanding of neuroscience, AI, and ethics. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide explanations where necessary.\n\nFormat your response using clear headings for each section and number your paragraphs within each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['brain_function']} and how it can be simulated in an AI system",
            f"The proposed AI system presents a plausible and creative approach for application in {t['application_domain']}",
            "The ethical implications are thoroughly analyzed with consideration of multiple perspectives",
            "The societal impacts are well-reasoned and consider both positive and negative consequences",
            "The response shows strong interdisciplinary knowledge integration and creative problem-solving"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
