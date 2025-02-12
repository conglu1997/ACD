import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "dilemma": "AI-Mediated Trust",
                "context": "A social network where AI algorithms control information flow between users",
                "ethical_concern": "Privacy vs. Social Cohesion vs. Information Accuracy"
            },
            {
                "dilemma": "Automated Moral Decisions",
                "context": "Self-driving cars programmed to make split-second ethical choices",
                "ethical_concern": "Utilitarianism vs. Individual Rights vs. Legal Liability"
            },
            {
                "dilemma": "AI Resource Allocation",
                "context": "An AI system distributing limited medical resources in a pandemic",
                "ethical_concern": "Equality vs. Efficiency vs. Long-term Public Health"
            },
            {
                "dilemma": "Predictive Justice",
                "context": "An AI-powered judicial system predicting and preventing crimes",
                "ethical_concern": "Security vs. Freedom vs. Algorithmic Bias"
            },
            {
                "dilemma": "AI-Driven Education",
                "context": "An AI system personalizing educational content and career paths for students",
                "ethical_concern": "Individual Potential vs. Societal Needs vs. Equality of Opportunity"
            },
            {
                "dilemma": "Emotional AI Companions",
                "context": "AI-powered emotional support systems for isolated individuals",
                "ethical_concern": "Mental Health vs. Human Connection vs. AI Dependency"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI-driven social experiment based on the following scenario:\n\nDilemma: {t['dilemma']}\nContext: {t['context']}\nEthical Concern: {t['ethical_concern']}\n\nYour response should include:\n\n1. Experiment Design (250-300 words):\n   a) Describe the setup of your experiment, including the role of AI.\n   b) Explain how it relates to the prisoner's dilemma or other relevant game theory concepts.\n   c) Detail the choices participants face and their potential outcomes.\n   d) Describe how the experiment incorporates all three aspects of the ethical concern.\n\n2. Behavioral Economics Analysis (200-250 words):\n   a) Discuss the behavioral economics principles at play in your experiment.\n   b) Predict how these principles might influence participant behavior.\n   c) Explain how the AI system could exploit or mitigate cognitive biases.\n   d) Analyze potential unintended consequences of the AI's influence on behavior.\n\n3. Ethical Implications (200-250 words):\n   a) Analyze the ethical concerns raised by your experiment, addressing all three aspects mentioned.\n   b) Discuss the potential societal impacts if such a system were implemented at scale.\n   c) Propose guidelines for responsible implementation and use of such AI systems.\n   d) Explore the long-term consequences of widespread adoption of this technology.\n\n4. Game Theory Application (150-200 words):\n   a) Model your experiment using game theory concepts.\n   b) Analyze potential equilibria and their implications.\n   c) Discuss how the presence of AI changes traditional game theory dynamics.\n   d) Propose a mathematical representation of the payoff structure in your experiment.\n\n5. AI Design Considerations (150-200 words):\n   a) Outline the key features and constraints of the AI system in your experiment.\n   b) Discuss potential challenges in implementing such an AI system.\n   c) Propose methods to ensure the AI behaves ethically and transparently.\n   d) Describe how the AI could be designed to balance the three competing ethical concerns.\n\nEnsure your response demonstrates a deep understanding of game theory, behavioral economics, AI ethics, and their interdisciplinary applications. Be creative in your design while maintaining scientific and ethical plausibility. Your total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of game theory and its application to the given scenario.",
            "The experiment design is creative, plausible, and effectively incorporates AI.",
            "The behavioral economics analysis shows insight into human decision-making processes and potential unintended consequences.",
            "The ethical implications are thoroughly considered, addressing all three aspects of the ethical concern.",
            "The response effectively applies game theory concepts to model the experiment, including a mathematical representation.",
            "The AI design considerations are well-thought-out, address potential challenges, and propose methods for ethical and transparent behavior.",
            "The overall response is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
