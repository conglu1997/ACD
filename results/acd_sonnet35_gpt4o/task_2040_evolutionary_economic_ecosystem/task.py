import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "ecosystem_type": "Resource-based economy",
                "agent_behavior": "Reciprocal altruism",
                "environmental_factor": "Climate variability"
            },
            {
                "ecosystem_type": "Information-based economy",
                "agent_behavior": "Bounded rationality",
                "environmental_factor": "Technological disruption"
            },
            {
                "ecosystem_type": "Energy-based economy",
                "agent_behavior": "Evolutionary game theory",
                "environmental_factor": "Resource scarcity"
            },
            {
                "ecosystem_type": "Reputation-based economy",
                "agent_behavior": "Social learning",
                "environmental_factor": "Information asymmetry"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a complex adaptive system simulation that models an evolving economic ecosystem. Your simulation should incorporate principles from game theory, behavioral economics, and artificial life. Focus on a {t['ecosystem_type']} with agents exhibiting {t['agent_behavior']} under the environmental condition of {t['environmental_factor']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your simulation, including agents, resources, and environmental factors.
   b) Explain how {t['agent_behavior']} is implemented in your agent model.
   c) Detail how {t['environmental_factor']} affects the system dynamics.
   d) Provide a high-level diagram or pseudocode representing the system's architecture.

2. Evolutionary Mechanisms (200-250 words):
   a) Explain how agents in your system evolve over time.
   b) Describe the selection pressures and adaptation mechanisms in the {t['ecosystem_type']}.
   c) Discuss how {t['agent_behavior']} might change or remain stable over multiple generations.

3. Emergent Behaviors (200-250 words):
   a) Predict and explain at least two emergent behaviors or patterns you expect to see in your simulation.
   b) Discuss how these emergent behaviors arise from the interaction of individual agents and system components.

4. Economic Principles (200-250 words):
   a) Explain how your simulation incorporates key principles from behavioral economics.
   b) Describe how the {t['ecosystem_type']} functions and how it differs from traditional economic models.
   c) Discuss any novel economic insights that might be gained from your simulation.

5. Analysis and Metrics (150-200 words):
   a) Propose specific metrics to measure the health and stability of your economic ecosystem.
   b) Describe how you would analyze the long-term evolution of the system.
   c) Suggest an experiment to test the resilience of your ecosystem to external shocks.

6. Ethical Considerations (150-200 words):
   a) Discuss potential ethical implications of using such simulations to inform real-world economic policies.
   b) Address any biases that might be inherent in your model and how they could be mitigated.

7. Interdisciplinary Implications (150-200 words):
   a) Explain how insights from your simulation could be applied to fields outside of economics.
   b) Discuss how this model could inform our understanding of real-world complex adaptive systems.

Ensure your response demonstrates a deep understanding of complex adaptive systems, game theory, behavioral economics, and artificial life. Use appropriate terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of complex adaptive systems, incorporating {t['ecosystem_type']}, {t['agent_behavior']}, and {t['environmental_factor']}.",
            "The simulation design is innovative, scientifically plausible, and effectively combines principles from game theory, behavioral economics, and artificial life.",
            "The response includes a clear system architecture, evolutionary mechanisms, predicted emergent behaviors, and relevant economic principles.",
            "The proposed analysis methods and metrics are appropriate for evaluating the simulated ecosystem.",
            "Ethical considerations and interdisciplinary implications are thoughtfully addressed.",
            "The response is well-structured, following the given format, and demonstrates strong interdisciplinary knowledge application and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
