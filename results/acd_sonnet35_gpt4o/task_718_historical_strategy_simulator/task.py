import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        historical_events = [
            {
                "event": "Cuban Missile Crisis (1962)",
                "context": "Cold War tensions between the USA and USSR reach a critical point over nuclear missiles in Cuba.",
                "actual_outcome": "Diplomatic resolution achieved through a combination of blockade and negotiations.",
                "game_theory_concept": "Brinkmanship"
            },
            {
                "event": "Treaty of Versailles (1919)",
                "context": "Negotiation of peace terms after World War I, primarily between the Allied Powers and Germany.",
                "actual_outcome": "Harsh terms imposed on Germany, contributing to future conflicts.",
                "game_theory_concept": "Bargaining and Negotiation Theory"
            },
            {
                "event": "Yalta Conference (1945)",
                "context": "Meeting of Allied leaders to discuss post-World War II reorganization of Europe.",
                "actual_outcome": "Division of Europe into spheres of influence, setting the stage for the Cold War.",
                "game_theory_concept": "Coalition Formation"
            },
            {
                "event": "Opium Wars (1839-1842 and 1856-1860)",
                "context": "Conflicts between Western powers and Qing dynasty China over trade and diplomacy.",
                "actual_outcome": "China forced to open ports and grant concessions to Western powers.",
                "game_theory_concept": "Asymmetric Conflict"
            },
            {
                "event": "Congress of Vienna (1814-1815)",
                "context": "European powers negotiate a balance of power after the Napoleonic Wars.",
                "actual_outcome": "Establishment of a new political order in Europe based on conservatism and legitimism.",
                "game_theory_concept": "Balance of Power Theory"
            }
        ]
        return {str(i+1): event for i, event in enumerate(random.sample(historical_events, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the historical event '{t['event']}' and propose an alternative strategy using game theory principles. Your task has the following components:

1. Historical Analysis (150-200 words):
   a) Briefly describe the key actors involved and their motivations.
   b) Explain the strategic dilemmas faced by the main parties.
   c) Analyze the actual outcome in terms of game theory, particularly focusing on the concept of {t['game_theory_concept']}.

2. Alternative Strategy (200-250 words):
   a) Propose an alternative strategy for one of the main actors, based on game theory principles.
   b) Explain how this strategy applies {t['game_theory_concept']} or another relevant game theory concept.
   c) Discuss potential short-term and long-term consequences of this strategy.

3. Counterfactual Scenario (200-250 words):
   a) Describe a plausible alternate historical outcome based on your proposed strategy.
   b) Analyze how this outcome might have affected subsequent historical events.
   c) Discuss potential unintended consequences of this alternate scenario.

4. Strategic Insights (150-200 words):
   a) Extract general strategic principles from this analysis that could be applied to modern international relations or business scenarios.
   b) Discuss the limitations of applying game theory to complex historical events.

Ensure your response demonstrates a deep understanding of the historical context, game theory principles, and strategic decision-making. Use appropriate terminology and provide clear explanations. Be creative in your alternate scenario while maintaining historical plausibility.

Cite at least one historical source or reference to support your analysis.

Format your response with clear headings for each section, adhering to the word limits provided. Your total response should not exceed 900 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must analyze the specific historical event '{t['event']}' and its context",
            f"The analysis should correctly apply the game theory concept of {t['game_theory_concept']}",
            "The proposed alternative strategy should be creative yet historically plausible",
            "The counterfactual scenario should logically follow from the proposed strategy and consider potential consequences",
            "The response should demonstrate a deep understanding of historical context and strategic decision-making",
            "The strategic insights should be applicable to modern scenarios and acknowledge limitations",
            "The response should be well-structured, clear, and adhere to the specified word limits",
            "At least one historical source or reference should be cited to support the analysis",
            "The total response should not exceed 900 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
