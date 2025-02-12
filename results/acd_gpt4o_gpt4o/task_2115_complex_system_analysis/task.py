class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data_sources": [
                    "An article discussing the environmental impact of renewable energy sources, highlighting both positive and negative aspects.",
                    "A statistical report on the cost-efficiency of various renewable energy technologies, including detailed figures and comparisons.",
                    "A news piece on recent advancements in solar panel technology, mentioning specific innovations and their potential impact."
                ],
                "decision_prompt": "Based on the given data sources, which renewable energy source should a developing country invest in and why?"
            },
            "2": {
                "data_sources": [
                    "A research paper on the health benefits of a balanced diet, providing scientific evidence and case studies.",
                    "A survey report on dietary habits of different age groups, including statistical data and trends.",
                    "An interview with a nutritionist discussing the latest dietary trends, with specific recommendations and insights."
                ],
                "decision_prompt": "Based on the given data sources, what dietary recommendations would you make for a middle-aged adult aiming to improve their overall health and why?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to analyze the following data sources and make an informed decision based on the given prompt:

Data Sources:
1. {t['data_sources'][0]}
2. {t['data_sources'][1]}
3. {t['data_sources'][2]}

Decision Prompt: {t['decision_prompt']}

Ensure that your response is coherent, well-structured, and considers all the provided data sources. Provide your response in the following format:

1. Analysis: [Your analysis of the data sources]
2. Decision: [Your informed decision based on the analysis]
3. Justification: [Your justification for the decision]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should consider all provided data sources.",
            "The decision should be coherent and based on the analysis.",
            "The justification should clearly explain the reasoning behind the decision."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
