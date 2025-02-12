import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "scenario": "global_trade_network",
                "actors": ["nations", "multinational corporations", "international organizations"],
                "constraints": ["resource scarcity", "geopolitical tensions", "environmental regulations"]
            },
            {
                "scenario": "urban_transportation_system",
                "actors": ["commuters", "public transit authorities", "ride-sharing companies", "city government"],
                "constraints": ["limited infrastructure", "environmental concerns", "budget constraints"]
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses game theory principles to model and optimize the complex economic system of a {t['scenario']}. Your system should account for the behavior and interactions of {', '.join(t['actors'])}, while considering the constraints of {', '.join(t['constraints'])}. Then, apply your system to propose a novel solution for optimizing this economic scenario. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system and how they integrate game theory with economic modeling.
   b) Explain how your system models the behavior and interactions of the different actors.
   c) Detail how your system incorporates the given constraints into its optimization process.
   d) Include a high-level diagram or pseudocode illustrating your system's structure and processes.

2. Game Theory Implementation (250-300 words):
   a) Explain which specific game theory concepts or models your system uses and why they are appropriate for this scenario.
   b) Describe how your system represents the strategies and payoffs for each actor.
   c) Detail how your AI handles incomplete information and uncertainty in the economic system.

3. Optimization Process (250-300 words):
   a) Describe the step-by-step process your AI system uses to optimize the economic scenario.
   b) Explain how your system balances the potentially conflicting interests of different actors.
   c) Discuss how your system adapts to changing conditions or new information.

4. Novel Solution Proposal (200-250 words):
   a) Present a specific, innovative solution your AI system proposes for optimizing the given economic scenario.
   b) Explain the rationale behind this solution, referencing your system's game theory analysis.
   c) Discuss the potential impacts and trade-offs of implementing this solution.

5. Ethical Considerations (150-200 words):
   a) Discuss the ethical implications of using AI to optimize complex economic systems.
   b) Address potential concerns about fairness, transparency, and accountability in your system's decision-making process.
   c) Propose guidelines for the responsible use of AI in economic policy-making.

6. Limitations and Future Developments (150-200 words):
   a) Identify potential limitations or challenges in your current system.
   b) Suggest two potential enhancements or extensions to your AI system.
   c) Discuss how this technology might evolve and impact the field of economics in the next decade.

Ensure your response demonstrates a deep understanding of game theory, economic principles, and AI technologies. Use appropriate terminology from all relevant fields and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific and economic plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of game theory and economic principles",
            "The AI system design is innovative and plausible",
            "The proposed solution is novel and well-reasoned",
            "The response addresses ethical considerations and limitations adequately",
            f"The response is tailored to the specific scenario of {t['scenario']} and considers the given actors and constraints"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
