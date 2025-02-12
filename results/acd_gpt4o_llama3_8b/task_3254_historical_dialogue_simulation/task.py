class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"figure1": "Albert Einstein", "figure2": "Isaac Newton", "topic": "the nature of gravity"},
            "2": {"figure1": "Cleopatra", "figure2": "Julius Caesar", "topic": "political strategy"}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        figure1 = t["figure1"]
        figure2 = t["figure2"]
        topic = t["topic"]
        return f"""Simulate a conversation between {figure1} and {figure2} on the topic of {topic}. The conversation should be historically plausible, reflect the personalities and knowledge of both figures, and be engaging and coherent. Ensure that the dialogue accurately represents the historical context and viewpoints of both figures. Submit your response as a plain text string in the following format:

[Figure 1]: [Their dialogue]
[Figure 2]: [Their dialogue]
...

Example format:
[Albert Einstein]: What do you think about the nature of gravity, Sir Isaac?
[Isaac Newton]: I believe gravity is a force that pulls objects towards one another...

Consider the following points while creating the dialogue:
- The conversation should be engaging and coherent.
- The historical context and viewpoints of both figures should be accurately represented.
- The dialogue should reflect the personalities and knowledge of both figures."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conversation should be engaging and coherent.",
            "The historical context and viewpoints of both figures should be accurately represented.",
            "The dialogue should reflect the personalities and knowledge of both figures.",
            "The conversational flow should be logical and natural.",
            "The submission should adhere to the specified format."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
