import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_principles = [
            'Superposition',
            'Entanglement',
            'Quantum Tunneling',
            'Quantum Interference'
        ]
        ethical_frameworks = [
            'Utilitarianism',
            'Deontological Ethics',
            'Virtue Ethics',
            'Care Ethics'
        ]
        ai_applications = [
            'Autonomous Vehicles',
            'Healthcare Diagnosis Systems',
            'Financial Trading Algorithms',
            'Criminal Justice Risk Assessment'
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "ethical_framework": random.choice(ethical_frameworks),
                "ai_application": random.choice(ai_applications)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "ethical_framework": random.choice(ethical_frameworks),
                "ai_application": random.choice(ai_applications)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for quantum-based ethical decision-making in AI systems, integrating principles of quantum computing, philosophy, and artificial intelligence. Your framework should incorporate the quantum principle of {t['quantum_principle']}, the ethical framework of {t['ethical_framework']}, and focus on the AI application of {t['ai_application']}.

Your response should include:

1. Framework Overview (250-300 words):
   a) Describe the key components of your quantum ethical AI framework.
   b) Explain how it integrates quantum computing, ethics, and AI.
   c) Discuss how the framework specifically addresses the given quantum principle, ethical framework, and AI application.

2. Quantum-Ethical Integration (200-250 words):
   a) Explain how the specified quantum principle is applied to model ethical decision-making.
   b) Describe how this integration enhances or challenges traditional ethical frameworks.
   c) Provide a conceptual or mathematical representation of this integration (use LaTeX formatting for equations if needed).

3. AI Implementation (200-250 words):
   a) Outline how your framework would be implemented in an AI system.
   b) Describe the data structures and algorithms that would be used.
   c) Explain how the AI system would process information and make ethical decisions using this framework.

4. Case Study Analysis (200-250 words):
   a) Present a specific ethical dilemma relevant to the given AI application.
   b) Describe how your framework would approach and resolve this dilemma.
   c) Compare this approach to how traditional AI systems might handle the same situation.

5. Philosophical Implications (150-200 words):
   a) Analyze the philosophical implications of your framework for ethics and decision-making.
   b) Discuss how it challenges or extends current theories in ethics and AI.
   c) Propose new questions or areas of inquiry that arise from your framework.

6. Practical Considerations and Limitations (150-200 words):
   a) Discuss the technical and conceptual challenges in implementing this framework.
   b) Address potential societal impacts and ethical concerns of using such a system.
   c) Describe the limitations of your approach and areas for future development.

Ensure your response demonstrates a deep understanding of quantum computing, ethics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively integrates the quantum principle of {t['quantum_principle']}, the ethical framework of {t['ethical_framework']}, and the AI application of {t['ai_application']}.",
            "The framework demonstrates a deep understanding of quantum computing, ethics, and artificial intelligence principles.",
            "The response provides creative and logically consistent solutions to the challenge of quantum-based ethical decision-making in AI.",
            "The case study analysis effectively applies the framework to a relevant ethical dilemma.",
            "The response addresses philosophical implications and practical considerations of the proposed framework."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
