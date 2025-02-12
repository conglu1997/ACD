class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"text": "I enjoy meeting new people and often find myself at the center of social gatherings. I thrive in dynamic environments and love taking on new challenges. My friends describe me as outgoing and energetic. I also like to explore new ideas and experiences. I am open to trying new things and always seek to learn more.", "task_type": "big_five"},
            "2": {"text": "I often feel anxious in unfamiliar situations and prefer routine and stability. I tend to be reserved and keep my thoughts to myself. My colleagues say I am meticulous and detail-oriented. I also value traditional approaches and consistency. I am not very spontaneous and prefer sticking to what I know.", "task_type": "myers_briggs"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if t['task_type'] == 'big_five':
            return f"Analyze the following text and infer the individual's personality traits based on the Big Five personality traits model (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism):\n\n'{t['text']}'\n\nSubmit your response as a plain text string in the following format:\nOpenness: [Low/Medium/High]\nConscientiousness: [Low/Medium/High]\nExtraversion: [Low/Medium/High]\nAgreeableness: [Low/Medium/High]\nNeuroticism: [Low/Medium/High]"
        elif t['task_type'] == 'myers_briggs':
            return f"Analyze the following text and infer the individual's Myers-Briggs Type Indicator (MBTI) personality type:\n\n'{t['text']}'\n\nSubmit your response as a plain text string with the inferred MBTI type (e.g., INFP, ESTJ)."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if t['task_type'] == 'big_five':
            criteria = ["The response should correctly infer levels for all Big Five personality traits (Openness, Conscientiousness, Extraversion, Agreeableness, Neuroticism)."]
        elif t['task_type'] == 'myers_briggs':
            criteria = ["The response should correctly infer the MBTI personality type."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
