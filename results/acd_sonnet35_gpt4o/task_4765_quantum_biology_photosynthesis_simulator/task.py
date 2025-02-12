import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        photosynthetic_systems = [
            {
                "name": "Fenna-Matthews-Olson (FMO) complex",
                "organism": "Green sulfur bacteria",
                "num_chromophores": 7,
                "coherence_time": "300 femtoseconds",
                "efficiency": 0.99
            },
            {
                "name": "Light-harvesting complex II (LHCII)",
                "organism": "Higher plants",
                "num_chromophores": 14,
                "coherence_time": "500 femtoseconds",
                "efficiency": 0.95
            }
        ]
        return {
            "1": random.choice(photosynthetic_systems),
            "2": random.choice(photosynthetic_systems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and implement a quantum simulation system to model and visualize quantum coherence effects in photosynthesis, focusing on the {t['name']} found in {t['organism']}. Then, use your simulation to analyze potential applications in artificial photosynthesis. Your response should include the following sections:

1. Quantum Simulation System Design (300-350 words):
   a) Describe the overall architecture of your quantum simulation system.
   b) Explain how your system models quantum coherence in the {t['name']}.
   c) Detail the quantum algorithms or methods used in your simulation.
   d) Discuss how your system integrates principles from quantum physics and biology.

2. Implementation and Visualization (250-300 words):
   a) Outline the steps to implement your simulation, including any necessary approximations or simplifications.
   b) Describe how you would visualize the quantum coherence effects in the {t['name']}.
   c) Explain how your visualization technique helps in understanding the quantum processes involved.
   d) Discuss any challenges in implementing this simulation and propose solutions.

3. Simulation Results and Analysis (250-300 words):
   a) Present the expected results from your simulation of the {t['name']}.
   b) Analyze how quantum coherence contributes to the high efficiency ({t['efficiency']}) of this system.
   c) Compare the simulated coherence time with the experimentally observed value ({t['coherence_time']}).
   d) Discuss any insights your simulation provides about the role of quantum effects in photosynthesis.

4. Application to Artificial Photosynthesis (200-250 words):
   a) Propose a design for an artificial photosynthetic system inspired by your simulation results.
   b) Explain how quantum coherence could be leveraged to improve the efficiency of artificial photosynthesis.
   c) Discuss potential challenges in translating these quantum effects to artificial systems.

5. Experimental Validation (150-200 words):
   a) Propose an experimental setup to validate your simulation results.
   b) Describe the measurements needed to confirm the presence of quantum coherence in your artificial system.
   c) Discuss any technical challenges in performing these experiments.

6. Broader Implications (150-200 words):
   a) Discuss the potential impact of your findings on our understanding of quantum biology.
   b) Explore possible applications of quantum-enhanced artificial photosynthesis in energy production or carbon capture.
   c) Speculate on other biological processes that might benefit from a similar quantum simulation approach.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, and complex systems modeling. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics and its application to biological systems.",
            "The proposed quantum simulation system is well-designed and scientifically plausible.",
            "The visualization and analysis techniques are innovative and insightful.",
            "The application to artificial photosynthesis is well-reasoned and shows potential for real-world impact.",
            "The response effectively integrates knowledge from quantum physics, biology, and computer science.",
            "The proposed experimental validation is scientifically sound and addresses potential challenges.",
            "The discussion of broader implications shows a good understanding of the field's potential and limitations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
