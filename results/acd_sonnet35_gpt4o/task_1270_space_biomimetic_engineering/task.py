import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        space_challenges = [
            {
                "challenge": "Radiation Protection",
                "context": "Long-term space travel exposes astronauts to harmful cosmic radiation"
            },
            {
                "challenge": "Microgravity Adaptation",
                "context": "Extended periods in microgravity lead to muscle and bone loss"
            },
            {
                "challenge": "Sustainable Life Support",
                "context": "Creating closed-loop systems for air, water, and food in space habitats"
            },
            {
                "challenge": "Extreme Temperature Regulation",
                "context": "Managing spacecraft temperature in extreme space environments"
            }
        ]
        return {
            "1": random.choice(space_challenges),
            "2": random.choice(space_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic solution for the space exploration challenge of {t['challenge']} in the context of {t['context']}. Then, analyze its feasibility and evaluate its ethical implications. Complete the following tasks:

1. Biomimetic Solution Design (250-300 words):
   a) Describe your proposed biomimetic solution, clearly stating which biological system or organism it's inspired by.
   b) Explain how your solution addresses the specific space challenge.
   c) Outline the key components or mechanisms of your design.
   d) Discuss how your solution improves upon or differs from current non-biomimetic approaches.

2. Scientific Principles (200-250 words):
   a) Explain the biological principles or mechanisms that your solution mimics.
   b) Describe how these principles are adapted to function in the space environment.
   c) Discuss any modifications needed to translate the biological concept to a space-worthy technology.

3. Feasibility Analysis (200-250 words):
   a) Analyze the technical feasibility of implementing your solution with current or near-future technology.
   b) Identify potential challenges in development, testing, or deployment of your solution.
   c) Propose methods to overcome these challenges.
   d) Estimate the timeline for developing a prototype and full implementation.

4. Ethical Implications (200-250 words):
   a) Discuss three potential ethical concerns raised by your biomimetic solution.
   b) Analyze these concerns using an ethical framework of your choice.
   c) Propose guidelines for addressing these ethical issues in the development and use of your technology.

5. Interdisciplinary Impact (150-200 words):
   a) Explain how your solution might advance knowledge in biology, engineering, and space science.
   b) Discuss potential applications of your technology beyond space exploration.
   c) Describe how insights from this project could inform future biomimetic designs for space challenges.

Ensure your response demonstrates a deep understanding of biology, engineering principles, and space science. Be creative while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response using the following structure:

1. Biomimetic Solution Design
   [Your response here]

2. Scientific Principles
   [Your response here]

3. Feasibility Analysis
   [Your response here]

4. Ethical Implications
   [Your response here]

5. Interdisciplinary Impact
   [Your response here]

Your entire response should not exceed 1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The biomimetic solution is clearly described and relevant to the given space challenge.",
            "The biological principles are accurately explained and appropriately adapted for the space environment.",
            "The feasibility analysis is comprehensive and realistic.",
            "The ethical implications are thoroughly discussed using a relevant ethical framework.",
            "The interdisciplinary impact is well-explained and plausible.",
            "The response demonstrates creativity and scientific plausibility.",
            "The response follows the specified format and does not exceed 1300 words."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
