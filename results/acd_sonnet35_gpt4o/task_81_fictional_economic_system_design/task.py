import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                "society": "Post-scarcity space colony",
                "constraints": [
                    "Unlimited energy from fusion reactors",
                    "Limited physical space",
                    "Dependency on Earth for rare materials",
                    "Population of 10,000 highly educated individuals"
                ],
                "challenge": "Design an economic system that promotes innovation and personal growth"
            },
            {
                "society": "Underwater civilization",
                "constraints": [
                    "Limited access to surface resources",
                    "Abundant marine resources",
                    "High energy cost for surface trips",
                    "Population of 50,000 with varying skill levels"
                ],
                "challenge": "Create an economic system that ensures sustainable resource management"
            }
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design and analyze a fictional economic system for a {t['society']} with the following constraints:\n\n" + \
               "\n".join(f"- {constraint}" for constraint in t['constraints']) + \
               f"\n\nYour task is to {t['challenge']}.\n\n" + \
               "Provide your response in the following format:\n\n" + \
               "1. Economic System Overview (3-4 sentences)\n" + \
               "2. Key Economic Mechanisms (list 3-4 points)\n" + \
               "3. Resource Allocation Method (2-3 sentences)\n" + \
               "4. Incentive Structure (2-3 sentences)\n" + \
               "5. Potential Challenges and Solutions (list 2-3 points)\n" + \
               "6. Comparative Analysis (2-3 sentences comparing your system to a real-world economic system)\n\n" + \
               "Ensure your economic system is creative, addresses the given constraints, and is theoretically feasible. " + \
               "Your response should demonstrate a strong understanding of economic principles and system dynamics."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The proposed economic system is creative and unique, while still being theoretically feasible.",
            "The system effectively addresses all given constraints and the specific challenge.",
            "The response demonstrates a strong understanding of economic principles and system dynamics.",
            "The key economic mechanisms and resource allocation methods are well-explained and logically consistent.",
            "The incentive structure is appropriate for the given society and promotes the desired outcomes.",
            "Potential challenges are identified, and proposed solutions are reasonable and well-thought-out.",
            "The comparative analysis shows insight into both the fictional system and real-world economic systems."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
