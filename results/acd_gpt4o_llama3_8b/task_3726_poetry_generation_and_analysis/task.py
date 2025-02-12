class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompt": "Evaluate the following poem and provide a detailed analysis of its themes, structure, and use of poetic devices.\n\nPoem:\nThe sun sets low, a crimson glow,\nWhispers of night begin to grow,\nStars awaken in the sky,\nAs the world bids day goodbye."},
            "2": {"prompt": "Generate a poem based on the following themes: love and loss. Ensure your poem includes at least one metaphor and follows a consistent rhyme scheme."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if "Evaluate" in t["prompt"]:
            return f"""Complete the following task based on the given prompt:\n\n{t["prompt"]}\n\nProvide a detailed analysis of the poem's themes, structure, and use of poetic devices. Your analysis should include:\n1. Identification of the main themes.\n2. Description of the poem's structure (e.g., rhyme scheme, meter).\n3. Examples of poetic devices used (e.g., metaphor, simile, alliteration).\n\nEnsure your analysis is coherent, well-structured, and insightful. Submit your response as a plain text string in the following format:\n\nThemes: [List the main themes]\nStructure: [Describe the poem's structure]\nPoetic Devices: [List and explain the poetic devices used]\n\nYour response should be at least 200 words."""
        else:
            return f"""Complete the following task based on the given prompt:\n\n{t["prompt"]}\n\nGenerate a poem based on the provided themes. Ensure your poem includes at least one metaphor and follows a consistent rhyme scheme. Submit your poem as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = []
        if "Evaluate" in t["prompt"]:
            criteria = ["The analysis should identify the main themes, describe the poem's structure, and provide examples of poetic devices used.", "The analysis should be coherent, well-structured, and insightful."]
        else:
            criteria = ["The generated poem should include at least one metaphor and follow a consistent rhyme scheme.", "The poem should be coherent and reflect the provided themes of love and loss."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
