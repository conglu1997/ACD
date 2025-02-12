class TaskFamily:

    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "client_statements": [
                    "I've been feeling really anxious lately, and I don't know how to handle it.",
                    "Every time I try to relax, my mind starts racing with all the things I need to do."
                ],
                "session_goal": "Help the client develop strategies to manage anxiety."
            },
            "2": {
                "client_statements": [
                    "I'm struggling to find motivation at work. I used to love my job, but now it feels like a chore.",
                    "Even tasks that used to excite me now seem boring and pointless."
                ],
                "session_goal": "Help the client explore possible reasons for their lack of motivation and find ways to rekindle their interest."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        client_statements = '\n'.join(t["client_statements"])
        session_goal = t["session_goal"]
        instructions = f"""Your task is to simulate a therapeutic session by responding to the client's statements with empathetic and constructive feedback.

Client's Statements:
{client_statements}

Session Goal: {session_goal}

Your response should include:
1. Empathetic acknowledgment of the client's feelings.
2. Constructive feedback or advice that aligns with the session goal.
3. A conversational tone that is supportive and encouraging.

Provide your response in the following format:

Response:
[Your response here]

Ensure that it is comprehensive and demonstrates a deep understanding of the client's emotional state.
"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should empathetically acknowledge the client's feelings.",
            "The response should provide constructive feedback or advice that aligns with the session goal.",
            "The response should maintain a conversational tone that is supportive and encouraging.",
            "The response should demonstrate a deep understanding of the client's emotional state.",
            "The response should follow the specified format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
