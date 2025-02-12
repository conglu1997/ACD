import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        neural_processes = [
            "synaptic plasticity",
            "neuronal oscillations",
            "predictive coding",
            "lateral inhibition",
            "spike-timing-dependent plasticity"
        ]
        environmental_phenomena = [
            "climate change patterns",
            "ecosystem dynamics",
            "ocean current systems",
            "atmospheric circulation",
            "biogeochemical cycles"
        ]
        ai_techniques = [
            "deep learning",
            "reinforcement learning",
            "evolutionary algorithms",
            "Bayesian networks",
            "reservoir computing"
        ]
        constraints = [
            "limited computational resources",
            "real-time processing requirements",
            "sparse data availability",
            "high noise levels in environmental data",
            "need for interpretable results"
        ]
        return {
            "1": {
                "neural_process": random.choice(neural_processes),
                "environmental_phenomenon": random.choice(environmental_phenomena),
                "ai_technique": random.choice(ai_techniques),
                "constraint": random.choice(constraints)
            },
            "2": {
                "neural_process": random.choice(neural_processes),
                "environmental_phenomenon": random.choice(environmental_phenomena),
                "ai_technique": random.choice(ai_techniques),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that mimics the neural process of {t['neural_process']} to model and predict the environmental phenomenon of {t['environmental_phenomenon']}, incorporating the AI technique of {t['ai_technique']}. Your system must also address the constraint of {t['constraint']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the main components of your AI system and their functions.
   b) Explain how your system integrates principles from neuroscience, environmental science, and artificial intelligence.
   c) Detail how the system incorporates {t['neural_process']} in its design and processing.
   d) Discuss how the system is adapted to model and predict {t['environmental_phenomenon']}.
   e) Explain how the system leverages {t['ai_technique']} in its implementation.
   f) Address how your system design accounts for the constraint of {t['constraint']}.

2. Neural-Environmental Mapping (250-300 words):
   a) Describe the process by which your system maps neural-inspired computations to environmental modeling.
   b) Explain how the system interprets and translates environmental data using principles from {t['neural_process']}.
   c) Provide an example of how the system would model a specific aspect of {t['environmental_phenomenon']} using this neural-inspired approach.
   d) Discuss how the system ensures accuracy and reliability in its environmental predictions, considering {t['constraint']}.

3. AI Integration and Optimization (250-300 words):
   a) Explain how {t['ai_technique']} is used to enhance the neural-inspired environmental modeling.
   b) Describe the key parameters or objectives that the AI system optimizes.
   c) Discuss how the AI system adapts to new environmental data or unexpected patterns.
   d) Propose a method for validating the AI's predictions and improving its performance over time.
   e) Explain how your AI approach addresses or mitigates {t['constraint']}.

4. Comparative Analysis (200-250 words):
   a) Compare your neural-inspired approach to traditional methods of modeling {t['environmental_phenomenon']}.
   b) Discuss potential advantages and limitations of your system, particularly in light of {t['constraint']}.
   c) Explain how your system might provide new insights into {t['environmental_phenomenon']} that traditional models might miss.

5. Applications and Implications (200-250 words):
   a) Suggest three potential real-world applications of your neural-inspired environmental modeling system.
   b) Discuss the ethical implications of using AI and neuroscience-inspired approaches in environmental science.
   c) Analyze potential risks and propose safeguards for this technology.
   d) Speculate on how this technology might impact future environmental policy and decision-making.

6. Future Directions and Challenges (150-200 words):
   a) Propose two potential improvements or extensions to your system.
   b) Identify key challenges that need to be overcome for real-world implementation, especially considering {t['constraint']}.
   c) Suggest areas of research that could significantly advance this interdisciplinary field.

Ensure your response demonstrates a deep understanding of neuroscience, environmental science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should demonstrate a clear understanding of {t['neural_process']} and how it can be applied to environmental modeling.",
            f"The system design should effectively incorporate the AI technique of {t['ai_technique']} and address the constraint of {t['constraint']}.",
            f"The proposed neural-environmental mapping should be innovative and well-explained for modeling {t['environmental_phenomenon']}.",
            "The response should address ethical implications and potential risks of the technology.",
            "The future directions and challenges should be relevant and thought-provoking, considering the given constraint."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
