import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "problem": "Design a water filtration system inspired by the way living organisms filter water.",
                "organism_hint": "Consider how mussels or baleen whales filter water."
            },
            {
                "problem": "Create an energy-efficient building cooling system inspired by natural temperature regulation in animals or plants.",
                "organism_hint": "Think about how termite mounds or elephant ears regulate temperature."
            },
            {
                "problem": "Develop a noise-reduction technology for urban environments inspired by natural sound-dampening mechanisms.",
                "organism_hint": "Consider how owl feathers or moth wings reduce noise."
            },
            {
                "problem": "Design an adhesive that works in wet conditions, inspired by marine organisms.",
                "organism_hint": "Think about how mussels or barnacles adhere to surfaces underwater."
            }
        ]
        return {
            "1": random.choice(challenges),
            "2": random.choice(challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Your task is to design a biomimetic engineering solution to the following problem:\n\n{t['problem']}\n\nHint: {t['organism_hint']}\n\nProvide your response in the following format:\n\n1. Biological Inspiration (2-3 sentences): Describe the biological system or organism that inspires your solution.\n\n2. Key Principles (2-3 bullet points): List the main principles or mechanisms from the biological system that you will apply to your design.\n\n3. Engineering Solution (4-5 sentences): Detail your proposed solution, explaining how it incorporates the biological principles and addresses the given problem.\n\n4. Advantages (2-3 bullet points): Describe the potential advantages of your biomimetic solution compared to conventional approaches.\n\n5. Challenges (1-2 sentences): Briefly discuss any potential challenges or limitations of implementing your solution.\n\nEnsure your response demonstrates a clear understanding of both the biological system and the engineering problem, and shows creativity in applying natural principles to technological solutions."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response should clearly describe a relevant biological system or organism that inspired the solution.",
            "The key principles extracted from the biological system should be logically connected to the engineering problem.",
            "The proposed engineering solution should demonstrate a creative application of the biological principles to address the given problem.",
            "The advantages of the biomimetic solution should be clearly articulated and relevant to the problem.",
            "The response should demonstrate an understanding of potential challenges or limitations in implementing the solution.",
            "The overall response should show interdisciplinary thinking, combining biology and engineering concepts effectively."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
