import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environmental_challenges = [
            "Urban heat island effect",
            "Water scarcity in arid regions",
            "Soil erosion in agricultural lands",
            "Air pollution in megacities",
            "Plastic waste in oceans"
        ]
        biological_inspirations = [
            "Termite mounds",
            "Namib desert beetle",
            "Prairie grass root systems",
            "Giant sequoia trees",
            "Manta rays"
        ]
        return {
            "1": {
                "challenge": random.choice(environmental_challenges),
                "inspiration": random.choice(biological_inspirations)
            },
            "2": {
                "challenge": random.choice(environmental_challenges),
                "inspiration": random.choice(biological_inspirations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses principles of biomimicry to address the environmental challenge of {t['challenge']}, drawing inspiration from {t['inspiration']}. Then, analyze its potential applications and ethical implications. Your response should include:

1. Biomimetic AI System Design (300-350 words):
   a) Describe the key features of your AI system and how it addresses the given environmental challenge.
   b) Explain how your system incorporates principles from the specified biological inspiration.
   c) Detail the AI algorithms or approaches used in your system.
   d) Provide a simple diagram or flowchart of your system architecture (describe this textually).

2. Biological-Technological Interface (200-250 words):
   a) Analyze how your AI system bridges the gap between biological processes and technological solutions.
   b) Discuss any novel algorithms or approaches used to translate biological principles into AI functionality.
   c) Explain how your system accounts for the complexity and adaptability of natural systems.

3. Environmental Impact Analysis (200-250 words):
   a) Predict the potential environmental impacts of implementing your AI system.
   b) Discuss both positive and negative consequences, considering short-term and long-term effects.
   c) Propose methods to monitor and mitigate any potential negative impacts.

4. Scalability and Adaptability (200-250 words):
   a) Explain how your AI system could be scaled up for wider implementation.
   b) Discuss how it might be adapted to address other environmental challenges.
   c) Propose a method for continually improving the system based on real-world performance data.

5. Ethical Considerations (200-250 words):
   a) Identify potential ethical issues related to the development and deployment of your biomimetic AI system.
   b) Discuss how your system addresses issues of environmental justice and equitable access to solutions.
   c) Propose guidelines for the responsible development and use of biomimetic AI in environmental management.

6. Future Research Directions (150-200 words):
   a) Suggest two potential extensions or modifications to your biomimetic AI system.
   b) Propose a research question that arises from your design.
   c) Discuss potential implications of your approach for the broader field of AI-driven environmental solutions.

Ensure your response demonstrates a deep understanding of biomimicry, environmental science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility and ecological soundness.

Format your response with clear headings for each section, numbered 1-6 as outlined above. Your total response should be between 1250-1550 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of biomimicry, environmental science, and artificial intelligence, particularly in addressing {t['challenge']} using principles from {t['inspiration']}.",
            "The proposed AI system effectively integrates biomimetic principles with artificial intelligence technologies.",
            "The analysis of environmental impacts is thorough and considers both positive and negative consequences.",
            "The scalability and adaptability discussion is well-reasoned and provides specific examples.",
            "Ethical considerations are thoughtfully addressed, including issues of environmental justice and responsible development.",
            "The future research directions are innovative and demonstrate an understanding of the field's potential.",
            "The response adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
