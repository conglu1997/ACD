class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"initial_prompt": "Write a short story about a magical forest.", "change_prompt": "Now, turn it into a science fiction story set in space."},
            "2": {"initial_prompt": "Compose a poem about the ocean.", "change_prompt": "Now, change it to be about a bustling city."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a response based on the initial prompt provided. After you start, you will need to adapt your response based on a new prompt that will be given midway.

Initial Prompt: {t['initial_prompt']}

Once you have started, you will receive the following change in prompt:
Change Prompt: {t['change_prompt']}

Ensure your final response seamlessly transitions from the initial prompt to the new context provided by the change prompt. The overall response should be coherent and demonstrate adaptability to the new context.

Provide your response in the following format:
[Initial Prompt Response]
[Change Prompt Adaptation]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should seamlessly transition from the initial prompt to the change prompt.",
            "The final response should be coherent and relevant to both prompts.",
            "The response should demonstrate adaptability to the new context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
