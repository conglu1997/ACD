class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"role": "therapist", "scenario": "A client is expressing anxiety about an upcoming job interview. They are worried about making a good impression and fear they might not meet the expectations of the interviewer."},
            "2": {"role": "teacher", "scenario": "A student is struggling with understanding a complex math concept. They have tried multiple times but still cannot grasp the idea, and they are feeling frustrated and demotivated."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As a {t['role']}, respond to the following scenario:

Scenario: {t['scenario']}

Your response should be detailed (at least 150 words), contextually appropriate, and maintain the character of a {t['role']}. Ensure that your response is empathetic and supportive, addressing the concerns mentioned in the scenario. Submit your response as a plain text string in the following format:

Response: [Your response here]

Example: 
Response: As a therapist, I understand that job interviews can be very stressful. Let's talk about what specifically is causing you anxiety and how we can address these concerns together..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [f"The response should be detailed (at least 150 words) and contextually appropriate for the role of a {t['role']}.", "The response should maintain the character and professionalism expected of the given role.", "The response should be empathetic and supportive.", "The response should have a logical flow and be coherent."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
