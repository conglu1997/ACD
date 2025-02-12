class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "task_type": "analysis",
                "poem": "The Road Not Taken by Robert Frost\n\nTwo roads diverged in a yellow wood,\nAnd sorry I could not travel both\nAnd be one traveler, long I stood\nAnd looked down one as far as I could\nTo where it bent in the undergrowth;\n\nThen took the other, as just as fair,\nAnd having perhaps the better claim,\nBecause it was grassy and wanted wear;\nThough as for that the passing there\nHad worn them really about the same,\n\nAnd both that morning equally lay\nIn leaves no step had trodden black.\nOh, I kept the first for another day!\nYet knowing how way leads on to way,\nI doubted if I should ever come back.\n\nI shall be telling this with a sigh\nSomewhere ages and ages hence:\nTwo roads diverged in a wood, and I—\nI took the one less traveled by,\nAnd that has made all the difference.",
                "prompts": [
                    "Identify the main theme of the poem.",
                    "Discuss at least three literary devices used in the poem and their effects.",
                    "Describe the emotional impact the poem aims to create."
                ]
            },
            "2": {
                "task_type": "creation",
                "theme": "nature",
                "form": "sonnet",
                "prompts": [
                    "Write an original sonnet focused on the theme of nature.",
                    "Ensure the sonnet follows the traditional Shakespearean form, consisting of 14 lines with a specific rhyme scheme (ABABCDCDEFEFGG)."
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'analysis':
            return f"""Analyze the given poem for the following elements:\n\n1. Identify the main theme of the poem.\n2. Discuss at least three literary devices used in the poem and their effects.\n3. Describe the emotional impact the poem aims to create.\n\nPoem:\n{t['poem']}\n\nFormat your response as follows:\n1. Theme: [Your identification of the main theme]\n2. Literary Devices: [Discussion of at least three literary devices and their effects]\n3. Emotional Impact: [Description of the emotional impact the poem aims to create]\n\nEnsure your analysis is thorough, precise, and well-supported by evidence from the poem."""
        elif t['task_type'] == 'creation':
            return f"""Write an original sonnet focused on the theme of nature. Ensure the sonnet follows the traditional Shakespearean form, consisting of 14 lines with a specific rhyme scheme (ABABCDCDEFEFGG).\n\nTheme: {t['theme']}\nForm: {t['form']}\n\nFormat your response as follows:\n[Your original sonnet]\n\nEnsure your poem adheres to the specified theme and form, and that it is creative, cohesive, and evocative."""
        else:
            return ""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'analysis':
            criteria = [
                "The response should identify the main theme of the poem.",
                "The response should discuss at least three literary devices used in the poem and their effects.",
                "The response should describe the emotional impact the poem aims to create."
            ]
        elif t['task_type'] == 'creation':
            criteria = [
                "The sonnet should follow the traditional Shakespearean form.",
                "The sonnet should focus on the theme of nature.",
                "The poem should be creative, cohesive, and evocative."
            ]
        else:
            criteria = []
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
