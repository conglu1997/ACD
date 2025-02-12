class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "issue": "Homelessness in urban areas",
                "context": "A major city with a growing homeless population and limited resources."
            },
            "2": {
                "issue": "Racial inequality in education",
                "context": "A diverse school district with significant disparities in academic performance and resources between different racial groups."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze the following social issue and provide thoughtful, well-structured recommendations to address it:\n\nIssue: {t['issue']}\nContext: {t['context']}\n\nYour analysis and recommendations should adhere to the following guidelines:\n1. Provide a clear and concise description of the issue and its underlying causes.\n2. Identify key stakeholders and their roles in addressing the issue.\n3. Suggest practical and actionable recommendations to address the issue, considering both short-term and long-term solutions.\n4. Ensure your recommendations are empathetic and take into account the perspectives of those affected by the issue.\n5. Support your recommendations with relevant data, examples, or case studies if possible.\n\nProvide your response in plain text format.\n\nExample Response:\nFor the issue of homelessness in urban areas: 'Homelessness in urban areas is a complex issue driven by factors such as lack of affordable housing, unemployment, and mental health challenges. Key stakeholders include local government, non-profit organizations, and the affected individuals themselves. Short-term solutions might include increasing access to emergency shelters and support services, while long-term solutions could focus on affordable housing projects and job training programs.'"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis provides a clear and concise description of the issue and its underlying causes.",
            "The analysis identifies key stakeholders and their roles in addressing the issue.",
            "The recommendations are practical, actionable, and consider both short-term and long-term solutions.",
            "The recommendations are empathetic and take into account the perspectives of those affected by the issue.",
            "The recommendations are supported with relevant data, examples, or case studies if possible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
