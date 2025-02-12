import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_principles = [
            "Utilitarianism",
            "Deontology",
            "Virtue Ethics",
            "Care Ethics",
            "Social Contract Theory"
        ]
        scenarios = [
            "Autonomous vehicles and accident decision-making",
            "AI-driven resource allocation in healthcare",
            "Privacy vs. security in digital surveillance",
            "Genetic engineering and human enhancement",
            "Environmental policy and intergenerational justice"
        ]
        tasks = [
            {
                'principle': random.choice(ethical_principles),
                'scenario': random.choice(scenarios)
            },
            {
                'principle': random.choice(ethical_principles),
                'scenario': random.choice(scenarios)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel ethical framework inspired by {t['principle']} and apply it to the scenario of {t['scenario']}. Your response should include:

1. Ethical Framework Design (300-350 words):
   a) Outline the key principles and concepts of your novel ethical framework.
   b) Explain how it draws inspiration from {t['principle']} while introducing new elements.
   c) Discuss how your framework addresses potential limitations or criticisms of {t['principle']}.
   d) Provide a name for your ethical framework and explain its significance.

2. Framework Application (250-300 words):
   a) Apply your ethical framework to the scenario of {t['scenario']}.
   b) Identify the key ethical issues and stakeholders involved in this scenario.
   c) Explain how your framework would guide decision-making in this context.
   d) Discuss any potential conflicts or dilemmas that arise when applying your framework.

3. Comparative Analysis (200-250 words):
   a) Compare your framework's approach to this scenario with that of traditional {t['principle']}.
   b) Identify at least two other ethical theories and briefly contrast their potential approaches.
   c) Argue for the advantages of your framework in addressing this specific scenario.

4. Practical Implementation (150-200 words):
   a) Propose guidelines or a decision-making process based on your framework for addressing {t['scenario']}.
   b) Discuss potential challenges in implementing your framework in real-world situations.
   c) Suggest ways to measure the effectiveness and outcomes of applying your framework.

5. Critique and Reflection (150-200 words):
   a) Identify potential weaknesses or limitations of your ethical framework.
   b) Discuss how your framework might evolve or be refined based on its application to this scenario.
   c) Reflect on the implications of your framework for broader ethical discourse and decision-making.

Ensure your response demonstrates a deep understanding of ethical theories, creative philosophical thinking, and the ability to apply abstract concepts to concrete scenarios. Use clear, precise language and provide examples where appropriate to illustrate your points.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of ethical theories and philosophical concepts.",
            "The proposed ethical framework is novel, well-defined, and coherently draws inspiration from the given ethical principle.",
            "The application of the framework to the given scenario is thorough, addressing key ethical issues and stakeholders.",
            "The comparative analysis shows critical thinking and a nuanced understanding of different ethical approaches.",
            "The practical implementation guidelines are clear, realistic, and demonstrate an understanding of real-world challenges.",
            "The critique and reflection section shows self-awareness and the ability to identify potential weaknesses in the proposed framework.",
            "The overall response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
