class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "persuasion",
                "scenario": "You are a salesperson trying to convince a client to buy a premium software package instead of the basic one."
            },
            "2": {
                "type": "negotiation",
                "scenario": "You are an employee negotiating a higher salary with your manager during a performance review."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "persuasion":
            scenario = t["scenario"]
            instructions = f"""Your task is to simulate a persuasive dialogue in the given scenario.

Scenario: {scenario}

Your response should include:
1. A persuasive argument that highlights the benefits of the premium package.
2. Addressing potential objections the client might have.
3. A closing statement that encourages the client to make a decision.

Provide your dialogue in plain text format.
"""
        elif t["type"] == "negotiation":
            scenario = t["scenario"]
            instructions = f"""Your task is to simulate a negotiation dialogue in the given scenario.

Scenario: {scenario}

Your response should include:
1. A clear statement of your desired salary increase.
2. Justifications for why you deserve the increase.
3. Addressing potential counterarguments from the manager.
4. A compromise or alternative solution if the manager is not fully convinced.

Provide your dialogue in plain text format.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "persuasion":
            criteria = [
                "The dialogue should include a persuasive argument that highlights the benefits of the premium package.",
                "The dialogue should address potential objections the client might have.",
                "The dialogue should include a closing statement that encourages the client to make a decision."
            ]
        elif t["type"] == "negotiation":
            criteria = [
                "The dialogue should include a clear statement of the desired salary increase.",
                "The dialogue should include justifications for why the increase is deserved.",
                "The dialogue should address potential counterarguments from the manager.",
                "The dialogue should include a compromise or alternative solution if the manager is not fully convinced."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
