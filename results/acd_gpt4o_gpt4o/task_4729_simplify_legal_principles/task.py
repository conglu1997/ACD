class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"legal_principle": "The principle of double jeopardy, which prohibits someone from being prosecuted twice for substantially the same crime.", "scenario": "A person is tried and acquitted of robbery. Later, new evidence emerges that suggests they might be guilty."},
            "2": {"legal_principle": "The principle of habeas corpus, which protects against unlawful and indefinite imprisonment.", "scenario": "A person is detained without trial for an extended period without being charged with a crime."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves two parts: simplifying a legal principle and creating a hypothetical scenario to illustrate it.

Part 1: Simplification
Explain the following legal principle in simple terms that a layperson can understand. Ensure your explanation is clear and concise.

Legal Principle: {t['legal_principle']}

Part 2: Hypothetical Scenario
Create a hypothetical scenario that clearly illustrates the given legal principle. The scenario should be realistic and demonstrate a situation where the principle would apply. Make sure the scenario is relevant and directly connected to the principle.

Provide your response in the following format:
Explanation: [Your simplified explanation]
Scenario: [Your hypothetical scenario]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation should simplify the legal principle correctly and clearly.",
            "The hypothetical scenario should accurately illustrate the legal principle.",
            "The response should follow the specified format.",
            "The scenario should be realistic and directly connected to the principle."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
