class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"article": "In this study, we investigate the effects of a new drug on reducing the symptoms of Alzheimer's disease. We conducted a double-blind, placebo-controlled trial with 200 participants over 6 months. The participants were randomly assigned to either the drug group or the placebo group. We measured cognitive function using the Mini-Mental State Examination (MMSE) at the beginning and end of the study. Our results showed a statistically significant improvement in the MMSE scores of the drug group compared to the placebo group. The improvement was most pronounced in participants with mild to moderate symptoms. These findings suggest that the new drug could be a promising treatment for Alzheimer's disease."},
            "2": {"article": "Climate change is having a profound impact on global biodiversity. In this study, we examined the effects of rising temperatures on the migratory patterns of birds. We collected data from 50 bird species over a period of 10 years. Our analysis revealed that many species are migrating earlier in the spring and later in the fall. This shift in migration timing is associated with changes in temperature and availability of food resources. The findings highlight the need for conservation strategies that consider the impacts of climate change on migratory species."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given article:

Article: {t['article']}

Read the provided scientific article and summarize the main findings, methodology, and conclusions in your own words. Your summary should be concise and clearly convey the key points of the study. Submit your response as a plain text string in the following format:
Summary: [Your summary]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The summary should accurately reflect the main findings of the study.",
            "The summary should accurately describe the methodology used in the study.",
            "The summary should accurately convey the conclusions of the study.",
            "The summary should be concise and clearly written."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
