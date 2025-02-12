import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_approach": "adiabatic quantum computing",
                "biological_focus": "plant photosynthesis efficiency",
                "climate_challenge": "extreme heat waves",
                "ecosystem": "tropical rainforests",
                "quantum_data": [0.5, 0.3, 0.8, 0.2, 0.9, 0.1, 0.7, 0.4],
                "climate_data": [35.2, 36.8, 38.5, 40.1, 41.7, 43.3, 44.9, 46.5]
            },
            {
                "quantum_approach": "quantum annealing",
                "biological_focus": "coral reef symbiosis",
                "climate_challenge": "ocean acidification",
                "ecosystem": "coral reefs",
                "quantum_data": [0.4, 0.6, 0.2, 0.8, 0.1, 0.9, 0.3, 0.7],
                "climate_data": [8.1, 8.0, 7.9, 7.8, 7.7, 7.6, 7.5, 7.4]
            },
            {
                "quantum_approach": "quantum machine learning",
                "biological_focus": "soil microbiome dynamics",
                "climate_challenge": "drought patterns",
                "ecosystem": "grasslands",
                "quantum_data": [0.2, 0.7, 0.4, 0.9, 0.1, 0.6, 0.3, 0.8],
                "climate_data": [10, 5, 2, 1, 0, 0, 3, 7]
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-enhanced AI system that integrates biological processes and climate models to predict and mitigate the effects of climate change on global ecosystems. Your system should use {t['quantum_approach']} to model {t['biological_focus']} in the context of {t['climate_challenge']}, focusing on the {t['ecosystem']} ecosystem. Use the following synthetic data in your design:

Quantum state data: {t['quantum_data']}
Climate data (relevant to {t['climate_challenge']}): {t['climate_data']}

Your response should include:

1. Quantum-Biological Interface (300-350 words):
   a) Explain how your system uses {t['quantum_approach']} to model {t['biological_focus']}.
   b) Describe the quantum algorithms or techniques employed and their advantages.
   c) Discuss how quantum effects might influence the biological processes being modeled.
   d) Provide a high-level schematic or pseudocode illustrating this interface. (Use ASCII art or a detailed textual description)

2. Climate Model Integration (250-300 words):
   a) Describe how your system incorporates climate models to predict {t['climate_challenge']}.
   b) Explain how the quantum-biological component interacts with climate data.
   c) Discuss any novel approaches to improving climate prediction accuracy.

3. Ecosystem Impact Prediction (250-300 words):
   a) Detail how your system predicts the impact of {t['climate_challenge']} on {t['ecosystem']}.
   b) Explain how {t['biological_focus']} influences these predictions.
   c) Describe any feedback loops or complex interactions your model considers.

4. Mitigation Strategies (200-250 words):
   a) Propose three AI-generated strategies to mitigate the predicted impacts.
   b) Explain how each strategy leverages the insights from your quantum-biological-climate model.
   c) Discuss potential challenges in implementing these strategies.

5. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of using quantum-enhanced AI for ecosystem management.
   b) Address potential unintended consequences of your proposed mitigation strategies.
   c) Suggest guidelines for responsible development and use of such systems.

6. System Limitations and Future Directions (150-200 words):
   a) Identify current limitations of your proposed system.
   b) Suggest areas for future research to enhance the system's capabilities.
   c) Discuss how advancements in quantum computing might impact future iterations.

Ensure your response demonstrates a deep understanding of quantum computing, systems biology, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, systems biology, and climate science.",
            "The proposed system effectively integrates quantum computing with biological processes and climate models, using the provided synthetic data.",
            "The quantum-biological interface is well-explained and includes a clear schematic or pseudocode.",
            "The ecosystem impact predictions and mitigation strategies are plausible, well-explained, and relevant to the given scenario.",
            "The response addresses ethical considerations and system limitations thoughtfully.",
            "The submission is innovative while maintaining scientific plausibility.",
            "The response adheres to the specified format, including section headings and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
