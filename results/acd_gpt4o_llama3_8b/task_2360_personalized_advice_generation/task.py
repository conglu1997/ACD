class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "user_profile": "Name: John\nAge: 30\nOccupation: Software Engineer\nLocation: San Francisco, CA\nInterests: Hiking, Reading, Cooking\nGoals: Career advancement, Balanced work-life",
                "advice_type": "Career"
            },
            "2": {
                "user_profile": "Name: Sarah\nAge: 25\nOccupation: Graphic Designer\nLocation: Austin, TX\nInterests: Painting, Traveling, Yoga\nGoals: Improved health, Creative growth",
                "advice_type": "Health"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Generate personalized {t['advice_type'].lower()} advice for the user based on the provided profile.

User Profile:
{t['user_profile']}

In your response, include the following sections:
1. Advice: Provide clear and actionable advice tailored to the user's profile.
2. Rationale: Explain why this advice is suitable and how it aligns with the user's characteristics, interests, and goals.

Ensure that your response is personalized, relevant, and demonstrates an understanding of the user's profile. Submit your response as a plain text string.

Example response format:

Advice:
[Your advice here]

Rationale:
[Your rationale here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The advice should be clear and actionable.",
            "The advice should be personalized and relevant to the user's profile.",
            "The rationale should explain why the advice is suitable and how it aligns with the user's characteristics, interests, and goals.",
            "The response should demonstrate an understanding of the user's profile."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
