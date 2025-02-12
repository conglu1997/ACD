import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'quantum_principle': 'Superposition',
                'cryptographic_goal': 'Secure key distribution',
                'ethical_consideration': 'Privacy in quantum networks'
            },
            {
                'quantum_principle': 'Entanglement',
                'cryptographic_goal': 'Quantum teleportation for secure messaging',
                'ethical_consideration': 'Potential for unbreakable government surveillance'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum cryptography puzzle based on the quantum principle of {t['quantum_principle']}, addressing the cryptographic goal of {t['cryptographic_goal']}. Then, analyze its implications and potential real-world applications. Your response should include:

1. Puzzle Design (250-300 words):
   a) Describe the setup and rules of your quantum cryptography puzzle.
   b) Explain how it incorporates the specified quantum principle.
   c) Detail how the puzzle addresses the given cryptographic goal.
   d) Include any necessary mathematical formulas or quantum circuit diagrams.

2. Solution and Analysis (200-250 words):
   a) Provide a step-by-step solution to your puzzle.
   b) Analyze the security of your cryptographic scheme.
   c) Discuss any potential vulnerabilities or limitations.

3. Quantum Advantage (150-200 words):
   a) Explain how your puzzle demonstrates quantum advantage over classical cryptography methods.
   b) Quantify this advantage if possible (e.g., in terms of computational complexity or security guarantees).

4. Real-world Application (200-250 words):
   a) Propose a practical application of your quantum cryptography puzzle.
   b) Describe how it could be implemented using current or near-future quantum technologies.
   c) Discuss any technical challenges that would need to be overcome.

5. Ethical Implications (200-250 words):
   a) Analyze the ethical consideration: {t['ethical_consideration']}.
   b) Discuss potential societal impacts of widespread adoption of your quantum cryptography scheme.
   c) Propose guidelines or policies to address these ethical concerns.

Ensure your response demonstrates a deep understanding of quantum mechanics, cryptography, and information theory. Use appropriate technical terminology and provide clear explanations. Be creative in your puzzle design while maintaining scientific accuracy.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, cryptography, and information theory.",
            "The quantum cryptography puzzle is innovative, scientifically accurate, and properly incorporates the specified quantum principle.",
            "The puzzle effectively addresses the given cryptographic goal.",
            "The solution and security analysis are thorough and well-reasoned.",
            "The explanation of quantum advantage is clear and quantified where possible.",
            "The proposed real-world application is practical and well-described.",
            "The ethical implications analysis is thoughtful and addresses the specified consideration.",
            "The response shows strong integration of knowledge from multiple scientific disciplines.",
            "The response includes creative solutions while maintaining scientific rigor.",
            "The response adheres to the specified word limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
