import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        social_phenomena = [
            {
                "phenomenon": "Groupthink",
                "context": "Corporate board meeting",
                "theory": "Social Identity Theory"
            },
            {
                "phenomenon": "Bystander effect",
                "context": "Urban emergency situation",
                "theory": "Diffusion of Responsibility"
            },
            {
                "phenomenon": "Conformity",
                "context": "Social media platform",
                "theory": "Normative Social Influence"
            },
            {
                "phenomenon": "Polarization",
                "context": "Political debate",
                "theory": "Group Polarization Theory"
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(random.sample(social_phenomena, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of simulating and analyzing social influence and group decision-making processes, then use it to model the social phenomenon of {t['phenomenon']} in the context of a {t['context']}. Your system should incorporate principles from {t['theory']}. Provide your response in the following format:\n\n1. System Architecture (250-300 words):\n   a) Describe the key components of your AI social dynamics simulator.\n   b) Explain how your system models individual and group behavior.\n   c) Detail how you incorporate principles from {t['theory']}.\n   d) Discuss any novel elements in your design that enable realistic simulation of {t['phenomenon']}.\n\n2. Theoretical Framework (200-250 words):\n   a) Explain {t['theory']} and its relevance to {t['phenomenon']}.\n   b) Describe how your AI system computationally models this theory.\n   c) Discuss potential limitations in applying social psychological theories to AI simulations.\n\n3. Simulation Process (250-300 words):\n   a) Provide a step-by-step description of how your system would simulate {t['phenomenon']} in a {t['context']}.\n   b) Explain how individual agents in your simulation make decisions and influence each other.\n   c) Describe how your system accounts for contextual factors specific to a {t['context']}.\n   d) Include a pseudo-code snippet or flowchart illustrating a key part of your simulation process.\n\n4. Analysis Capabilities (200-250 words):\n   a) Explain how your AI system analyzes the simulated social dynamics.\n   b) Describe the key metrics or features your system uses to quantify {t['phenomenon']}.\n   c) Discuss how your system might generate insights or predictions about real-world social behavior.\n\n5. Ethical Considerations (150-200 words):\n   a) Discuss potential ethical implications of using AI to simulate and analyze human social behavior.\n   b) Address concerns about privacy, consent, and potential misuse of such technology.\n   c) Propose guidelines for the responsible development and use of social dynamics simulators.\n\n6. Future Developments (150-200 words):\n   a) Suggest two potential enhancements or extensions to your AI social dynamics simulator.\n   b) Propose a research study that could validate or improve your system's accuracy in modeling {t['phenomenon']}.\n   c) Speculate on how this technology might influence fields such as sociology, political science, or marketing.\n\nEnsure your response demonstrates a deep understanding of social psychology, artificial intelligence, and complex systems modeling. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and technological plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1200-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture effectively incorporates principles from {t['theory']} to model {t['phenomenon']}.",
            f"The simulation process realistically represents {t['phenomenon']} in the context of a {t['context']}.",
            "The analysis capabilities demonstrate a deep understanding of social dynamics and provide meaningful insights.",
            "The response shows creativity and innovation in AI system design while maintaining scientific plausibility.",
            "Ethical considerations are thoroughly addressed with thoughtful guidelines proposed.",
            "The response demonstrates a strong interdisciplinary understanding, integrating concepts from social psychology, AI, and complex systems modeling."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
