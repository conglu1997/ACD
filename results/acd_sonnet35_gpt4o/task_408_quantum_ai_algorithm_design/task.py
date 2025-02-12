import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "ai_task": "Reinforcement Learning",
                "quantum_property": "Superposition",
                "constraint": "Limited qubit coherence time"
            },
            {
                "ai_task": "Neural Network Training",
                "quantum_property": "Quantum Entanglement",
                "constraint": "Noisy intermediate-scale quantum (NISQ) devices"
            },
            {
                "ai_task": "Dimensionality Reduction",
                "quantum_property": "Quantum Tunneling",
                "constraint": "Limited quantum circuit depth"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a quantum algorithm to enhance {t['ai_task']} by leveraging the quantum property of {t['quantum_property']}, while considering the constraint of {t['constraint']}. Your response should include:

1. Algorithm Design (250-300 words):
   - Describe the key components and steps of your quantum algorithm.
   - Explain how it integrates with the specified AI task.
   - Detail how it leverages the given quantum property.

2. Quantum Advantage Analysis (200-250 words):
   - Analyze the potential advantages of your quantum approach over classical methods.
   - Discuss any trade-offs or limitations.
   - Provide a theoretical analysis of the algorithm's complexity or performance.

3. Implementation Considerations (200-250 words):
   - Address the given constraint and how your algorithm accounts for it.
   - Discuss any additional technical challenges in implementing your algorithm.
   - Propose potential solutions or mitigation strategies for these challenges.

4. Broader Implications (150-200 words):
   - Discuss how your algorithm might impact the field of AI or quantum computing.
   - Explore potential applications beyond the specified AI task.
   - Consider any ethical implications or potential misuses of the technology.

5. Future Research Directions (100-150 words):
   - Suggest at least two avenues for future research to improve or expand upon your algorithm.
   - Explain the potential impact of these research directions.

Ensure your response demonstrates a deep understanding of both quantum computing and artificial intelligence principles. Be creative in your approach while maintaining scientific and technological plausibility. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the specific AI task of {t['ai_task']}",
            f"The algorithm should clearly leverage the quantum property of {t['quantum_property']}",
            f"The design must consider and address the constraint of {t['constraint']}",
            "The response should demonstrate a deep understanding of both quantum computing and AI principles",
            "The algorithm design should be innovative yet scientifically plausible",
            "The analysis should include a thoughtful discussion of quantum advantages, implementation challenges, and broader implications",
            "The response should be well-structured with clear headings for each section",
            "The total response should be comprehensive, between 900-1150 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
