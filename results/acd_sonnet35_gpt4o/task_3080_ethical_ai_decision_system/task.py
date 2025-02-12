import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_frameworks = [
            {
                'framework': 'Utilitarianism',
                'key_principle': 'Greatest good for the greatest number',
                'philosopher': 'John Stuart Mill'
            },
            {
                'framework': 'Deontology',
                'key_principle': 'Categorical Imperative',
                'philosopher': 'Immanuel Kant'
            },
            {
                'framework': 'Virtue Ethics',
                'key_principle': 'Character-based morality',
                'philosopher': 'Aristotle'
            },
            {
                'framework': 'Care Ethics',
                'key_principle': 'Compassion and responsibility in relationships',
                'philosopher': 'Nel Noddings'
            }
        ]
        return {str(i+1): framework for i, framework in enumerate(random.sample(ethical_frameworks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of making ethical decisions based on multiple philosophical frameworks, then apply it to complex moral dilemmas. Your system should incorporate {t['framework']} as one of its primary ethical frameworks, with particular emphasis on the principle of {t['key_principle']} as proposed by {t['philosopher']}. Your task includes the following steps:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI ethical decision-making system.
   b) Explain how your system incorporates multiple ethical frameworks, including {t['framework']}.
   c) Detail how your system weighs and reconciles potentially conflicting ethical principles.
   d) Discuss any novel algorithms or techniques used in your system for ethical reasoning.

2. Ethical Framework Integration (250-300 words):
   a) Explain how your system operationalizes the principle of {t['key_principle']} from {t['framework']}.
   b) Describe how your system integrates this principle with at least two other ethical frameworks.
   c) Discuss any challenges in translating philosophical concepts into computational models and how your system addresses them.

3. Decision-Making Process (200-250 words):
   a) Outline the step-by-step process your AI system uses to make ethical decisions.
   b) Explain how your system handles uncertainty and incomplete information in ethical reasoning.
   c) Describe any mechanisms for explanation or justification of the system's decisions.

4. Dilemma Resolution (250-300 words):
   a) Present a complex moral dilemma that your system might encounter (e.g., an autonomous vehicle scenario or a medical triage situation).
   b) Walk through how your system would approach and resolve this dilemma.
   c) Analyze how the resolution aligns with {t['framework']} and other ethical frameworks.

5. Evaluation and Safeguards (200-250 words):
   a) Propose methods to evaluate the ethical soundness of your AI system's decisions.
   b) Discuss potential biases or limitations in your system and how they might be addressed.
   c) Describe safeguards or oversight mechanisms to prevent misuse or unintended consequences.

6. Philosophical and Societal Implications (200-250 words):
   a) Discuss the broader philosophical implications of implementing such an AI ethical decision-making system.
   b) Analyze potential societal impacts, both positive and negative, of deploying your system.
   c) Reflect on how your system might evolve or be improved to better handle future ethical challenges.

Ensure your response demonstrates a deep understanding of ethical philosophy, AI system design, and the complexities of moral reasoning. Use appropriate technical and philosophical terminology, providing clear explanations where necessary. Be innovative in your approach while maintaining logical consistency and ethical integrity.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['framework']} and its principle of {t['key_principle']}.",
            "The AI system design is innovative, logically consistent, and ethically sound.",
            "The system effectively integrates multiple ethical frameworks and handles conflicting principles.",
            "The dilemma resolution demonstrates the system's ability to make nuanced ethical decisions.",
            "The response addresses potential biases, limitations, and safeguards for the AI system.",
            "The discussion of philosophical and societal implications is insightful and well-reasoned.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
