class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "data": "[{'month': 'January', 'temperature': 5}, {'month': 'February', 'temperature': 7}, {'month': 'March', 'temperature': 10}, {'month': 'April', 'temperature': 15}, {'month': 'May', 'temperature': 20}, {'month': 'June', 'temperature': 25}, {'month': 'July', 'temperature': 30}, {'month': 'August', 'temperature': 28}, {'month': 'September', 'temperature': 22}, {'month': 'October', 'temperature': 18}, {'month': 'November', 'temperature': 10}, {'month': 'December', 'temperature': 5}]", "prompt": "Interpret the given temperature data for the year and provide insights on seasonal variations and trends."},
            "2": {"task_type": "analyze", "data": "[{'year': 2000, 'rainfall': 800}, {'year': 2001, 'rainfall': 750}, {'year': 2002, 'rainfall': 900}, {'year': 2003, 'rainfall': 850}, {'year': 2004, 'rainfall': 870}, {'year': 2005, 'rainfall': 920}, {'year': 2006, 'rainfall': 880}, {'year': 2007, 'rainfall': 860}, {'year': 2008, 'rainfall': 890}, {'year': 2009, 'rainfall': 910}, {'year': 2010, 'rainfall': 930}]", "prompt": "Analyze the given rainfall data over the years and identify any noticeable patterns or anomalies."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following temperature data for the year and provide insights on seasonal variations and trends.\n\nData: {t['data']}\n\nEnsure your interpretation covers the following aspects:\n- Seasonal variations: Describe how temperatures change across different seasons.\n- Trends: Identify any noticeable trends or patterns in the data.\nProvide your response in the following format:\n\nInterpretation:\n- Seasonal Variations: [Your analysis]\n- Trends: [Your analysis]\n\nExample Interpretation:\n- Seasonal Variations: Temperatures increase gradually from January to July, peaking in July, and then decrease towards December.\n- Trends: The data shows a clear pattern of rising temperatures from winter to summer, followed by a decline towards winter."""
        elif t['task_type'] == 'analyze':
            return f"""Your task is to analyze the following rainfall data over the years and identify any noticeable patterns or anomalies.\n\nData: {t['data']}\n\nEnsure your analysis covers the following aspects:\n- Patterns: Describe any consistent patterns observed in the data.\n- Anomalies: Identify any years with unusual rainfall compared to others.\nProvide your response in the following format:\n\nAnalysis:\n- Patterns: [Your analysis]\n- Anomalies: [Your analysis]\n\nExample Analysis:\n- Patterns: Rainfall generally fluctuates around 850-900 mm per year.\n- Anomalies: The year 2002 shows significantly higher rainfall at 900 mm, while 2001 shows lower rainfall at 750 mm."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ["The response should be formatted with headings for 'Seasonal Variations' and 'Trends'.", "The interpretation must cover both aspects in detail.", "The analysis must be relevant to the given data."]
        elif t['task_type'] == 'analyze':
            criteria = ["The response should be formatted with headings for 'Patterns' and 'Anomalies'.", "The analysis must cover both aspects in detail.", "The analysis must be relevant to the given data."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
