import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanets = [
            'Super-Earth with dense atmosphere',
            'Gas giant with complex cloud structures',
            'Ocean world with subsurface liquid water',
            'Tidally locked planet with permanent day-night divide',
            'Rocky planet with extreme volcanic activity'
        ]
        biosignatures = [
            'Methane and oxygen disequilibrium',
            'Seasonal variations in atmospheric composition',
            'Presence of complex organic molecules',
            'Unusual infrared absorption patterns',
            'Circadian rhythm-like fluctuations in atmospheric properties'
        ]
        quantum_techniques = [
            'Quantum Fourier Transform',
            'Quantum Phase Estimation',
            'Quantum Principal Component Analysis',
            'Quantum Support Vector Machines',
            'Quantum Annealing'
        ]
        tasks = [
            {
                'exoplanet': random.choice(exoplanets),
                'biosignature': random.choice(biosignatures),
                'quantum_technique': random.choice(quantum_techniques)
            },
            {
                'exoplanet': random.choice(exoplanets),
                'biosignature': random.choice(biosignatures),
                'quantum_technique': random.choice(quantum_techniques)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum computing system to decode potential biosignatures in exoplanet atmospheres, then analyze its implications for astrobiology and quantum information theory. Your system should focus on a {t['exoplanet']} and aim to detect the biosignature of {t['biosignature']}. Incorporate the quantum computing technique of {t['quantum_technique']} in your design.

Provide your response in the following format:

1. Quantum Biosignature Decoder Design (300-350 words):
   a) Describe the key components and architecture of your quantum computing system.
   b) Explain how your system utilizes {t['quantum_technique']} to analyze atmospheric data.
   c) Detail how your system is optimized to detect {t['biosignature']} on a {t['exoplanet']}.
   d) Provide a high-level quantum circuit or algorithm description for a critical part of your system.

2. Astrobiology Implications (250-300 words):
   a) Discuss how your quantum system could advance our understanding of potential life on {t['exoplanet']}s.
   b) Analyze the significance of detecting {t['biosignature']} in the context of astrobiology.
   c) Explore potential alternative explanations for the detected biosignature and how your system might distinguish between them.

3. Quantum Information Theory Advancements (250-300 words):
   a) Explain how your system pushes the boundaries of current quantum information theory.
   b) Discuss any novel quantum effects or principles your system exploits.
   c) Analyze the theoretical advantages of your quantum approach over classical methods for biosignature detection.

4. Technical Challenges and Solutions (200-250 words):
   a) Identify the main technical challenges in implementing your quantum biosignature decoder.
   b) Propose innovative solutions or research directions to address these challenges.
   c) Discuss any potential limitations of your approach and how they might be mitigated.

5. Ethical Implications and Future Directions (150-200 words):
   a) Discuss the ethical considerations of using advanced quantum systems in the search for extraterrestrial life.
   b) Explore potential societal impacts of confirming the existence of biosignatures on exoplanets.
   c) Suggest future research directions or applications stemming from your quantum biosignature decoder.

Ensure your response demonstrates a deep understanding of quantum computing, astrobiology, and information theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum computing, astrobiology, and information theory, particularly in relation to {t['quantum_technique']}, {t['biosignature']}, and {t['exoplanet']}s.",
            "The quantum biosignature decoder design is innovative, scientifically plausible, and effectively incorporates the specified quantum technique.",
            "The analysis of astrobiology implications is insightful and considers both the potential significance and alternative explanations for the biosignature.",
            "The discussion of quantum information theory advancements is well-reasoned and identifies novel applications or extensions of current theory.",
            "The technical challenges and proposed solutions are realistic and demonstrate a strong grasp of the practical aspects of quantum computing and exoplanet research.",
            "The ethical implications and future directions are thoughtfully considered and show an understanding of the broader impacts of this technology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
