import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "domain": "Transportation",
                "challenge": "Design an energy-efficient high-speed train system",
                "inspiration": "Kingfisher bird's beak shape for reducing air resistance"
            },
            {
                "domain": "Architecture",
                "challenge": "Create a passive cooling system for skyscrapers",
                "inspiration": "Termite mounds' natural ventilation systems"
            },
            {
                "domain": "Materials Science",
                "challenge": "Develop a self-cleaning surface coating",
                "inspiration": "Lotus leaf's water-repellent and self-cleaning properties"
            },
            {
                "domain": "Robotics",
                "challenge": "Design a soft robotic gripper for delicate object manipulation",
                "inspiration": "Octopus tentacles' flexibility and adaptability"
            }
        ]
        return {
            "1": random.choice(challenges),
            "2": random.choice(challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic engineering solution for the following challenge in the domain of {t['domain']}:

{t['challenge']}

Your solution should be inspired by the following biological phenomenon:
{t['inspiration']}

Provide your response in the following format:

1. Biological Principle Analysis (200-250 words):
   a) Describe the biological phenomenon in detail.
   b) Explain the key principles or mechanisms that make this biological feature effective.
   c) Discuss how these principles could be relevant to the engineering challenge.

2. Biomimetic Solution Design (250-300 words):
   a) Present your innovative engineering solution inspired by the biological principle.
   b) Explain how your design incorporates the key aspects of the biological phenomenon.
   c) Describe the main components or features of your solution.
   d) Discuss how your solution addresses the specific engineering challenge.

3. Technical Feasibility (200-250 words):
   a) Analyze the technical feasibility of implementing your biomimetic solution.
   b) Discuss any potential materials, technologies, or processes required.
   c) Identify any technical challenges or limitations and propose ways to overcome them.

4. Performance Analysis (200-250 words):
   a) Predict the potential performance improvements offered by your biomimetic solution.
   b) Compare your solution to existing conventional approaches to the problem.
   c) Discuss any trade-offs or compromises in your design.

5. Broader Implications (150-200 words):
   a) Discuss the potential impact of your solution on the field of {t['domain']}.
   b) Explore any additional applications or adaptations of your biomimetic design.
   c) Address any environmental or sustainability aspects of your solution.

Ensure your response demonstrates a deep understanding of both the biological principles and the engineering domain. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific and engineering plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of the biological principle and its relevance to the engineering challenge.",
            "The biomimetic solution is innovative, well-explained, and directly addresses the given engineering challenge.",
            "The technical feasibility analysis is thorough and considers relevant materials, technologies, and potential limitations.",
            "The performance analysis provides a meaningful comparison to conventional approaches and discusses trade-offs.",
            "The discussion of broader implications is insightful and considers the solution's potential impact and adaptability.",
            "The response maintains scientific and engineering plausibility while showcasing creativity in problem-solving.",
            "The submission is well-structured with clear sections as requested in the instructions."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
