import random
import math

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'organism': 'Green sulfur bacteria',
                'environment': 'Deep sea hydrothermal vents',
                'light_condition': 'Extremely low light'
            },
            {
                'organism': 'Desert cyanobacteria',
                'environment': 'Atacama Desert',
                'light_condition': 'Intense sunlight'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum-inspired neural network that mimics the photosynthetic process of {t['organism']} in {t['environment']} under {t['light_condition']} conditions. Your task has the following components:

1. Quantum Bio-Inspired Architecture (300-350 words):
   a) Describe the key components of your quantum bio-neural network.
   b) Explain how your architecture incorporates quantum principles (e.g., superposition, entanglement) to model photosynthetic energy transfer.
   c) Discuss how your design accounts for the specific environmental conditions and organism characteristics.
   d) Include a diagram or detailed textual description of your network architecture.

2. Quantum-Classical Interface (200-250 words):
   a) Explain how your network integrates quantum and classical information processing.
   b) Describe the mechanism for translating quantum states into classical neural network outputs.
   c) Discuss challenges in maintaining quantum coherence in a biological context and how you address them.

3. Learning and Adaptation (250-300 words):
   a) Propose a learning algorithm for your quantum bio-neural network.
   b) Explain how this algorithm allows the network to optimize photosynthetic efficiency.
   c) Describe how your network might adapt to changes in light conditions or environmental factors.

4. Performance Analysis (200-250 words):
   a) Predict the potential improvements in photosynthetic efficiency using your quantum bio-neural network.
   b) Compare your model's theoretical performance to classical artificial neural networks and natural photosynthetic systems.
   c) Discuss any trade-offs or limitations in your approach.

5. Broader Implications (150-200 words):
   a) Explore potential applications of your quantum bio-neural network beyond photosynthesis modeling.
   b) Discuss how this technology might impact fields such as energy production, quantum computing, or artificial photosynthesis.
   c) Address any ethical considerations or potential risks associated with this technology.

Ensure your response demonstrates a deep understanding of quantum mechanics, photosynthesis, neural networks, and the specific biological context. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum mechanics, photosynthesis, and neural networks.",
            "The quantum bio-neural network design is innovative, scientifically plausible, and clearly explained.",
            "The quantum-classical interface and learning algorithm are well-thought-out and relevant to the task.",
            "The performance analysis includes meaningful comparisons and discusses limitations.",
            "The response addresses broader implications and potential applications thoughtfully.",
            "The design effectively accounts for the specific organism and environmental conditions provided.",
            "The response adheres to the specified word count for each section and the overall submission."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
