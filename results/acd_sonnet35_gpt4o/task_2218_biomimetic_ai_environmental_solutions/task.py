import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            {
                "challenge": "Urban heat island effect",
                "description": "Increased temperature in urban areas due to human activities and infrastructure",
                "impact": "Higher energy consumption, health risks, and reduced air quality"
            },
            {
                "challenge": "Microplastic pollution in oceans",
                "description": "Accumulation of tiny plastic particles in marine ecosystems",
                "impact": "Harm to marine life, potential human health risks through food chain"
            }
        ]
        return {
            "1": random.choice(environmental_challenges),
            "2": random.choice(environmental_challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses principles of biomimicry to develop innovative solutions for the environmental challenge of {t['challenge']} ({t['description']}). The impact of this challenge includes: {t['impact']}

Your response should include the following sections:

1. Biomimicry Analysis (250-300 words):
   a) Identify and describe 2-3 natural systems or organisms that have evolved strategies relevant to addressing the given environmental challenge.
   b) Explain how these biological strategies could be applied to the challenge.
   c) Discuss any limitations or adaptations needed when translating these strategies to human-scale solutions.

2. AI System Design (300-350 words):
   a) Describe the architecture of your AI system, including its main components and how they interact.
   b) Explain how your system integrates biomimicry principles with machine learning or other AI techniques.
   c) Detail the data sources and types of input your system would use.
   d) Discuss any novel algorithms or approaches you've incorporated to handle the unique aspects of biomimetic design.

3. Solution Generation and Evaluation (250-300 words):
   a) Explain the process by which your AI system generates potential solutions.
   b) Describe how the system evaluates and refines these solutions.
   c) Discuss how your system balances innovation with feasibility and effectiveness.
   d) Provide an example of a potential solution your system might generate, including its biomimetic inspiration and how it addresses the environmental challenge.

4. Implementation and Scaling (200-250 words):
   a) Describe how your AI-generated solutions could be implemented in real-world settings.
   b) Discuss potential challenges in scaling these solutions to address the environmental issue on a larger scale.
   c) Explain how your system could adapt its solutions for different geographic or cultural contexts.

5. Environmental Impact Analysis (200-250 words):
   a) Analyze the potential positive and negative environmental impacts of implementing your AI-generated solutions.
   b) Discuss any potential unintended consequences and how they might be mitigated.
   c) Compare the expected effectiveness of your biomimetic approach to traditional solutions for the given environmental challenge.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues related to using AI and biomimicry for environmental solutions.
   b) Discuss limitations of your system and areas where human expertise is still necessary.
   c) Propose guidelines for responsible development and implementation of biomimetic AI solutions.

7. Future Directions and Interdisciplinary Impact (150-200 words):
   a) Suggest potential improvements or extensions to your AI system.
   b) Propose a novel research question that your system could help address in the field of environmental science or biomimicry.
   c) Discuss how your approach could impact other fields such as urban planning, materials science, or sustainable technology development.

Ensure your response demonstrates a deep understanding of environmental science, biomimicry, and artificial intelligence. Use technical terminology appropriately and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility and addressing the complexity of the environmental challenge.

Your total response should be between 1500-1850 words, with each section adhering to the specified word ranges."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear and accurate understanding of the environmental challenge ({t['challenge']}) and its impacts.",
            "The biomimicry analysis identifies relevant natural systems or organisms and explains their strategies in relation to the challenge.",
            "The AI system design integrates biomimicry principles with AI techniques in a novel and plausible manner.",
            "The solution generation and evaluation process is well-explained and demonstrates how the system balances innovation with feasibility.",
            "The implementation and scaling section addresses real-world challenges and adaptability of the solutions.",
            "The environmental impact analysis considers both positive and negative consequences, including potential unintended effects.",
            "Ethical considerations and limitations are thoughtfully discussed, with appropriate guidelines proposed.",
            "Future directions and interdisciplinary impacts are insightful and demonstrate the broader potential of the approach.",
            "The response uses appropriate terminology from environmental science, biomimicry, and artificial intelligence throughout.",
            "The proposed solutions and analyses are creative while maintaining scientific plausibility.",
            "The response adheres to the specified word counts for each section and the overall limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
