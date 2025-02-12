class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "role": "customer service representative",
                "scenario": "You are a customer service representative for a tech company. A customer is calling in to report an issue with their laptop overheating. Engage in a dialogue with the customer, identify the problem, and guide them through troubleshooting steps.",
                "turns": 5
            },
            "2": {
                "role": "historical figure",
                "scenario": "You are role-playing as Albert Einstein in a dialogue with a curious student who wants to learn about the theory of relativity. Engage in a dialogue and explain the key concepts of the theory in a clear and accessible manner.",
                "turns": 5
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"""Your task is to engage in a multi-turn dialogue while maintaining the role of a {t['role']}.

Scenario: {t['scenario']}

You need to engage in {t['turns']} turns of dialogue. Each turn should be a natural and coherent response that fits the context and maintains the role you are playing. You should simulate both sides of the conversation (your role and the other party) to ensure the dialogue is coherent. Provide your responses in plain text format, clearly indicating each turn. Format your response as follows:
Turn 1 (Your Role): <your response>
Turn 2 (Other Party): <your response>
Turn 3 (Your Role): <your response>
Turn 4 (Other Party): <your response>
Turn 5 (Your Role): <your response>"""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The responses should be coherent and contextually appropriate.",
            "The responses should maintain the specified role and scenario.",
            "The dialogue should flow naturally across the specified number of turns.",
            "The agent should simulate both sides of the conversation clearly."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
