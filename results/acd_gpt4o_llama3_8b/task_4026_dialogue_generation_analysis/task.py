class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "characters": "Alice and Bob",
                "setting": "A coffee shop",
                "requirements": "Generate a fictional dialogue between Alice and Bob who are meeting for the first time in a coffee shop. The dialogue should be natural, engaging, and at least 15 exchanges long. Ensure the conversation reveals something interesting about each character."
            },
            "2": {
                "dialogue": "Alice: Hi, I'm Alice.\nBob: Nice to meet you, Alice. I'm Bob.\nAlice: What brings you to this coffee shop today?\nBob: Just taking a break from work. How about you?\nAlice: I'm here to meet a friend, actually.\nBob: That's nice. What do you do for a living?\nAlice: I'm a graphic designer. And you?\nBob: I'm a software developer. I work on creating mobile apps.\nAlice: That sounds interesting! Do you enjoy it?\nBob: I do, especially when I get to work on innovative projects. What about you, do you enjoy designing?\nAlice: Absolutely! I love bringing ideas to life through design.\nBob: That's great to hear. Do you have any favorite projects you've worked on?\nAlice: Yes, there's this one project where I designed a whole brand identity for a startup. It was a challenging but rewarding experience.\nBob: That sounds impressive! I'd love to hear more about it.\nAlice: Sure, I'd be happy to share. What about you, any memorable projects?\nBob: There's one where I worked on an app that helps people track their fitness goals. It was a collaborative effort, and we received great feedback from users.",
                "requirements": "Analyze the given dialogue between Alice and Bob. Provide a detailed analysis of the characters' personalities, the flow of the conversation, and any underlying themes or subtext. Your analysis should be thorough and cover various aspects of the dialogue."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'characters' in t:
            return f"""Generate a fictional dialogue based on the following characters and setting:

Characters: {t['characters']}
Setting: {t['setting']}

Requirements: {t['requirements']}

Your dialogue should be at least 15 exchanges long, natural, engaging, and reveal something interesting about each character. Submit your dialogue as a plain text string in the following format:

Alice: [Alice's dialogue]
Bob: [Bob's dialogue]
..."""
        else:
            return f"""Analyze the following dialogue and provide a detailed analysis based on the requirements:

Dialogue: {t['dialogue']}

Requirements: {t['requirements']}

Your analysis should cover the characters' personalities, the flow of the conversation, and any underlying themes or subtext. Ensure that your analysis is thorough and covers various aspects of the dialogue. Submit your analysis as a plain text string in the following format:

Character Analysis: [Your analysis of the characters' personalities]
Flow Analysis: [Your analysis of the flow of the conversation]
Theme Analysis: [Your analysis of any underlying themes or subtext]
..."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'characters' in t:
            validation_criteria = [
                "The dialogue should be at least 15 exchanges long.",
                "The dialogue should be natural and engaging.",
                "The dialogue should reveal something interesting about each character."
            ]
        else:
            validation_criteria = [
                "The analysis should cover the characters' personalities.",
                "The analysis should cover the flow of the conversation.",
                "The analysis should cover any underlying themes or subtext.",
                "The analysis should be thorough and cover various aspects of the dialogue."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
