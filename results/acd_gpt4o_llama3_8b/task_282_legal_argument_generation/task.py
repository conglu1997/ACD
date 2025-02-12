class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A tenant claims that their landlord has failed to make necessary repairs to the property, resulting in significant damage to their personal belongings. The tenant seeks compensation for the damages. The landlord argues that the tenant did not provide proper notice of the needed repairs."},
            "2": {"scenario": "An employee was terminated without notice after reporting safety violations in the workplace. The employee is suing for wrongful termination, claiming retaliation for whistleblowing. The employer argues that the termination was due to poor performance."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        scenario = t["scenario"]
        return f"""Generate a legal argument based on the following scenario. Ensure that your argument is well-structured, logical, and persuasive. Include relevant legal principles and precedents to support your argument. Here is the scenario:

{scenario}

Your argument should include:
1. A clear statement of your position.
2. Supporting evidence and legal principles, with references to relevant precedents.
3. Rebuttal of the opposing party's argument.
4. A concise conclusion summarizing your argument.

Submit your argument as a plain text string in the following format:
[Position Statement]
[Supporting Evidence and Legal Principles]
[Rebuttal]
[Conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be well-structured and logical.",
            "The argument should include relevant legal principles and precedents.",
            "The argument should effectively rebut the opposing party's argument.",
            "The conclusion should summarize the argument concisely."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
