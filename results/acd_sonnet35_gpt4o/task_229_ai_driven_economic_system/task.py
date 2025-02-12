import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'system_focus': 'Resource Allocation',
                'ai_capability': 'Predictive Analytics',
                'behavioral_principle': 'Loss Aversion'
            },
            {
                'system_focus': 'Labor Market',
                'ai_capability': 'Natural Language Processing',
                'behavioral_principle': 'Social Proof'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel economic system that incorporates artificial intelligence and behavioral economics principles. Your task has four parts:

1. System Design (150-200 words):
   Create an economic system focused on {t['system_focus']} that integrates AI with {t['ai_capability']} capabilities and the behavioral economics principle of {t['behavioral_principle']}. Describe the key components and mechanisms of your system.

2. AI Integration (100-150 words):
   Explain how the AI's {t['ai_capability']} capabilities would be utilized in the system. Discuss potential benefits and risks of this integration.

3. Behavioral Economics Application (100-150 words):
   Describe how the principle of {t['behavioral_principle']} is incorporated into the system. Analyze its potential effects on individual and collective economic behavior.

4. System Analysis (150-200 words):
   Identify two potential challenges or unintended consequences that could arise in your proposed system. For each, suggest a possible solution or mitigation strategy.

Ensure your response demonstrates a deep understanding of economic principles, artificial intelligence, and behavioral economics. Your system should be innovative, logically consistent, and consider ethical implications.

Format your response as follows:

System Design:
[Your description here]

AI Integration:
[Your explanation here]

Behavioral Economics Application:
[Your description and analysis here]

System Analysis:
1. [First challenge and solution]
2. [Second challenge and solution]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The economic system design effectively incorporates {t['system_focus']}, AI with {t['ai_capability']} capabilities, and the behavioral economics principle of {t['behavioral_principle']}.",
            "The response demonstrates a clear understanding of economic principles, artificial intelligence, and behavioral economics.",
            "The system design is innovative, logically consistent, and considers ethical implications.",
            "The analysis of challenges and proposed solutions is thoughtful and plausible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
