import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        atmospheric_compositions = [
            "hydrogen-rich",
            "oxygen-rich",
            "carbon dioxide-dominated",
            "nitrogen-dominated"
        ]
        evolutionary_pathways = [
            "photosynthesis-based",
            "chemosynthesis-based",
            "alternative biochemistry",
            "silicon-based life"
        ]
        quantum_concepts = [
            "superposition",
            "entanglement",
            "quantum tunneling",
            "quantum annealing"
        ]
        biosignatures = [
            "methane",
            "oxygen",
            "nitrous oxide",
            "phosphine"
        ]
        return {
            "1": {
                "atmosphere": random.choice(atmospheric_compositions),
                "evolution": random.choice(evolutionary_pathways),
                "quantum_concept": random.choice(quantum_concepts),
                "target_biosignature": random.choice(biosignatures)
            },
            "2": {
                "atmosphere": random.choice(atmospheric_compositions),
                "evolution": random.choice(evolutionary_pathways),
                "quantum_concept": random.choice(quantum_concepts),
                "target_biosignature": random.choice(biosignatures)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired genetic algorithm to optimize the search for potential biosignatures in exoplanetary atmospheres. Your algorithm should focus on a {t['atmosphere']} atmosphere, considering a {t['evolution']} evolutionary pathway, and incorporate the quantum concept of {t['quantum_concept']}. Your target biosignature for this task is {t['target_biosignature']}. Your response should include:

1. Algorithm Design (300-350 words):
   a) Describe the overall structure of your quantum-inspired genetic algorithm.
   b) Explain how you incorporate {t['quantum_concept']} into the genetic operations.
   c) Detail how your algorithm represents and evolves potential biosignatures, with a focus on {t['target_biosignature']}.
   d) Discuss how your approach accounts for the {t['atmosphere']} atmosphere and {t['evolution']} evolutionary pathway.

2. Quantum-Classical Integration (250-300 words):
   a) Explain how your algorithm balances quantum and classical computing elements.
   b) Describe any novel quantum operators or techniques used in your design.
   c) Discuss how quantum principles enhance the search for {t['target_biosignature']} compared to classical methods.

3. Fitness Function and Selection (200-250 words):
   a) Define the fitness function used to evaluate potential biosignatures, specifically for {t['target_biosignature']}.
   b) Explain how your algorithm selects and evolves the most promising candidates.
   c) Describe how the fitness function accounts for the {t['atmosphere']} atmosphere and {t['evolution']} evolutionary pathway.

4. Simulation and Analysis (250-300 words):
   a) Outline a hypothetical simulation using your algorithm to search for {t['target_biosignature']}.
   b) Provide example results and explain how they would be interpreted.
   c) Discuss potential challenges or limitations in applying your algorithm to real exoplanetary data.

5. Interdisciplinary Implications (200-250 words):
   a) Analyze how your algorithm contributes to the field of astrobiology.
   b) Discuss potential applications of your approach in other scientific domains.
   c) Propose a follow-up research question that emerges from your algorithm design.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using quantum-inspired algorithms in the search for extraterrestrial life.
   b) Address potential societal impacts of discovering biosignatures through your method.
   c) Propose guidelines for responsible development and use of advanced algorithms in astrobiology.

Ensure your response demonstrates a deep understanding of quantum computing, evolutionary algorithms, astrobiology, and atmospheric chemistry. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above (1. Algorithm Design, 2. Quantum-Classical Integration, etc.). Include subsections labeled a), b), c) as appropriate. Your total response should be between 1350-1650 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, evolutionary algorithms, astrobiology, and atmospheric chemistry.",
            f"The algorithm design effectively incorporates the quantum concept of {t['quantum_concept']} and accounts for the {t['atmosphere']} atmosphere and {t['evolution']} evolutionary pathway.",
            f"The fitness function and selection process are well-defined and specifically tailored for detecting {t['target_biosignature']}.",
            "The simulation and analysis section provides a clear and plausible example of how the algorithm would be applied.",
            "The interdisciplinary implications and ethical considerations are thoroughly explored and demonstrate critical thinking.",
            "The response addresses all required sections with appropriate depth, clarity, and follows the specified format.",
            "The approach is innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
