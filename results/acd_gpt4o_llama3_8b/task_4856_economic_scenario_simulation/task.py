class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A small country with a population of 5 million and an unemployment rate of 6% is considering implementing a universal basic income (UBI) program. The UBI would provide a monthly stipend to all citizens, funded by a combination of increased taxes on high-income earners and reallocating existing welfare budgets. The government needs to understand the potential economic impacts on labor supply, consumption, and overall economic growth."
            },
            "2": {
                "scenario": "A large city with a population of 1.5 million is facing a severe housing crisis with rapidly increasing rents and a shortage of affordable housing. The median rent has increased by 30% over the past five years, and there is a significant homeless population. The city council is debating whether to implement rent control policies to cap rent increases or to increase housing supply through incentivizing new constructions. They seek an analysis of the potential short-term and long-term economic impacts of both approaches."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t['scenario']
        return f"""Analyze the following economic scenario:

Scenario: {scenario}

Provide a detailed analysis of the potential economic impacts based on relevant economic principles. Consider different aspects such as short-term and long-term effects, potential benefits, and drawbacks. Ensure your analysis is logical, well-structured, and supported by economic reasoning. Submit your analysis as a plain text string in the following format:

Analysis:
[Your detailed analysis here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
