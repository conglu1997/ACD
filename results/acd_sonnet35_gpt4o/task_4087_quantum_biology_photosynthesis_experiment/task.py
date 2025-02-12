import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        experiments = [
            {
                "biological_system": "Light-harvesting complexes in green sulfur bacteria",
                "quantum_effect": "Quantum entanglement",
                "experimental_technique": "Two-dimensional electronic spectroscopy",
                "environmental_condition": "Low light intensity"
            },
            {
                "biological_system": "Reaction centers in purple bacteria",
                "quantum_effect": "Quantum tunneling",
                "experimental_technique": "Ultrafast transient absorption spectroscopy",
                "environmental_condition": "High temperature"
            },
            {
                "biological_system": "Photosystem II in spinach chloroplasts",
                "quantum_effect": "Quantum coherence",
                "experimental_technique": "Coherent multidimensional spectroscopy",
                "environmental_condition": "Varying pH levels"
            }
        ]
        return {
            "1": random.choice(experiments),
            "2": random.choice(experiments)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an experiment to investigate the role of quantum coherence in photosynthesis, focusing on {t['quantum_effect']} in {t['biological_system']}, and propose a quantum-inspired artificial photosynthetic system. Your response should include:

1. Theoretical Background (250-300 words):
   1.1. Explain the concept of quantum coherence and its potential role in photosynthesis.
   1.2. Describe the current understanding of {t['quantum_effect']} in biological systems.
   1.3. Discuss the significance of studying {t['biological_system']} in the context of quantum biology.

2. Experimental Design (300-350 words):
   2.1. Propose a detailed experimental setup to investigate {t['quantum_effect']} in {t['biological_system']}.
   2.2. Explain how you will use {t['experimental_technique']} in your experiment.
   2.3. Describe the specific measurements you will take and the data you expect to collect.
   2.4. Discuss how you will account for the {t['environmental_condition']} in your experiment.
   2.5. Address potential challenges in your experimental design and how you plan to overcome them.
   2.6. Include a simple diagram of your experimental setup (use ASCII art).

3. Data Analysis and Interpretation (250-300 words):
   3.1. Describe the methods you will use to analyze the experimental data.
   3.2. Explain how you will distinguish quantum effects from classical phenomena in your results.
   3.3. Discuss potential alternative interpretations of your expected results.
   3.4. Propose a statistical or mathematical model to quantify the quantum coherence effects.

4. Quantum-Inspired Artificial Photosynthetic System (300-350 words):
   4.1. Based on your experimental design, propose an artificial system that mimics the quantum aspects of photosynthesis.
   4.2. Describe the key components and working principles of your artificial system.
   4.3. Explain how your system incorporates {t['quantum_effect']} to enhance its efficiency.
   4.4. Discuss potential applications of your quantum-inspired artificial photosynthetic system.

5. Implications and Future Directions (200-250 words):
   5.1. Discuss the potential implications of your research for our understanding of quantum biology and photosynthesis.
   5.2. Propose future experiments or technological developments that could build on your work.
   5.3. Speculate on how quantum biology might influence the development of future quantum technologies.

6. Ethical Considerations (150-200 words):
   6.1. Discuss any ethical implications of your research in quantum biology.
   6.2. Address potential concerns about developing artificial photosynthetic systems.
   6.3. Propose guidelines for responsible research and application in this field.

Ensure your response demonstrates a deep understanding of quantum physics, biology, and experimental techniques. Be creative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear numbered headings and subheadings as shown above. Your total response should be between 1450-1750 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of quantum coherence and its potential role in photosynthesis, particularly in {t['biological_system']}.",
            f"The experimental design effectively investigates {t['quantum_effect']} using {t['experimental_technique']} and accounts for {t['environmental_condition']}.",
            "The data analysis and interpretation methods are appropriate, well-explained, and include a proposed mathematical model.",
            "The proposed quantum-inspired artificial photosynthetic system is innovative, scientifically plausible, and clearly incorporates the studied quantum effect.",
            "The response addresses implications, future directions, and ethical considerations thoughtfully and comprehensively.",
            "The response is creative while maintaining scientific accuracy and plausibility throughout all sections.",
            "The response follows the specified format with clear numbered headings and subheadings, and adheres to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
