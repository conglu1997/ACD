import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            {
                'name': 'Photosynthesis',
                'description': 'Quantum coherence in light-harvesting complexes',
                'key_concepts': ['exciton energy transfer', 'quantum superposition', 'decoherence']
            },
            {
                'name': 'Magnetoreception',
                'description': 'Quantum entanglement in cryptochrome proteins for bird navigation',
                'key_concepts': ['radical pair mechanism', 'spin chemistry', 'magnetic field sensitivity']
            },
            {
                'name': 'Enzyme Catalysis',
                'description': 'Quantum tunneling in enzyme-catalyzed reactions',
                'key_concepts': ['proton tunneling', 'zero-point energy', 'isotope effects']
            },
            {
                'name': 'Olfaction',
                'description': 'Quantum effects in scent molecule detection',
                'key_concepts': ['vibrational theory of olfaction', 'electron tunneling', 'molecular recognition']
            }
        ]
        
        tasks = random.sample(phenomena, 2)
        return {str(i+1): {'phenomenon': p} for i, p in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that models and predicts quantum effects in the biological process of {t['phenomenon']['name']}. Your system should focus on {t['phenomenon']['description']}. Provide your response in the following format:

1. System Architecture (250-300 words):
   a) Describe the main components of your AI system for modeling quantum-biological interactions.
   b) Explain how these components integrate quantum mechanics principles with biological processes.
   c) Detail any novel computational approaches or algorithms you would employ.

2. Quantum-Biological Modeling (200-250 words):
   a) Explain how your system models the quantum effects in {t['phenomenon']['name']}.
   b) Describe how you handle the transition between quantum and classical regimes in your model.
   c) Discuss how your system addresses the challenge of maintaining quantum coherence in a noisy biological environment.

3. Data Integration and Processing (200-250 words):
   a) Specify the types of data your system would require (e.g., spectroscopic data, structural information).
   b) Explain how your system processes and integrates data from different sources and scales.
   c) Describe any data preprocessing or feature extraction techniques specific to quantum-biological modeling.

4. Predictive Capabilities (200-250 words):
   a) Detail the specific predictions your system can make about quantum effects in {t['phenomenon']['name']}.
   b) Explain how your system quantifies uncertainty in its predictions.
   c) Describe how your system could be used to guide experimental design in quantum biology research.

5. Validation and Benchmarking (150-200 words):
   a) Propose methods to validate your system's predictions against experimental data.
   b) Suggest benchmarks to compare your system's performance against existing quantum biology models.
   c) Discuss the limitations of your approach and potential areas for improvement.

6. Interdisciplinary Implications (150-200 words):
   a) Discuss how your system could contribute to advancements in quantum biology, biophysics, and AI.
   b) Propose potential applications of your system beyond basic research (e.g., in biotechnology or medicine).
   c) Speculate on how improved understanding of quantum effects in biology might impact our view of life processes.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and machine learning. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1150-1450 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum mechanics principles as they apply to {t['phenomenon']['name']}.",
            f"The proposed AI system effectively integrates concepts from quantum physics, biology, and machine learning.",
            f"The system architecture and modeling approach are innovative yet scientifically plausible.",
            f"The response addresses the key concepts of {', '.join(t['phenomenon']['key_concepts'])}.",
            "The predictive capabilities and validation methods are well-explained and appropriate for the quantum-biological system.",
            "The response discusses interdisciplinary implications and potential applications of the proposed system.",
            "The answer adheres to the specified word count (1150-1450 words) and section structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
