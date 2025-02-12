class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {'parameters': 'Create a device that can help reduce air pollution in urban areas.'},
            '2': {'parameters': 'Design an invention that can improve water conservation in agricultural practices.'}
        }
        assert len(tasks) == 2, 'There should be exactly two tasks.'
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate an innovative and feasible idea for a scientific invention based on the following parameters.

Parameters: {t['parameters']}

Provide a detailed description of your invention, including its purpose, how it works, and the scientific principles it relies on. Ensure that your description is clear, logical, and demonstrates both creativity and scientific understanding. Provide your response in plain text format.
Example format:
1. Purpose: [Describe the purpose of the invention]
2. Mechanism: [Explain how the invention works]
3. Scientific Principles: [Detail the scientific principles it relies on]
4. Feasibility: [Discuss the feasibility of the invention and potential challenges]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            'The response should include a clear purpose for the invention.',
            'The mechanism of how the invention works should be explained logically.',
            'The response should demonstrate an understanding of relevant scientific principles.',
            'The idea should be innovative and feasible.',
            'The response should discuss the feasibility and potential challenges of the invention.'
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
