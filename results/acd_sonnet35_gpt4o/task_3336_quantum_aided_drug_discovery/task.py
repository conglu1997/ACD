import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "target": "BRCA1 gene mutations",
                "constraint": "Minimize off-target effects",
                "quantum_concept": "Quantum annealing",
                "genetic_factor": "Single Nucleotide Polymorphisms (SNPs)"
            },
            {
                "target": "Tau protein misfolding",
                "constraint": "Optimize blood-brain barrier penetration",
                "quantum_concept": "Quantum tunneling",
                "genetic_factor": "Copy Number Variations (CNVs)"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing system to simulate and optimize drug-protein interactions for personalized medicine, focusing on {t['target']} and considering the constraint to {t['constraint']}. Your system should incorporate the quantum concept of {t['quantum_concept']} and account for the genetic factor of {t['genetic_factor']}. Your response should include:

1. Quantum System Architecture (300-350 words):
   a) Describe the key components of your quantum computing system for drug discovery.
   b) Explain how it leverages {t['quantum_concept']} for molecular simulations.
   c) Detail how your system integrates classical and quantum computing elements.
   d) Discuss any novel quantum algorithms or techniques used in your design.

2. Molecular Modeling Approach (250-300 words):
   a) Explain how your system models drug-protein interactions at the quantum level.
   b) Describe how it accounts for {t['genetic_factor']} in personalized drug design.
   c) Discuss how your approach addresses the constraint to {t['constraint']}.
   d) Provide an example of how your system would simulate a specific drug-protein interaction.

3. Optimization Strategy (200-250 words):
   a) Detail your system's strategy for optimizing drug candidates.
   b) Explain how quantum and classical optimization techniques are combined.
   c) Describe how your system balances multiple objectives (e.g., efficacy, safety, {t['constraint']}).
   d) Discuss the role of machine learning or AI in your optimization process.

4. Personalization Framework (200-250 words):
   a) Explain how your system incorporates individual genetic data for personalized drug design.
   b) Describe the process of adapting drug candidates based on {t['genetic_factor']}.
   c) Discuss how environmental factors are considered in your personalization approach.
   d) Provide an example scenario demonstrating your system's personalization capabilities.

5. Performance Analysis (150-200 words):
   a) Propose metrics to evaluate the performance of your quantum-aided drug discovery system.
   b) Compare the expected performance of your system to classical drug discovery methods.
   c) Discuss potential speedup or accuracy improvements offered by your quantum approach.

6. Ethical and Practical Considerations (150-200 words):
   a) Discuss ethical implications of using quantum computing and genetic data in drug discovery.
   b) Address potential challenges in implementing your system with current technology.
   c) Propose guidelines for responsible development and use of quantum-aided personalized medicine.

7. Future Directions (100-150 words):
   a) Suggest two potential extensions or improvements to your system.
   b) Discuss how these extensions could enhance its capabilities or address limitations.

8. Code Snippet (50-100 words of explanation + code):
   Provide a small Python code snippet (10-20 lines) that demonstrates a key aspect of your quantum system, such as quantum state preparation or measurement. Briefly explain what the code does and how it relates to your overall system design.

Ensure your response demonstrates a deep understanding of quantum computing, biochemistry, and genetics. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1450-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must address the target of {t['target']} and the constraint to {t['constraint']}.",
            f"The proposed system must incorporate the quantum concept of {t['quantum_concept']} in a meaningful and scientifically plausible way.",
            f"The system must account for the genetic factor of {t['genetic_factor']} in its personalized approach.",
            "The submission must include all eight required elements as specified in the instructions, with each section adequately addressing its respective topics.",
            "The proposed quantum-aided drug discovery system must be logically coherent and demonstrate a clear understanding of how quantum computing, biochemistry, and genetics work together.",
            "The response must be creative and propose novel ideas while remaining grounded in scientific principles from the relevant fields.",
            "The performance analysis and ethical considerations must be thoughtful and demonstrate an understanding of the broader implications of the proposed system.",
            "The code snippet must be relevant to the proposed quantum system and demonstrate a basic understanding of quantum computing principles.",
            "The response must show a clear integration of quantum concepts with biochemistry and genetics, explaining how quantum effects are leveraged for drug discovery and personalized medicine."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
