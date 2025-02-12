class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"prompts": [
                "At 7:00 AM, John wakes up.",
                "At 8:00 AM, John has breakfast.",
                "At 10:00 AM, John goes for a jog in the park.",
                "At 12:00 PM, John meets a friend for lunch."
            ]},
            "2": {"prompts": [
                "At 6:00 PM, Sarah finishes her work.",
                "At 7:00 PM, Sarah attends a yoga class.",
                "At 9:00 PM, Sarah has dinner with her family.",
                "At 11:00 PM, Sarah goes to bed."
            ]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to generate a coherent and engaging story based on the following time-based prompts. Ensure that the story logically follows the sequence of events and maintains consistency throughout. Provide your story in plain text format.

Prompts:
{t['prompts'][0]}
{t['prompts'][1]}
{t['prompts'][2]}
{t['prompts'][3]}

Your response should include:
1. A detailed and engaging narrative that incorporates all the given time-based prompts.
2. Logical transitions between the events based on their temporal sequence.
3. Consistency in the storyline and character actions.
4. Ensure the story is engaging and well-written, making the reader interested in the events.

Ensure your story is coherent and follows the sequence of events accurately."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The story should incorporate all the given time-based prompts.",
            "The story should have logical transitions between the events based on their temporal sequence.",
            "The story should maintain consistency in the storyline and character actions.",
            "The story should be engaging and well-written, making the reader interested in the events."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
