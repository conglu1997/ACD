class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "theme": "Nature",
                "requirements": "Generate a poem of at least 12 lines that captures the beauty and essence of nature. The poem should include vivid imagery and evoke a sense of awe."
            },
            "2": {
                "poem": "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\n\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,\n\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.\n\nI shall be telling this with a sigh\nSomewhere ages and ages hence:\nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference.",
                "requirements": "Interpret the given poem 'The Road Not Taken' by Robert Frost. Provide a detailed analysis of the poem's themes, imagery, and overall message. Your analysis should be thorough and cover various aspects of the poem."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'theme' in t:
            return f"""Generate a poem based on the following theme:

Theme: {t['theme']}

Requirements: {t['requirements']}

Your poem should be at least 12 lines long, capture the essence of the theme, include vivid imagery, and evoke a sense of awe. Submit your poem as a plain text string."""
        else:
            return f"""Interpret the following poem and provide a detailed analysis based on the requirements:

Poem: {t['poem']}

Requirements: {t['requirements']}

Your analysis should cover the poem's themes, imagery, and overall message. Ensure that your analysis is thorough and covers various aspects of the poem. Submit your analysis as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'theme' in t:
            validation_criteria = [
                "The poem should be at least 12 lines long.",
                "The poem should capture the essence of the given theme.",
                "The poem should include vivid imagery and evoke a sense of awe."
            ]
        else:
            validation_criteria = [
                "The analysis should cover the poem's themes.",
                "The analysis should cover the poem's imagery.",
                "The analysis should cover the poem's overall message.",
                "The analysis should be thorough and cover various aspects of the poem."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
