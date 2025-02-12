class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"premise": "All humans are mortal. Socrates is a human.", "fallacy_argument": "All humans are mortal. Socrates is a human. Therefore, Socrates is a dog."},
            "2": {"premise": "If it rains, the ground gets wet. It is raining.", "fallacy_argument": "If it rains, the ground gets wet. The ground is wet. Therefore, it is raining."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts:

1. Construct a valid logical argument based on the given premise.
2. Identify and explain the logical fallacy in the provided argument.

Premise: {t['premise']}
Fallacy Argument: {t['fallacy_argument']}

Provide your response in the following format:

Valid Argument: [Your valid argument based on the premise]
Fallacy Explanation: [Your explanation of the logical fallacy in the provided argument]

Example 1:
Premise: All humans are mortal. Socrates is a human.
Fallacy Argument: All humans are mortal. Socrates is a human. Therefore, Socrates is a dog.

Valid Argument: All humans are mortal. Socrates is a human. Therefore, Socrates is mortal.
Fallacy Explanation: The provided argument commits a non sequitur fallacy by concluding something that does not logically follow from the premises.

Example 2:
Premise: If it rains, the ground gets wet. It is raining.
Fallacy Argument: If it rains, the ground gets wet. The ground is wet. Therefore, it is raining.

Valid Argument: If it rains, the ground gets wet. It is raining. Therefore, the ground is wet.
Fallacy Explanation: The provided argument commits the fallacy of affirming the consequent by assuming that the only reason for the ground being wet is that it is raining, ignoring other possible causes."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should construct a valid logical argument based on the given premise.", 
            "The response should correctly identify and explain the logical fallacy in the provided argument.",
            "The valid argument should follow logically from the given premises.",
            "The fallacy explanation should be accurate and demonstrate understanding of the flaw in reasoning."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
