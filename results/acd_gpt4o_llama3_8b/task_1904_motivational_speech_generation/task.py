class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A high school graduation ceremony",
                "audience": "Graduating students and their families"
            },
            "2": {
                "scenario": "A corporate team-building event",
                "audience": "Company employees aiming to improve collaboration"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate a motivational speech for the following scenario and audience:

Scenario: {t['scenario']}
Audience: {t['audience']}

Ensure that the speech is inspiring, contextually appropriate, and persuasive. The speech should be about 400-500 words long and should address the specific needs and aspirations of the audience. Use a tone that is suitable for the given scenario and audience, and incorporate relevant anecdotes, metaphors, or rhetorical devices to enhance the impact of the speech.

Submit your speech as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The speech should be motivational and persuasive.",
            "The speech should be contextually appropriate for the given scenario and audience.",
            "The speech should be about 400-500 words long.",
            "The speech should use a suitable tone and incorporate relevant anecdotes, metaphors, or rhetorical devices."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
