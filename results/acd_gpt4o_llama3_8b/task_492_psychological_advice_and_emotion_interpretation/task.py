class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "A person named Alex is feeling overwhelmed with work and personal life responsibilities. They are struggling to find a balance and are experiencing high levels of stress and anxiety. Alex has been working late hours, missing meals, and has had trouble sleeping. Provide psychological advice to help Alex manage their stress and find a better balance.",
            },
            "2": {
                "scenario": "A teenager named Jamie is feeling isolated and lonely after moving to a new city. Jamie is having trouble making new friends and is feeling homesick. They spend most of their time alone in their room, browsing social media and missing their old life. Interpret Jamie's emotional state and provide advice on how they can cope with their feelings and improve their situation.",
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Complete the following task based on the given scenario:

Scenario:
{t['scenario']}

Your response should include the following sections:
1. Emotional State: Interpret the person's emotional state based on the scenario. Describe their feelings in detail and explain why they might be feeling this way.
2. Advice: Provide psychological advice to help the person cope with their emotions and improve their situation. Your advice should include at least two distinct strategies or methods.

Ensure that your response is empathetic, clear, and demonstrates a thorough understanding of human psychology. Provide enough detail in each section to show a deep comprehension of the scenario and applicable psychological principles. Each section should be clearly labeled and well-organized. Submit your response as a plain text string.

Example response format:

Emotional State:
- Interpretation of emotions: Description...

Advice:
- Strategy 1: Description...
- Strategy 2: Description...

Your response should be at least 200 words to ensure depth and detail."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The emotional state should be accurately interpreted and relevant to the scenario.",
            "The advice should be clear, empathetic, and well-structured.",
            "Each section should be clearly labeled and well-organized.",
            "The response should demonstrate a thorough understanding of human psychology and coping strategies.",
            "The response should be at least 200 words in length.",
            "The advice should include at least two distinct strategies or methods."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
