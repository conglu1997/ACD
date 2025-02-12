import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                'domain': 'financial markets',
                'quantum_principle': 'superposition',
                'cognitive_aspect': 'decision-making under uncertainty',
                'example_problem': 'predicting stock market crashes'
            },
            {
                'domain': 'drug discovery',
                'quantum_principle': 'entanglement',
                'cognitive_aspect': 'pattern recognition',
                'example_problem': 'identifying potential drug interactions'
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates principles of quantum mechanics into cognitive science and artificial intelligence to solve complex decision-making problems. Your framework should focus on the domain of {t['domain']}, incorporate the quantum principle of {t['quantum_principle']}, and address the cognitive aspect of {t['cognitive_aspect']}. Use the example problem of {t['example_problem']} to illustrate your framework's application.

Your response should include:

1. Framework Overview (250-300 words):
   a) Describe the key components of your quantum cognitive AI framework.
   b) Explain how it integrates quantum mechanics, cognitive science, and AI.
   c) Discuss how the framework specifically addresses the given domain, quantum principle, and cognitive aspect.

2. Quantum-Cognitive Integration (200-250 words):
   a) Explain how the specified quantum principle is applied to model cognitive processes.
   b) Describe how this integration enhances traditional cognitive models or AI approaches.
   c) Provide a mathematical or conceptual representation of this integration (use LaTeX formatting for equations).

3. AI Implementation (200-250 words):
   a) Outline how your framework would be implemented in an AI system.
   b) Describe the data structures and algorithms that would be used.
   c) Explain how the AI system would process information and make decisions using this framework.

4. Problem-Solving Approach (200-250 words):
   a) Describe how your framework would approach the given example problem.
   b) Explain the step-by-step process of how the framework would analyze and solve the problem.
   c) Discuss how this approach differs from traditional methods.

5. Theoretical Implications (150-200 words):
   a) Analyze the theoretical implications of your framework for our understanding of cognition and AI.
   b) Discuss how it challenges or extends current theories in cognitive science and AI.
   c) Propose testable hypotheses derived from your framework.

6. Practical Applications and Limitations (150-200 words):
   a) Suggest potential real-world applications of your framework beyond the given domain.
   b) Discuss the technical and conceptual challenges in implementing this framework.
   c) Describe the limitations of your approach and areas for future development.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and logical consistency.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The framework successfully integrates the quantum principle of {t['quantum_principle']} with cognitive processes related to {t['cognitive_aspect']} in the domain of {t['domain']}.",
            f"The response adequately addresses the example problem of {t['example_problem']} using the proposed framework.",
            "The proposed framework demonstrates innovative thinking and a deep understanding of quantum mechanics, cognitive science, and AI.",
            "The mathematical or conceptual representation of the quantum-cognitive integration is clear and well-explained.",
            "The AI implementation section provides a plausible approach for realizing the framework computationally.",
            "The theoretical implications and practical applications are well-reasoned and demonstrate an understanding of the field's current state.",
            "The response adheres to the specified format and word count requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
