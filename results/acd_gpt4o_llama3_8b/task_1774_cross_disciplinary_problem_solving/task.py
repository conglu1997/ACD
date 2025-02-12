class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "A biologist is studying the effect of a new drug on rats. The drug is suspected to affect the metabolic rate. The biologist has data on the rats' weight, food intake, and activity levels before and after administering the drug. Design an experiment to test the drug's effect on metabolism, and describe the statistical methods you would use to analyze the results.",
                "data": {
                    "weights_before": [200, 220, 210, 230, 240],
                    "weights_after": [195, 215, 205, 225, 235],
                    "food_intake_before": [25, 27, 26, 28, 30],
                    "food_intake_after": [24, 26, 25, 27, 29],
                    "activity_levels_before": [300, 320, 310, 330, 340],
                    "activity_levels_after": [290, 310, 300, 320, 330]
                }
            },
            "2": {
                "problem": "A city planner is designing a new park that must include features to improve air quality, provide recreational space, and support local wildlife. Propose a design for the park, detailing the specific elements you would include to meet these goals and explaining how each element contributes to the overall objectives."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "data" in t:
            data_info = f"\nData:\nWeights Before: {t['data']['weights_before']}\nWeights After: {t['data']['weights_after']}\nFood Intake Before: {t['data']['food_intake_before']}\nFood Intake After: {t['data']['food_intake_after']}\nActivity Levels Before: {t['data']['activity_levels_before']}\nActivity Levels After: {t['data']['activity_levels_after']}"
        else:
            data_info = ""
        return f"""Solve the following problem by integrating knowledge from multiple disciplines. Provide a detailed and well-reasoned solution.

Problem:
{t['problem']}{data_info}

Submit your solution as a plain text string, clearly explaining your reasoning and the steps you took to arrive at your solution. Structure your response in the following format:
1. Introduction
2. Methods (for Task 1: include experimental design and detailed statistical methods)
3. Analysis
4. Conclusion
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        task_key = list(TaskFamily.get_tasks().keys())[list(TaskFamily.get_tasks().values()).index(t)]
        criteria = ["The solution should be detailed and reasonable.", "The solution should integrate knowledge from multiple disciplines.", "The reasoning should be clear and logical.", "The response should follow the specified structure.", "For Task 1: The statistical methods should be appropriate for the data provided.", "For Task 2: The park design should clearly relate to the goals of improving air quality, providing recreational space, and supporting local wildlife."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
