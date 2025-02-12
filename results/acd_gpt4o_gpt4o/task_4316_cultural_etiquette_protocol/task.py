class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "You are attending a formal dinner in Japan hosted by a traditional Japanese family. Describe the appropriate etiquette for greeting the host, the proper way to handle the chopsticks, and any specific table manners you should observe.",
                "expected_output": "Appropriate etiquette for greeting the host in Japan includes bowing as a sign of respect. When handling chopsticks, you should not point them at others, stick them upright in a bowl of rice, or pass food directly from your chopsticks to someone else's. Specific table manners include waiting for the host to start eating before you start, saying 'itadakimasu' before eating, and 'gochisousama' after finishing the meal."
            },
            "2": {
                "scenario": "You are invited to a business meeting in Saudi Arabia by a high-ranking official. Describe the appropriate dress code, the protocol for greeting your business partners, and any cultural considerations you should keep in mind during the meeting.",
                "expected_output": "The appropriate dress code for a business meeting in Saudi Arabia typically includes conservative attire, such as a suit and tie for men and modest clothing for women, often covering the arms and legs. The protocol for greeting business partners includes a handshake, but be aware that some Saudi men may not shake hands with women. It's also customary to engage in small talk before getting down to business. Cultural considerations include avoiding discussing politics or religion, and showing respect for Saudi customs and traditions."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to understand the given scenario and describe the appropriate cultural etiquette and protocol.

Scenario: {t['scenario']}

Provide your response in plain text format. Ensure your response is detailed and covers all aspects of the scenario."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response correctly describes the cultural etiquette and protocol based on the given scenario.",
            "The response should be accurate, contextually appropriate, and respectful of cultural norms.",
            "The response should be detailed and address all aspects of the scenario."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
