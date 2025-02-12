import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "name": "Resource Allocation",
                "players": ["Government", "Private Sector", "NGOs"],
                "resources": ["Financial", "Human", "Technological"],
                "objectives": ["Economic Growth", "Social Welfare", "Environmental Sustainability"]
            },
            {
                "name": "Global Trade Negotiation",
                "players": ["Developed Nations", "Emerging Economies", "International Organizations"],
                "resources": ["Raw Materials", "Intellectual Property", "Market Access"],
                "objectives": ["Economic Dominance", "Technological Advancement", "Equitable Development"]
            },
            {
                "name": "Cybersecurity Arms Race",
                "players": ["Nation States", "Tech Companies", "Hacker Groups"],
                "resources": ["Zero-day Exploits", "AI Defense Systems", "Cyber Workforce"],
                "objectives": ["Information Dominance", "Privacy Protection", "Technological Superiority"]
            },
            {
                "name": "Pandemic Response",
                "players": ["Health Organizations", "Pharmaceutical Companies", "Local Governments"],
                "resources": ["Vaccines", "Medical Infrastructure", "Public Trust"],
                "objectives": ["Disease Containment", "Economic Stability", "Scientific Advancement"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an adaptive game theory simulation that models complex social dynamics and strategic decision-making in the context of {t['name']}. Your simulation should incorporate the following elements:

1. Game Structure (250-300 words):
   a) Define the game's players: {', '.join(t['players'])}
   b) Specify the resources: {', '.join(t['resources'])}
   c) Outline the objectives: {', '.join(t['objectives'])}
   d) Describe the basic rules and constraints of the game
   e) Explain how the game incorporates incomplete information and uncertainty

2. Adaptive Mechanisms (200-250 words):
   a) Design mechanisms for players to learn and adapt their strategies over time
   b) Explain how the game environment evolves in response to players' actions
   c) Describe how new strategies or options can emerge during gameplay

3. AI Implementation (250-300 words):
   a) Propose an AI architecture to model player behavior and decision-making
   b) Explain how your AI system incorporates game theory principles
   c) Describe how the AI adapts to changing game dynamics and opponent strategies
   d) Discuss any novel features that distinguish your AI from traditional game-playing algorithms
   e) Provide a simple pseudocode or flowchart description of your proposed AI system

4. Equilibrium Analysis (200-250 words):
   a) Discuss potential equilibrium states in your game
   b) Explain how these equilibria might shift as the game evolves
   c) Analyze the stability and efficiency of these equilibria

5. Real-world Applications (150-200 words):
   a) Discuss how your simulation could provide insights into real-world {t['name']} scenarios
   b) Propose two specific applications of your model in policy-making or strategic planning
   c) Provide a brief case study illustrating how your model could be applied to a current real-world situation

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues in using AI for modeling social dynamics and decision-making
   b) Discuss the implications of using such simulations for real-world policy decisions
   c) Propose guidelines for the responsible development and use of adaptive game theory simulations

Ensure your response demonstrates a deep understanding of game theory, AI, and complex social systems. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your answer with clear headings for each section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of game theory principles and their application in AI systems.",
            "The proposed adaptive mechanisms and AI implementation are innovative and well-explained, including a clear pseudocode or flowchart description.",
            "The equilibrium analysis shows a nuanced understanding of complex strategic interactions.",
            "The real-world applications and case study are thoughtful, relevant, and well-illustrated.",
            "The ethical considerations are comprehensive and show critical thinking about the implications of the technology.",
            f"The simulation effectively models the specified scenario: {t['name']}."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
