class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "dilemma": "Is it ethical to use animals for scientific research? Provide a reasoned argument supporting your position.",
                "position": "Supporting the use of animals for scientific research"
            },
            "2": {
                "dilemma": "Should wealthy nations be obligated to help poorer nations during a global crisis? Critique the following argument:",
                "argument": "Wealthy nations have enough resources to manage their own crises and should not be obligated to help poorer nations. Each country should prioritize its own citizens during a global crisis."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'position' in t:
            return f"""Read the following ethical dilemma and provide a coherent argument supporting the given position:

Dilemma:
{t['dilemma']}

Position: {t['position']}

Ensure your argument is logical, well-structured, and considers multiple perspectives. Submit your response as a plain text string in the following format:

Argument: [Your argument]"""
        else:
            return f"""Read the following ethical dilemma and critique the provided argument:

Dilemma:
{t['dilemma']}

Argument:
{t['argument']}

Identify any logical fallacies, unsupported assumptions, or areas for improvement. Submit your critique as a plain text string in the following format:

Critique: [Your critique]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'position' in t:
            validation_criteria = [
                "The argument should be logical and well-structured.",
                "The argument should consider multiple perspectives.",
                "The argument should support the given position clearly and convincingly."
            ]
        else:
            validation_criteria = [
                "The critique should identify logical fallacies or unsupported assumptions.",
                "The critique should suggest areas for improvement.",
                "The critique should be logical and well-structured."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
