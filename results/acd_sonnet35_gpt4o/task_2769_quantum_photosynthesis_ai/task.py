import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            {
                "effect": "Quantum coherence",
                "description": "Maintenance of quantum superposition in biological systems"
            },
            {
                "effect": "Quantum entanglement",
                "description": "Non-local quantum correlations between particles"
            }
        ]
        ai_applications = [
            "Energy-efficient neural networks",
            "Quantum-inspired optimization algorithms"
        ]
        
        tasks = {}
        for i in range(2):
            effect = random.choice(quantum_effects)
            application = random.choice(ai_applications)
            coherence_time = round(random.uniform(0.1, 1.0), 2)  # in picoseconds
            energy_efficiency = round(random.uniform(10, 100), 2)  # in percent
            tasks[str(i+1)] = {
                "quantum_effect": effect["effect"],
                "effect_description": effect["description"],
                "ai_application": application,
                "coherence_time": coherence_time,
                "target_energy_efficiency": energy_efficiency
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model of quantum effects in photosynthesis and apply it to create a novel AI system for energy-efficient information processing. Focus on the quantum effect of {t['quantum_effect']} ({t['effect_description']}) and apply it to the AI application of {t['ai_application']}. Your model should account for a quantum coherence time of {t['coherence_time']} picoseconds and aim for a target energy efficiency improvement of {t['target_energy_efficiency']}% over classical systems.

Your response should include:

1. Quantum Photosynthesis Model (250-300 words):
   a) Describe the key components of your model for quantum effects in photosynthesis.
   b) Explain how your model incorporates the specified quantum effect.
   c) Discuss how your model accounts for the transition from quantum to classical behavior in biological systems.
   d) Include a mathematical representation of your model using LaTeX notation.

2. Quantum-Biological Interface (200-250 words):
   a) Explain how your model bridges quantum physics and biological processes.
   b) Discuss how it accounts for decoherence and other challenges in maintaining quantum effects in warm, wet environments.
   c) Propose a method for experimentally validating your model in photosynthetic systems.

3. AI System Design (250-300 words):
   a) Describe a novel AI system architecture inspired by your quantum photosynthesis model.
   b) Explain how this system implements the specified AI application.
   c) Discuss potential advantages of your quantum-inspired approach over classical AI systems.
   d) Include a flowchart of your AI system using ASCII art.

4. Energy Efficiency Analysis (150-200 words):
   a) Provide a quantitative analysis of the energy efficiency of your AI system.
   b) Compare its efficiency to traditional computing approaches using specific metrics.
   c) Discuss any trade-offs between energy efficiency and computational power in your system.

5. Practical Implementation (200-250 words):
   a) Propose a roadmap for developing a practical implementation of your system.
   b) Discuss potential challenges and how they might be overcome.
   c) Suggest potential applications of your system beyond the specified AI application.

6. Ethical and Societal Implications (100-150 words):
   a) Discuss potential ethical considerations of developing AI systems inspired by quantum biology.
   b) Explore possible societal impacts if such systems become widely adopted.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, and artificial intelligence. Be creative and innovative while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-designed quantum photosynthesis model that incorporates {t['quantum_effect']} and accounts for a coherence time of {t['coherence_time']} picoseconds",
            f"The proposed AI system should clearly apply {t['quantum_effect']} to {t['ai_application']}",
            "The response should demonstrate a deep understanding of quantum mechanics, biology, and AI principles",
            f"The energy efficiency analysis should provide a quantitative comparison showing an improvement approaching {t['target_energy_efficiency']}% over classical systems",
            "The practical implementation roadmap and ethical considerations should be well-thought-out and relevant",
            "The response must include the required mathematical representation and ASCII flowchart"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
