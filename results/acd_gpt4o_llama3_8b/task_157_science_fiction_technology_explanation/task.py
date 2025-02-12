class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "In the year 2150, humanity has established colonies on Mars. Invent and explain a technology that allows for efficient transportation between Earth and Mars."
            },
            "2": {
                "scenario": "In a distant future, humans have developed the ability to communicate telepathically using a special device. Explain how this device works and its implications on society."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Based on the following fictional scenario, invent and explain a plausible science fiction technology:

Scenario: {t['scenario']}

Ensure that the technology is scientifically plausible, clearly explained, and includes its potential impact on society. Submit your explanation as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The technology should be scientifically plausible.",
            "The explanation should be clear and coherent.",
            "The impact on society should be addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
