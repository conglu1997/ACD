import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        brain_regions = [
            "hippocampus",
            "prefrontal cortex",
            "amygdala",
            "cerebellum"
        ]
        climate_phenomena = [
            "El Niño",
            "monsoons",
            "Arctic amplification",
            "jet streams"
        ]
        adaptation_mechanisms = [
            "synaptic pruning",
            "neurogenesis",
            "long-term potentiation",
            "dendritic spine formation"
        ]
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "brain_region": random.choice(brain_regions),
                "climate_phenomenon": random.choice(climate_phenomena),
                "adaptation_mechanism": random.choice(adaptation_mechanisms)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neural network architecture for climate prediction inspired by the {t['brain_region']}'s role in adaptation and learning. Your model should specifically address the prediction of {t['climate_phenomenon']} and incorporate a mechanism analogous to {t['adaptation_mechanism']}. Your response should include:

1. Neuroscience Basis (250-300 words):
   a) Explain the function of the {t['brain_region']} in learning and adaptation.
   b) Describe how {t['adaptation_mechanism']} contributes to neuroplasticity.
   c) Discuss how these neural processes could be analogous to adaptive climate prediction.

2. Neural Network Architecture (300-350 words):
   a) Describe the overall structure of your neural network.
   b) Explain how it incorporates principles inspired by the {t['brain_region']} and {t['adaptation_mechanism']}.
   c) Detail how this architecture is particularly suited for predicting {t['climate_phenomenon']}.
   d) Include a diagram or pseudocode representation of your model.

3. Learning and Adaptation Process (250-300 words):
   a) Explain how your model learns from and adapts to new climate data.
   b) Describe how it handles conflicting or anomalous data.
   c) Compare your model's adaptation process to biological neuroplasticity.

4. Climate Prediction Capabilities (200-250 words):
   a) Describe the specific predictions your model can make about {t['climate_phenomenon']}.
   b) Explain how the neuroscience-inspired features enhance these predictions.
   c) Discuss potential limitations in applying brain-inspired models to climate science.

5. Comparative Analysis (200-250 words):
   a) Compare your neuroadaptive model to traditional climate prediction models.
   b) Discuss potential advantages and disadvantages of your approach.
   c) Propose a method to empirically evaluate your model against existing ones.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Discuss ethical implications of using brain-inspired AI for climate prediction.
   b) Suggest potential applications beyond climate science.
   c) Propose future research directions to further integrate neuroscience and climate AI.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and climate science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility. Your total response should be between 1350-1650 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, artificial intelligence, and climate science.",
            "The proposed neural network architecture effectively incorporates principles inspired by the specified brain region and adaptation mechanism.",
            "The model's learning and adaptation process is well-explained and analogous to biological neuroplasticity.",
            "The climate prediction capabilities are clearly described and linked to the neuroscience-inspired features.",
            "The comparative analysis provides thoughtful insights into the advantages and limitations of the approach.",
            "Ethical considerations are thoroughly addressed, and future research directions are innovative and well-reasoned.",
            "The response is creative and scientifically plausible.",
            "The writing is clear, well-structured, and adheres to the specified word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
