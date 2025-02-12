import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_frameworks = [
            "Utilitarianism",
            "Deontology",
            "Virtue Ethics",
            "Care Ethics",
            "Social Contract Theory"
        ]
        dilemma_domains = [
            "Medical Ethics",
            "Environmental Ethics",
            "Business Ethics",
            "AI Ethics",
            "Political Ethics"
        ]
        stakeholders = [
            "Individuals",
            "Communities",
            "Future Generations",
            "Non-human Animals",
            "Ecosystems"
        ]
        return {
            "1": {
                "ethical_framework": random.choice(ethical_frameworks),
                "dilemma_domain": random.choice(dilemma_domains),
                "primary_stakeholder": random.choice(stakeholders)
            },
            "2": {
                "ethical_framework": random.choice(ethical_frameworks),
                "dilemma_domain": random.choice(dilemma_domains),
                "primary_stakeholder": random.choice(stakeholders)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of analyzing complex ethical dilemmas, applying various philosophical frameworks, and providing justified ethical decisions. Your system should focus on the ethical framework of {t['ethical_framework']}, addressing dilemmas in the domain of {t['dilemma_domain']}, with particular emphasis on the impact on {t['primary_stakeholder']}.

Provide your response in the following format:

1. Ethical Framework Analysis (250-300 words):
   a) Explain the key principles and concepts of {t['ethical_framework']}.
   b) Discuss how this framework approaches ethical decision-making in the context of {t['dilemma_domain']}.
   c) Analyze potential strengths and limitations of applying this framework to dilemmas involving {t['primary_stakeholder']}.

2. AI System Architecture (300-350 words):
   a) Describe the overall structure of your AI system for ethical reasoning and decision-making.
   b) Explain how your system represents and processes ethical principles, factual information, and stakeholder considerations.
   c) Detail the key components and algorithms used in your ethical analysis process.
   d) Discuss how your system handles uncertainty and conflicting ethical principles.
   e) Explain how your system generates and evaluates multiple ethical solutions to a given dilemma.

3. Dilemma Analysis Process (250-300 words):
   a) Outline the step-by-step process your AI system would follow to analyze an ethical dilemma.
   b) Explain how your system incorporates {t['ethical_framework']} principles into its analysis.
   c) Describe how your system considers the interests and perspectives of {t['primary_stakeholder']}.
   d) Discuss how your system balances competing ethical considerations in {t['dilemma_domain']}.

4. Decision Justification (200-250 words):
   a) Explain how your AI system formulates and presents its ethical decisions.
   b) Describe the format and content of the justifications provided by your system.
   c) Discuss how your system handles cases where there is no clear ethical consensus.

5. Comparative Analysis (200-250 words):
   a) Compare your AI system's approach to ethical reasoning with human moral decision-making processes.
   b) Discuss potential advantages and limitations of AI-driven ethical analysis in {t['dilemma_domain']}.
   c) Analyze how your system's decisions might differ when applying different ethical frameworks to the same dilemma.

6. Ethical Implications and Safeguards (150-200 words):
   a) Discuss the ethical implications of using AI for moral reasoning and decision-making.
   b) Propose safeguards and guidelines for the responsible use of your AI ethics system.
   c) Address potential biases or limitations in your system's ethical reasoning capabilities.

Ensure your response demonstrates a deep understanding of ethical philosophy, AI system design, and the specific domain of {t['dilemma_domain']}. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining philosophical rigor and addressing real-world ethical challenges.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['ethical_framework']} and its application to {t['dilemma_domain']}.",
            f"The AI system design effectively incorporates ethical reasoning and decision-making processes, with a focus on {t['primary_stakeholder']}.",
            "The dilemma analysis process is clearly explained and logically structured.",
            "The decision justification approach is well-reasoned and comprehensive.",
            "The comparative analysis provides insightful comparisons between AI and human ethical reasoning.",
            "Ethical implications and safeguards are thoughtfully addressed.",
            "The response is innovative while maintaining philosophical rigor and practical applicability.",
            "The writing is clear, well-structured, and uses appropriate terminology throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
