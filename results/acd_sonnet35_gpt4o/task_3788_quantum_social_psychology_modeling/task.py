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
        social_psych_theories = [
            "Social identity theory",
            "Cognitive dissonance theory",
            "Group polarization",
            "Conformity and obedience"
        ]
        social_phenomena = [
            "Viral information spread",
            "Collective decision-making",
            "Formation of social norms",
            "Emergence of social movements"
        ]
        return {
            "1": {
                "quantum_principle": random.choice(quantum_principles),
                "social_theory": random.choice(social_psych_theories),
                "phenomenon": random.choice(social_phenomena)
            },
            "2": {
                "quantum_principle": random.choice(quantum_principles),
                "social_theory": random.choice(social_psych_theories),
                "phenomenon": random.choice(social_phenomena)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired model of social influence and decision-making that integrates the quantum mechanical principle of {t['quantum_principle']} with the social psychological theory of {t['social_theory']} to analyze the social phenomenon of {t['phenomenon']}. Your response should include the following sections:

1. Theoretical Framework (250-300 words):
   a) Explain the key aspects of the quantum principle {t['quantum_principle']}.
   b) Describe the main tenets of the social psychological theory {t['social_theory']}.
   c) Discuss how these two concepts might be related or analogous in the context of social behavior.

2. Model Design (300-350 words):
   a) Propose a mathematical or conceptual model that integrates the quantum principle and social theory.
   b) Explain how your model represents individual and collective states or behaviors.
   c) Describe how your model simulates or predicts changes in social dynamics.
   d) Include a simple diagram or equation representing your model (using ASCII art or clear textual description).

3. Application to Social Phenomenon (250-300 words):
   a) Apply your quantum-inspired social model to analyze the phenomenon of {t['phenomenon']}.
   b) Provide a specific example or scenario demonstrating how your model works.
   c) Discuss any novel insights or predictions your model generates about this phenomenon.

4. Comparison with Classical Models (200-250 words):
   a) Compare your quantum-inspired model to traditional approaches in social psychology.
   b) Discuss potential advantages and limitations of your approach.
   c) Propose an experiment to test the validity of your model against classical predictions.

5. Ethical Implications and Societal Impact (150-200 words):
   a) Discuss potential ethical concerns arising from applying quantum concepts to social behavior.
   b) Analyze possible societal impacts of using such models in social science or policy-making.
   c) Propose guidelines for responsible development and application of quantum-inspired social models.

6. Future Research Directions (100-150 words):
   a) Suggest two potential extensions or refinements to your model.
   b) Briefly describe how these developments could enhance our understanding of social dynamics.

Ensure your response demonstrates a deep understanding of both quantum mechanics and social psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of the quantum principle {t['quantum_principle']} and the social psychological theory {t['social_theory']}.",
            f"The proposed model should creatively integrate the quantum principle and social theory to analyze {t['phenomenon']}.",
            "The application to the social phenomenon should be well-explained with specific examples or scenarios.",
            "The comparison with classical models should be thoughtful and include a proposed experiment.",
            "Ethical implications and future research directions should be addressed comprehensively.",
            "The overall response should be well-structured, coherent, and demonstrate interdisciplinary knowledge synthesis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
