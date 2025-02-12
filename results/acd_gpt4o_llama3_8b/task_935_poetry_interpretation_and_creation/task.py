class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "poem": "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\n\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,\n\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.\n\nI shall be telling this with a sigh\nSomewhere ages and ages hence:\nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference.",
                "question": "Analyze the given poem 'The Road Not Taken' by Robert Frost. Explain its themes, metaphors, and emotions. Format your response as follows: \n\nThemes: [Your explanation here]\nMetaphors: [Your explanation here]\nEmotions: [Your explanation here]"
            },
            "2": {
                "prompt": "Write a poem about the feeling of hope in the face of adversity. Format your response as a poem with at least 12 lines."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "poem" in t:
            return f"Analyze the given poem and explain its themes, metaphors, and emotions.\n\nPoem:\n{t['poem']}\n\nFormat your response as follows:\nThemes: [Your explanation here]\nMetaphors: [Your explanation here]\nEmotions: [Your explanation here]"
        else:
            return f"Write a poem based on the given prompt.\n\nPrompt:\n{t['prompt']}"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if "poem" in t:
            criteria = [
                "The analysis should correctly identify the themes of the poem.",
                "The analysis should accurately explain the metaphors used in the poem.",
                "The analysis should capture the emotions conveyed in the poem."
            ]
        else:
            criteria = [
                "The poem should creatively address the prompt.",
                "The poem should be coherent and have a clear structure.",
                "The poem should evoke the feeling of hope in the face of adversity."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
