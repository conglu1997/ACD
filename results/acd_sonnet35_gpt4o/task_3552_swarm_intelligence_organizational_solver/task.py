import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        insect_types = ['Ants', 'Bees', 'Termites']
        organizational_problems = [
            'Optimizing global supply chain logistics during a pandemic',
            'Improving decision-making in decentralized teams across multiple time zones',
            'Enhancing information flow in large corporations with conflicting departmental interests',
            'Balancing workload distribution in project management with limited resources and tight deadlines',
            'Adapting to rapidly changing market conditions in a highly regulated industry'
        ]
        constraints = [
            'Minimize environmental impact',
            'Ensure data privacy and security',
            'Maintain employee well-being and work-life balance',
            'Operate within strict budget limitations',
            'Comply with complex international regulations'
        ]
        
        return {
            "1": {
                "insect_type": random.choice(insect_types),
                "organizational_problem": random.choice(organizational_problems),
                "constraint": random.choice(constraints)
            },
            "2": {
                "insect_type": random.choice(insect_types),
                "organizational_problem": random.choice(organizational_problems),
                "constraint": random.choice(constraints)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that simulates the evolution of collective intelligence in {t['insect_type']} and applies these principles to solve the human organizational problem of {t['organizational_problem']}, while satisfying the constraint: {t['constraint']}. Your response should include:\n\n1. Swarm Intelligence Analysis (200-250 words):\n   a) Describe the key features of collective intelligence in {t['insect_type']}.\n   b) Explain how these features contribute to problem-solving and adaptation in their colonies.\n   c) Discuss any limitations or potential issues in directly applying these principles to human organizations.\n\n2. AI System Design (250-300 words):\n   a) Outline the architecture of your AI system, including its main components and how they interact.\n   b) Explain how your system models and simulates the evolution of collective intelligence.\n   c) Describe how your system translates insect swarm behaviors into applicable strategies for human organizations.\n   d) Discuss any novel algorithms or approaches you've incorporated to handle the complexities of both biological and organizational systems.\n\n3. Application to Organizational Problem (200-250 words):\n   a) Analyze the given organizational problem, identifying key challenges and current limitations in solving it.\n   b) Explain how your AI system would approach solving this problem using swarm intelligence principles.\n   c) Provide a specific example of a solution your system might generate, including its swarm-inspired rationale and how it addresses the organizational issue.\n   d) Describe how your solution satisfies the given constraint.\n\n4. Implementation and Evaluation (150-200 words):\n   a) Describe how your AI-generated solutions could be implemented in real-world organizational settings.\n   b) Propose metrics for evaluating the effectiveness of these swarm-inspired solutions.\n   c) Discuss potential challenges in adapting insect-inspired strategies to human contexts and how your system addresses these.\n\n5. Ethical Considerations and Limitations (100-150 words):\n   a) Identify potential ethical issues related to using AI and swarm intelligence principles in human organizations.\n   b) Discuss limitations of your system and areas where human expertise is still necessary.\n   c) Propose guidelines for responsible development and implementation of swarm-inspired AI solutions in organizational contexts.\n\n6. Future Directions and Broader Impact (100-150 words):\n   a) Suggest potential improvements or extensions to your AI system.\n   b) Discuss how this approach could impact fields such as management science, organizational psychology, or artificial intelligence.\n   c) Propose a novel research question that your system could help address in the field of collective intelligence or organizational behavior.\n\nEnsure your response demonstrates a deep understanding of swarm intelligence, organizational theory, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and addressing the complexity of both biological and human systems.\n\nYour total response should be between 1000-1300 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of swarm intelligence in the specified insect type.",
            "The AI system design effectively integrates swarm intelligence principles with organizational problem-solving.",
            "The application to the given organizational problem is creative, plausible, and well-reasoned.",
            "The proposed solution adequately addresses the specified constraint.",
            "The implementation and evaluation plan is practical and considers real-world challenges.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "Future directions and broader impact are insightful and demonstrate interdisciplinary thinking."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
