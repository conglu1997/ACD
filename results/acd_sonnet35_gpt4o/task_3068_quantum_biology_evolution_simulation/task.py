import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            'quantum tunneling',
            'quantum coherence',
            'quantum entanglement',
            'superposition'
        ]
        biological_processes = [
            'photosynthesis',
            'enzyme catalysis',
            'DNA mutation',
            'neural signaling'
        ]
        environmental_factors = [
            'extreme temperature',
            'high radiation',
            'low gravity',
            'high pressure'
        ]
        
        tasks = [
            {
                'quantum_effect': random.choice(quantum_effects),
                'biological_process': random.choice(biological_processes),
                'environmental_factor': random.choice(environmental_factors)
            },
            {
                'quantum_effect': random.choice(quantum_effects),
                'biological_process': random.choice(biological_processes),
                'environmental_factor': random.choice(environmental_factors)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a simulation of evolutionary processes incorporating quantum biological effects, focusing on the role of {t['quantum_effect']} in {t['biological_process']} under conditions of {t['environmental_factor']}. Your response should include:

1. Simulation Design (300-350 words):
   a) Describe the key components and mechanisms of your quantum biology evolution simulation.
   b) Explain how you model the specified quantum effect in the given biological process.
   c) Detail how your simulation incorporates evolutionary processes and the given environmental factor.
   d) Provide a high-level pseudocode or flowchart of your simulation algorithm.

2. Quantum-Classical Interface (250-300 words):
   a) Explain how your simulation bridges quantum and classical effects in biological systems.
   b) Discuss potential challenges in modeling quantum effects at the biological scale and how you address them.
   c) Describe any novel algorithms or approximations used in your simulation.

3. Evolutionary Analysis (250-300 words):
   a) Predict how the incorporation of quantum effects might influence evolutionary trajectories.
   b) Discuss potential implications for adaptation and speciation rates.
   c) Compare your quantum-inclusive model with traditional evolutionary simulations.

4. Speculative Outcomes (200-250 words):
   a) Propose three potential evolutionary outcomes that might emerge from your simulation.
   b) Explain how these outcomes could challenge or extend current evolutionary theory.
   c) Discuss any implications for our understanding of life's diversity and adaptability.

5. Experimental Validation (200-250 words):
   a) Propose an experimental setup to test a key prediction from your simulation.
   b) Describe potential observables and measurement techniques.
   c) Discuss challenges in verifying quantum effects in biological evolution experimentally.

6. Interdisciplinary Implications (150-200 words):
   a) Explore how your simulation might impact other scientific fields.
   b) Discuss potential technological applications inspired by your findings.
   c) Consider philosophical implications of quantum effects in biological evolution.

Ensure your response demonstrates a deep understanding of quantum mechanics, evolutionary biology, and complex systems modeling. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and evolutionary biology",
            "The simulation design is scientifically plausible and clearly incorporates the specified quantum effect, biological process, and environmental factor",
            "The analysis of evolutionary implications is thorough and creative, while remaining grounded in scientific principles",
            "The proposed experimental validation is well-thought-out and addresses the challenges of studying quantum effects in biological systems",
            "The response shows strong interdisciplinary thinking and explores broader implications of the research"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
