class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "historical_event": "The signing of the Declaration of Independence in 1776. Include at least two historical figures and one fictional character.",
                "task_type": "create"
            },
            "2": {
                "fiction_excerpt": "John stood in the bustling streets of Paris, 1789. The air was thick with the fervor of revolution, as citizens rallied for liberty, equality, and fraternity. He clutched a worn letter from his brother, who had joined the insurgents at the Bastille, urging him to join the cause. As he pondered his next move, he saw Marie, an old friend turned revolutionary, passionately addressing the crowd.",
                "task_type": "interpret"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t["task_type"] == "create":
            return f"""Create a historical fiction narrative based on the following historical event. Ensure that your narrative is engaging, historically accurate, and captures the essence of the period. Include at least two historical figures and one fictional character in your narrative. Your narrative should be between 200 to 300 words.

Historical Event:
{t['historical_event']}

Submit your narrative as a plain text string."""
        elif t["task_type"] == "interpret":
            return f"""Interpret the following historical fiction excerpt. Identify the key elements of the narrative and the historical context in which it is set. Your interpretation should be clear, logically organized, and demonstrate an understanding of the historical period described.

Excerpt:
{t['fiction_excerpt']}

Submit your interpretation as a plain text string in the following format:
"Key Elements: [Your interpretation here] Historical Context: [Your interpretation here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t["task_type"] == "create":
            validation_criteria = ["The narrative should be engaging and historically accurate.", "The narrative should capture the essence of the historical period.", "The narrative should include at least two historical figures and one fictional character."]
        elif t["task_type"] == "interpret":
            validation_criteria = ["The interpretation should accurately identify the key elements of the narrative.", "The interpretation should demonstrate an understanding of the historical context."]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
