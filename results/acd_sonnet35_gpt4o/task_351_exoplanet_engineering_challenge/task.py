import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanets = [
            {
                "name": "Kepler-16b",
                "characteristics": "Circumbinary planet orbiting two stars, similar in size to Saturn, likely gaseous",
                "challenge": "Stabilize the planet's orbit and create a habitable zone"
            },
            {
                "name": "Gliese 581c",
                "characteristics": "Super-Earth in the habitable zone of a red dwarf star, tidally locked, potential for extreme temperature differences",
                "challenge": "Establish a habitable environment on a tidally locked planet"
            },
            {
                "name": "HD 189733b",
                "characteristics": "Hot Jupiter with extreme winds and possible glass rain, orbits very close to its star",
                "challenge": "Cool the planet and establish a stable atmosphere"
            }
        ]
        return {
            "1": random.choice(exoplanets),
            "2": random.choice(exoplanets)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a terraforming solution for the exoplanet {t['name']}. Your task is to propose a scientifically plausible method to make this planet habitable for human colonization, considering its unique characteristics and challenges. Address the following points in your response:\n\n1. Exoplanet Analysis (100-150 words):\n   a) Summarize the key characteristics of {t['name']}: {t['characteristics']}\n   b) Explain the main challenge: {t['challenge']}\n   c) Identify two additional potential obstacles for terraforming this planet\n\n2. Terraforming Solution (200-250 words):\n   a) Propose a detailed terraforming method, explaining the key technologies or processes involved\n   b) Describe how your solution addresses the main challenge and the additional obstacles you identified\n   c) Estimate the timeframe required for your terraforming process and justify your estimate\n\n3. Resource Requirements (100-150 words):\n   a) List the essential resources needed for your terraforming project\n   b) Explain how these resources would be obtained or transported to the exoplanet\n   c) Discuss any potential resource constraints or sustainability issues\n\n4. Ecological Considerations (100-150 words):\n   a) Describe the target ecosystem you aim to establish on the terraformed planet\n   b) Explain how you would introduce and maintain biodiversity\n   c) Discuss any potential unforeseen consequences of your terraforming process\n\n5. Societal Implications (100-150 words):\n   a) Discuss the potential impact of this terraforming project on human society\n   b) Address any ethical considerations related to exoplanet colonization\n   c) Propose a governance structure for the newly terraformed planet\n\n6. Future Research (50-100 words):\n   Suggest two areas of scientific or technological advancement that could significantly improve your terraforming solution\n\nEnsure your response is grounded in scientific principles while demonstrating creativity in applying current knowledge to futuristic scenarios. Provide specific examples and explanations for each point, and make sure to address all parts of the task. Your total response should not exceed 800 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response comprehensively addresses the main challenge of terraforming {t['name']}: {t['challenge']}",
            "The terraforming solution is scientifically plausible, well-explained, and includes specific technologies or processes",
            "The response considers detailed resource requirements, including acquisition and transportation methods",
            "The ecological considerations are thorough, addressing biodiversity and potential consequences",
            "The societal implications are well-thought-out, including ethical considerations and a proposed governance structure",
            "The submission demonstrates interdisciplinary knowledge application across physics, biology, engineering, and social sciences",
            "The response is creative while maintaining scientific integrity and plausibility",
            "The submission follows the specified format, addresses all required points, and adheres to word count guidelines",
            "The future research suggestions are relevant and have the potential to significantly improve the proposed solution"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
