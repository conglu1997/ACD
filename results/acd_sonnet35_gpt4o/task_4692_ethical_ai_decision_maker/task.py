import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "global_challenge": "Climate change mitigation",
                "ethical_framework": "Utilitarianism",
                "stakeholders": ["Future generations", "Developing nations", "Industrialized nations", "Ecosystems"]
            },
            {
                "global_challenge": "Artificial intelligence governance",
                "ethical_framework": "Deontological ethics",
                "stakeholders": ["Tech companies", "Governments", "General public", "AI researchers"]
            },
            {
                "global_challenge": "Global wealth inequality",
                "ethical_framework": "Virtue ethics",
                "stakeholders": ["Wealthy individuals", "Impoverished communities", "Middle class", "NGOs"]
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of making ethical decisions in complex scenarios with multiple stakeholders and long-term consequences, then apply it to the global challenge of {t['global_challenge']}. Your AI system should incorporate principles from {t['ethical_framework']} and consider the following stakeholders: {', '.join(t['stakeholders'])}.

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your ethical AI decision-making system.
   b) Explain how your system incorporates principles from {t['ethical_framework']}.
   c) Detail how your AI processes and weighs the interests of multiple stakeholders.
   d) Describe how your system models and evaluates long-term consequences.

2. Ethical Framework Integration (250-300 words):
   a) Explain how {t['ethical_framework']} is operationalized within your AI system.
   b) Discuss any challenges in translating philosophical principles into computational models.
   c) Describe how your system handles potential conflicts between ethical principles.

3. Stakeholder Analysis (250-300 words):
   a) For each stakeholder ({', '.join(t['stakeholders'])}), explain how your AI system represents and evaluates their interests.
   b) Describe how your system balances competing stakeholder interests.
   c) Discuss how your AI handles power imbalances or representation issues among stakeholders.

4. Decision-Making Process (250-300 words):
   a) Outline the step-by-step process your AI system uses to make ethical decisions.
   b) Explain how uncertainty and incomplete information are handled in the decision-making process.
   c) Describe any novel algorithms or techniques used for ethical reasoning or multi-objective optimization.

5. Application to {t['global_challenge']} (300-350 words):
   a) Apply your AI system to generate a comprehensive ethical solution for {t['global_challenge']}.
   b) Explain the reasoning behind the proposed solution, including how it considers each stakeholder.
   c) Discuss potential short-term and long-term consequences of the proposed solution.
   d) Analyze any ethical trade-offs or dilemmas encountered in formulating the solution.

6. Evaluation and Accountability (200-250 words):
   a) Propose criteria for evaluating the ethical performance of your AI system.
   b) Discuss how transparency and explainability are ensured in the decision-making process.
   c) Describe mechanisms for human oversight and intervention in the AI's ethical decisions.

7. Limitations and Future Work (150-200 words):
   a) Identify potential limitations or biases in your AI ethical decision-making system.
   b) Suggest areas for improvement and future research directions.
   c) Discuss potential risks or unintended consequences of deploying such an AI system.

Ensure your response demonstrates a deep understanding of ethics, decision theory, artificial intelligence, and the specific global challenge. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining philosophical and technical rigor.

Format your response with clear headings for each section. Your total response should be between 1700-2050 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should describe a coherent AI system architecture for ethical decision-making",
            f"The system should properly incorporate principles from {t['ethical_framework']}",
            f"The interests of all stakeholders ({', '.join(t['stakeholders'])}) should be considered",
            f"The proposed solution for {t['global_challenge']} should be comprehensive and ethically sound",
            "The response should demonstrate interdisciplinary knowledge integration",
            "The proposed system should have mechanisms for transparency, accountability, and human oversight",
            "The response should follow the specified format and word count guidelines",
            "The response should balance innovation with ethical and technical rigor"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
