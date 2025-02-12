import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_biological_phenomena = [
            {
                "phenomenon": "Quantum coherence in photosynthesis",
                "system": "Light-harvesting complexes in plants",
                "implications": "Enhanced energy transfer efficiency"
            },
            {
                "phenomenon": "Quantum tunneling in enzyme catalysis",
                "system": "Hydrogen transfer in enzyme reactions",
                "implications": "Increased reaction rates and specificity"
            },
            {
                "phenomenon": "Quantum entanglement in avian magnetoreception",
                "system": "Cryptochrome proteins in bird retinas",
                "implications": "Precise navigation using Earth's magnetic field"
            },
            {
                "phenomenon": "Quantum vibrations in olfaction",
                "system": "Olfactory receptors in the nose",
                "implications": "Enhanced odor discrimination and sensitivity"
            }
        ]
        return {
            "1": random.choice(quantum_biological_phenomena),
            "2": random.choice(quantum_biological_phenomena)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze and expand upon a hypothetical quantum biological mechanism in living systems. The quantum biological phenomenon you will focus on is: {t['phenomenon']} in the context of {t['system']}, with potential implications of {t['implications']}.

Address the following points in your response:

1. Theoretical Framework (200-250 words):
   a) Explain the quantum mechanical principles underlying the given phenomenon.
   b) Describe how these quantum effects might manifest in the biological system.
   c) Discuss current scientific understanding and debates surrounding this phenomenon.

2. Hypothesis Generation (200-250 words):
   a) Propose a novel hypothesis about how quantum effects could influence the biological system in question.
   b) Explain how your hypothesis builds upon or challenges existing theories.
   c) Discuss potential implications of your hypothesis for our understanding of life processes.

3. Experimental Design (250-300 words):
   a) Propose an experiment to test your hypothesis.
   b) Describe the methodology, including any specialized equipment or techniques required.
   c) Explain how you would control for classical (non-quantum) effects.
   d) Discuss potential challenges in isolating and measuring quantum effects in biological systems.

4. Data Analysis and Interpretation (200-250 words):
   a) Describe how you would analyze the data from your proposed experiment.
   b) Explain what results would support or refute your hypothesis.
   c) Discuss how you would distinguish quantum effects from classical phenomena in your analysis.

5. Implications and Ethics (200-250 words):
   a) Discuss the potential implications of your findings for biology, medicine, or technology.
   b) Consider any ethical concerns that might arise from this research or its applications.
   c) Propose guidelines for responsible conduct of quantum biology research.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how your work in quantum biology could inform or be informed by other scientific disciplines.
   b) Propose a collaborative research project that combines quantum biology with another field of study.

Ensure your response demonstrates a deep understanding of both quantum mechanics and biological systems. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both quantum mechanics and biological systems",
            "The proposed hypothesis is novel and scientifically plausible",
            "The experimental design is well-thought-out and addresses potential challenges",
            "The data analysis approach is appropriate and considers both quantum and classical effects",
            "The discussion of implications and ethics is thoughtful and comprehensive",
            "The interdisciplinary connections are insightful and demonstrate broad scientific knowledge",
            "The response is well-structured, clear, and within the specified word count"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
