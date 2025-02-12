import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "domain": "Autonomous Vehicles",
                "dilemma": "An autonomous vehicle must choose between hitting a group of pedestrians or sacrificing its passenger",
                "stakeholders": ["Pedestrians", "Vehicle passengers", "AI developers", "Car manufacturers", "Insurance companies", "Policymakers"]
            },
            {
                "domain": "Healthcare AI",
                "dilemma": "An AI system must allocate limited medical resources among patients with varying survival probabilities and quality of life outcomes",
                "stakeholders": ["Patients", "Healthcare providers", "AI developers", "Hospital administrators", "Ethicists", "Policymakers"]
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Analyze the following AI ethics dilemma in the domain of {t['domain']}:\n\n" + \
               f"{t['dilemma']}\n\n" + \
               f"Stakeholders: {', '.join(t['stakeholders'])}\n\n" + \
               "Provide your analysis and proposed solution in the following format:\n\n" + \
               "1. Ethical Analysis (200-250 words):\n" + \
               "   - Identify the key ethical principles at stake\n" + \
               "   - Discuss the potential consequences for each stakeholder\n" + \
               "   - Explain any relevant ethical frameworks or theories that apply to this scenario\n\n" + \
               "2. AI System Design Considerations (150-200 words):\n" + \
               "   - Describe how the AI system should be designed to handle this dilemma\n" + \
               "   - Discuss any technical limitations or challenges in implementing your proposed solution\n\n" + \
               "3. Proposed Solution (200-250 words):\n" + \
               "   - Present a detailed solution that addresses the ethical dilemma\n" + \
               "   - Explain how your solution balances the interests of different stakeholders\n" + \
               "   - Discuss any potential drawbacks or unintended consequences of your solution\n\n" + \
               "4. Policy Recommendations (150-200 words):\n" + \
               "   - Suggest policy or regulatory measures to govern AI decision-making in this domain\n" + \
               "   - Explain how these measures would help prevent or mitigate similar ethical dilemmas\n\n" + \
               "Ensure your response demonstrates a deep understanding of AI ethics, creative problem-solving skills, and the ability to balance competing interests in complex scenarios."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the ethical implications of the dilemma",
            "The analysis considers multiple ethical frameworks and their applicability to the scenario",
            "The proposed AI system design is technically feasible and addresses the ethical concerns",
            "The solution effectively balances the interests of different stakeholders",
            "The policy recommendations are practical and likely to mitigate similar ethical dilemmas in the future",
            "The response shows creativity and original thinking in addressing the complex issue",
            "The analysis and proposed solutions are well-reasoned and logically consistent"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
