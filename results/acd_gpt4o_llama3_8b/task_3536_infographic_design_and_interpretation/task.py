class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"data": "Yearly population growth of City X from 2010-2020: 2010: 500,000; 2011: 520,000; 2012: 540,000; 2013: 560,000; 2014: 580,000; 2015: 600,000; 2016: 620,000; 2017: 640,000; 2018: 670,000; 2019: 700,000; 2020: 750,000. Additional data: Median Age: 2010: 30; 2015: 32; 2020: 34. Employment Rate: 2010: 60%; 2015: 62%; 2020: 65%.", "theme": "Demographic Changes"},
            "2": {"infographic": "An infographic showing the distribution of energy sources in Country Y: 40% from fossil fuels, 30% from nuclear energy, 20% from wind energy, and 10% from solar energy.", "question": "What percentage of energy comes from renewable sources according to the infographic?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "data" in t:
            return f"""Design an infographic based on the following data and theme: {t['data']}.

Theme: {t['theme']}

Ensure the infographic is visually appealing, accurately represents the data, and clearly communicates the theme. Provide a detailed description of your infographic, including the layout, colors, icons, and any other visual elements used. Submit your description as a plain text string in the format:

Infographic Description: [Your description]"""
        else:
            return f"""Interpret the following infographic and answer the accompanying question:

Infographic: {t['infographic']}

Question: {t['question']}

Ensure your answer is precise and based on the information provided in the infographic. Submit your answer as a plain text string in the format:

Answer: [Your answer]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "data" in t:
            criteria = ["The infographic description should clearly represent the data provided.", "The description should include details about layout, colors, and visual elements.", "The infographic should accurately communicate the theme of Demographic Changes."]
        else:
            criteria = ["The answer should be precise and based on the provided infographic.", "The answer should clearly address the question regarding the percentage of energy from renewable sources."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
