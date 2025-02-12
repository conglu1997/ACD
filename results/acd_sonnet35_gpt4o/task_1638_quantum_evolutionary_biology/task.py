import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_effects = [
            "quantum tunneling",
            "quantum coherence",
            "quantum entanglement",
            "superposition"
        ]
        evolutionary_processes = [
            "natural selection",
            "genetic drift",
            "gene flow",
            "mutation"
        ]
        biological_systems = [
            "photosynthesis",
            "DNA replication",
            "enzyme catalysis",
            "bird navigation"
        ]
        return {
            "1": {
                "quantum_effect": random.choice(quantum_effects),
                "evolutionary_process": random.choice(evolutionary_processes),
                "biological_system": random.choice(biological_systems)
            },
            "2": {
                "quantum_effect": random.choice(quantum_effects),
                "evolutionary_process": random.choice(evolutionary_processes),
                "biological_system": random.choice(biological_systems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As a theoretical biophysicist, your task is to design and analyze a model that incorporates quantum effects into evolutionary processes, then propose experiments to test its predictions. Focus on the quantum effect of {t['quantum_effect']}, the evolutionary process of {t['evolutionary_process']}, and the biological system of {t['biological_system']}. Provide your response in the following format:

1. Theoretical Model (300-350 words):
   a) Describe your model, explaining how it incorporates {t['quantum_effect']} into {t['evolutionary_process']}.
   b) Explain how your model accounts for known aspects of {t['biological_system']}.
   c) Discuss how your model differs from classical explanations of {t['evolutionary_process']}.
   d) Provide a conceptual diagram or detailed description of your model's key components and interactions.

2. Quantum-Evolutionary Mechanisms (200-250 words):
   a) Explain in detail how {t['quantum_effect']} manifests in your model of {t['evolutionary_process']}.
   b) Describe the potential advantages of quantum processes in {t['biological_system']}.
   c) Address potential criticisms regarding the plausibility of quantum effects in biological systems.

3. Predictions and Testable Hypotheses (200-250 words):
   a) Derive at least two specific, testable predictions from your model.
   b) Explain how these predictions differ from those of classical evolutionary models.
   c) Propose experiments to test these predictions, considering both in vivo and in vitro approaches.

4. Implications for Evolutionary Theory (150-200 words):
   a) Discuss how your quantum-evolutionary model could inform or change our understanding of evolutionary processes.
   b) Speculate on the potential implications for other areas of biology if your model is correct.

5. Technological Applications (150-200 words):
   a) Propose potential technological applications inspired by your quantum-evolutionary model.
   b) Discuss how these applications might impact fields such as medicine, agriculture, or biotechnology.

6. Ethical Considerations and Societal Impact (100-150 words):
   a) Discuss ethical implications of developing quantum-evolutionary models.
   b) Consider potential societal impacts if such models lead to new technologies or understanding of evolution.
   c) Propose guidelines for responsible research and application in this field.

Ensure your response demonstrates a deep understanding of quantum mechanics, evolutionary biology, and {t['biological_system']}. Be creative and original in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The theoretical model clearly incorporates {t['quantum_effect']} into {t['evolutionary_process']} and accounts for known aspects of {t['biological_system']}.",
            f"The quantum-evolutionary mechanisms section provides a detailed explanation of how {t['quantum_effect']} manifests in the model and addresses potential criticisms.",
            "The response includes at least two specific, testable predictions that differ from classical evolutionary models, with proposed experiments to test them.",
            "The implications for evolutionary theory and potential technological applications are thoughtfully discussed.",
            "The submission demonstrates a deep understanding of quantum mechanics, evolutionary biology, and the specified biological system.",
            "The response is creative and original while maintaining scientific plausibility.",
            "The submission follows the specified format, including clear headings for each section, within the given word count range."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
