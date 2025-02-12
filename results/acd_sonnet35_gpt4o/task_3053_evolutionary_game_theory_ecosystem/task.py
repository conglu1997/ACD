import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = [
            {
                "name": "Coral Reef",
                "species": ["coral", "clownfish", "sea urchin", "parrotfish", "shark"],
                "resources": ["space", "food", "protection"]
            },
            {
                "name": "Savanna",
                "species": ["acacia tree", "giraffe", "lion", "zebra", "dung beetle"],
                "resources": ["water", "vegetation", "prey"]
            }
        ]
        
        return {
            "1": random.choice(ecosystems),
            "2": random.choice(ecosystems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze a simulated ecosystem using principles of evolutionary game theory and artificial intelligence to model strategic decision-making among species. Focus on the {t['name']} ecosystem, which includes the following species: {', '.join(t['species'])}. The key resources in this ecosystem are: {', '.join(t['resources'])}.

Your task has six parts:

1. Ecosystem Modeling (300-350 words):
   a) Describe the key interactions and relationships between the species in the {t['name']} ecosystem.
   b) Explain how the available resources influence these interactions.
   c) Propose a mathematical model to represent the ecosystem's dynamics, including equations for population growth, resource consumption, and species interactions.

2. Game Theory Framework (250-300 words):
   a) Define the players, strategies, and payoffs for a game theory model of this ecosystem.
   b) Explain how evolutionary stability can be incorporated into your model.
   c) Describe at least one potential evolutionary stable strategy (ESS) in this ecosystem.

3. AI Integration (250-300 words):
   a) Design an AI system to simulate and analyze the strategic decisions of species in your ecosystem.
   b) Explain how your AI system incorporates principles of evolutionary game theory.
   c) Describe how your AI system could learn and adapt strategies over time.

4. Simulation and Analysis (300-350 words):
   a) Outline a simulation of your ecosystem over 100 generations.
   b) Analyze the emerging patterns and strategies in your simulation.
   c) Discuss any unexpected outcomes or emergent behaviors.
   d) Explain how your results compare to real-world observations of the {t['name']} ecosystem.

5. Environmental Perturbation (200-250 words):
   a) Introduce a significant environmental change to your ecosystem (e.g., climate change, invasive species).
   b) Predict how this change would affect the game theory dynamics and evolutionary strategies.
   c) Describe how your AI system would adapt to this change.

6. Ethical and Practical Implications (200-250 words):
   a) Discuss the potential applications of your model in conservation biology or resource management.
   b) Address any ethical considerations in using AI to model and potentially influence natural ecosystems.
   c) Propose an extension of your model to address a real-world ecological challenge.

Ensure your response demonstrates a deep understanding of game theory, evolutionary biology, and artificial intelligence. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of game theory, evolutionary biology, and artificial intelligence.",
            "The ecosystem model and game theory framework are well-defined and scientifically plausible.",
            "The AI system design effectively incorporates principles of evolutionary game theory.",
            "The simulation analysis provides insightful observations about ecosystem dynamics.",
            "The response addresses the impact of environmental perturbation on the ecosystem model.",
            "Ethical and practical implications are thoughtfully discussed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
