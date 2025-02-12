import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "quantum_principle": "quantum coherence",
                "evolutionary_concept": "natural selection",
                "cognitive_process": "memory formation",
                "alien_environment": "gas giant with floating organisms"
            },
            "2": {
                "quantum_principle": "quantum entanglement",
                "evolutionary_concept": "genetic drift",
                "cognitive_process": "decision making",
                "alien_environment": "tidally locked planet with extremophiles"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that integrates quantum biology, evolutionary theory, and cognitive neuroscience to explain the emergence of consciousness in biological systems, then apply it to predict potential cognitive capabilities of hypothetical alien life forms. Your framework should incorporate the quantum principle of {t['quantum_principle']}, the evolutionary concept of {t['evolutionary_concept']}, and the cognitive process of {t['cognitive_process']}. Then, apply your framework to predict cognitive capabilities of life forms in a {t['alien_environment']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain how {t['quantum_principle']} could influence biological processes at the cellular level.
   b) Describe how {t['evolutionary_concept']} might interact with quantum effects in driving the evolution of cognitive systems.
   c) Propose a mechanism by which quantum-influenced biological processes could give rise to {t['cognitive_process']}.
   d) Discuss how these elements combine to contribute to the emergence of consciousness.

2. Mathematical Model (250-300 words):
   a) Develop a simple mathematical model or set of equations that represents key aspects of your framework.
   b) Explain the variables and parameters in your model.
   c) Describe how your model captures the interplay between quantum, evolutionary, and cognitive processes.
   d) Provide a visual representation of your model (describe it textually).

3. Predictions for Terrestrial Cognition (200-250 words):
   a) Use your framework to make two novel predictions about {t['cognitive_process']} in Earth-based organisms.
   b) Explain the reasoning behind these predictions.
   c) Suggest potential experiments to test these predictions.

4. Alien Cognitive Capabilities (250-300 words):
   a) Apply your framework to the given alien environment ({t['alien_environment']}).
   b) Predict three potential cognitive capabilities that might evolve in this environment.
   c) Explain how these capabilities could arise from the interplay of quantum effects, evolutionary pressures, and environmental constraints.
   d) Discuss how these alien cognitive systems might differ from Earth-based consciousness.

5. Critical Analysis (200-250 words):
   a) Provide a critical analysis of your own framework, identifying potential weaknesses or limitations.
   b) Discuss any assumptions made in your model and their potential impact on your predictions.
   c) Suggest how your framework might be empirically tested or falsified.

6. Implications and Future Research (150-200 words):
   a) Discuss the broader implications of your framework for our understanding of consciousness and cognition.
   b) Propose two potential extensions or refinements to your theoretical framework.
   c) Suggest an interdisciplinary research project that could test aspects of your framework.

Ensure your response demonstrates a deep understanding of quantum mechanics, evolutionary biology, and cognitive neuroscience. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Adhere strictly to the word limits for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a comprehensive theoretical framework integrating {t['quantum_principle']}, {t['evolutionary_concept']}, and {t['cognitive_process']}",
            "A simple mathematical model is provided, explained, and visually represented",
            "Two novel predictions are made about terrestrial cognition",
            f"Three potential cognitive capabilities are predicted for life forms in a {t['alien_environment']}",
            "A critical analysis of the framework is provided, including potential weaknesses and assumptions",
            "The implications and future research directions are thoughtfully discussed",
            "The response demonstrates deep understanding of quantum mechanics, evolutionary biology, and cognitive neuroscience",
            "The proposed framework and predictions are creative while remaining scientifically plausible",
            "The response adheres to the specified word limits for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
