class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Analyze the following poem for its thematic elements, tone, and use of literary devices:\n\n'The Road Not Taken' by Robert Frost\n\nTwo roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\n\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,\n\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.\n\nI shall be telling this with a sigh\nSomewhere ages and ages hence:\nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference.'"},
            "2": {"prompt": "Compose a poem based on the following theme: 'The passage of time.' Your poem should be at least 12 lines long and make use of at least two literary devices (e.g., metaphor, simile, alliteration)."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task involves analyzing and composing poetry:\n\nPrompt: {t['prompt']}\n\nFor Task 1: Analyze the provided poem for its thematic elements, tone, and use of literary devices. Clearly label each part of your analysis (e.g., 'Theme: ...', 'Tone: ...', 'Literary Devices: ...').\nFor Task 2: Compose a poem based on the given theme. Ensure your poem is at least 12 lines long and makes use of at least two literary devices. Clearly indicate the literary devices used in your poem (e.g., 'Metaphor: ...', 'Simile: ...').\n"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis for Task 1 should accurately identify the theme, tone, and use of literary devices in the provided poem.", "The poem generated in Task 2 should be at least 12 lines long and make use of at least two literary devices.", "The poem should be coherent, creative, and relevant to the given theme."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
