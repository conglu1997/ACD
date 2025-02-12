class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"type": "analysis", "context": "During the American Civil War, Abraham Lincoln faced numerous challenges both politically and militarily. Analyze his leadership decisions during this period and infer how they contributed to the Union's victory."},
            "2": {"type": "narrative", "context": "Imagine you are a historian in the 22nd century looking back at the global impact of the COVID-19 pandemic in the early 21st century. Create a narrative that describes the social, economic, and political changes that resulted from the pandemic."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["type"] == "analysis":
            instructions = f"""Your task is to analyze the leadership decisions of Abraham Lincoln during the American Civil War and infer how these decisions contributed to the Union's victory. Provide a detailed analysis that includes specific examples of his decisions, the context in which they were made, and their impact on the war's outcome. Ensure your analysis is logically structured and historically accurate. Your response should be between 300-500 words. Provide your response in plain text format as follows:

Analysis:
[Your detailed analysis]"""
        elif t["type"] == "narrative":
            instructions = f"""Your task is to create a historical narrative from the perspective of a 22nd-century historian looking back at the global impact of the COVID-19 pandemic. Describe the social, economic, and political changes that resulted from the pandemic. Ensure your narrative is coherent, engaging, and reflects a deep understanding of the historical context. Your response should be between 300-500 words. Provide your response in plain text format as follows:

Narrative:
[Your detailed narrative]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["type"] == "analysis":
            criteria = ["The analysis should include specific examples of Lincoln's decisions.", "The context and impact of the decisions should be clearly explained.", "The analysis should be logically structured and historically accurate.", "The response should be between 300-500 words."]
        elif t["type"] == "narrative":
            criteria = ["The narrative should describe social, economic, and political changes.", "The narrative should be coherent and engaging.", "The narrative should reflect a deep understanding of the historical context.", "The response should be between 300-500 words."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
