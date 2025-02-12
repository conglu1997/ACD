class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are a lawmaker in a society facing a severe housing crisis. Many people are homeless while others own multiple properties. Propose a law aimed at addressing this issue.",
                "principle": "Equality"
            },
            "2": {
                "scenario": "In your society, there is a growing concern about environmental degradation caused by industrial activities. Propose a law to mitigate this issue.",
                "principle": "Sustainability"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario and principle:

Scenario:
{t['scenario']}

Principle: {t['principle']}

Your task is to:
1. Propose a new law or policy that addresses the issue described in the scenario.
2. Justify the law based on the given principle.
3. Describe potential benefits and drawbacks of the proposed law.
4. Consider and address potential opposition to the law.

Submit your response as a plain text string in the following format:
- Proposed Law: [Your proposed law here]
- Justification: [Your justification here]
- Benefits and Drawbacks: [Your description of benefits and drawbacks here]
- Addressing Opposition: [Your response to potential opposition here]

Ensure that your response is well-structured, coherent, and demonstrates a deep understanding of the principle and the scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should accurately propose a law or policy.",
            "The response should justify the law based on the given principle.",
            "The response should describe potential benefits and drawbacks.",
            "The response should address potential opposition to the law.",
            "The response should be well-structured, coherent, and demonstrate a deep understanding of the principle and the scenario."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
