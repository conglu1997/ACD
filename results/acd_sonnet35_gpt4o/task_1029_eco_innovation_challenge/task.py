import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            {
                "challenge": "Urban heat island effect",
                "context": "Large metropolitan area with limited green space",
                "constraints": ["Limited budget", "High population density", "Existing infrastructure"]
            },
            {
                "challenge": "Microplastic pollution in oceans",
                "context": "Coastal region with heavy fishing and tourism industries",
                "constraints": ["International waters", "Economic impact on local industries", "Technological limitations"]
            },
            {
                "challenge": "Soil degradation in agricultural areas",
                "context": "Rural farming community with declining crop yields",
                "constraints": ["Traditional farming practices", "Limited water resources", "Economic pressure"]
            },
            {
                "challenge": "Air pollution in industrial zones",
                "context": "Rapidly developing industrial city with poor air quality",
                "constraints": ["Economic growth priorities", "Outdated infrastructure", "Limited regulatory enforcement"]
            },
            {
                "challenge": "Deforestation and biodiversity loss",
                "context": "Tropical region with expanding agriculture and logging industries",
                "constraints": ["Economic dependence on resource extraction", "Lack of alternative livelihoods", "Limited conservation funding"]
            },
            {
                "challenge": "Freshwater scarcity",
                "context": "Arid region with growing urban population and agriculture",
                "constraints": ["Climate change impacts", "Competing water demands", "Limited groundwater resources"]
            }
        ]
        return {
            "1": random.choice(environmental_challenges),
            "2": random.choice(environmental_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        instructions = f"Design an innovative solution to address the environmental challenge of {t['challenge']} in the context of {t['context']}. Your solution should be creative, scientifically grounded, and consider the following constraints: {', '.join(t['constraints'])}."

        instructions += "\n\nYour response should include:"
        instructions += "\n1. Solution Overview (100-150 words):"
        instructions += "\n   - Briefly describe your proposed solution and its key components."
        instructions += "\n   - Explain how it addresses the specific environmental challenge."

        instructions += "\n\n2. Scientific Basis (150-200 words):"
        instructions += "\n   - Discuss the scientific principles underlying your solution."
        instructions += "\n   - Explain how your solution integrates knowledge from multiple disciplines (e.g., biology, chemistry, engineering)."

        instructions += "\n\n3. Implementation Strategy (150-200 words):"
        instructions += "\n   - Outline a step-by-step plan for implementing your solution."
        instructions += "\n   - Address how your solution navigates the given constraints."

        instructions += "\n\n4. Impact Analysis (100-150 words):"
        instructions += "\n   - Predict the potential environmental impact of your solution."
        instructions += "\n   - Discuss any possible unintended consequences and how to mitigate them."

        instructions += "\n\n5. Interdisciplinary Connections (100-150 words):"
        instructions += "\n   - Explain how your solution draws from or impacts other fields (e.g., economics, urban planning, public health)."
        instructions += "\n   - Discuss potential collaborations needed to fully realize your solution."

        instructions += "\n\nEnsure your response demonstrates a deep understanding of environmental science, creative problem-solving, and the ability to integrate knowledge from multiple disciplines. Be innovative in your approach while considering practical feasibility and addressing the given constraints."

        instructions += "\n\nYour total response should be between 600-850 words, adhering to the specified word counts for each section."

        return instructions

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The solution is innovative and creative in addressing the given environmental challenge.",
            "The response demonstrates a deep understanding of relevant scientific principles and interdisciplinary knowledge.",
            "The proposed implementation strategy is well-thought-out and addresses the given constraints.",
            "The impact analysis shows consideration of both positive environmental effects and potential unintended consequences.",
            "The solution effectively integrates knowledge from multiple disciplines and suggests relevant collaborations.",
            "The overall response is well-structured, clear, and adheres to the specified word counts for each section and the total word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
