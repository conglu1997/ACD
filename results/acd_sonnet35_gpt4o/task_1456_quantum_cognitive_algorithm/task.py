import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            'Working memory',
            'Attention allocation',
            'Pattern recognition',
            'Decision making',
            'Cognitive control'
        ]
        quantum_concepts = [
            'Superposition',
            'Entanglement',
            'Quantum tunneling',
            'Quantum annealing',
            'Quantum error correction'
        ]
        tasks = [
            {
                'cognitive_process': random.choice(cognitive_processes),
                'quantum_concept': random.choice(quantum_concepts)
            },
            {
                'cognitive_process': random.choice(cognitive_processes),
                'quantum_concept': random.choice(quantum_concepts)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing algorithm inspired by the cognitive process of {t['cognitive_process']}, incorporating the quantum concept of {t['quantum_concept']}. Then, analyze its potential applications and implications for both quantum computing and cognitive science. Your response should include the following sections:

1. Algorithm Design (300-350 words):
   a) Describe the key features of your quantum algorithm and how it mimics or is inspired by {t['cognitive_process']}.
   b) Explain how you've incorporated {t['quantum_concept']} into your algorithm.
   c) Provide a high-level description or pseudocode of your algorithm's steps.
   d) Discuss any novel quantum gates or operations you've designed for this algorithm.

2. Quantum Advantage (200-250 words):
   a) Analyze the potential advantages of your quantum algorithm over classical approaches.
   b) Discuss the expected computational complexity and how it compares to classical algorithms for similar tasks.
   c) Explain any limitations or challenges in implementing your algorithm on current or near-term quantum hardware.

3. Cognitive Science Insights (200-250 words):
   a) Discuss how your algorithm might provide new insights into the cognitive process of {t['cognitive_process']}.
   b) Explain how the quantum nature of the algorithm might reflect or challenge current understanding of cognitive processes.
   c) Propose an experiment that could test whether human cognition exhibits quantum-like properties similar to your algorithm.

4. Practical Applications (150-200 words):
   a) Suggest potential real-world applications of your quantum cognitive algorithm.
   b) Discuss how these applications might impact fields such as artificial intelligence, neuroscience, or cognitive psychology.
   c) Consider any ethical implications of using quantum-inspired cognitive models.

5. Future Directions (150-200 words):
   a) Propose extensions or modifications to your algorithm to address other cognitive processes.
   b) Discuss how advancements in quantum hardware might enhance the capabilities of your algorithm.
   c) Suggest areas of future research at the intersection of quantum computing and cognitive science inspired by your work.

Ensure your response demonstrates a deep understanding of both quantum computing and cognitive science principles. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology from both fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1000-1250 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of both {t['cognitive_process']} and {t['quantum_concept']}.",
            "The quantum algorithm design is creative, innovative, and scientifically plausible.",
            "The analysis of quantum advantage is well-reasoned and considers both benefits and limitations.",
            "The discussion of cognitive science insights is thought-provoking and grounded in current understanding.",
            "The proposed practical applications and future directions are innovative and demonstrate interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
