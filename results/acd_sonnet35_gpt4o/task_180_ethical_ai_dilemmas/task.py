import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "title": "AI-Driven Healthcare Triage",
                "description": "An AI system is developed to triage patients in overcrowded hospitals. It's highly accurate but occasionally makes errors that human doctors wouldn't. Hospital administrators are considering full deployment."
            },
            {
                "title": "Autonomous Weapon Systems",
                "description": "A country develops AI-powered autonomous weapons capable of making targeting decisions without human intervention. They argue it will reduce military casualties, but concerns about accountability and potential misuse arise."
            },
            {
                "title": "AI in Criminal Justice",
                "description": "An AI system is proposed to assist judges in sentencing decisions. It promises more consistent sentences but raises concerns about bias and the right to be judged by humans."
            },
            {
                "title": "Emotional AI in Education",
                "description": "A school system considers implementing AI tutors capable of reading and responding to students' emotions. It could personalize learning but raises privacy concerns and questions about emotional manipulation."
            }
        ]
        
        tasks = {}
        selected_scenarios = random.sample(scenarios, 2)
        for i, scenario in enumerate(selected_scenarios, 1):
            tasks[str(i)] = scenario
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze the following ethical dilemma involving AI:

Scenario: {t['title']}
{t['description']}

Your task is to:

1. Identify and explain the key ethical issues involved (100-150 words)
2. Analyze the potential consequences of implementing or not implementing the AI system (100-150 words)
3. Propose a solution or policy recommendation, considering all stakeholders (100-150 words)
4. Justify your recommendation, addressing potential counterarguments (100-150 words)

Ensure your response is well-reasoned, considers multiple perspectives, and demonstrates a nuanced understanding of both AI capabilities and ethical principles. Your total response should not exceed 600 words.

Format your response as follows:

Ethical Issues:
[Your analysis]

Potential Consequences:
[Your analysis]

Proposed Solution:
[Your recommendation]

Justification:
[Your justification]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response identifies and explains the key ethical issues comprehensively",
            "The analysis of potential consequences is thorough and considers multiple stakeholders",
            "The proposed solution or policy recommendation is well-reasoned and practical",
            "The justification addresses potential counterarguments effectively",
            "The response demonstrates a nuanced understanding of both AI capabilities and ethical principles",
            "The response follows the specified format and word limits"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
