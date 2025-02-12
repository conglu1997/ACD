class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "John is suspected of stealing a valuable painting from an art gallery between 8 PM and 10 PM on Saturday. Provide a plausible alibi for John that explains his whereabouts during the specified time frame. John was seen leaving his house at 7:30 PM and returning at 10:30 PM.",
                "constraints": "John must be in a public place with witnesses during the entire time frame, and he must have a valid reason for being there."
            },
            "2": {
                "scenario": "Emily is accused of hacking into a company's database at midnight on Friday. Provide a plausible alibi for Emily that explains her activities during the specified time frame. Emily was last seen online at 11:45 PM and her computer was found turned off at 12:30 AM.",
                "constraints": "Emily must be engaged in an activity that requires her full attention, away from any electronic devices, and in the presence of others."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a plausible alibi for the following character based on the given scenario and constraints.

Scenario: {t['scenario']}

Constraints: {t['constraints']}

Instructions:
1. Create a detailed narrative that explains the character's whereabouts and activities during the specified time frame.
2. Ensure the alibi is believable and consistent with the given constraints.
3. Your response should be in the following format:
Alibi: [Your alibi]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The alibi should be detailed and believable.", "The alibi should be consistent with the given constraints."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
