class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "premises": [
                    "All humans are mortal.",
                    "Socrates is a human.",
                    "All mortals have a finite lifespan."
                ]
            },
            "2": {
                "premises": [
                    "If it rains, the ground will be wet.",
                    "It is raining.",
                    "If the ground is wet, the grass will grow."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        premises_str = '\n'.join(t['premises'])
        return f"""Generate a logical argument based on the following premises:

{premises_str}

Your argument should be clear, coherent, and logically valid. Do not add any new premises or make assumptions beyond the given premises. Ensure to explicitly state the conclusion that follows from the premises. Submit your response as a plain text string in the following format:

Argument:
[Your argument here]

Example:
Argument:
All humans are mortal. Socrates is a human. Therefore, Socrates is mortal."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The argument should be clear and coherent.",
            "The argument should be logically valid based on the given premises.",
            "The conclusion should explicitly follow from the premises.",
            "No new premises or assumptions should be introduced.",
            "The response should follow the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
