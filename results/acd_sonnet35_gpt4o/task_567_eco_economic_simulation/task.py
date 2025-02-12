import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "resource": "rare earth metals",
                "industry": "electronics manufacturing",
                "environmental_factor": "water pollution"
            },
            "2": {
                "resource": "timber",
                "industry": "construction",
                "environmental_factor": "deforestation"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a game-theoretic model of a circular economy focused on {t['resource']} in the {t['industry']} industry, considering the environmental impact of {t['environmental_factor']}. Your task has the following components:

1. Model Design (250-300 words):
   a) Describe the key players in your model (e.g., resource extractors, manufacturers, consumers, recyclers).
   b) Outline the main strategies available to each player.
   c) Explain how the circular economy concept is incorporated into your model.
   d) Describe how you quantify and incorporate the environmental impact ({t['environmental_factor']}) into the model.

2. Game Theory Analysis (200-250 words):
   a) Identify potential Nash equilibria in your model.
   b) Discuss whether these equilibria are environmentally sustainable.
   c) Explain any prisoner's dilemmas or other game-theoretic concepts that emerge in your model.

3. Policy Intervention (150-200 words):
   a) Propose a policy intervention that could shift the equilibrium towards a more sustainable outcome.
   b) Analyze the potential effectiveness and any unintended consequences of this intervention.

4. Long-term Dynamics (150-200 words):
   a) Describe how your model might evolve over time, considering technological advancements and changing consumer preferences.
   b) Discuss any tipping points or feedback loops that could lead to significant shifts in the system.

5. Real-world Application (100-150 words):
   Discuss how insights from your model could be applied to real-world decision-making in the {t['industry']} industry or environmental policy related to {t['environmental_factor']}.

Ensure your response demonstrates a deep understanding of game theory, circular economy principles, and environmental science. Be creative in your approach while maintaining economic and ecological plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a well-designed game-theoretic model of a circular economy for {t['resource']} in the {t['industry']} industry.",
            f"The model should incorporate the environmental impact of {t['environmental_factor']}.",
            "The response should include a thorough game theory analysis, including Nash equilibria and sustainability considerations.",
            "The proposed policy intervention should be logical and well-analyzed.",
            "The discussion of long-term dynamics should demonstrate understanding of complex systems and feedback loops.",
            "The real-world application should be practical and relevant to the given industry and environmental factor."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
