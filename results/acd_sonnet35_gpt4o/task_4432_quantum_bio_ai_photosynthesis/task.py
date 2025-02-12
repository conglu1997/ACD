import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "plant_type": "C3 plants",
                "environmental_condition": "High CO2 concentration",
                "quantum_effect": "Quantum coherence",
                "optimization_goal": "Increase carbon fixation efficiency"
            },
            {
                "plant_type": "C4 plants",
                "environmental_condition": "Water scarcity",
                "quantum_effect": "Quantum tunneling",
                "optimization_goal": "Improve water use efficiency"
            },
            {
                "plant_type": "CAM plants",
                "environmental_condition": "High temperature",
                "quantum_effect": "Quantum entanglement",
                "optimization_goal": "Enhance heat resistance"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired AI system to model and optimize photosynthesis in {t['plant_type']}, focusing on {t['environmental_condition']}. Your system should incorporate the quantum effect of {t['quantum_effect']} and aim to {t['optimization_goal']}. Provide your response in the following format:

1. Quantum Biology Framework (250-300 words):
   a) Explain the relevance of {t['quantum_effect']} in photosynthesis for {t['plant_type']}.
   b) Describe how this quantum effect influences photosynthetic efficiency under {t['environmental_condition']}.
   c) Discuss current limitations in modeling this quantum effect in biological systems.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your quantum-inspired AI system for modeling photosynthesis.
   b) Explain how your system integrates quantum principles with machine learning algorithms.
   c) Describe how your AI model simulates the quantum effects in photosynthesis.
   d) Discuss any novel algorithms or techniques you've developed for this purpose.

3. Data Integration and Processing (200-250 words):
   a) Describe the types of data your system would use to model photosynthesis (e.g., spectroscopic data, genetic information).
   b) Explain how your system processes and integrates data from various sources.
   c) Discuss how you handle the challenges of modeling quantum effects at a biological scale.

4. Optimization Strategies (250-300 words):
   a) Propose specific strategies your AI system would use to {t['optimization_goal']}.
   b) Explain how these strategies leverage the modeled quantum effects.
   c) Describe how your system would adapt its optimization approach for {t['environmental_condition']}.

5. Practical Applications and Predictions (200-250 words):
   a) Discuss potential real-world applications of your quantum-bio-AI system in agriculture or biotechnology.
   b) Make specific, testable predictions about how your system could improve photosynthetic efficiency.
   c) Propose an experiment to validate your system's predictions or effectiveness.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues in applying quantum-inspired AI to biological optimization.
   b) Discuss limitations of your approach and areas needing further research.
   c) Propose guidelines for responsible development and application of quantum-bio-AI technologies.

Ensure your response demonstrates a deep understanding of quantum mechanics, plant biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes all six required sections with appropriate content for the {t['plant_type']} scenario",
            f"The quantum-inspired AI system effectively incorporates {t['quantum_effect']} for modeling photosynthesis",
            f"The system demonstrates innovative approaches to optimize photosynthesis under {t['environmental_condition']}",
            "The response shows a deep understanding of quantum biology, plant physiology, and artificial intelligence",
            "The proposed system is scientifically plausible and addresses potential limitations and ethical considerations"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
