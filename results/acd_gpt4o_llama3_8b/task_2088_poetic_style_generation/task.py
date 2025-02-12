class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "poet": "William Wordsworth",
                "theme": "nature",
                "prompt": "Write a poem about nature, capturing its serene beauty and the emotions it evokes, in the style of William Wordsworth. Wordsworth's style often includes the use of blank verse, vivid imagery, and themes of nature and the sublime."
            },
            "2": {
                "poet": "Emily Dickinson",
                "theme": "solitude",
                "prompt": "Write a poem about solitude, exploring its depth and the introspection it brings, in the style of Emily Dickinson. Dickinson's style often features short lines, slant rhyme, and unconventional capitalization and punctuation."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Write a poem based on the specified theme and in the style of the specified poet:

Poet: {t['poet']}
Theme: {t['theme']}
Prompt: {t['prompt']}

Ensure that your poem mimics the style of the specified poet and captures the essence of the given theme. Your poem should be around 100-150 words. Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = ["The poem should mimic the style of the specified poet.", "The poem should capture the essence of the given theme.", "The poem should be around 100-150 words.", "The poem should include specific poetic techniques known to the poet (e.g., blank verse for Wordsworth, slant rhyme for Dickinson)."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
