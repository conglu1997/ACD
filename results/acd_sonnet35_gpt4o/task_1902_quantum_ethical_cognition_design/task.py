import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "ethical_framework": "Utilitarianism",
                "application_domain": "Healthcare resource allocation"
            },
            {
                "quantum_principle": "Entanglement",
                "ethical_framework": "Deontological ethics",
                "application_domain": "Autonomous weapon systems"
            },
            {
                "quantum_principle": "Quantum tunneling",
                "ethical_framework": "Virtue ethics",
                "application_domain": "Environmental policy decisions"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing architecture for ethical decision-making, incorporating the quantum principle of {t['quantum_principle']}, based on the ethical framework of {t['ethical_framework']}, and applied to the domain of {t['application_domain']}. Your response should include:

1. Quantum-Ethical Architecture (250-300 words):
   a) Describe the key components of your quantum computing architecture for ethical decision-making.
   b) Explain how you incorporate the specified quantum principle into your design.
   c) Detail how your architecture implements the given ethical framework.
   d) Discuss how your design is tailored to the specified application domain.

2. Quantum-Ethical Integration (200-250 words):
   a) Explain how the quantum principle enhances or modifies the ethical decision-making process.
   b) Describe any novel ethical considerations that arise from the integration of quantum principles.
   c) Provide a conceptual or mathematical representation of how quantum states could represent ethical choices.

3. Potential Societal Impacts (200-250 words):
   a) Analyze the potential benefits of your quantum-ethical system for society.
   b) Discuss possible risks or unintended consequences of implementing such a system.
   c) Consider how this technology might influence human decision-making and moral reasoning.

4. Experimental Design (200-250 words):
   a) Propose an experiment to test the efficacy of your quantum-ethical decision-making system.
   b) Describe the methodology, including how you would measure ethical outcomes.
   c) Discuss potential challenges in evaluating a quantum system for ethical decision-making.

5. Comparative Analysis (150-200 words):
   a) Compare your quantum-ethical approach to traditional computational methods for ethical reasoning.
   b) Discuss the scalability and adaptability of your system to other ethical frameworks or application domains.
   c) Speculate on how this technology might evolve in the next 20-30 years.

Ensure your response demonstrates a deep understanding of quantum computing principles, ethical philosophy, and the specified application domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should incorporate the quantum principle of {t['quantum_principle']}",
            f"The ethical framework of {t['ethical_framework']} should be correctly implemented",
            f"The design should be appropriately tailored to the domain of {t['application_domain']}",
            "The quantum-ethical integration should be logically explained",
            "The potential societal impacts should be thoroughly analyzed",
            "The experimental design should be well-thought-out and feasible",
            "The comparative analysis should demonstrate deep understanding of both quantum and traditional approaches"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
