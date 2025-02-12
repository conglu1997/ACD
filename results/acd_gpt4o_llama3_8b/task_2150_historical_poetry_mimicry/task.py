class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "period": "Romantic Era",
                "prompt": "Write a poem about the sublime beauty of nature in the style of the Romantic Era. Ensure the poem captures the essence of Romantic poetry, which often emphasizes deep emotion, individualism, and the awe-inspiring aspects of nature. Use rich, evocative language typical of poets like Wordsworth or Coleridge."
            },
            "2": {
                "period": "Modernist Era",
                "prompt": "Write a poem about the complexities of urban life in the style of the Modernist Era. Ensure the poem captures the essence of Modernist poetry, which often includes themes of disillusionment, fragmentation, and a break from traditional forms. Use innovative language and structure typical of poets like T.S. Eliot or Ezra Pound."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        period = t['period']
        prompt = t['prompt']
        return f"""Generate a poem in the specified poetic style from the given historical period. Ensure your poem adheres to the tone, language, and structure typical of that period.
\nHistorical Period: {period}
\nPrompt: {prompt}
\nSubmit your poem as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The poem should adhere to the tone, language, and structure typical of the specified historical period.",
            "The poem should be coherent and capture the essence of the prompt."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
