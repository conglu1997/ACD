import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            'quantum tunneling',
            'quantum entanglement',
            'quantum superposition',
            'quantum coherence',
            'quantum measurement'
        ]
        cellular_components = [
            'mitochondria',
            'ribosomes',
            'cell membrane',
            'nucleus',
            'endoplasmic reticulum'
        ]
        systems_biology_problems = [
            'metabolic flux analysis',
            'gene regulatory network inference',
            'protein-protein interaction prediction',
            'cellular signaling pathway modeling',
            'multi-scale biological system simulation'
        ]
        return {
            '1': {
                'quantum_effect': random.choice(quantum_effects),
                'cellular_component': random.choice(cellular_components),
                'problem': random.choice(systems_biology_problems)
            },
            '2': {
                'quantum_effect': random.choice(quantum_effects),
                'cellular_component': random.choice(cellular_components),
                'problem': random.choice(systems_biology_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum cellular computation system that leverages {t['quantum_effect']} within {t['cellular_component']} to perform complex computations, then apply it to solve the systems biology problem of {t['problem']}. Your response should include:

1. Quantum Cellular Computation System Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum cellular computation system.
   b) Explain how {t['quantum_effect']} is utilized within {t['cellular_component']} for computation.
   c) Discuss how your system interfaces with other cellular processes and maintains quantum effects in a biological environment.
   d) Provide a hypothetical scenario demonstrating how your system would operate within a cell.

2. Quantum-Biological Information Processing (250-300 words):
   a) Explain how information is encoded, processed, and read out in your quantum cellular system.
   b) Describe the basic computational operations your system can perform.
   c) Discuss how your system achieves advantages over classical cellular processes or traditional computing.
   d) Provide a concrete example of a simple computation performed by your system.

3. Application to {t['problem']} (250-300 words):
   a) Describe how you would apply your quantum cellular computation system to address the problem of {t['problem']}.
   b) Explain the specific algorithms or processes your system would use for this application.
   c) Discuss any advantages your approach might have over classical computational methods for this problem.
   d) Provide a hypothetical case study demonstrating the application of your system to this problem.

4. Challenges and Limitations (150-200 words):
   a) Identify at least three major challenges in implementing your quantum cellular computation system.
   b) Discuss any limitations of your approach compared to classical cellular processes or traditional computing methods.
   c) Propose potential solutions or future research directions to address these challenges.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to using quantum effects in living cells for computation.
   b) Explore the broader societal implications of quantum cellular computation technology.
   c) Propose guidelines for the responsible development and use of such systems.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how your quantum cellular computation system integrates principles from quantum physics, molecular biology, and information theory.
   b) Discuss potential applications of your system in fields other than systems biology.
   c) Propose a future research direction that combines insights from your system with another scientific discipline.

Ensure your response demonstrates a deep understanding of quantum physics, molecular biology, and information theory. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Provide concrete examples or hypothetical scenarios to illustrate your ideas.

Format your response with clear headings for each section. Adhere strictly to the word count limits provided for each section. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['quantum_effect']} and its potential for computation within {t['cellular_component']}, providing concrete examples or scenarios.",
            "The quantum cellular computation system design is innovative, scientifically plausible, and well-explained, with a clear hypothetical scenario of its operation.",
            f"The application to {t['problem']} is clearly described with a specific case study, demonstrating potential advantages over traditional methods.",
            "The response addresses challenges, limitations, and ethical implications thoughtfully, proposing realistic solutions or research directions.",
            "The interdisciplinary connections are well-explored, demonstrating a broad understanding of quantum physics, molecular biology, and information theory, with innovative cross-disciplinary applications proposed.",
            "The response is well-structured, adheres to the specified word count for each section, and provides concrete examples throughout."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
