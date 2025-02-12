import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "event": "World War II",
                "year": 1939,
                "advancement": "Artificial Intelligence"
            },
            {
                "event": "The Industrial Revolution",
                "year": 1760,
                "advancement": "Fusion Energy"
            },
            {
                "event": "The American Revolution",
                "year": 1775,
                "advancement": "Genetic Engineering"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the historical event '{t['event']}' (which began around {t['year']}) and create an alternative scenario where the technology of '{t['advancement']}' was introduced during this time period. Then, explore the consequences of this change.

Your response should include:

1. Brief Overview (2-3 sentences):
   Summarize the key aspects of the original historical event.

2. Scientific Advancement (2-3 sentences):
   Describe how the given advanced technology could have realistically been developed at that time, considering the era's scientific knowledge and resources.

3. Alternative Scenario (3-4 sentences):
   Create a plausible alternative outcome of the historical event, incorporating the advanced technology. Be creative but logical in your approach.

4. Short-term Consequences (2-3 sentences):
   Analyze the immediate effects of this change on the course of history.

5. Long-term Impact (3-4 sentences):
   Explore how this alternative scenario might have affected the world up to the present day, considering political, social, and technological aspects.

6. Ethical Implications (2-3 sentences):
   Discuss potential ethical concerns or dilemmas arising from this alternative history.

Ensure your response is creative yet grounded in historical and scientific plausibility. Demonstrate a nuanced understanding of the interplay between technology, history, and society."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response should include a brief overview of the original {t['event']}",
            f"The response should describe how {t['advancement']} could have been developed in {t['year']}",
            "The response should create a plausible alternative historical scenario",
            "The response should analyze both short-term and long-term consequences",
            "The response should discuss ethical implications of the alternative history",
            "The response should demonstrate understanding of historical, scientific, and societal concepts",
            "The response should follow the specified format"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
