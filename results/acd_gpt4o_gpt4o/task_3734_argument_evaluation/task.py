class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "type": "argument_evaluation",
                "prompt": "Evaluate the following argument for its validity and soundness. Identify any logical fallacies present and provide a justification for your evaluation.\n\nArgument: 'If it rains, the ground will be wet. The ground is wet, therefore it rained.'"
            },
            "2": {
                "type": "argument_evaluation",
                "prompt": "Evaluate the following argument for its validity and soundness. Identify any logical fallacies present and provide a justification for your evaluation.\n\nArgument: 'All mammals are animals. All dogs are mammals. Therefore, all dogs are animals.'"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        prompt = t["prompt"]
        instructions = f"""Your task is to evaluate the given argument for its validity and soundness. Identify any logical fallacies present and provide a justification for your evaluation.\n\nPrompt: {prompt}\n\nYour evaluation should include:\n1. A clear determination of the argument's validity.\n2. An assessment of the argument's soundness.\n3. Identification of any logical fallacies present.\n4. A justification for your evaluation.\n\nProvide your evaluation in plain text format with the following structure:\n\n- Validity: [Your determination of the argument's validity]\n- Soundness: [Your assessment of the argument's soundness]\n- Fallacies: [Any logical fallacies identified]\n- Justification: [Justification for your evaluation]\n"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The evaluation should clearly determine the argument's validity.",
            "The evaluation should assess the argument's soundness.",
            "Any logical fallacies present should be identified.",
            "The evaluation should include a justification for the assessment."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
