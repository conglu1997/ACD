import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = ['quantum coherence', 'quantum entanglement', 'quantum tunneling']
        brain_regions = ['neocortex', 'hippocampus', 'thalamus']
        cognitive_functions = ['working memory', 'attention', 'decision-making']
        computational_paradigms = ['quantum annealing', 'adiabatic quantum computation', 'topological quantum computation']
        
        tasks = [
            {
                'quantum_effect': effect,
                'brain_region': region,
                'cognitive_function': function,
                'computational_paradigm': paradigm
            }
            for effect in quantum_effects
            for region in brain_regions
            for function in cognitive_functions
            for paradigm in computational_paradigms
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical quantum-biological model of consciousness and use it to propose a novel quantum cognitive computing architecture. Your model should focus on the quantum effect of {t['quantum_effect']} in the {t['brain_region']}, emphasizing its role in {t['cognitive_function']}. Then, use this model to design a quantum cognitive computer based on {t['computational_paradigm']}. Your response should include:

1. Quantum-Biological Consciousness Model (300-350 words):
   a) Describe the key components and mechanisms of your quantum-biological model of consciousness.
   b) Explain how {t['quantum_effect']} in the {t['brain_region']} contributes to consciousness and {t['cognitive_function']}.
   c) Discuss how your model addresses the hard problem of consciousness.
   d) Provide a diagram or schematic representation of your model (describe it textually).

2. Quantum Cognitive Computing Architecture (300-350 words):
   a) Outline the key components and processes of your quantum cognitive computing architecture.
   b) Explain how it implements the principles from your consciousness model.
   c) Describe how it utilizes {t['computational_paradigm']} to perform cognitive computations.
   d) Discuss any novel features or innovations in your design.

3. Information Processing and Cognitive Function (250-300 words):
   a) Explain how your quantum cognitive computer processes information.
   b) Describe how it models or performs {t['cognitive_function']}.
   c) Compare its information processing capabilities to classical computing and biological brains.

4. Theoretical Performance Analysis (200-250 words):
   a) Estimate the theoretical performance capabilities of your quantum cognitive computer.
   b) Compare these to current classical and quantum computing systems.
   c) Discuss potential advantages and limitations of your approach.

5. Experimental Proposals (200-250 words):
   a) Propose two experiments to test or validate aspects of your quantum-biological consciousness model.
   b) Suggest an experiment to evaluate the performance of your quantum cognitive computer in {t['cognitive_function']}.

6. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical implications of creating computers based on models of consciousness.
   b) Explore the philosophical questions raised by your model and architecture.
   c) Consider the potential societal impacts of advanced quantum cognitive computing.

Ensure your response demonstrates a deep understanding of quantum mechanics, neuroscience, cognitive science, and computer architecture. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively incorporates {t['quantum_effect']} in the {t['brain_region']} for modeling consciousness and {t['cognitive_function']}.",
            f"The quantum cognitive computing architecture clearly utilizes {t['computational_paradigm']} in a relevant and innovative way.",
            "The model and architecture demonstrate a deep understanding of quantum mechanics, neuroscience, and cognitive science.",
            "The proposed experiments are well-designed and relevant to validating the model and architecture.",
            "The response shows creativity and innovation while maintaining scientific plausibility.",
            "The ethical and philosophical implications are thoroughly discussed and relevant to the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
