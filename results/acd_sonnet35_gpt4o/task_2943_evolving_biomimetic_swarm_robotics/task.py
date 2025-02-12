import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "environment": "deep sea",
                "biological_inspiration": "bioluminescent creatures",
                "challenge": "extreme pressure and darkness"
            },
            {
                "environment": "volcanic regions",
                "biological_inspiration": "extremophile bacteria",
                "challenge": "high temperatures and acidity"
            }
        ]
        return {
            "1": random.choice(environments),
            "2": random.choice(environments)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI-driven evolutionary system for developing biomimetic swarm robots that can adapt to the {t['environment']} environment, drawing inspiration from {t['biological_inspiration']} and addressing the challenge of {t['challenge']}. Then, analyze the ethical implications of deploying such a system. Your response should include the following sections:

1. Evolutionary System Architecture (300-350 words):
   a) Describe the key components of your AI-driven evolutionary system.
   b) Explain how your system incorporates principles from evolutionary algorithms and swarm intelligence.
   c) Detail how your system would evolve robot designs based on the specified biological inspiration.
   d) Include a high-level diagram or pseudocode snippet illustrating a key part of your evolutionary algorithm.

2. Biomimetic Robot Design (250-300 words):
   a) Describe the basic structure and features of your swarm robots.
   b) Explain how the robot design incorporates biomimetic elements inspired by {t['biological_inspiration']}.
   c) Discuss how the robots are adapted to overcome the challenge of {t['challenge']}.
   d) Propose an innovative feature that enhances the robots' ability to operate in the {t['environment']}.

3. Swarm Behavior and Adaptation (250-300 words):
   a) Explain the swarm behaviors your robots would exhibit.
   b) Describe how individual robots communicate and coordinate within the swarm.
   c) Discuss how the swarm adapts to changing conditions in the {t['environment']}.
   d) Propose a method for evaluating the fitness of evolved swarm behaviors.

4. Environmental Interaction and Impact (200-250 words):
   a) Analyze how your robotic swarm would interact with the {t['environment']} ecosystem.
   b) Discuss potential positive and negative impacts on the environment.
   c) Propose safeguards to minimize ecological disruption.

5. Ethical Implications (250-300 words):
   a) Discuss the ethical considerations of deploying an evolving robotic swarm in a natural environment.
   b) Analyze potential dual-use concerns and unintended consequences of this technology.
   c) Propose guidelines for responsible development and deployment of evolving biomimetic swarms.

6. Future Applications and Research Directions (150-200 words):
   a) Suggest two potential applications of your evolving biomimetic swarm technology beyond the {t['environment']}.
   b) Propose areas for future research to enhance the capabilities of your system.
   c) Discuss how this technology might impact the field of robotics and AI in the long term.

Ensure your response demonstrates a deep understanding of evolutionary algorithms, swarm robotics, biomimetics, and environmental science. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of evolutionary algorithms, swarm robotics, biomimetics, and environmental science.",
            f"The proposed system effectively incorporates inspiration from {t['biological_inspiration']} and addresses the challenge of {t['challenge']} in the {t['environment']}.",
            "The biomimetic robot design and swarm behavior are well-reasoned and scientifically plausible.",
            "The ethical analysis is thorough and considers multiple perspectives.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge application."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
