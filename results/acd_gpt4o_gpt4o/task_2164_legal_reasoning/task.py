class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"statute": "In the fictional jurisdiction of Lexland, the following statute applies: 'Any person who intentionally causes physical harm to another shall be guilty of assault and liable to imprisonment for up to 5 years.'", "scenario": "Alex and Jamie were involved in a heated argument at a party. In the heat of the moment, Alex pushed Jamie, causing Jamie to fall and break their arm. Alex claims it was an accident and did not intend to cause harm."},
            "2": {"statute": "In the fictional jurisdiction of Lexland, the following statute applies: 'A person who enters another's property without permission and with the intent to commit a crime therein shall be guilty of burglary and liable to imprisonment for up to 10 years.'", "scenario": "Taylor entered Morgan's house through an open window at night. Taylor did not take anything but was caught by Morgan while looking around. Taylor claims they were just curious and had no intention to steal or commit any crime."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to interpret the given legal statute and apply it to the hypothetical scenario provided. Based on your interpretation, determine whether the individual in the scenario is guilty under the statute and explain your reasoning.

Statute:
{t['statute']}

Scenario:
{t['scenario']}

Instructions:
1. Interpret the legal statute provided.
2. Apply the statute to the scenario and determine whether the individual is guilty.
3. Provide a detailed explanation of your reasoning, addressing all relevant aspects of the statute and scenario.

Your response should be in the following format:
Guilty or Not Guilty: [Your determination]
Reasoning: [Your detailed reasoning]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The determination of guilt should be logically consistent with the statute and scenario.", "The reasoning should be detailed and address all relevant aspects of the statute and scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
