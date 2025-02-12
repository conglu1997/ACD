import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain": "healthcare",
                "dilemma": "resource allocation during a pandemic",
                "stakeholders": ["patients", "healthcare workers", "general public"],
                "ethical_frameworks": ["utilitarianism", "deontology", "care ethics"]
            },
            {
                "domain": "autonomous vehicles",
                "dilemma": "crash scenario with unavoidable harm",
                "stakeholders": ["passengers", "pedestrians", "manufacturer"],
                "ethical_frameworks": ["virtue ethics", "social contract theory", "utilitarianism"]
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of making ethical decisions in the domain of {t['domain']}, specifically addressing the dilemma of {t['dilemma']}. Your system should consider the perspectives of {', '.join(t['stakeholders'])} and apply the following ethical frameworks: {', '.join(t['ethical_frameworks'])}.

1. System Architecture (250-300 words):
   a) Describe the key components of your AI ethical decision-making system.
   b) Explain how your system incorporates the specified ethical frameworks.
   c) Detail how the system analyzes and weighs the interests of different stakeholders.
   d) Include a high-level diagram or pseudocode representation of a key decision-making process in your system.

2. Ethical Framework Integration (200-250 words):
   a) Explain how your system applies each of the specified ethical frameworks to the given dilemma.
   b) Discuss any conflicts or synergies between these frameworks in the context of the dilemma.
   c) Describe how your system resolves conflicts between different ethical considerations.

3. Stakeholder Analysis (200-250 words):
   a) Detail how your system identifies and represents the interests of each stakeholder group.
   b) Explain the process by which your system weighs and balances these different interests.
   c) Discuss how your system handles potential biases or inequalities among stakeholders.

4. Decision-Making Process (250-300 words):
   a) Provide a step-by-step explanation of how your system would approach the given ethical dilemma.
   b) Include an example scenario within the specified domain and dilemma.
   c) Explain how your system would arrive at a final decision, including any trade-offs or compromises.
   d) Discuss how your system handles uncertainty or incomplete information in the decision-making process.

5. Evaluation and Accountability (150-200 words):
   a) Propose methods for evaluating the ethical soundness of your system's decisions.
   b) Discuss how you would ensure transparency and explainability in your system's decision-making process.
   c) Address potential criticisms or concerns about using AI for ethical decision-making in this context.

6. Limitations and Future Work (100-150 words):
   a) Identify potential limitations or weaknesses in your proposed system.
   b) Suggest areas for future research or improvement in AI ethical decision-making systems.

Ensure your response demonstrates a deep understanding of ethical philosophy, AI decision-making processes, and the complexities of the given domain. Be innovative in your approach while maintaining logical consistency and practical feasibility. Use appropriate technical and philosophical terminology, providing clear explanations for complex concepts.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response adequately addresses the domain of {t['domain']} and the dilemma of {t['dilemma']}.",
            f"The system considers the perspectives of {', '.join(t['stakeholders'])}.",
            f"The ethical frameworks {', '.join(t['ethical_frameworks'])} are applied and analyzed.",
            "The proposed AI system is innovative, coherent, and ethically sound.",
            "The response demonstrates a deep understanding of ethical philosophy, AI decision-making, and the complexities of the given domain.",
            "All six sections are adequately addressed within the specified word count ranges."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
