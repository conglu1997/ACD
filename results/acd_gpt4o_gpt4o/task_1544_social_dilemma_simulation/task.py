class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "You are the manager of a small team. One of your team members, Alex, has been consistently underperforming due to personal issues. Another team member, Jamie, has been picking up the slack but is now feeling overwhelmed. You need to decide how to address the situation.", "options": ["Option 1: Have a private conversation with Alex to understand their situation and offer support.", "Option 2: Reassign some of Alex's tasks to other team members to balance the workload.", "Option 3: Provide additional resources or temporary help to support the team.", "Option 4: Take disciplinary action against Alex for underperformance."]},
            "2": {"scenario": "You are a high school teacher. One of your students, Taylor, has been showing signs of bullying another student, Jordan. You need to decide how to handle the situation.", "options": ["Option 1: Have a private conversation with Taylor to understand their behavior and provide guidance.", "Option 2: Report the incident to the school administration for further action.", "Option 3: Organize a mediation session between Taylor and Jordan to resolve the conflict.", "Option 4: Implement an anti-bullying program in your class."]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to navigate the following social dilemma and make a decision considering ethical, emotional, and social factors. Here is the scenario and the options:
Scenario: {t['scenario']}
Options: {', '.join(t['options'])}
Please describe which option you would choose and provide a detailed explanation of your reasoning. Consider the ethical, emotional, and social implications of your decision. Structure your response as follows:
- Chosen option: [Your chosen option]
- Reasoning: [Detailed explanation of your reasoning, considering ethical, emotional, and social implications]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The response should include a clear choice of option and a detailed explanation of the reasoning behind the decision, considering ethical, emotional, and social implications."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
