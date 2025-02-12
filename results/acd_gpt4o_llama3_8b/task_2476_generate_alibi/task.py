class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            '1': {'scenario': 'A character named John is accused of stealing a valuable painting from a museum between 2 PM and 4 PM on a Saturday. John claims he was at a local café from 1:30 PM to 2:30 PM, attended a movie from 2:45 PM to 4:45 PM, and then visited a bookstore from 5 PM to 6 PM. Provide a detailed alibi for John, ensuring the alibi is plausible and accounts for his whereabouts during the entire timeframe. Include interactions with other characters, specific locations, and activities that can be verified.'},
            '2': {'scenario': 'A character named Sarah is accused of hacking into a company’s server on a Wednesday night between 8 PM and 10 PM. Sarah claims she was at a friend’s house for a study group from 7 PM to 8:30 PM, then went to a 24-hour diner from 8:45 PM to 9:30 PM, and finally visited a local library from 9:45 PM to 10:30 PM. Provide a detailed alibi for Sarah, ensuring the alibi is plausible and accounts for her whereabouts during the entire timeframe. Include interactions with other characters, specific locations, and activities that can be verified.'}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a detailed alibi for the following scenario: {t['scenario']} \nEnsure the alibi is plausible and accounts for the character's whereabouts during the entire timeframe. Include interactions with other characters, specific locations, and activities that can be verified. Your alibi should be coherent, logically consistent, and detailed. Submit your alibi as a plain text string in the following format:\n\nAlibi: [Your detailed alibi here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The alibi should be plausible and account for the character's whereabouts during the entire timeframe.", "The alibi should include interactions with other characters, specific locations, and activities that can be verified.", "The alibi should be coherent, logically consistent, and detailed."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
