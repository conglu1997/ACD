import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_bio_phenomena = [
            {
                "name": "Quantum Coherent Photosynthesis",
                "description": "A process where plants utilize quantum coherence to enhance energy transfer efficiency in photosynthesis."
            },
            {
                "name": "Quantum Entangled Neurotransmission",
                "description": "A mechanism where neurotransmitters become quantum entangled, allowing for instantaneous signal propagation across synapses."
            },
            {
                "name": "Biological Quantum Tunneling",
                "description": "A phenomenon where biological molecules utilize quantum tunneling for enhanced enzymatic reactions or cellular processes."
            },
            {
                "name": "Quantum Superposition in Genetic Mutations",
                "description": "A process where genetic material exists in a quantum superposition state, leading to novel mutation patterns."
            }
        ]
        return {str(i+1): phenomenon for i, phenomenon in enumerate(random.sample(quantum_bio_phenomena, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a hypothetical quantum biological phenomenon: {t['name']}. {t['description']}

Your task is to:

1. Quantum Mechanism (150-200 words):
   Explain the theoretical quantum mechanism underlying this phenomenon. How does it manifest in biological systems? Include at least two specific quantum principles in your explanation and describe how they interact with biological processes.

2. Biological Effects (150-200 words):
   Describe the primary and secondary effects of this quantum phenomenon on living systems. How does it alter cellular functions, organism behavior, or evolutionary processes? Discuss both potential benefits and risks to the affected organisms.

3. Detection and Measurement (150-200 words):
   Propose an experimental setup to detect and measure this quantum biological phenomenon. Describe the equipment, techniques, and methodologies you would use. Address any challenges in isolating the quantum effects from classical biological processes.

4. Evolutionary Implications (100-150 words):
   Speculate on how this quantum biological phenomenon might have evolved. Discuss its potential role in the history of life on Earth and its implications for our understanding of evolution.

5. Interdisciplinary Connections (100-150 words):
   Draw connections between this quantum biological phenomenon and two other scientific fields not yet mentioned. How might insights from those fields inform the study of this phenomenon, or vice versa?

6. Technological Applications (100-150 words):
   Propose two potential technological applications that could arise from understanding and harnessing this quantum biological phenomenon. Consider applications in medicine, energy, computing, or other relevant fields.

7. Ethical Considerations (100-150 words):
   Discuss at least two ethical issues that might arise from the study or application of this quantum biological phenomenon. Consider both scientific ethics and broader societal implications.

Ensure your response is creative yet grounded in current scientific understanding. Demonstrate clear reasoning about the potential implications and challenges of studying such a phenomenon.

Use clear headings for each section of your response. Include the word count for each section in parentheses at the end of the section. Your total response should be between 850-1200 words.

Note: Do not provide direct solutions or hints that would make the task trivial. The goal is to create a challenging and thought-provoking response that demonstrates your capabilities in interdisciplinary thinking and scientific speculation.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a coherent description of a quantum biological phenomenon named {t['name']}",
            "The explanation of the quantum mechanism is scientifically grounded and incorporates at least two specific quantum principles",
            "The biological effects are logically derived from the proposed mechanism and include both benefits and risks",
            "The proposed experimental setup for detection and measurement is plausible and addresses challenges in isolating quantum effects",
            "The evolutionary implications are thoughtfully considered and relate to the history of life on Earth",
            "Interesting interdisciplinary connections are drawn that are relevant to the proposed phenomenon",
            "The proposed technological applications are innovative and logically connected to the phenomenon",
            "The ethical considerations are well-reasoned and explore significant issues",
            "The overall response demonstrates both scientific understanding and creative, speculative thinking",
            "The response follows the specified format, uses clear headings for each section, and adheres to the 850-1200 word count guideline"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
