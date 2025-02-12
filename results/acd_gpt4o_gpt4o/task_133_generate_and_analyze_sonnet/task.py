class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"theme": "love"},
            "2": {"sonnet": "Shall I compare thee to a summer's day? / Thou art more lovely and more temperate: / Rough winds do shake the darling buds of May, / And summer's lease hath all too short a date: / Sometime too hot the eye of heaven shines, / And often is his gold complexion dimm'd; / And every fair from fair sometime declines, / By chance or nature's changing course untrimm'd; / But thy eternal summer shall not fade / Nor lose possession of that fair thou owest; / Nor shall Death brag thou wanderest in his shade, / When in eternal lines to time thou growest: / So long as men can breathe or eyes can see, / So long lives this, and this gives life to thee."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Your task is to write an original Shakespearean sonnet based on the following theme: {t['theme']}.

A Shakespearean sonnet consists of 14 lines written in iambic pentameter, with a rhyme scheme of ABABCDCDEFEFGG. Ensure that your sonnet adheres to this structure and theme.

Provide your response in plain text format."""
        elif 'sonnet' in t:
            return f"""Your task is to analyze the following Shakespearean sonnet:

{t['sonnet']}

Provide your analysis in the following format:

1. Identify the theme of the sonnet.
2. Comment on the use of imagery and metaphors.
3. Explain how the rhyme scheme and meter contribute to the overall effect of the sonnet.

Provide your response in plain text format."""
        return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            criteria = [
                "The response should be an original Shakespearean sonnet.",
                "The sonnet should adhere to the ABABCDCDEFEFGG rhyme scheme.",
                "The sonnet should be written in iambic pentameter.",
                "The sonnet should reflect the given theme."]
        elif 'sonnet' in t:
            criteria = [
                "The response should correctly identify the theme of the sonnet.",
                "The response should comment accurately on the use of imagery and metaphors.",
                "The response should explain the contribution of the rhyme scheme and meter to the sonnet's effect."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
