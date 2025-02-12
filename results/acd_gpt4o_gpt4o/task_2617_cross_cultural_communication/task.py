class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are attending a business meeting in Japan. Your task is to greet your Japanese colleagues appropriately and navigate the initial conversation, respecting Japanese business etiquette. Specifically, you should consider the following: bowing as a greeting, exchanging business cards with both hands, and addressing colleagues with appropriate honorifics.", "roles": {"you": "You", "colleague_1": "Mr. Sato", "colleague_2": "Ms. Tanaka"}},
            "2": {"scenario": "You are invited to a traditional dinner in Morocco. Your task is to interact with your hosts and other guests, demonstrating an understanding of Moroccan dining etiquette. Specifically, you should consider the following: washing your hands before the meal, eating with your right hand, and showing appreciation for the food and hospitality.", "roles": {"you": "You", "host": "Mr. Ahmed", "guest": "Ms. Fatima"}}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to navigate a cross-cultural scenario and demonstrate an understanding of the cultural norms and etiquette described below:

Scenario: {t['scenario']}

Roles:
{t['roles']}

Provide a detailed response that demonstrates cultural understanding, empathy, and adaptability. Your response should include:
1. An initial approach to address the situation.
2. Steps to navigate the cultural norms appropriately.
3. Consideration of the cultural sensitivities involved.
4. A final resolution or interaction that aims to foster positive cross-cultural relations.

Provide your response in plain text format, clearly separating each of the four components.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should demonstrate an understanding of the cultural norms involved.",
            "The response should include steps to navigate the cultural situation appropriately.",
            "The response should show empathy and respect for cultural sensitivities.",
            "The response should aim to foster positive cross-cultural relations."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
