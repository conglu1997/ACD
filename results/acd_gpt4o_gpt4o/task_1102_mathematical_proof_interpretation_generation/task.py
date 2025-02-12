class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "proof": "Let x be an element of a set S. Assume that for all y in S, x+y is also in S. Prove that S is closed under addition.", "question": "Is the given proof valid? Explain why or why not."},
            "2": {"task_type": "generate", "description": "Generate a proof for the statement: 'The sum of two even numbers is always even.'", "criteria": "The proof should be clear, logical, and mathematically rigorous."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpret":
            instructions = f"""Your task is to interpret the given mathematical proof and determine its validity. Provide a detailed explanation of why the proof is valid or invalid.

Proof: {t['proof']}

Question: {t['question']}

Provide your response in plain text format. Ensure your explanation is thorough and logically sound. Here is an example of how your response should look:

Response: The proof is invalid because...

Your explanation should address all logical steps and assumptions made in the proof."""
        else:
            instructions = f"""Your task is to generate a mathematical proof based on the following statement:

{t['description']}

Ensure that the proof is clear, logical, and mathematically rigorous. Provide your response in plain text format. Your proof should include all necessary steps and justifications. Here is an example of how your response should look:

Proof: Let a and b be two even numbers...

Your proof should be structured logically and cover all necessary steps."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "interpret":
            criteria = ["The response should correctly assess the validity of the given proof.", "The explanation should be thorough and logically sound.", "The response should address all logical steps and assumptions made in the proof."]
        else:
            criteria = ["The generated proof should be clear, logical, and mathematically rigorous.", "All necessary steps and justifications should be included.", "The proof should be structured logically and cover all necessary steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
