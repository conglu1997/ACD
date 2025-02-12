class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "John has been feeling increasingly anxious about his job performance. He often worries about making mistakes and feels that his colleagues are more competent than he is. Recently, he has been avoiding social interactions at work and prefers to work alone."},
            "2": {"scenario": "Samantha has been feeling very stressed due to her upcoming exams. She spends long hours studying and has trouble sleeping. Despite her hard work, she feels that she is not prepared and fears failing her exams. She has also been experiencing headaches and irritability."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following scenario and provide a detailed interpretation of the emotions and behaviors exhibited by the individual. Your analysis should include possible underlying causes, the impact on the individual's well-being, and potential strategies to help them cope with their emotions.

Scenario: {t["scenario"]}

Submit your response as a plain text string in the following format:

Analysis: [Your detailed analysis]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The analysis should include possible underlying causes of the emotions.", "The analysis should discuss the impact on the individual's well-being.", "The analysis should provide potential coping strategies."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
