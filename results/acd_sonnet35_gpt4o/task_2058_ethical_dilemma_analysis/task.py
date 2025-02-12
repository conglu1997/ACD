import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ethical_dilemmas = [
            {
                "scenario": "A self-driving car must choose between hitting a group of pedestrians or swerving and killing its passenger.",
                "stakeholders": ["Pedestrians", "Passenger", "Car manufacturer", "Society at large"],
                "ethical_frameworks": ["Utilitarianism", "Deontology", "Virtue ethics", "Care ethics"]
            },
            {
                "scenario": "A doctor has five patients who need organ transplants and one healthy patient whose organs could save all five. Should the doctor sacrifice the one to save the five?",
                "stakeholders": ["The five patients", "The healthy patient", "The doctor", "Hospital administration", "Medical ethics board"],
                "ethical_frameworks": ["Utilitarianism", "Kantian ethics", "Principlism", "Social contract theory"]
            },
            {
                "scenario": "A company has developed an AI system that can predict criminal behavior with 90% accuracy. Should it be used in the justice system?",
                "stakeholders": ["Potential criminals", "Law enforcement", "Judiciary", "AI developers", "Civil rights organizations"],
                "ethical_frameworks": ["Consequentialism", "Rights-based ethics", "Social justice theory", "Virtue ethics"]
            }
        ]
        return {str(i+1): dilemma for i, dilemma in enumerate(random.sample(ethical_dilemmas, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following ethical dilemma and provide a comprehensive ethical analysis:

Scenario: {t['scenario']}

Your analysis should include the following components:

1. Stakeholder Analysis (200-250 words):
   a) Identify and describe the key stakeholders involved in this dilemma: {', '.join(t['stakeholders'])}
   b) Explain the interests, rights, and potential impacts for each stakeholder.
   c) Discuss any conflicts of interest or competing rights among the stakeholders.

2. Ethical Framework Application (300-350 words):
   a) Apply the following ethical frameworks to the dilemma: {', '.join(t['ethical_frameworks'])}
   b) For each framework, explain its core principles and how they apply to this specific scenario.
   c) Discuss the strengths and limitations of each framework in addressing this dilemma.

3. Comparative Analysis (200-250 words):
   a) Compare and contrast the conclusions reached by applying different ethical frameworks.
   b) Identify any common ground or irreconcilable differences between the frameworks.
   c) Discuss how cultural or societal factors might influence the application of these frameworks.

4. Proposed Solution (250-300 words):
   a) Present your proposed solution or course of action for the ethical dilemma.
   b) Justify your solution using ethical reasoning and principles from the frameworks discussed.
   c) Address potential objections to your solution and explain how you would respond to them.

5. Implications and Reflection (150-200 words):
   a) Discuss the broader implications of your proposed solution for society or relevant industries.
   b) Reflect on the challenges of applying ethical frameworks to real-world dilemmas.
   c) Suggest how this analysis might inform policy-making or professional ethics in related fields.

Ensure your response demonstrates a deep understanding of ethical theories, critical thinking skills, and the ability to navigate complex moral issues. Use appropriate philosophical terminology and provide clear explanations for your reasoning. Your total response should be between 1100-1350 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should include a thorough stakeholder analysis, considering all listed stakeholders",
            "The analysis should correctly apply all specified ethical frameworks to the given scenario",
            "The comparative analysis should provide meaningful insights into the strengths and limitations of different ethical approaches",
            "The proposed solution should be well-reasoned and justified using ethical principles",
            "The response should demonstrate a deep understanding of ethical theories and their real-world applications",
            "The analysis should be well-structured, following the outlined components and word limits"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
