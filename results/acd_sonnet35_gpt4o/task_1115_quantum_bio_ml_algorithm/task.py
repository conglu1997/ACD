import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_processes = [
            'Photosynthesis',
            'DNA Replication'
        ]
        quantum_effects = [
            'Quantum Coherence',
            'Quantum Entanglement'
        ]
        ml_paradigms = [
            'Supervised Learning',
            'Unsupervised Learning'
        ]
        
        tasks = [
            {
                'biological_process': random.choice(biological_processes),
                'quantum_effect': random.choice(quantum_effects),
                'ml_paradigm': random.choice(ml_paradigms)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired machine learning algorithm based on the biological process of {t['biological_process']}, incorporating the quantum effect of {t['quantum_effect']}, and applying it to the machine learning paradigm of {t['ml_paradigm']}. Then, analyze its potential applications and limitations. Your response should include:

1. Algorithm Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum-inspired algorithm.
   b) Explain how it mimics or draws inspiration from {t['biological_process']}.
   c) Detail how {t['quantum_effect']} is incorporated into the algorithm.
   d) Outline how the algorithm applies to the {t['ml_paradigm']} paradigm.

2. Quantum-Biological Basis (200-250 words):
   a) Explain the relevant quantum effects observed in the chosen biological process.
   b) Discuss how these quantum effects contribute to the efficiency or functionality of the biological process.
   c) Describe how your algorithm leverages these quantum-biological principles.

3. Machine Learning Integration (200-250 words):
   a) Detail how your algorithm implements {t['ml_paradigm']}.
   b) Explain any novel features or advantages your quantum-bio-inspired approach offers over classical machine learning techniques.
   c) Discuss potential challenges in implementing this algorithm on current or near-future quantum computing hardware.

4. Potential Applications (200-250 words):
   a) Propose at least three potential applications for your quantum-bio-inspired machine learning algorithm.
   b) Explain how each application leverages the unique features of your algorithm.
   c) Discuss the potential impact of these applications on their respective fields.

5. Limitations and Ethical Considerations (200-250 words):
   a) Identify at least three potential limitations or drawbacks of your algorithm.
   b) Discuss any ethical concerns that may arise from the development or application of this technology.
   c) Propose guidelines for responsible development and use of quantum-bio-inspired AI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential avenues for further research to enhance or expand your algorithm.
   b) Discuss how advancements in quantum biology might influence the future development of quantum machine learning.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and machine learning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use subheadings where appropriate. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, biology, and machine learning.",
            f"The algorithm design clearly incorporates {t['biological_process']}, {t['quantum_effect']}, and {t['ml_paradigm']}.",
            "The quantum-biological basis is well-explained and scientifically plausible.",
            "The machine learning integration is coherent and innovative.",
            "At least three potential applications are proposed with clear explanations.",
            "Limitations, ethical considerations, and future research directions are thoughtfully discussed.",
            "The response is well-structured, using appropriate technical terminology and clear explanations.",
            "The proposed algorithm and its applications are creative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
