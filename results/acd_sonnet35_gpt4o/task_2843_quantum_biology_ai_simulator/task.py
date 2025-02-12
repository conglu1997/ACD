import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement"
        ]
        biological_processes = [
            "photosynthesis",
            "enzyme catalysis",
            "magnetoreception in birds"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "biological_process": random.choice(biological_processes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates the quantum effect of {t['quantum_effect']} in the biological process of {t['biological_process']} and predicts its impact on macroscopic biological phenomena. Your response should include the following sections:

1. Quantum Biology Framework (250-300 words):
   a) Explain the relevance of {t['quantum_effect']} to {t['biological_process']}.
   b) Describe the current scientific understanding of this quantum-biological interaction.
   c) Discuss the challenges in studying and modeling this phenomenon.

2. AI System Architecture (300-350 words):
   a) Outline the key components of your AI system for simulating this quantum-biological process.
   b) Explain how your system integrates quantum mechanical principles with biological modeling.
   c) Describe any novel AI techniques or algorithms you've incorporated to handle the complexity of this simulation.
   d) Include a high-level diagram of your system architecture (describe this textually).

3. Simulation Methodology (250-300 words):
   a) Detail the steps your AI system takes to simulate the quantum effect in the biological process.
   b) Explain how your system scales from quantum-level simulations to macroscopic predictions.
   c) Discuss how your approach might improve upon current modeling techniques in quantum biology.

4. Data Requirements and Preprocessing (200-250 words):
   a) Identify the types of data your system would require for accurate simulation.
   b) Explain how you would preprocess and integrate data from different scales (quantum to macroscopic).
   c) Discuss any ethical considerations in data collection or usage for this task.

5. Predictive Capabilities (200-250 words):
   a) Describe the types of predictions your AI system could make about macroscopic biological phenomena.
   b) Explain how these predictions could be validated experimentally.
   c) Discuss the potential impact of these predictions on our understanding of {t['biological_process']}.

6. Challenges and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in implementing your AI system.
   b) Propose solutions or approaches to overcome these challenges.
   c) Suggest future research directions that could enhance the capabilities of your system.

7. Ethical Implications and Societal Impact (150-200 words):
   a) Discuss the ethical implications of using AI to simulate and predict quantum biological phenomena.
   b) Analyze potential societal impacts of advanced quantum biology simulations.
   c) Propose guidelines for responsible development and use of such AI systems in scientific research.

Ensure your response demonstrates a deep understanding of quantum mechanics, biology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and addressing the complexity of quantum-biological interactions.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, biology, and artificial intelligence",
            "The AI system architecture is well-designed and integrates quantum and biological principles effectively",
            "The simulation methodology is clearly explained and addresses the complexity of quantum-biological interactions",
            "The predictive capabilities of the system are well-described and scientifically plausible",
            "Ethical implications and societal impacts are thoughtfully discussed",
            "The response is well-structured, adhering to the specified sections and word counts",
            "Technical terminology is used appropriately and complex concepts are explained clearly"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
