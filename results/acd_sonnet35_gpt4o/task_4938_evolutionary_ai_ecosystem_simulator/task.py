import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            "Coral reef",
            "Tropical rainforest",
            "Arctic tundra",
            "Savanna grassland",
            "Deep sea hydrothermal vent"
        ]
        timescales = [
            "1 million years",
            "10 million years",
            "100 million years",
            "500 million years",
            "1 billion years"
        ]
        evolutionary_pressures = [
            "Rapid global warming",
            "Increased ocean acidification",
            "Extreme solar radiation fluctuations",
            "Periodic asteroid impacts",
            "Emergence of a dominant, highly adaptive species"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                "ecosystem": random.choice(ecosystems),
                "timescale": random.choice(timescales),
                "evolutionary_pressure": random.choice(evolutionary_pressures)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and predicts the evolution of a {t['ecosystem']} ecosystem over a timescale of {t['timescale']}, incorporating principles of evolutionary biology, ecological dynamics, and climate change. Your system should specifically address the evolutionary pressure of {t['evolutionary_pressure']}. Provide your response in the following format:

1. Ecosystem Modeling Framework (300-350 words):
   a) Describe the key components and interactions of the {t['ecosystem']} ecosystem that your model will simulate.
   b) Explain how your AI system will represent and track individual species, populations, and their interactions.
   c) Discuss how your model incorporates principles of evolutionary biology and ecological dynamics.

2. AI System Architecture (250-300 words):
   a) Outline the main components of your AI system for simulating long-term ecosystem evolution.
   b) Explain any novel algorithms or techniques used in your model to handle the extended timescale of {t['timescale']}.
   c) Describe how your system integrates data from various scientific domains (e.g., climatology, geology, biology).

3. Evolutionary Pressure Simulation (200-250 words):
   a) Detail how your AI system models the specific evolutionary pressure of {t['evolutionary_pressure']}.
   b) Explain how this pressure is expected to influence species adaptation and ecosystem dynamics over time.
   c) Discuss any unique challenges in simulating this pressure over the given timescale.

4. Prediction and Analysis Capabilities (250-300 words):
   a) Describe the types of predictions and analyses your AI system can generate about the ecosystem's evolution.
   b) Explain how your system quantifies and communicates uncertainty in its long-term predictions.
   c) Propose a method for validating your system's predictions given the extended timescale.

5. Interdisciplinary Insights (200-250 words):
   a) Discuss how your AI system might generate novel insights or hypotheses about evolutionary biology or ecology.
   b) Explain how these insights could inform real-world conservation strategies or climate change mitigation efforts.
   c) Propose an experiment or field study that could be designed based on your system's predictions.

6. Technical Implementation and Scaling (150-200 words):
   a) Outline the computational resources required to run your simulation over the specified timescale.
   b) Discuss any technical challenges in implementing this system and propose potential solutions.
   c) Explain how your system could be scaled or adapted to simulate multiple interconnected ecosystems.

7. Ethical Considerations and Limitations (150-200 words):
   a) Discuss potential ethical implications of using AI to predict long-term ecosystem evolution.
   b) Address limitations of your model and how these might affect interpretation of its results.
   c) Propose guidelines for the responsible use of such ecosystem evolution predictions in scientific research and policy-making.

Ensure your response demonstrates a deep understanding of evolutionary biology, ecology, and artificial intelligence. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the {t['ecosystem']} ecosystem and its potential evolution over {t['timescale']}.",
            f"The AI system effectively models and addresses the evolutionary pressure of {t['evolutionary_pressure']}.",
            "The proposed system integrates knowledge from evolutionary biology, ecology, and artificial intelligence in a novel and plausible manner.",
            "The response includes innovative approaches to long-term ecosystem simulation and prediction.",
            "The submission addresses ethical considerations and limitations of the proposed system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
