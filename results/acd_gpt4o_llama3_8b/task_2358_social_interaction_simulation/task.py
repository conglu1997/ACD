class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are at a party and notice someone standing alone, looking uncomfortable. Initiate a conversation to make them feel welcome and engaged."
            },
            "2": {
                "scenario": "A colleague is visibly upset at work. Engage in a dialogue to understand their situation and offer support."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario:

Scenario:
{t['scenario']}

Your response should include the following elements:
1. Initiation: Start the conversation in a friendly and non-intrusive manner. Use open-ended questions to encourage engagement.
2. Engagement: Maintain the dialogue by showing empathy, listening actively, and understanding social cues. Acknowledge the other person's feelings and respond appropriately.
3. Resolution: Conclude the interaction in a way that leaves the other person feeling better or more comfortable. Offer assistance or a follow-up where appropriate.

Ensure that your response is coherent, contextually appropriate, and demonstrates a deep understanding of social interactions and empathy. Provide enough detail to show your ability to navigate the social scenario effectively. Submit your response as a plain text string.

Example response format:

Initiation:
- [Your initiation here]

Engagement:
- [Your engagement here]

Resolution:
- [Your resolution here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The conversation should start in a friendly and non-intrusive manner.",
            "The dialogue should include open-ended questions to encourage engagement.",
            "The dialogue should show empathy, active listening, and understanding of social cues.",
            "The interaction should conclude in a way that leaves the other person feeling better or more comfortable.",
            "The response should be coherent and contextually appropriate."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
