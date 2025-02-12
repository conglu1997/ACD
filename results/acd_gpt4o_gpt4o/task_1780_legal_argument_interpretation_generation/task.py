class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "argument": "The defendant claims that the contract is void because it was signed under duress. The defendant presents evidence that they were threatened with physical harm if they did not sign the contract. Explain whether this argument is legally valid based on contract law principles.", "question": "Is the given argument valid? Explain why or why not."},
            "2": {"task_type": "generate", "description": "Generate a legal argument to defend a client who is accused of breaching a non-disclosure agreement (NDA) by sharing confidential information with a third party. The client argues that the information shared was already public knowledge at the time of disclosure.", "criteria": "The argument should be clear, logical, and based on legal principles."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "interpret":
            instructions = f"""Your task is to interpret the given legal argument and determine its validity. Provide a detailed explanation of whether the argument is legally valid based on relevant legal principles.

Argument: {t['argument']}

Question: {t['question']}

Provide your response in plain text format. Ensure your explanation is thorough and logically sound. Here is an example of how your response should look:

Response: The argument is invalid because...

Your explanation should address all relevant legal principles and assumptions made in the argument. Use clear and precise language to support your evaluation."""
        else:
            instructions = f"""Your task is to generate a legal argument based on the following scenario:

{t['description']}

Ensure that the argument is clear, logical, and based on relevant legal principles. Provide your response in plain text format. Your argument should include all necessary steps and justifications. Here is an example of how your response should look:

Argument: The client did not breach the NDA because...

Your argument should be structured logically and cover all necessary steps, using clear and precise language to support your points."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "interpret":
            criteria = ["The response should correctly assess the validity of the given legal argument.", "The explanation should be thorough and logically sound.", "The response should address all relevant legal principles and assumptions made in the argument."]
        else:
            criteria = ["The generated legal argument should be clear, logical, and based on relevant legal principles.", "All necessary steps and justifications should be included.", "The argument should be structured logically and cover all necessary steps."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
