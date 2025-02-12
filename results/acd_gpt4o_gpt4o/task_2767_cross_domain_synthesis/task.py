class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"domains": ["Technology", "Biology"], "task": "Propose a novel bioengineering application that leverages recent advancements in artificial intelligence."},
            "2": {"domains": ["History", "Economics"], "task": "Analyze the economic impact of a major historical event and propose a modern policy that could mitigate similar impacts if the event were to occur today."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        domains = ', '.join(t['domains'])
        return f"""Your task is to synthesize information from the fields of {domains} to address the following prompt:

{t['task']}

Ensure that your response is comprehensive, well-organized, and demonstrates an integration of knowledge from both fields. Provide your response in plain text format with clear sections that outline your thought process and conclusions:
1. Introduction: [Introduce the task and the fields involved]
2. Synthesis: [Integrate knowledge from both fields to address the task]
3. Conclusion: [Summarize your findings and propose a solution or insight]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should demonstrate integration of knowledge from both fields.", "The response should be well-organized with clear sections."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
