class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"poem": "Two roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.\nI shall be telling this with a sigh\nSomewhere ages and ages hence:\nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference.", "theme": "choices", "form": "sonnet"},
            "2": {"poem": "I met a traveler from an antique land\nWho said: Two vast and trunkless legs of stone\nStand in the desert. Near them on the sand,\nHalf sunk, a shattered visage lies, whose frown,\nAnd wrinkled lip, and sneer of cold command,\nTell that its sculptor well those passions read\nWhich yet survive, stamped on these lifeless things,\nThe hand that mocked them and the heart that fed.\nAnd on the pedestal these words appear:\nMy name is Ozymandias, King of Kings;\nLook on my Works, ye Mighty, and despair!\nNothing beside remains. Round the decay\nOf that colossal Wreck, boundless and bare\nThe lone and level sands stretch far away.", "theme": "impermanence", "form": "haiku"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the given poem and then generate a new poem based on the specified theme and form.

Poem: {t['poem']}

Tasks:
1. Analyze the poem, discussing its structure, themes, and literary devices.
2. Generate a new poem based on the specified theme and form.

Ensure that your analysis is thorough and insightful, covering the structure, themes, and literary devices used in the poem. Your generated poem should adhere to the specified form and theme. Submit your response as a plain text string in the following format:

Analysis: [Your analysis here]
New Poem: [Your new poem here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The analysis should be thorough and insightful, covering structure, themes, and literary devices.",
            "The generated poem should adhere to the specified form and theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
