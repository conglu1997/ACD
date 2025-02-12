class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "job interview", "role": "interviewee", "context": "You are applying for a software engineering position at a tech company. You need to answer questions about your experience, skills, and fit for the role."},
            "2": {"scenario": "diplomatic negotiation", "role": "diplomat", "context": "You are a diplomat representing your country in a negotiation to resolve a trade dispute. You need to navigate the conversation to achieve a favorable outcome for your country."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Engage in the following role-playing scenario as described below:

Scenario: {t["scenario"]}
Role: {t["role"]}
Context: {t["context"]}

Maintain the context throughout the conversation and generate coherent dialogue. Your responses should be appropriate for the role and scenario. Submit your dialogue as a plain text string in the following format:

Prompt 1: [Interviewer/Diplomat's question]
Response 1: [Your response to Prompt 1]
Prompt 2: [Interviewer/Diplomat's question]
Response 2: [Your response to Prompt 2]
...
Prompt N: [Interviewer/Diplomat's question]
Response N: [Your response to Prompt N]

Ensure your responses are contextually appropriate and logically consistent with the scenario and role. The dialogue should be coherent and relevant to the prompts given."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["Responses should be contextually appropriate and logically consistent with the role and scenario.", "Dialogue should be coherent and relevant to the prompts given."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
