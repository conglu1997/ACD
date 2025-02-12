class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "statement": "If it rains, then the ground is wet. It is not raining. Therefore, the ground is not wet.",
                "proof": "1. If it rains, then the ground is wet. (Premise)\n2. It is not raining. (Premise)\n3. Therefore, the ground is not wet. (Invalid reasoning)"
            },
            "2": {
                "statement": "If the battery is charged, the device will turn on. The device turned on. Therefore, the battery is charged.",
                "proof": "1. If the battery is charged, the device will turn on. (Premise)\n2. The device turned on. (Premise)\n3. Therefore, the battery is charged. (Affirming the consequent)"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        statement = t["statement"]
        proof = t["proof"]
        instructions = f"""Your task is to generate a formal proof for the following logical statement and verify the provided proof:

Statement: {statement}

Your response should include:
1. A formal proof of the statement.
2. Verification of the provided proof, indicating whether it is correct or not and explaining any errors. Do not use the given proof in your generated proof.

Provide your response in plain text format as follows:

Formal Proof: [Your formal proof]
Verification: [Your verification of the provided proof]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The generated proof should be logically valid.",
            "The verification should accurately identify the correctness of the provided proof and explain any errors.",
            "The response should be clear and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
