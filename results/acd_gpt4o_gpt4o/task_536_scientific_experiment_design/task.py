class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "hypothesis": "Plants grow faster when exposed to classical music compared to silence.",
                "variables": [
                    "Plant growth rate",
                    "Music type (classical vs. silence)",
                    "Watering frequency",
                    "Sunlight exposure"
                ]
            },
            "2": {
                "hypothesis": "People remember information better when it is presented with visuals compared to text alone.",
                "variables": [
                    "Memory retention",
                    "Presentation format (visuals vs. text)",
                    "Duration of exposure",
                    "Complexity of information"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        hypothesis = t["hypothesis"]
        variables = '\n'.join(t["variables"])
        instructions = f"""Your task is to design and analyze a scientific experiment based on the given hypothesis.

Hypothesis:
{hypothesis}

Variables:
{variables}

Your response should include:
1. A detailed experimental design that includes the control and experimental groups, independent and dependent variables, and how you plan to measure the outcomes.
2. A step-by-step procedure for conducting the experiment.
3. A plan for analyzing the data and drawing conclusions.

Provide your response in the following format:

Experimental Design:
[Your design here]

Procedure:
[Your step-by-step procedure here]

Data Analysis:
[Your data analysis plan here]

Ensure that your response is comprehensive and demonstrates a deep understanding of the scientific method.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The experimental design should include control and experimental groups.",
            "The design should clearly identify independent and dependent variables.",
            "The procedure should be detailed and feasible.",
            "The data analysis plan should be logical and thorough.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
