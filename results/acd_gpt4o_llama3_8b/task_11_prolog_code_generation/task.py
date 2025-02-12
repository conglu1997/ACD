class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "requirement": "Write a Prolog program to define a family tree. Include facts for parent/2, male/1, female/1 and rules for ancestor/2."
            },
            "2": {
                "requirement": "Write a Prolog program to solve the following logic puzzle: There are three houses in a row, each painted a different color (red, blue, green). The person in the red house drinks tea, the person in the blue house drinks coffee, and the person in the green house drinks milk. The tea drinker lives next to the coffee drinker. Define facts and rules to determine who drinks milk."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a Prolog program based on the given requirement:

Requirement:
{t['requirement']}

Ensure the Prolog code is syntactically correct and meets the specified requirements. Include both facts and rules in your Prolog program. Submit your code as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The Prolog code should be syntactically correct.", "The program should meet the given requirement.", "The submission should include both facts and rules."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
