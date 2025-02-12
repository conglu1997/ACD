class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "domain": "Sustainable urban planning",
                "concepts": ["Vertical farming", "Smart grid technology", "Biomimicry"]
            },
            "2": {
                "domain": "Space exploration",
                "concepts": ["Swarm robotics", "Quantum communication", "Bioengineering"]
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that implements conceptual blending for creative problem-solving, then apply it to generate novel solutions in the domain of {t['domain']}. Your system should blend the following concepts: {', '.join(t['concepts'])}. Provide your response in the following format:

1. Conceptual Blending Theory (200-250 words):
   a) Explain the key principles of conceptual blending theory.
   b) Discuss how conceptual blending relates to creative problem-solving.
   c) Describe any challenges in implementing conceptual blending in AI systems.

2. AI System Design (300-350 words):
   a) Outline the architecture of your AI system for conceptual blending.
   b) Explain how your system represents and manipulates concepts.
   c) Describe the algorithms or techniques used to generate blended concepts.
   d) Discuss how your system evaluates and refines the blended outputs.
   e) Explain how your system incorporates domain-specific knowledge.

3. Application to {t['domain']} (250-300 words):
   a) Apply your AI system to blend the given concepts: {', '.join(t['concepts'])}.
   b) Describe the process of how your system generates at least two novel solutions.
   c) Explain how these solutions leverage the blended concepts.
   d) Discuss the potential impact and feasibility of your generated solutions.

4. Evaluation and Analysis (200-250 words):
   a) Propose criteria for evaluating the creativity and effectiveness of your system's outputs.
   b) Analyze the strengths and limitations of your approach.
   c) Compare your system's approach to traditional problem-solving methods in AI.

5. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to AI systems that can generate novel ideas and solutions.
   b) Explore the societal implications of deploying such systems in {t['domain']}.
   c) Propose guidelines for responsible development and use of conceptual blending AI systems.

Ensure your response demonstrates a deep understanding of conceptual blending theory, AI system design, and the specific domain. Be innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of conceptual blending theory and its application to AI systems.",
            "The AI system design is innovative, well-explained, and plausibly implements conceptual blending for creative problem-solving.",
            f"The application to {t['domain']} effectively blends the given concepts ({', '.join(t['concepts'])}) to generate novel and potentially impactful solutions.",
            "The evaluation and analysis section provides insightful criteria and a thoughtful comparison to traditional AI problem-solving methods.",
            "The discussion of ethical and societal implications is nuanced and proposes relevant guidelines for responsible development and use.",
            "The response maintains scientific plausibility while demonstrating creativity and interdisciplinary knowledge application.",
            "The writing is clear, well-structured, and adheres to the specified word count and format."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
