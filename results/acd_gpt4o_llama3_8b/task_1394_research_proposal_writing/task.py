class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_description": "Write a research proposal for a study investigating the effects of microgravity on plant growth.",
                "instructions": "Compose a detailed research proposal for a study investigating the effects of microgravity on plant growth. Your proposal should include the following sections: 1. Introduction and Background: Overview of the topic and previous research. 2. Hypothesis: Clearly state the hypothesis to be tested. 3. Methodology: Describe the experimental design, materials, and methods. 4. Expected Results: Outline the anticipated outcomes. 5. Significance: Explain the potential impact of the research. Submit your proposal as a plain text string formatted as follows:\n\nIntroduction and Background:\n[Description]\n\nHypothesis:\n[Description]\n\nMethodology:\n[Description]\n\nExpected Results:\n[Description]\n\nSignificance:\n[Description]\n"
            },
            "2": {
                "task_description": "Write a research proposal for a study exploring the use of AI in early diagnosis of Alzheimer's disease.",
                "instructions": "Compose a detailed research proposal for a study exploring the use of AI in early diagnosis of Alzheimer's disease. Your proposal should include the following sections: 1. Introduction and Background: Overview of the topic and previous research. 2. Hypothesis: Clearly state the hypothesis to be tested. 3. Methodology: Describe the experimental design, materials, and methods. 4. Expected Results: Outline the anticipated outcomes. 5. Significance: Explain the potential impact of the research. Submit your proposal as a plain text string formatted as follows:\n\nIntroduction and Background:\n[Description]\n\nHypothesis:\n[Description]\n\nMethodology:\n[Description]\n\nExpected Results:\n[Description]\n\nSignificance:\n[Description]\n"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a detailed research proposal for the following study: {t['task_description']}. Include the specified sections and describe each in detail. Here are the detailed instructions:\n\n{t['instructions']}\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The proposal should be logically structured and coherent.",
            "Each section should be accurately described and comprehensive.",
            "The proposal should demonstrate a clear understanding of scientific research methods."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
