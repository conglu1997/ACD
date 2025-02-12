class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"idioms": ["Kick the bucket (English)", "Break the ice (English)", "Catch someone red-handed (English)", "Cost an arm and a leg (English)", "Bite the bullet (English)", "Spill the beans (English)"]},
            "2": {"idioms": ["Under the weather (English)", "Piece of cake (English)", "Let the cat out of the bag (English)", "Eat crow (American)", "The ball is in your court (American)", "Hold your horses (American)"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        idioms = t["idioms"]
        instructions = f"""Your task is to interpret and explain the following idioms from different cultures. For each idiom, provide the meaning and a brief explanation of its origin:

Idioms: {', '.join(idioms)}

Your response should be structured as follows:
1. Idiom: [Idiom]
2. Meaning: [Meaning of the idiom]
3. Origin: [Brief explanation of the idiom's origin]"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The meaning of each idiom should be correct.",
            "The explanation of the origin should be accurate and relevant."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
