class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "Imagine a society where all actions are determined by a central algorithm that maximizes overall happiness. Critically analyze the ethical implications of such a society from the perspective of utilitarianism and deontology.", "principles": ["Utilitarianism focuses on the greatest good for the greatest number.", "Deontology emphasizes the importance of rules and duties regardless of outcomes."]},
            "2": {"scenario": "Suppose an AI has achieved a level of consciousness. Discuss the moral status of this AI and whether it should be granted rights similar to humans. Consider arguments from both functionalism and personhood theories.", "principles": ["Functionalism considers mental states in terms of their functional roles.", "Personhood theories focus on characteristics like self-awareness, rationality, and the capacity for suffering."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        principles = "\n".join(t["principles"])
        instructions = f"""Your task is to interpret the following philosophical scenario and provide a reasoned argument or solution based on the given facts and principles:

Scenario: {scenario}

Relevant Philosophical Principles:
{principles}

Your argument should be clear, logical, and philosophically sound. Ensure that you address all relevant aspects of the scenario and apply the philosophical principles accurately. Provide your argument in plain text format."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should address all relevant aspects of the scenario.",
            "The argument should apply the given philosophical principles accurately.",
            "The argument should be clear, logical, and philosophically sound."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
