class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "proposition": "The use of artificial intelligence in warfare is ethically justifiable.",
                "stance": "for"
            },
            "2": {
                "proposition": "Universal basic income should be implemented globally.",
                "stance": "against"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Engage in a structured debate based on the given proposition and stance:

Proposition: {t['proposition']}
Stance: {t['stance']}

Your response should include the following sections:
1. Introduction: Briefly introduce the topic and state your stance.
2. Argument: Present your main arguments supporting your stance. Provide at least three distinct points with logical reasoning and evidence. Ensure your reasoning is detailed and well-supported by facts.
3. Counterarguments: Address potential counterarguments to your stance. Provide at least two rebuttals to these counterarguments, explaining why they may be flawed or insufficient.
4. Conclusion: Summarize your arguments and restate your stance convincingly.

Ensure that your response is logically consistent, well-structured, persuasive, and demonstrates a deep understanding of the topic. Provide enough detail in each section to show thorough reasoning and consideration of different perspectives. Each section should be clearly labeled and well-organized. Submit your response as a plain text string.

Response format example:

Introduction:
- Brief introduction...

Argument:
- Point 1: Description and reasoning...
- Point 2: Description and reasoning...
- Point 3: Description and reasoning...

Counterarguments:
- Counterargument 1: Rebuttal...
- Counterargument 2: Rebuttal...

Conclusion:
- Summary and restatement of stance..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The introduction should clearly state the topic and stance.",
            "The argument section should include at least three distinct points with logical reasoning and evidence.",
            "The counterarguments section should address potential counterarguments and provide at least two rebuttals.",
            "The conclusion should summarize the arguments and restate the stance convincingly.",
            "Each section should be clearly labeled and well-organized.",
            "The response should be logically consistent, well-structured, persuasive, and detailed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
