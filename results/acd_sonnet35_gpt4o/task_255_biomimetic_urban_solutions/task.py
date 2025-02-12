import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ecosystems = ['coral reef', 'rainforest', 'desert', 'tundra', 'savanna']
        urban_challenges = ['water management', 'energy efficiency', 'waste reduction', 'air quality improvement', 'urban heat island effect']
        tasks = [
            {
                'ecosystem': random.choice(ecosystems),
                'urban_challenge': random.choice(urban_challenges)
            },
            {
                'ecosystem': random.choice(ecosystems),
                'urban_challenge': random.choice(urban_challenges)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a biomimetic solution for an urban challenge based on the following parameters:

Ecosystem: {t['ecosystem']}
Urban Challenge: {t['urban_challenge']}

Your task:

1. Ecosystem Analysis (150-200 words):
   - Briefly describe the key characteristics and adaptations of the given ecosystem.
   - Identify at least three unique features or processes in this ecosystem that could inspire solutions to urban challenges.

2. Bio-Inspired Solution (250-300 words):
   - Propose a detailed solution to the given urban challenge, drawing clear inspiration from the assigned ecosystem.
   - Explain how specific biological adaptations or processes from the ecosystem inform your design.
   - Describe the key components and functioning of your solution.

3. Feasibility Assessment (150-200 words):
   - Evaluate the technical feasibility of implementing your solution in a real urban environment.
   - Discuss potential challenges in scaling up the solution and propose ways to overcome them.
   - Consider the economic aspects of your solution, including potential costs and benefits.

4. Environmental Impact (150-200 words):
   - Analyze the potential positive and negative environmental impacts of your solution.
   - Explain how your solution promotes sustainability and aligns with ecological principles.
   - Discuss any potential unintended consequences and how they might be mitigated.

5. Interdisciplinary Connections (100-150 words):
   - Identify at least two other scientific or engineering disciplines that would be crucial in developing and implementing your solution.
   - Briefly explain how these disciplines would contribute to the success of your biomimetic design.

6. Future Adaptations (100-150 words):
   - Propose how your biomimetic solution could be adapted or expanded to address a different urban challenge.
   - Explain how the core principles of your design could be applied in a different context.

Ensure your response demonstrates a deep understanding of both the biological ecosystem and the urban challenge. Use scientific terminology appropriately and provide clear explanations of complex concepts. Be creative in your design while maintaining scientific plausibility and addressing real-world constraints.

Format your response with clear headings for each section. Your total response should be between 900-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given ecosystem and its unique features.",
            "The proposed solution clearly draws inspiration from the ecosystem and addresses the urban challenge effectively.",
            "The feasibility assessment is thorough and considers real-world implementation challenges.",
            "The environmental impact analysis is comprehensive and considers both positive and negative effects.",
            "The interdisciplinary connections are relevant and well-explained.",
            "The future adaptations proposed are creative and demonstrate the versatility of the biomimetic approach.",
            "The overall response shows a high level of creativity, scientific understanding, and analytical reasoning."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
