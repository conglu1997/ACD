import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Wave function collapse"
        ]
        neuro_concepts = [
            "Neural plasticity",
            "Default mode network",
            "Predictive coding",
            "Neurogenesis"
        ]
        ethical_domains = [
            "Medical ethics",
            "Environmental ethics",
            "AI ethics",
            "Social justice"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "neuro_concept": random.choice(neuro_concepts),
                "ethical_domain": random.choice(ethical_domains)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "neuro_concept": random.choice(neuro_concepts),
                "ethical_domain": random.choice(ethical_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates the quantum mechanics principle of {t['quantum_principle']} with the neuroscientific concept of {t['neuro_concept']} to analyze and resolve complex ethical dilemmas in the domain of {t['ethical_domain']}. Then, apply your framework to a specific ethical scenario. Provide your response in the following format:

1. Quantum-Neuro-Ethical Framework (300-350 words):
   a) Explain how you integrate the specified quantum principle and neuroscientific concept.
   b) Describe the key components of your framework and their interactions.
   c) Discuss how this integration provides new insights into ethical decision-making.
   d) Include a visual representation (described in text) of your framework's structure or a key process.

2. Ethical Analysis Method (250-300 words):
   a) Outline the steps involved in applying your framework to an ethical dilemma.
   b) Explain how quantum and neural concepts inform each step of the analysis.
   c) Describe any novel decision-making tools or processes emerging from your framework.

3. Scenario Application (300-350 words):
   a) Present a specific ethical dilemma relevant to the given ethical domain.
   b) Apply your quantum-neuro-ethical framework to analyze this scenario.
   c) Explain how the integration of quantum and neural concepts leads to novel ethical insights or solutions.
   d) Discuss any limitations or challenges in applying your framework to this scenario.

4. Implications and Predictions (200-250 words):
   a) Discuss the broader implications of your framework for ethics and decision-making.
   b) Propose two testable predictions about human behavior or decision-making that arise from your framework.
   c) Explain how these predictions differ from those of classical ethical theories.

5. Philosophical and Scientific Considerations (200-250 words):
   a) Examine how your framework challenges or extends current understanding in ethics, neuroscience, or quantum physics.
   b) Discuss potential criticisms of your approach from philosophical and scientific perspectives.
   c) Propose future research directions to validate or refine your framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, and ethical theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and philosophical rigor.

Format your response with clear headings for each section. Your total response should be between 1250-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must integrate the quantum principle of {t['quantum_principle']} with the neuroscientific concept of {t['neuro_concept']}.",
            f"The framework should be applied to resolve ethical dilemmas in the domain of {t['ethical_domain']}.",
            "The response must include all five required sections: Quantum-Neuro-Ethical Framework, Ethical Analysis Method, Scenario Application, Implications and Predictions, and Philosophical and Scientific Considerations.",
            "The framework should demonstrate a novel and coherent integration of quantum mechanics, neuroscience, and ethics.",
            "The scenario application should show a clear and logical use of the framework to analyze a relevant ethical dilemma.",
            "The response should include testable predictions and discuss broader implications of the framework.",
            "The answer should demonstrate a deep understanding of quantum mechanics, neuroscience, and ethical theory, using appropriate terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
