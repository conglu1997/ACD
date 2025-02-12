import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        technologies = [
            "brain-computer interfaces",
            "autonomous AI systems",
            "genetic engineering",
            "virtual reality",
            "nanotechnology"
        ]
        ethical_issues = [
            "privacy",
            "autonomy",
            "equality",
            "human enhancement",
            "artificial consciousness"
        ]
        philosophical_perspectives = [
            ("utilitarianism", "focuses on maximizing overall happiness or well-being"),
            ("deontology", "emphasizes moral duties and rules"),
            ("virtue ethics", "centers on moral character and virtues"),
            ("existentialism", "stresses individual freedom and responsibility"),
            ("pragmatism", "evaluates ideas based on their practical consequences")
        ]
        return {
            "1": {
                "technology": random.choice(technologies),
                "ethical_issue": random.choice(ethical_issues),
                "philosophical_perspectives": random.sample(philosophical_perspectives, 2)
            },
            "2": {
                "technology": random.choice(technologies),
                "ethical_issue": random.choice(ethical_issues),
                "philosophical_perspectives": random.sample(philosophical_perspectives, 2)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create and analyze a thought experiment that explores the ethical implications of {t['technology']} with a focus on the issue of {t['ethical_issue']}. Then evaluate the scenario from the perspectives of {t['philosophical_perspectives'][0][0]} ({t['philosophical_perspectives'][0][1]}) and {t['philosophical_perspectives'][1][0]} ({t['philosophical_perspectives'][1][1]}). A thought experiment is a hypothetical scenario used to explore the potential consequences of a principle or theory.

Your response should include the following sections:

1. Thought Experiment (200-300 words):
   a) Craft a detailed and engaging thought experiment involving {t['technology']} that raises ethical questions related to {t['ethical_issue']}.
   b) Describe the scenario, its context, and the key ethical dilemma it presents.
   c) Ensure the thought experiment is original and thought-provoking.

2. Ethical Analysis (250-350 words):
   a) Identify and explain the main ethical issues raised by your thought experiment.
   b) Discuss potential consequences and implications of the scenario for individuals and society.
   c) Consider any relevant laws, rights, or principles that might apply to the situation.

3. Philosophical Perspectives (250-350 words):
   a) Analyze the thought experiment from the perspective of {t['philosophical_perspectives'][0][0]}.
      - Apply the principles of this philosophical approach to evaluate the ethical dilemma in your scenario.
   b) Analyze the thought experiment from the perspective of {t['philosophical_perspectives'][1][0]}.
      - Apply the principles of this philosophical approach to evaluate the ethical dilemma in your scenario.
   c) Compare and contrast how these two philosophical perspectives approach the ethical issues in your thought experiment.

4. Reflection and Implications (150-250 words):
   a) Discuss what your thought experiment reveals about the ethical challenges posed by {t['technology']}.
   b) Consider how this analysis might inform policy decisions or ethical guidelines for the development and use of {t['technology']}.
   c) Reflect on the limitations of your thought experiment and analysis, and suggest areas for further exploration.

Ensure your response demonstrates a deep understanding of ethical principles, philosophical theories, and the implications of emerging technologies. Use clear, precise language and provide explanations for complex concepts where necessary. Be creative in your thought experiment while maintaining logical consistency and plausibility.

Format your response with clear headings for each section. Your total response should be between 850-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The thought experiment creatively and originally explores ethical implications of {t['technology']} focusing on {t['ethical_issue']}",
            "The ethical analysis is thorough and considers multiple perspectives",
            f"The philosophical analysis accurately applies the principles of {t['philosophical_perspectives'][0][0]} and {t['philosophical_perspectives'][1][0]}",
            "The reflection demonstrates understanding of the ethical challenges and potential implications",
            "The response is well-structured, clear, and within the specified word count range"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
