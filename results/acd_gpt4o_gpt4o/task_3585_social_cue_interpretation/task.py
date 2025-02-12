class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"dialogue": "Person A: 'I guess I'll just go home then.'\nPerson B: 'Yeah, maybe that's for the best.'"},
            "2": {"dialogue": "Person A: 'Are you coming to the party tonight?'\nPerson B: 'Oh, I didn't know there was a party.'"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        dialogue = t["dialogue"]
        instructions = f"""Your task is to interpret the implicit social cues present in the following dialogue and explain the underlying emotions or intentions of the speakers. Analyze the dialogue carefully and provide a detailed explanation of what each person might be feeling or intending based on their words and the context.

Dialogue:
{dialogue}

Your response should include:
1. Interpretation: [Your interpretation of the social cues]
2. Explanation: [Your explanation of the underlying emotions or intentions]
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The interpretation should accurately reflect the implicit social cues.",
            "The explanation should clearly describe the underlying emotions or intentions.",
            "The response should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
