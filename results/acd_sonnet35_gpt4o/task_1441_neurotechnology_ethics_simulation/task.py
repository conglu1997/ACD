import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neurotechnologies = [
            "Memory enhancement implant",
            "Emotion regulation neural interface",
            "Thought-to-text brain-computer interface",
            "Dream recording and playback device",
            "Cognitive ability augmentation chip"
        ]
        societal_domains = [
            "Education",
            "Criminal justice",
            "Workforce and employment",
            "Personal relationships",
            "Political processes"
        ]
        ethical_principles = [
            "Autonomy",
            "Privacy",
            "Equality",
            "Human dignity",
            "Social justice"
        ]
        constraints = [
            "Limited to medical use only",
            "Available to general public",
            "Requires government approval for use",
            "Irreversible once implemented",
            "Temporary effects lasting up to one year"
        ]
        return {
            "1": {
                "neurotechnology": random.choice(neurotechnologies),
                "societal_domain": random.choice(societal_domains),
                "ethical_principle": random.choice(ethical_principles),
                "constraint": random.choice(constraints)
            },
            "2": {
                "neurotechnology": random.choice(neurotechnologies),
                "societal_domain": random.choice(societal_domains),
                "ethical_principle": random.choice(ethical_principles),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical neurotechnology and its potential societal impacts, considering ethical implications and proposing governance frameworks. Use the following specifications:

Neurotechnology: {t['neurotechnology']}
Societal Domain: {t['societal_domain']}
Ethical Principle: {t['ethical_principle']}
Constraint: {t['constraint']}

Your task has the following components:

1. Neurotechnology Design (200-250 words):
   a) Describe the key features and functioning of the specified neurotechnology.
   b) Explain the neuroscientific principles underlying its operation.
   c) Discuss its intended benefits and potential risks.
   d) Incorporate the given constraint into your design and explain its implications.

2. Societal Impact Analysis (200-250 words):
   a) Analyze how the neurotechnology could impact the specified societal domain.
   b) Provide two positive and two negative potential consequences, with at least one example for each that is non-obvious or counterintuitive.
   c) Discuss how these impacts might evolve over time (5, 10, and 20 years).

3. Ethical Implications (200-250 words):
   a) Examine the ethical challenges posed by the neurotechnology, focusing on the specified ethical principle.
   b) Discuss any conflicts between individual benefits and societal concerns.
   c) Propose two methods to address these ethical challenges, explaining their potential effectiveness and limitations.

4. Governance Framework (200-250 words):
   a) Propose a governance framework for regulating the development and use of this neurotechnology.
   b) Include specific roles for government, industry, and civil society in your framework.
   c) Explain how your framework balances innovation with ethical concerns.
   d) Describe at least one potential loophole in your framework and how it might be addressed.

5. Speculative Scenario (150-200 words):
   Describe a specific scenario set 15 years in the future that illustrates a complex ethical dilemma arising from the widespread adoption of this neurotechnology in the specified societal domain. Your scenario should:
   a) Introduce a protagonist facing a difficult decision related to the neurotechnology.
   b) Clearly articulate the ethical dilemma, showing how it relates to the specified ethical principle.
   c) Demonstrate how the societal impact and governance framework you've described influence the situation.

Ensure your response demonstrates a deep understanding of neuroscience, ethics, and policy-making. Be creative in your approach while grounding your ideas in plausible scientific and societal developments. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 950-1150 words. Responses outside this range will be penalized."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience and the specified neurotechnology, incorporating the given constraint effectively.",
            "The societal impact analysis is comprehensive, well-reasoned, and includes non-obvious or counterintuitive examples.",
            "The ethical implications are thoroughly examined, with a clear focus on the specified ethical principle and proposed methods to address challenges.",
            "The proposed governance framework is well-structured, addresses key concerns, and identifies potential loopholes.",
            "The speculative scenario is creative, plausible, and effectively illustrates a complex ethical dilemma with a clear protagonist and decision point.",
            "The response is well-organized, coherent, and adheres to the specified word limits for each section and overall."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
