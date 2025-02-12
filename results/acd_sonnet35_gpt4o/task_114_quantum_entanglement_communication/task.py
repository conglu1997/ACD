import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'scenario': 'interplanetary_communication',
                'constraint': 'energy_efficiency'
            },
            {
                'scenario': 'underwater_civilization',
                'constraint': 'information_security'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a communication system for a civilization in a universe where quantum entanglement can be easily manipulated at macroscopic scales. Your system should address the following scenario and constraint:

Scenario: {t['scenario']}
Constraint: {t['constraint']}

Your task:
1. Briefly explain the concept of quantum entanglement and its potential for communication (2-3 sentences).
2. Design a communication system that leverages macroscopic quantum entanglement for the given scenario. Describe its key components and functioning (4-5 sentences).
3. Explain how your system addresses the given constraint (2-3 sentences).
4. Provide two specific examples of how your system would transmit different types of information.
5. Discuss one potential limitation of your system and propose a solution (2-3 sentences).
6. Analyze how this communication system might impact the civilization's social structures or technological development (3-4 sentences).
7. Explore one ethical implication of using such a communication system (2-3 sentences).

Format your response as follows:

Quantum Entanglement Explanation:
[Your explanation]

Communication System Design:
[Your description]

Addressing the Constraint:
[Your explanation]

Information Transmission Examples:
1. [First example]
2. [Second example]

Limitation and Solution:
[Your discussion]

Societal Impact:
[Your analysis]

Ethical Implication:
[Your exploration]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The explanation of quantum entanglement is accurate and clear.",
            "The communication system design creatively incorporates macroscopic quantum entanglement.",
            "The system effectively addresses the given scenario and constraint.",
            "The information transmission examples are diverse and demonstrate the system's capabilities.",
            "The limitation discussion and proposed solution are thoughtful and relevant.",
            "The analysis of societal impact is insightful and well-reasoned.",
            "The ethical implication explored is relevant and thought-provoking.",
            "The overall response demonstrates a deep understanding of quantum mechanics and its potential applications in communication."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
