class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"concept": "electric current", "analogy": "water flow in pipes"},
            "2": {"concept": "cellular respiration", "analogy": "a car engine burning fuel"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        concept = t["concept"]
        analogy = t["analogy"]
        instructions = f"""Your task is to create an analogy to explain the given scientific concept. Use the provided analogy as a basis, and explain in detail how the analogy helps to understand the concept.

Concept: {concept}
Analogy: {analogy}

Provide your response in the following format:

Analogy Explanation:
[Your detailed explanation of how the analogy relates to the concept]

Here are some guidelines for creating a good analogy:
1. Ensure the analogy is relevant and closely related to the concept.
2. Cover multiple aspects of the concept in your analogy.
3. Make sure the explanation is clear, detailed, and logically connects the analogy to the concept.

Example:
Concept: electric current
Analogy: water flow in pipes

Analogy Explanation:
Electric current can be compared to water flowing through pipes. Just as water flows from a region of high pressure to low pressure, electric current flows from a region of high voltage to low voltage. The pipes represent the wires, and any restrictions in the pipes (like narrow sections) are analogous to resistors that limit the flow of current. Similarly, a pump that pushes water through the pipes is analogous to a battery or power source that drives the current through the circuit."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analogy should be clear and relevant to the concept.", "The explanation should cover multiple aspects of the concept and be detailed.", "The explanation should logically relate the analogy to the concept."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
