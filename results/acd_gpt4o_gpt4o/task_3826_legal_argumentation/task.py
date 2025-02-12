class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A company has been accused of violating environmental regulations by dumping toxic waste into a river. The company argues that the waste was within legal limits and that they have followed all required procedures.", "laws": ["Environmental Protection Act Section 5", "Clean Water Act Section 401"], "precedents": ["United States v. Riverside Bayview Homes, Inc.", "Friends of the Earth, Inc. v. Laidlaw Environmental Services, Inc."]},
            "2": {"scenario": "An employee has been terminated from their job and claims wrongful dismissal. The employer states that the termination was due to poor performance, but the employee argues that it was due to discrimination.", "laws": ["Civil Rights Act Title VII", "Employment Protection Act Section 3"], "precedents": ["McDonnell Douglas Corp. v. Green", "Burlington Industries, Inc. v. Ellerth"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the given legal scenario and construct a coherent legal argument based on the specified laws and precedents.

Scenario: {t["scenario"]}

Laws: {', '.join(t["laws"])}
Precedents: {', '.join(t["precedents"])}

Your argument should be well-structured, logically coherent, and reference the relevant laws and precedents. Provide your response in the following format:

1. Introduction: [Brief introduction of the scenario]
2. Legal Analysis: [Detailed legal analysis referencing the specified laws and precedents]
3. Conclusion: [Summary of your argument and conclusion]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The argument should be logically coherent and well-structured.",
            "The argument should reference the relevant laws and precedents appropriately."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
