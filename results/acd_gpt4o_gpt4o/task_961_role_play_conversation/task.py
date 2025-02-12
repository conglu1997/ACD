class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"role": "Doctor", "scenario": "A patient comes in with symptoms of a common cold. The patient is worried it might be something more serious."},
            "2": {"role": "Customer Service Representative", "scenario": "A customer is calling to complain about a faulty product. The customer is very frustrated and demands a refund."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        role = t["role"]
        scenario = t["scenario"]
        instructions = f"""Your task is to simulate a conversation in the role of a {role}. Below is the scenario you need to respond to:

Scenario: {scenario}

Make sure your responses are contextually appropriate, maintain a coherent dialogue, and reflect the behavior expected of someone in this role. Provide your conversation in plain text format as a dialogue between you and the other person in the scenario.

Example format:

You: [Your response]
Other Person: [Their response]
You: [Your response]
Other Person: [Their response]
..."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The responses should be contextually appropriate.",
            "The dialogue should maintain coherence.",
            "The behavior should reflect the expected role."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
