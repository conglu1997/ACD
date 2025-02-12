import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            "Superposition",
            "Entanglement",
            "Quantum tunneling",
            "Wave-particle duality"
        ]
        ethical_frameworks = [
            "Utilitarianism",
            "Deontological ethics",
            "Virtue ethics",
            "Care ethics"
        ]
        ai_techniques = [
            "Neural networks",
            "Reinforcement learning",
            "Bayesian inference",
            "Genetic algorithms"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "ethical_framework": random.choice(ethical_frameworks),
                "ai_technique": random.choice(ai_techniques)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "ethical_framework": random.choice(ethical_frameworks),
                "ai_technique": random.choice(ai_techniques)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system for ethical decision-making, incorporating the quantum principle of {t['quantum_principle']}, the ethical framework of {t['ethical_framework']}, and the AI technique of {t['ai_technique']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your quantum-inspired AI system.
   b) Explain how {t['quantum_principle']} is integrated into the system's design.
   c) Detail how {t['ai_technique']} is utilized in the decision-making process.
   d) Discuss how the system incorporates {t['ethical_framework']} in its ethical reasoning.

2. Quantum-Ethical Integration (200-250 words):
   a) Explain how {t['quantum_principle']} enhances or modifies ethical decision-making.
   b) Discuss any novel ethical insights or capabilities that emerge from this integration.
   c) Address potential challenges or limitations in combining quantum principles with ethics.

3. Decision-Making Process (200-250 words):
   a) Provide a step-by-step explanation of how your system would approach an ethical dilemma.
   b) Illustrate with a specific example scenario related to {t['ethical_framework']}.
   c) Explain how quantum effects influence the decision-making process.

4. Philosophical Implications (150-200 words):
   a) Analyze how your system might impact or challenge traditional moral philosophy.
   b) Discuss potential new ethical paradigms that could emerge from quantum-inspired AI ethics.
   c) Address any metaphysical implications of applying quantum principles to ethics.

5. Experimental Design (200-250 words):
   a) Propose an experiment to test the effectiveness of your quantum-inspired ethical AI system.
   b) Describe the methodology, including control groups and variables to be measured.
   c) Discuss potential challenges in empirically evaluating ethical decision-making.
   d) Explain how you would account for quantum effects in your experimental design.

Ensure your response demonstrates a deep understanding of quantum mechanics, artificial intelligence, and ethical philosophy. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and philosophical rigor.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of {t['quantum_principle']} and how it can be applied to AI and ethics.",
            f"The system architecture effectively integrates {t['ai_technique']} with quantum-inspired elements.",
            f"The ethical decision-making process clearly incorporates principles from {t['ethical_framework']}.",
            "The response includes a thoughtful analysis of philosophical implications and potential new ethical paradigms.",
            "The proposed experiment is well-designed and addresses the challenges of testing quantum-inspired ethical AI."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
