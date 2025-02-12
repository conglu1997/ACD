class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "scenario": "Alice has been working at her company for 5 years. She has always been punctual and hardworking. Recently, she has been coming late to work and missing deadlines. Her colleagues have noticed her change in behavior and are concerned. Today, her manager called her into the office for a meeting. Alice has been facing personal issues at home, which she has not shared with anyone at work. Her manager is known to be supportive but also has high expectations for performance. Additionally, there have been recent layoffs in the company due to performance issues.",
                "question": "What is the most likely outcome of the meeting between Alice and her manager?"
            },
            "2": {
                "scenario": "John and his friends have planned a surprise birthday party for their friend, Sam. They have been organizing it for weeks and have invited all of Sam's close friends. On the day of the party, Sam receives an urgent work call and has to decide whether to attend the party or deal with the work emergency. Sam is known to be a very responsible person and has a close relationship with his friends. The work emergency is critical and could have significant consequences if not addressed immediately. Additionally, Sam has been feeling guilty about missing out on social events due to work commitments in the past.",
                "question": "What is Sam most likely to do, and what are the potential outcomes of his decision?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the given social scenario and predict the outcome based on common social norms and human behavior. Your response should include:
1. A brief summary of the scenario.
2. A prediction of the most likely outcome.
3. A brief explanation of the reasoning behind your prediction.

Scenario:
{t['scenario']}

Question:
{t['question']}

Example response format:
- Scenario Summary: Alice has been working at her company for 5 years and has recently started showing signs of being late and missing deadlines. Her manager calls her for a meeting.
- Predicted Outcome: The manager is likely to express concern and ask if there is anything troubling Alice, offering support or suggesting ways to improve her performance.
- Reasoning: Based on common workplace behavior, managers typically address performance issues by first understanding the underlying causes and offering support to help employees improve, especially when the company has high performance expectations and recent layoffs have occurred."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The scenario summary should accurately reflect the given scenario.",
            "The predicted outcome should be plausible based on common social norms and human behavior.",
            "The reasoning should logically explain why the predicted outcome is likely, considering the additional context provided."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
