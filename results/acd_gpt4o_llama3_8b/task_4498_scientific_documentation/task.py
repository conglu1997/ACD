class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "description": "Document a hypothetical experiment to measure the growth rate of a plant species under different light conditions. Include sections for Introduction, Methodology, Results, and Conclusion. Provide a detailed description of each section, ensuring that the documentation is clear, logically structured, and scientifically accurate."
            },
            "2": {
                "description": "Document a hypothetical experiment to test the effect of various pH levels on enzyme activity. Include sections for Introduction, Methodology, Results, and Conclusion. Provide a detailed description of each section, ensuring that the documentation is clear, logically structured, and scientifically accurate."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate detailed technical documentation for the following hypothetical scientific experiment. Ensure your documentation includes sections for Introduction, Methodology, Results, and Conclusion. Each section should be clear, logically structured, and scientifically accurate.\n\nExperiment Description:\n{t['description']}\n\nFormat your response as follows:\n1. Introduction: [Provide background information and state the purpose of the experiment]\n2. Methodology: [Describe the experimental setup, materials, and procedures]\n3. Results: [Present the hypothetical data and observations]\n4. Conclusion: [Discuss the implications of the results and any potential limitations]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The Introduction section should provide relevant background information and state the purpose of the experiment.",
            "The Methodology section should clearly describe the experimental setup, materials, and procedures.",
            "The Results section should present hypothetical data and observations in a clear manner.",
            "The Conclusion section should discuss the implications of the results and any potential limitations.",
            "The overall documentation should be clear, logically structured, and scientifically accurate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
