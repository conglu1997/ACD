class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"event": "The fall of the Berlin Wall in 1989", "query": "Analyze the significance of this event in world history. Discuss its impact on the political landscape, economic conditions, and social changes in Europe."},
            "2": {"hypothetical_change": "What if the Roman Empire had never fallen?", "query": "Predict the potential outcomes and global implications if the Roman Empire had continued to exist and thrive. Consider political, cultural, and technological aspects in your response."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'event' in t:
            return f"""Your task is to analyze the significance of the following historical event:\n\nEvent: {t['event']}\n\n{t['query']}\n\nEnsure that your analysis is detailed, covers multiple aspects (political, economic, social), and is historically accurate. Provide your response in plain text format.\n\nYour response should be in the following format:\n\nAnalysis: [Your detailed analysis here]"""
        elif 'hypothetical_change' in t:
            return f"""Your task is to predict the potential outcomes of the following hypothetical historical change:\n\nHypothetical Change: {t['hypothetical_change']}\n\n{t['query']}\n\nEnsure that your prediction is logical, covers multiple aspects (political, cultural, technological), and is grounded in historical context. Provide your response in plain text format.\n\nYour response should be in the following format:\n\nPrediction: [Your detailed prediction here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'event' in t:
            criteria = ["The analysis should be detailed and cover political, economic, and social aspects.", "The analysis should be historically accurate."]
        else:
            criteria = ["The prediction should be logical and cover political, cultural, and technological aspects.", "The prediction should be grounded in historical context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
