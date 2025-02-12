class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "generate", "constraints": "Create a historical narrative about the events leading up to the signing of the Magna Carta in 1215. Include at least three significant events and mention key figures involved."},
            "2": {"task_type": "interpret", "narrative": """The American Civil War:

The American Civil War began in 1861 after several southern states seceded from the Union following the election of Abraham Lincoln. The war was primarily fought over issues of slavery and states' rights. Major battles included the Battle of Gettysburg and the Battle of Antietam. The war ended in 1865 with the surrender of General Robert E. Lee at Appomattox Court House."""}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'generate':
            return f"""Your task is to generate a historical narrative based on the following constraints:\n\nConstraints: {t['constraints']}\n\nEnsure that the narrative is historically accurate, follows the given constraints, and is engaging to read. Provide your narrative in plain text format. Your response should be structured as follows:\n\n- Title\n- Narrative: [detailed historical narrative]"""
        elif t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following historical narrative and identify key events and their significance:\n\nNarrative:\n{t['narrative']}\n\nFor each key event, provide a detailed explanation of its significance in the context of the narrative. Ensure your explanations are clear and comprehensive, capturing all necessary details to understand the historical context. Provide your explanations in plain text format, numbered to correspond with the key events."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'generate':
            criteria = ["The narrative should be historically accurate and engaging.", "The narrative should cover the events leading up to the signing of the Magna Carta in 1215.", "The narrative should include at least three significant events and mention key figures involved."]
        elif t['task_type'] == 'interpret':
            criteria = ["The explanations should accurately and comprehensively detail the key events and their significance."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
