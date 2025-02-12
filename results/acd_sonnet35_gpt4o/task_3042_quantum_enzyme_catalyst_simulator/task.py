import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        enzymes = [
            {
                'name': 'alcohol dehydrogenase',
                'reaction': 'ethanol to acetaldehyde',
                'cofactor': 'NAD+'
            },
            {
                'name': 'soybean lipoxygenase',
                'reaction': 'linoleic acid to hydroperoxide',
                'cofactor': 'iron'
            }
        ]
        return {str(i+1): enzyme for i, enzyme in enumerate(random.sample(enzymes, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing simulation system to model and optimize the catalytic activity of {t['name']} in the {t['reaction']} reaction, focusing on the role of quantum tunneling in hydrogen transfer. Your system should incorporate the {t['cofactor']} cofactor. Provide a detailed response covering the following aspects:

1. Quantum System Architecture (300-350 words):
   a) Describe the key components of your quantum computing system for enzyme catalysis simulation.
   b) Explain how your system models quantum tunneling in the context of hydrogen transfer.
   c) Detail how you incorporate the enzyme's active site and {t['cofactor']} cofactor into your quantum model.
   d) Discuss any hybrid quantum-classical approaches your system employs.

2. Quantum Algorithm Design (250-300 words):
   a) Outline the quantum algorithm(s) your system uses to simulate enzyme catalysis.
   b) Explain how these algorithms account for quantum effects in biological systems.
   c) Describe how your algorithm handles the interplay between quantum and classical phenomena in enzyme function.
   d) Include a brief pseudocode or mathematical formulation of a key part of your quantum algorithm.

3. Enzyme Modeling and Optimization (200-250 words):
   a) Explain how your system models the structure and function of {t['name']}.
   b) Describe how quantum tunneling is incorporated into the catalytic mechanism for the {t['reaction']} reaction.
   c) Discuss your approach to optimizing enzyme activity using quantum simulation.

4. Data Integration and Analysis (200-250 words):
   a) Explain how your system integrates experimental data on enzyme kinetics and structure.
   b) Describe any machine learning techniques used to enhance your quantum simulations.
   c) Discuss how your system handles the interface between quantum simulation results and classical biochemical analysis.

5. Simulation Process and Output (200-250 words):
   a) Detail the step-by-step process of how your system simulates enzyme catalysis.
   b) Explain how the system generates and evaluates potential optimizations.
   c) Describe the output format and how it can be interpreted by biochemists and enzyme engineers.

6. Comparative Analysis (150-200 words):
   a) Compare your quantum approach to traditional methods of studying enzyme catalysis.
   b) Provide a quantitative estimate of the potential improvements in understanding or optimizing enzyme function.
   c) Discuss any trade-offs or potential drawbacks of using quantum computing for this application.

7. Future Directions and Implications (150-200 words):
   a) Propose potential improvements or expansions to your system.
   b) Discuss the broader implications of your approach for the field of quantum biology.
   c) Consider potential applications in drug discovery, biocatalysis, or other areas of biotechnology.

Ensure your response demonstrates a deep understanding of quantum mechanics, enzyme biochemistry, and computational modeling. Use appropriate technical terminology and provide clear explanations where necessary. Be innovative in your approach while maintaining scientific plausibility and practical considerations.

Format your response using clear headings for each section and subsections labeled a, b, c, d as appropriate. Your total response should be between 1450-1800 words. Responses significantly outside this range may be penalized in scoring."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum mechanics and its application to enzyme catalysis, specifically for {t['name']} in the {t['reaction']} reaction.",
            f"The proposed quantum computing system effectively models quantum tunneling in hydrogen transfer and incorporates the {t['cofactor']} cofactor.",
            "The quantum algorithm design is innovative yet scientifically grounded, with clear explanations of how it handles both quantum and classical aspects of enzyme function.",
            "The approach to enzyme modeling and optimization is well-thought-out and leverages the potential advantages of quantum simulation.",
            "The response shows creative problem-solving and interdisciplinary knowledge integration across quantum physics, biochemistry, and computational modeling.",
            "The response adheres to the specified word count range and formatting requirements."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
