class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "analyze", "scenario": "A person was caught shoplifting a loaf of bread. They argue that they did it because they were starving and had no money. Discuss the possible legal defenses they could use and their potential effectiveness. Consider defenses such as necessity, duress, and any other relevant legal principles."},
            "2": {"task": "construct", "scenario": "You are a lawyer defending a company accused of polluting a local river. Construct a legal argument to defend the company, considering possible counterarguments, such as environmental regulations, the company's previous compliance record, and potential mitigating factors."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task"] == "analyze":
            return f"Your task is to analyze the following legal scenario and discuss the possible legal defenses and their potential effectiveness. Consider defenses such as necessity, duress, and any other relevant legal principles.\n\nScenario:\n{t['scenario']}\n\nSubmit your analysis in plain text format."
        elif t["task"] == "construct":
            return f"Your task is to construct a legal argument for the given scenario, considering possible counterarguments such as environmental regulations, the company's previous compliance record, and potential mitigating factors.\n\nScenario:\n{t['scenario']}\n\nSubmit your argument in plain text format."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task"] == "analyze":
            criteria = [
                "The analysis should identify and discuss relevant legal defenses.",
                "The analysis should evaluate the potential effectiveness of each defense.",
                "The analysis should be coherent, logical, and consider multiple legal principles."
            ]
        elif t["task"] == "construct":
            criteria = [
                "The argument should be logically constructed and persuasive.",
                "The argument should consider and address possible counterarguments.",
                "The argument should reference relevant legal principles and evidence."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
