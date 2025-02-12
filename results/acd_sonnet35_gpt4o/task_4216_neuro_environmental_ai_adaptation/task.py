import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "organism": "Coral reefs",
                "climate_factor": "Ocean acidification",
                "neural_process": "Synaptic plasticity"
            },
            {
                "organism": "Migratory birds",
                "climate_factor": "Shifting seasonal patterns",
                "neural_process": "Spatial memory formation"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics the neural adaptation processes of {t['organism']} responding to {t['climate_factor']}, focusing on the neural process of {t['neural_process']}. Then, use your system to predict and model ecosystem responses to this environmental shift. Your response should include:

1. Biological Basis (200-250 words):
   a) Describe the neural adaptation process in {t['organism']} in response to {t['climate_factor']}.
   b) Explain the role of {t['neural_process']} in this adaptation.
   c) Discuss any unique features of this organism's neural system relevant to climate adaptation.

2. AI System Architecture (250-300 words):
   a) Outline the key components of your AI system that model the neural adaptation process.
   b) Explain how your system incorporates {t['neural_process']} in its architecture.
   c) Describe how your AI system simulates the interaction between neural processes and environmental factors.
   d) Include a simple diagram or pseudocode representation of a key component in your system.

3. Environmental Modeling (200-250 words):
   a) Explain how your AI system integrates environmental data to simulate {t['climate_factor']}.
   b) Describe the methods your system uses to predict ecosystem responses based on neural adaptations.
   c) Discuss any novel approaches in your system for modeling complex environmental-biological interactions.

4. Simulation and Predictions (200-250 words):
   a) Describe a specific simulation scenario using your AI system.
   b) Provide example predictions your system might generate about ecosystem responses to {t['climate_factor']}.
   c) Explain how these predictions account for both neural adaptations and environmental factors.

5. Validation and Limitations (150-200 words):
   a) Propose methods for validating your AI system's predictions against real-world data.
   b) Discuss the limitations of your approach and potential sources of error.
   c) Suggest improvements or extensions to enhance the accuracy of your system.

6. Ethical Implications and Applications (150-200 words):
   a) Discuss ethical considerations in using AI to model biological responses to climate change.
   b) Explore potential applications of your system in conservation efforts or climate policy.
   c) Address any potential misuse or misinterpretation of your system's predictions.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and environmental science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified neural process and how it relates to climate adaptation in the given organism.",
            "The AI system architecture is innovative, coherent, and effectively mimics the biological neural adaptation process.",
            "The environmental modeling approach is well-thought-out and integrates both neural and environmental factors.",
            "The simulation scenario and predictions are plausible and demonstrate a clear link between neural adaptations and ecosystem responses.",
            "The response addresses validation methods, limitations, and ethical implications thoughtfully.",
            "The overall solution shows creativity and scientific plausibility throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
