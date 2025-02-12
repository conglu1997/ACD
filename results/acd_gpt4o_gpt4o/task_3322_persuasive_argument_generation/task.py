class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"topic": "Should schools implement a four-day school week?"},
            "2": {"topic": "Is it better to rent or buy a home?"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        topic = t["topic"]
        instructions = f"""Your task is to generate persuasive arguments for and against the following topic. Ensure that your arguments are well-structured, logical, persuasive, and supported by evidence or reasoning.

Topic: {topic}

Provide your response in the following format:

Arguments For:
1. [First Argument]
    Reasoning: [Reasoning or evidence for the first argument]
2. [Second Argument]
    Reasoning: [Reasoning or evidence for the second argument]
3. [Third Argument]
    Reasoning: [Reasoning or evidence for the third argument]

Arguments Against:
1. [First Argument]
    Reasoning: [Reasoning or evidence for the first argument]
2. [Second Argument]
    Reasoning: [Reasoning or evidence for the second argument]
3. [Third Argument]
    Reasoning: [Reasoning or evidence for the third argument]

Ensure that:
1. Each argument is clear and concise.
2. Each argument is relevant to the topic.
3. Each argument is supported by evidence or reasoning.
4. The arguments are balanced and consider multiple perspectives."""
        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The arguments should be well-structured, logical, and persuasive.",
            "Each argument should be clear and concise.",
            "Each argument should be relevant to the topic.",
            "Each argument should be supported by evidence or reasoning.",
            "The arguments should be balanced and consider multiple perspectives."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
