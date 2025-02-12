class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "A recently discovered exoplanet in the habitable zone of its star, showing signs of water and a unique atmosphere composition.",
                "constraints": "The report should include a description of the exoplanet, its potential for supporting life, and the implications of the discovery. The narrative should be engaging and scientifically plausible."
            },
            "2": {
                "data": "A newly found deep-sea organism with bioluminescent properties and an unusual method of energy production.",
                "constraints": "The report should include a description of the organism, its habitat, its biological characteristics, and the potential applications of this discovery. The narrative should be engaging and scientifically plausible."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a fictional scientific discovery report based on the given data and constraints:

Data:
{t['data']}

Constraints:
{t['constraints']}

Ensure the report is engaging, scientifically plausible, and follows a clear narrative structure. Submit your report as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The report should be scientifically plausible.",
            "The narrative should be engaging and coherent.",
            "The report should include a description of the discovery, its characteristics, and its implications.",
            "The submission should follow a clear narrative structure."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
