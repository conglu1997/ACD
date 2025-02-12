class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "topic": "The importance of renewable energy",
                "requirements": "Write a persuasive argument supporting the importance of renewable energy. Your argument should be well-structured, include at least three key points, address potential counterarguments, and be logically compelling."
            },
            "2": {
                "argument": "Many people believe that investing in renewable energy is crucial for the future of our planet. Firstly, renewable energy sources such as solar and wind power are sustainable and will never run out, unlike fossil fuels which are finite. Secondly, renewable energy has a much lower environmental impact, reducing pollution and greenhouse gas emissions. Thirdly, investing in renewable energy can create jobs and stimulate economic growth. However, some argue that the initial cost of setting up renewable energy infrastructure is too high. Nonetheless, the long-term benefits of renewable energy far outweigh these initial costs, making it a necessary investment for a sustainable future.",
                "requirements": "Identify and list the three key points in the given argument and explain how each point supports the overall argument. Additionally, identify the counterargument presented and explain how it is addressed."
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        if 'topic' in t:
            return f"""Craft a persuasive argument on the following topic:

Topic: {t['topic']}

Requirements: {t['requirements']}

Your argument should be well-structured, include at least three key points, address potential counterarguments, and be logically compelling. Submit your argument as a plain text string in the following format:

Argument: [Your argument]"""
        else:
            return f"""Identify and list the key points in the following argument and explain how each point supports the overall argument. Additionally, identify the counterargument presented and explain how it is addressed:

Argument: {t['argument']}

Requirements: {t['requirements']}

Submit your response as a plain text string in the following format:

Key Points: [List of key points]
Explanation: [Explanation of how each point supports the argument]
Counterargument: [The counterargument identified]
Addressing Counterargument: [Explanation of how the counterargument is addressed]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        if 'topic' in t:
            validation_criteria = [
                "The argument should be well-structured.",
                "The argument should include at least three key points.",
                "The argument should address potential counterarguments.",
                "The argument should be logically compelling."
            ]
        else:
            validation_criteria = [
                "The response should list the three key points in the argument.",
                "The response should explain how each point supports the overall argument.",
                "The response should identify the counterargument and explain how it is addressed."
            ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
