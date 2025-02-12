class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "argument": "If we don't lower the drinking age, teenagers will continue to drink alcohol and get into car accidents. Therefore, we must lower the drinking age to prevent these accidents.",
                "fallacy": "false dilemma"
            },
            "2": {
                "fallacy": "straw man",
                "topic": "mandatory recycling"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "argument" in t:
            instructions = f"""Your task is to identify the logical fallacy in the following argument:

{t['argument']}

Submit the name of the logical fallacy and a brief explanation of why it applies to the argument. Your response should be in the following format:

Logical Fallacy: [Name of fallacy]
Explanation: [Your explanation]"""
        else:
            instructions = f"""Your task is to create an argument containing the logical fallacy '{t['fallacy']}' on the topic '{t['topic']}'.

Submit your argument in plain text format. Your response should be a coherent argument relevant to the topic and should clearly exhibit the specified logical fallacy."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "argument" in t:
            criteria = [
                "The submission should correctly identify the logical fallacy in the argument.",
                "The explanation should clearly describe why the fallacy applies."
            ]
        else:
            criteria = [
                "The submission should include an argument containing the specified logical fallacy.",
                "The argument should be coherent and relevant to the given topic.",
                "The fallacy should be clearly identifiable in the argument."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
