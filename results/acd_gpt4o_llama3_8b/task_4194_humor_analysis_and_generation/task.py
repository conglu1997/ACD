class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "joke": "Why don't scientists trust atoms? Because they make up everything!",
                "theme": "science"
            },
            "2": {
                "joke": "Why did the scarecrow win an award? Because he was outstanding in his field!",
                "theme": "farm"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are given a joke and a theme. Your tasks are:
1. Analyze the given joke, explaining its structure and elements that make it humorous.
2. Generate a new joke based on the specified theme.

Joke: {t['joke']}

Theme: {t['theme']}

Submit your response as a plain text string in the following format:

Analysis: [Your analysis of the given joke, including the type of humor (e.g., pun, wordplay, situational), why it is funny, and any cultural references.]
New Joke: [Your generated joke based on the theme. Ensure it is creative, coherent, and fits the theme.]

Example:
Analysis: The joke is a play on words (pun) involving the double meaning of 'make up' (to fabricate and to constitute). It is funny because it plays on the scientific context and the common phrase 'make up'.
New Joke: Why don't biologists ever get lost? Because they always have their cell maps!"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should correctly identify the joke's structure and humor elements.",
            "The new joke should be coherent, creative, and related to the specified theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
