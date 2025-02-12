import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = ['water conservation', 'energy efficiency', 'waste reduction', 'sustainable transportation']
        psychological_principles = ['nudge theory', 'cognitive dissonance', 'social proof', 'gamification']
        return {
            "1": {
                "issue": random.choice(environmental_issues),
                "principle": random.choice(psychological_principles)
            },
            "2": {
                "issue": random.choice(environmental_issues),
                "principle": random.choice(psychological_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses the psychological principle of {t['principle']} to modify human behavior for {t['issue']}. Then, analyze its ethical implications and potential societal impacts. Your response should include:

1. AI System Design (300-350 words):
   a) Describe the key components and architecture of your AI system.
   b) Explain how it incorporates {t['principle']} to influence behavior related to {t['issue']}.
   c) Detail the data sources and types of data your system would use.
   d) Discuss how your system would interact with users and measure its effectiveness.

2. Psychological Mechanism (200-250 words):
   a) Explain the psychological principle of {t['principle']} in depth.
   b) Describe how this principle can be effectively applied to {t['issue']}.
   c) Discuss potential challenges in using this principle for behavior modification.

3. Environmental Impact Analysis (200-250 words):
   a) Estimate the potential environmental impact of your system if widely adopted.
   b) Discuss any possible negative environmental consequences of your approach.
   c) Compare your AI-driven approach to traditional methods of promoting {t['issue']}.

4. Ethical Considerations (250-300 words):
   a) Analyze the ethical implications of using AI and psychological principles for behavior modification.
   b) Discuss potential issues related to privacy, autonomy, and informed consent.
   c) Consider the fairness and potential biases of your system.
   d) Propose guidelines for the ethical development and deployment of such systems.

5. Societal Impact (200-250 words):
   a) Predict potential long-term societal changes resulting from widespread use of your system.
   b) Discuss how it might affect social norms, policies, and individual freedoms.
   c) Consider potential unintended consequences of your approach.

6. Future Developments (150-200 words):
   a) Propose two potential advancements or extensions of your system.
   b) Discuss how emerging technologies might enhance or alter your approach in the future.
   c) Suggest a research question that could further explore the intersection of AI, psychology, and environmental sustainability.

Ensure your response demonstrates a deep understanding of AI, psychology, environmental science, and ethics. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and ethical plausibility.

Format your answer with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['principle']} and its application to {t['issue']}.",
            "The AI system design should be innovative yet plausible, with clear components and data sources.",
            "The psychological mechanism should be accurately explained and appropriately applied to the environmental issue.",
            "The environmental impact analysis should be logical and consider both positive and negative consequences.",
            "The ethical considerations should be comprehensive, addressing privacy, autonomy, fairness, and consent.",
            "The societal impact analysis should be thoughtful and consider long-term and unintended consequences.",
            "The future developments should be creative and relevant to the intersection of AI, psychology, and environmental sustainability.",
            "The overall response must demonstrate strong interdisciplinary knowledge integration and ethical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
