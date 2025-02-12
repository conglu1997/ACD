class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task": "Argue for or against the proposition that 'The use of facial recognition technology by law enforcement should be banned'.", "context": "Consider legal principles such as privacy rights, public safety, and constitutional rights."},
            "2": {"task": "Argue for or against the proposition that 'Corporations should have the same free speech rights as individuals'.", "context": "Consider legal principles such as the First Amendment, corporate influence on politics, and public interest."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a detailed legal argument for or against the given proposition based on the provided context and legal principles. Provide a thorough explanation of your reasoning, citing relevant laws, cases, and ethical considerations.

Task:
{t['task']}

Context:
{t['context']}

Provide your argument below. Your response should include:
1. A clear statement of your position (for or against).
2. A detailed legal argument supporting your position.
3. Citations of relevant laws, cases, and ethical considerations.
4. An analysis of potential counterarguments and your responses to them.

Format your response as follows:
Position: [Your position]
Argument: [Your detailed legal argument]
Citations: [Relevant laws, cases, and ethical considerations]
Counterarguments: [Analysis of potential counterarguments and your responses]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The legal argument should be well-reasoned and coherent.", "The response should include relevant laws, cases, and ethical considerations.", "The response should address potential counterarguments."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
