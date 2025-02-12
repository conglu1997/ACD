import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "dilemma": "quantum_privacy",
                "stakeholders": ["government", "citizens", "corporations"],
                "quantum_property": "superposition"
            },
            "2": {
                "dilemma": "quantum_resource_allocation",
                "stakeholders": ["scientists", "policymakers", "general_public"],
                "quantum_property": "entanglement"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum game theory model for resolving the ethical dilemma of {t['dilemma']} in a hypothetical quantum-enabled society. Your model should incorporate the quantum property of {t['quantum_property']} and consider the interests of the following stakeholders: {', '.join(t['stakeholders'])}. Your response should include:

1. Dilemma Description (100-150 words):
   a) Explain the ethical dilemma in the context of a quantum-enabled society.
   b) Describe how the specified quantum property relates to or exacerbates the dilemma.

2. Quantum Game Theory Model (250-300 words):
   a) Design a quantum game theory model that represents the ethical dilemma and its potential resolutions.
   b) Explain how your model incorporates the specified quantum property.
   c) Describe the possible strategies or actions available to each stakeholder.
   d) Provide a mathematical formulation of your model, including payoff functions or utility calculations.

3. Ethical Analysis (200-250 words):
   a) Discuss the ethical implications of different outcomes in your model.
   b) Analyze how the quantum nature of the model affects ethical considerations.
   c) Propose a framework for evaluating the ethical acceptability of potential resolutions.

4. Solution and Justification (200-250 words):
   a) Present the optimal solution or equilibrium state according to your model.
   b) Justify why this solution is ethically sound and beneficial for all stakeholders.
   c) Discuss any trade-offs or compromises inherent in your proposed solution.

5. Implementation and Challenges (150-200 words):
   a) Describe how your solution could be implemented in a quantum-enabled society.
   b) Identify potential challenges or obstacles to implementation.
   c) Propose methods to overcome these challenges.

6. Broader Implications (100-150 words):
   a) Discuss how your model and solution might impact other areas of society or ethics.
   b) Speculate on how quantum game theory could be applied to other ethical dilemmas.

Ensure your response demonstrates a deep understanding of quantum mechanics, game theory, and ethical reasoning. Use appropriate scientific and philosophical terminology, and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining logical consistency and plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts",
            "The quantum game theory model incorporates the specified quantum property correctly",
            "The ethical analysis demonstrates a nuanced understanding of the dilemma and stakeholder interests",
            "The proposed solution is logically derived from the model and ethically justified",
            "The response shows creativity and innovation while maintaining scientific and philosophical rigor",
            "The broader implications are insightful and demonstrate interdisciplinary thinking"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
