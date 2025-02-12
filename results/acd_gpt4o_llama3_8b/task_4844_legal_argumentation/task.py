class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A person finds a wallet with $500 inside on a park bench and decides to keep it. Analyze whether this action constitutes theft under common law principles.",
                "principles": "Common law defines theft as the unlawful taking of someone else's property with the intent to permanently deprive the owner of it."
            },
            "2": {
                "scenario": "A company is sued for breach of contract after failing to deliver goods on time. The company argues that a natural disaster prevented timely delivery. Analyze the company's defense under contract law principles.",
                "principles": "Under contract law, a breach of contract occurs when one party fails to fulfill its obligations. However, defenses such as 'force majeure' can excuse performance due to unforeseen events beyond the control of the parties."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following legal scenario and construct a coherent legal argument based on the given principles:

Scenario:
{t['scenario']}

Principles:
{t['principles']}

Your argument should include the following points:
1. A clear statement on whether the action in the scenario constitutes a violation of the given principles.
2. Detailed reasoning, referencing relevant aspects of the principles.
3. Logical consistency and a well-structured argument.

Submit your legal argument as a plain text string in the following format:

Argument:
[Your argument here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should clearly state whether the action constitutes a violation of the principles.",
            "The argument should provide detailed reasoning and reference relevant aspects of the principles.",
            "The argument should be logically sound and well-structured."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
