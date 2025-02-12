import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_systems = [
            {
                "system": "Lotus leaf",
                "key_feature": "Superhydrophobicity",
                "challenge": "Develop a self-cleaning surface for solar panels"
            },
            {
                "system": "Gecko feet",
                "key_feature": "Adhesion through van der Waals forces",
                "challenge": "Create a reusable adhesive for space applications"
            }
        ]
        return {
            "1": random.choice(biological_systems),
            "2": random.choice(biological_systems)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Biomimicry is an approach to innovation that seeks sustainable solutions to human challenges by emulating nature's time-tested patterns and strategies. With this in mind, analyze the {t['system']} and its key feature of {t['key_feature']}, then apply these principles to {t['challenge']}. Your response should include:\n\n" + \
               "1. Biological System Analysis (150-200 words):\n" + \
               "   - Describe the key feature and its function in the biological system\n" + \
               "   - Explain the underlying mechanisms or principles that enable this feature\n" + \
               "   - Discuss any limitations or trade-offs in the biological system\n\n" + \
               "2. Problem Analysis (100-150 words):\n" + \
               "   - Analyze the given challenge and its requirements\n" + \
               "   - Identify similarities between the biological system and the challenge\n" + \
               "   - Discuss any potential obstacles in applying the biological principle\n\n" + \
               "3. Biomimetic Solution (200-250 words):\n" + \
               "   - Propose a detailed solution that applies the biological principle to the challenge\n" + \
               "   - Explain how your solution mimics or adapts the biological feature\n" + \
               "   - Describe the potential advantages of your biomimetic approach\n\n" + \
               "4. Implementation and Scalability (150-200 words):\n" + \
               "   - Outline the key steps or technologies needed to implement your solution\n" + \
               "   - Discuss any modifications needed to scale up from the biological system\n" + \
               "   - Address potential challenges in manufacturing or deploying your solution\n\n" + \
               "5. Environmental and Ethical Considerations (100-150 words):\n" + \
               "   - Discuss the environmental impact of your proposed solution\n" + \
               "   - Address any ethical considerations in mimicking biological systems\n" + \
               "   - Propose ways to ensure sustainable and responsible development\n\n" + \
               "Ensure your response demonstrates a deep understanding of both the biological system and the engineering principles involved. Be creative in your approach while maintaining scientific accuracy and feasibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the biological system and its key feature",
            "The proposed solution effectively applies the biological principle to the given challenge",
            "The analysis shows creativity and innovation in adapting the biological system to the engineering problem",
            "The implementation and scalability discussion is thorough and addresses potential challenges",
            "Environmental and ethical considerations are thoughtfully addressed",
            "The overall response integrates knowledge from biology and engineering in a cohesive manner"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
