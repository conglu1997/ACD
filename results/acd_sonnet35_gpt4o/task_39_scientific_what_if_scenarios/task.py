import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "principle": "gravity",
                "change": "Earth's gravity suddenly becomes repulsive instead of attractive"
            },
            {
                "principle": "speed of light",
                "change": "The speed of light is reduced to 1 meter per second"
            },
            {
                "principle": "thermodynamics",
                "change": "The Second Law of Thermodynamics is reversed, causing entropy to decrease over time"
            },
            {
                "principle": "electromagnetism",
                "change": "All electromagnetic forces suddenly become 100 times stronger"
            },
            {
                "principle": "quantum mechanics",
                "change": "Quantum superposition becomes observable at the macroscopic level"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a scientific 'what if' scenario based on the following change to a fundamental principle:

{t['change']}

Your task is to:
1. Explain the immediate consequences of this change (2-3 sentences).
2. Describe three long-term effects on the physical world or human society (1-2 sentences each).
3. Propose one creative solution or adaptation that could help mitigate the most severe consequence (2-3 sentences).

Ensure your response is scientifically grounded, logically consistent, and creative in its approach to the altered scenario. Your answer should demonstrate a deep understanding of the scientific principle involved and its interconnections with other aspects of the natural world and human civilization.

Format your response as follows:

Immediate Consequences:
[Your explanation here]

Long-term Effects:
1. [First effect]
2. [Second effect]
3. [Third effect]

Creative Solution:
[Your proposed solution here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the scientific principle and its implications.",
            "The immediate consequences and long-term effects are logically derived from the given change.",
            "The creative solution is innovative and relevant to the scenario.",
            "The answer maintains scientific plausibility while exploring creative outcomes."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
