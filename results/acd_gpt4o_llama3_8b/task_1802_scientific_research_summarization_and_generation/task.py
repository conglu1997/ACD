class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"abstract": "Machine learning (ML) has revolutionized various industries by leveraging data to make informed decisions. This research explores the application of ML techniques in healthcare, focusing on disease prediction and personalized treatment planning. The study demonstrates significant improvements in predictive accuracy and patient outcomes through the integration of ML models."},
            "2": {"title": "Advancements in Renewable Energy Technologies for Sustainable Development", "keywords": ["renewable energy", "sustainable development", "solar power", "wind energy"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "abstract" in t:
            return f"""Summarize the following scientific research abstract:

'{t['abstract']}'

Ensure your summary captures the main points and is concise and coherent. Submit your response as a plain text string."""
        elif "title" in t and "keywords" in t:
            return f"""Generate a scientific research abstract based on the following title and keywords:

Title: {t['title']}
Keywords: {', '.join(t['keywords'])}

Ensure your abstract is informative, coherent, and incorporates the given title and keywords effectively. Submit your response as a plain text string."""
        else:
            raise ValueError("Invalid task format")

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "abstract" in t:
            criteria = ["The summary should capture the main points of the research.", "The summary should be concise and coherent."]
        elif "title" in t and "keywords" in t:
            criteria = ["The abstract should be informative and coherent.", "The abstract should effectively incorporate the given title and keywords."]
        else:
            raise ValueError("Invalid task format")
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
