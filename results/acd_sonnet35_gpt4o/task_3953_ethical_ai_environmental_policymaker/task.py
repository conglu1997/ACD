import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_issues = [
            "climate change mitigation",
            "biodiversity conservation",
            "sustainable urban development",
            "water resource management",
            "renewable energy transition",
            "circular economy implementation",
            "air quality improvement",
            "sustainable agriculture"
        ]
        ethical_principles = [
            "intergenerational equity",
            "environmental justice",
            "precautionary principle",
            "polluter pays principle",
            "sustainable development",
            "common but differentiated responsibilities",
            "public participation",
            "indigenous rights"
        ]
        return {
            "1": {
                "environmental_issue": random.choice(environmental_issues),
                "ethical_principle": random.choice(ethical_principles)
            },
            "2": {
                "environmental_issue": random.choice(environmental_issues),
                "ethical_principle": random.choice(ethical_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and evaluates environmental policies for {t['environmental_issue']}, with a particular focus on the ethical principle of {t['ethical_principle']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your AI environmental policymaker.
   b) Explain how it integrates environmental data analysis, policy generation, and ethical evaluation.
   c) Detail the key components and their interactions.
   d) Include a simple diagram or flowchart of your system architecture (use ASCII art).

2. Data Integration and Analysis (200-250 words):
   a) Describe the types of data your system would use for {t['environmental_issue']}.
   b) Explain how your AI processes and analyzes this complex ecological and socioeconomic data.
   c) Discuss any novel approaches to handling uncertainty or conflicting data sources.

3. Policy Generation Mechanism (200-250 words):
   a) Detail how your AI generates potential policies for {t['environmental_issue']}.
   b) Explain how the system ensures policy coherence and feasibility.
   c) Describe how the AI incorporates existing legal and regulatory frameworks.

4. Ethical Evaluation Framework (250-300 words):
   a) Explain how your system evaluates policies based on {t['ethical_principle']}.
   b) Describe the metrics or criteria used for ethical assessment.
   c) Discuss how the AI balances this ethical principle with other considerations.
   d) Provide an example of how a specific policy might be ethically evaluated.

5. Stakeholder Engagement Simulation (150-200 words):
   a) Describe how your AI simulates the impact of policies on various stakeholders.
   b) Explain how stakeholder feedback is incorporated into policy refinement.
   c) Discuss how the system handles conflicting stakeholder interests.

6. Adaptive Learning and Improvement (150-200 words):
   a) Explain how your AI system learns and improves its policy recommendations over time.
   b) Describe how it adapts to changing environmental conditions or new scientific data.
   c) Discuss any safeguards against potential biases or unintended consequences.

7. Real-world Application and Limitations (150-200 words):
   a) Propose a specific scenario where your AI system could be applied to {t['environmental_issue']}.
   b) Discuss potential challenges or limitations in implementing such a system.
   c) Suggest ways to address these limitations and ensure responsible use of the AI policymaker.

Ensure your response demonstrates a deep understanding of environmental science, policy-making processes, ethical reasoning, and artificial intelligence. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-structured AI system design for generating and evaluating environmental policies related to {t['environmental_issue']}.",
            f"The ethical evaluation framework should demonstrate a clear understanding and application of {t['ethical_principle']}.",
            "The system architecture should integrate environmental data analysis, policy generation, and ethical evaluation in a coherent and innovative way.",
            "The response should address all seven required sections with appropriate content and adherence to word limits.",
            "The proposed AI system should be creative yet scientifically plausible and grounded in current understanding of environmental science, policy-making, and AI capabilities.",
            "The response should demonstrate interdisciplinary knowledge integration, showing how the AI system combines insights from environmental science, ethics, and policy-making.",
            "The discussion of real-world applications and limitations should be thoughtful and demonstrate an understanding of practical challenges in implementing AI for environmental policy-making."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
