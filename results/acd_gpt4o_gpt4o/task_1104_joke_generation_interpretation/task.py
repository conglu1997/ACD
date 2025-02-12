class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"task_type": "interpret", "jokes": """1. Why don't scientists trust atoms? Because they make up everything!\n2. What do you call fake spaghetti? An impasta!\n3. Why did the scarecrow win an award? Because he was outstanding in his field!\n4. How does the ocean say hi? It waves!\n5. Why don't skeletons fight each other? They don't have the guts."""},
            "2": {"task_type": "generate", "prompt": "Generate a joke that includes a pun about computers."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'interpret':
            return f"""Your task is to interpret the following jokes and explain why they are funny:\n\n{t['jokes']}\n\nFor each joke, provide a brief explanation of why it is humorous. Your explanations should be clear and concise, capturing the essence of the joke. Provide your explanations in plain text format, numbered to correspond with the jokes."""
        elif t['task_type'] == 'generate':
            return f"""Your task is to generate a joke based on the following prompt:\n\nPrompt: {t['prompt']}\n\nEnsure that your joke is funny, coherent, and includes a pun about computers. Provide your joke in plain text format."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'interpret':
            criteria = ["The explanations should accurately reflect why the jokes are funny."]
        elif t['task_type'] == 'generate':
            criteria = ["The joke should include a pun about computers and be funny."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
