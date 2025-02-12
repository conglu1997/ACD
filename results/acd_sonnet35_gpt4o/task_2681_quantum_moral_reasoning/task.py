import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            "AI rights",
            "Interplanetary resource allocation",
            "Time travel paradoxes",
            "Genetic enhancement ethics",
            "Quantum consciousness manipulation"
        ]
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Wave function collapse",
            "Quantum interference"
        ]
        ethical_frameworks = [
            "Utilitarianism",
            "Deontology",
            "Virtue ethics",
            "Care ethics",
            "Moral particularism"
        ]
        
        tasks = {
            "1": {
                "scenario": random.choice(scenarios),
                "quantum_principle": random.choice(quantum_principles),
                "ethical_framework": random.choice(ethical_frameworks)
            },
            "2": {
                "scenario": random.choice(scenarios),
                "quantum_principle": random.choice(quantum_principles),
                "ethical_framework": random.choice(ethical_frameworks)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum cognitive model for moral decision-making, then apply it to resolve a complex ethical dilemma. Your task has the following components:

1. Quantum Cognitive Model (300-350 words):
   a) Design a cognitive model that incorporates the quantum principle of {t['quantum_principle']} into moral reasoning processes.
   b) Explain how this quantum principle influences decision-making in your model.
   c) Describe the key components and mechanisms of your model, including how it represents and processes moral information.
   d) Discuss how your model differs from classical cognitive models of moral reasoning.

2. Ethical Framework Integration (200-250 words):
   a) Explain how you integrate the ethical framework of {t['ethical_framework']} into your quantum cognitive model.
   b) Discuss any challenges or synergies between the quantum approach and this ethical framework.
   c) Provide an example of how a simple moral decision might be processed in your model.

3. Scenario Analysis (250-300 words):
   a) Present a complex ethical dilemma related to the scenario: {t['scenario']}.
   b) Apply your quantum cognitive model to analyze this dilemma.
   c) Explain how the quantum nature of your model influences the analysis of the scenario.
   d) Discuss any novel insights or approaches that emerge from using your model.

4. Decision and Justification (200-250 words):
   a) Using your model, propose a resolution to the ethical dilemma.
   b) Justify this decision based on the principles of your quantum cognitive model and the chosen ethical framework.
   c) Discuss how this decision might differ from one reached using a classical moral reasoning approach.

5. Implications and Limitations (150-200 words):
   a) Discuss the broader implications of using quantum cognitive models for moral reasoning.
   b) Address potential criticisms or limitations of your approach.
   c) Suggest areas for further research or refinement of your model.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and ethical philosophy. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining logical consistency and scientific plausibility.

Format your answer with clear headings for each section, numbered as above. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate detail and adheres to the specified word count for each section.",
            f"The quantum cognitive model effectively incorporates the principle of {t['quantum_principle']} and clearly explains its influence on moral reasoning.",
            f"The ethical framework of {t['ethical_framework']} is well-integrated into the quantum cognitive model, with a thoughtful discussion of challenges and synergies.",
            f"The scenario analysis related to {t['scenario']} demonstrates a thorough application of the quantum cognitive model to a complex ethical dilemma.",
            "The proposed resolution to the ethical dilemma is well-justified based on the quantum cognitive model and chosen ethical framework.",
            "The response shows creativity, interdisciplinary knowledge integration, and critical thinking in addressing the implications and limitations of the approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
