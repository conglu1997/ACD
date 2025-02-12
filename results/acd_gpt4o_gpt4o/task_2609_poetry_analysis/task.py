class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "Hope is the thing with feathers\nThat perches in the soul,\nAnd sings the tune without the words,\nAnd never stops at all,\nAnd sweetest in the gale is heard;\nAnd sore must be the storm\nThat could abash the little Bird\nThat kept so many warm.\nI've heard it in the chillest land,\nAnd on the strangest Sea;\nYet, never, in Extremity,\nIt asked a crumb of Me."},
            "2": {"poem": "Shall I compare thee to a summer's day?\nThou art more lovely and more temperate:\nRough winds do shake the darling buds of May,\nAnd summer's lease hath all too short a date:\nSometime too hot the eye of heaven shines,\nAnd often is his gold complexion dimm'd;\nAnd every fair from fair sometime declines,\nBy chance, or nature's changing course, untrimm'd;\nBut thy eternal summer shall not fade\nNor lose possession of that fair thou ow'st;\nNor shall Death brag thou wander'st in his shade,\nWhen in eternal lines to time thou grow'st;\nSo long as men can breathe, or eyes can see,\nSo long lives this, and this gives life to thee."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the following poem and provide a detailed analysis that includes:
1. The main themes of the poem.
2. Examples of metaphorical language used.
3. The emotional tone of the poem.

Poem:
{t['poem']}

Provide your response in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should correctly identify the main themes of the poem.",
            "The response should provide accurate examples of metaphorical language.",
            "The response should correctly describe the emotional tone of the poem."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
