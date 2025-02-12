import re

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "nature", "constraints": ["must be a sonnet", "should evoke a sense of tranquility"], "expected_result": "A coherent poem that meets the constraints"},
            "2": {"poem": "Shall I compare thee to a summer's day?\nThou art more lovely and more temperate:\nRough winds do shake the darling buds of May,\nAnd summer's lease hath all too short a date:\nSometime too hot the eye of heaven shines,\nAnd often is his gold complexion dimm'd;\nAnd every fair from fair sometime declines,\nBy chance or nature's changing course untrimm'd;\nBut thy eternal summer shall not fade\nNor lose possession of that fair thou owest;\nNor shall Death brag thou wanderest in his shade,\nWhen in eternal lines to time thou growest:\nSo long as men can breathe or eyes can see,\nSo long lives this, and this gives life to thee.", "questions": ["Who is the speaker comparing in the poem?", "What is meant by 'eternal summer'?", "Identify one metaphor used in the poem."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "theme" in t:
            return f"""Generate a poem based on the following theme and constraints:

Theme: {t['theme']}
Constraints: {', '.join(t['constraints'])}

Provide the poem in a clear, coherent format, ensuring it adheres to the given constraints. The poem should be at least 14 lines long and should follow the structure of a sonnet. Provide your poem in plain text format.
"""
        else:
            return f"""Interpret the following poem and answer the questions below:

Poem: {t['poem']}

Questions: {', '.join(t['questions'])}

Provide your answers in plain text format, ensuring they are clear and concise."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "theme" in t:
            criteria = ["The poem should be coherent, follow the given constraints, and be in the specified format."]
        else:
            criteria = ["The answers should be correct based on the provided poem."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
