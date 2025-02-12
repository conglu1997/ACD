class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'prompt': 'Write a diary entry from the perspective of a high school student who just participated in their first school play. Include their feelings before, during, and after the play, interactions with friends, and any memorable moments.'},
            '2': {'prompt': 'Write a diary entry from the perspective of an astronaut on the International Space Station, describing a day in space. Include details about their daily routine, any scientific experiments, interactions with crew members, and their thoughts about being in space.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a detailed fictional diary entry based on the following prompt: {t['prompt']} \nEnsure the diary entry captures the emotional and situational nuances of the scenario. Your entry should be coherent, logically consistent, and detailed. Submit your diary entry as a plain text string in the following format:\n\nDiary Entry: [Your detailed diary entry here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The diary entry should capture the emotional and situational nuances of the scenario.", "The diary entry should be coherent, logically consistent, and detailed.", "The diary entry should include specific details and moments from the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
