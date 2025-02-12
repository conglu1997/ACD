import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "environment": "A planet with extreme temperature fluctuations",
                "societal_value": "Collective survival and resource conservation"
            },
            {
                "environment": "A gas giant with floating cities",
                "societal_value": "Technological innovation and energy efficiency"
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(random.sample(scenarios, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a fictional economic system for an alien civilization living in the following scenario:

Environment: {t['environment']}
Key Societal Value: {t['societal_value']}

Your task is to create a coherent and innovative economic system that addresses the unique challenges and values of this alien society. Your response should include:

1. A name for your economic system (be creative but clear).
2. A brief overview of how the system works (2-3 sentences).
3. Explanation of how the system addresses the environmental challenges (2-3 sentences).
4. Description of how the system reflects and promotes the key societal value (2-3 sentences).
5. One unique economic concept or mechanism central to your system (1-2 sentences).
6. Potential challenges or drawbacks of your system (1-2 sentences).
7. A simple example of how a common economic transaction would work in this system (2-3 sentences).

Ensure your economic system is logically consistent, creative, and demonstrates an understanding of basic economic principles while adapting them to the alien context."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes a creative and clear name for the economic system",
            "The economic system addresses the specified environmental challenges",
            "The system reflects and promotes the given key societal value",
            "The response introduces at least one unique economic concept or mechanism",
            "The system is logically consistent and demonstrates understanding of basic economic principles",
            "The response includes a coherent example of how a transaction would work in this system",
            "The economic system is innovative and not simply a minor variation of existing Earth-based systems"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
