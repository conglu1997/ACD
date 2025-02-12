import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "domain": "social networks",
                "data_type": "user interactions",
                "objective": "identify influential users",
                "tda_concept": "persistent homology"
            },
            {
                "domain": "medical imaging",
                "data_type": "brain scans",
                "objective": "detect early signs of neurological disorders",
                "tda_concept": "mapper algorithm"
            },
            {
                "domain": "financial markets",
                "data_type": "stock price time series",
                "objective": "predict market crashes",
                "tda_concept": "zigzag persistence"
            },
            {
                "domain": "climate science",
                "data_type": "temperature and precipitation patterns",
                "objective": "identify extreme weather events",
                "tda_concept": "persistent homology"
            }
        ]
        return {
            "1": random.choice(problems),
            "2": random.choice(problems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"You are a data scientist specializing in topological data analysis (TDA). Your task is to propose a solution to the following problem using TDA techniques:\n\nDomain: {t['domain']}\nData type: {t['data_type']}\nObjective: {t['objective']}\nTDA concept to focus on: {t['tda_concept']}\n\nYour response should include:\n\n1. A brief explanation of how the specified TDA concept can be applied to this problem (2-3 sentences)\n2. A step-by-step approach to solving the problem using the specified TDA technique (3-4 steps)\n3. One potential challenge in applying this TDA concept to the problem and how you would address it (1-2 sentences)\n4. A creative idea for visualizing the results of your TDA approach (1-2 sentences)\n5. A hypothetical insight that could be gained from applying this TDA technique to the given problem (1-2 sentences)\n\nEnsure your solution is mathematically sound and demonstrates a clear understanding of the specified topological data analysis concept."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the {t['tda_concept']} concept in topological data analysis.",
            f"The proposed solution is mathematically sound and applicable to the {t['domain']} problem.",
            "The step-by-step approach is logical and correctly uses the specified TDA technique.",
            "The potential challenge and its solution are relevant and well-reasoned.",
            "The visualization idea is creative and appropriate for the TDA results.",
            "The hypothetical insight is plausible and demonstrates understanding of both the TDA concept and the problem domain."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
