import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "organism": "Purple bacteria",
                "light_harvesting_complex": "LH2",
                "environmental_condition": "Low light intensity"
            },
            {
                "organism": "Green sulfur bacteria",
                "light_harvesting_complex": "Chlorosome",
                "environmental_condition": "Extreme low light"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze a quantum-mechanical model of photosynthesis for {t['organism']}, focusing on the role of quantum coherence in energy transfer efficiency within the {t['light_harvesting_complex']} under {t['environmental_condition']} conditions. Your response should include the following sections:\n\n1. Quantum Model Design (250-300 words):\n   a) Describe the key components of your quantum-mechanical model for the given photosynthetic system.\n   b) Explain how your model incorporates quantum coherence effects.\n   c) Discuss how your model accounts for the specific light-harvesting complex and environmental conditions.\n   d) Provide a mathematical formulation of your model, including relevant equations.\n\n2. Simulation Methodology (200-250 words):\n   a) Outline the computational approach you would use to simulate your quantum model.\n   b) Explain how you would calculate energy transfer efficiency in your simulation.\n   c) Describe any approximations or simplifications used in your simulation method.\n\n3. Predicted Results and Analysis (200-250 words):\n   a) Present the expected results from your simulation, including energy transfer efficiency.\n   b) Analyze how quantum coherence contributes to the efficiency of the photosynthetic process in this scenario.\n   c) Compare your model's predictions with classical (non-quantum) models of photosynthesis.\n\n4. Experimental Validation (150-200 words):\n   a) Propose an experimental setup to test the predictions of your quantum model.\n   b) Describe the measurements you would perform and the equipment required.\n   c) Discuss potential challenges in experimentally verifying quantum effects in biological systems.\n\n5. Implications and Applications (200-250 words):\n   a) Discuss the broader implications of quantum coherence in photosynthesis for our understanding of biological systems.\n   b) Explore potential applications of your model in fields such as artificial photosynthesis or quantum computing.\n   c) Propose a novel research direction that combines quantum biology with another scientific field.\n\nEnsure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, and computational modeling. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility and rigor."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics and its application to biological systems.",
            "The quantum model design is well-thought-out and incorporates relevant quantum coherence effects.",
            "The simulation methodology is clearly explained and scientifically sound.",
            "The predicted results and analysis show insight into the role of quantum effects in photosynthesis.",
            "The proposed experimental validation is feasible and addresses the challenges of quantum biology.",
            "The discussion of implications and applications demonstrates creative thinking and interdisciplinary knowledge.",
            "The overall response is scientifically rigorous, well-structured, and demonstrates advanced problem-solving skills."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
