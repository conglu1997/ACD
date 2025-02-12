import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        economic_principles = [
            {
                "game_theory": "Nash equilibrium",
                "behavioral_economics": "Prospect theory",
                "social_psychology": "Social identity theory"
            },
            {
                "game_theory": "Prisoner's dilemma",
                "behavioral_economics": "Nudge theory",
                "social_psychology": "Conformity and social influence"
            }
        ]
        return {
            "1": random.choice(economic_principles),
            "2": random.choice(economic_principles)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel economic system that incorporates principles from game theory, behavioral economics, and social psychology. Your system should be based on the following concepts:

1. Game Theory: {t['game_theory']}
   (A branch of mathematics dealing with strategic decision-making)
   Example application: Using game theory to design market mechanisms or policy interventions.
2. Behavioral Economics: {t['behavioral_economics']}
   (The study of psychological, social, and emotional factors on economic decisions)
   Example application: Designing choice architectures that account for cognitive biases.
3. Social Psychology: {t['social_psychology']}
   (The scientific study of how people's thoughts, feelings, and behaviors are influenced by others)
   Example application: Leveraging group dynamics to promote cooperative economic behavior.

Your task is to integrate these three concepts throughout your economic system design. Each concept should play a significant role in shaping the system's mechanisms and outcomes. Provide at least one concrete example or scenario for each section of your response.

Your task has the following parts:

1. System Design (250-300 words):
   a) Describe the key components and mechanisms of your economic system.
   b) Explain how it incorporates each of the three given concepts.
   c) Discuss how your system differs from traditional economic models.
   d) Provide a concrete example of how your system would operate in a specific economic scenario.

2. Incentive Structure (200-250 words):
   a) Detail the incentives and motivations built into your system.
   b) Explain how these incentives align with or challenge human behavioral tendencies.
   c) Discuss potential unintended consequences and how your system might address them.
   d) Illustrate with a specific example of how an incentive in your system would work.

3. Social Dynamics (200-250 words):
   a) Analyze how your system might influence social structures and interactions.
   b) Discuss potential changes in group dynamics or social hierarchies.
   c) Explain how your system accounts for diverse social and cultural contexts.
   d) Provide an example of how your system might affect a particular social group or community.

4. Implementation and Transition (200-250 words):
   a) Propose a method for implementing your system in a real-world context.
   b) Discuss challenges in transitioning from current economic systems.
   c) Suggest strategies to overcome resistance or skepticism.
   d) Describe a hypothetical pilot program to test your system on a small scale.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues arising from your economic system.
   b) Discuss how these issues might be addressed or mitigated.
   c) Reflect on the overall ethical implications of implementing such a system.
   d) Provide an example of an ethical dilemma that could arise and how it might be resolved.

6. Simulation and Testing (200-250 words):
   a) Describe a hypothetical experiment or simulation to test your economic system.
   b) Explain what metrics or outcomes would be measured.
   c) Discuss how the results could be interpreted and used for system refinement.
   d) Propose a specific scenario to be tested in your simulation.

7. Limitations and Criticisms (100-150 words):
   a) Discuss potential limitations or weaknesses of your proposed economic system.
   b) Address possible criticisms from different perspectives (e.g., economic, social, political).
   c) Suggest areas for future research or improvement in your system.

Ensure your response demonstrates a deep understanding of game theory, behavioral economics, and social psychology. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining logical consistency and plausibility.

Format your response using clear headings for each section, exactly as numbered above. Adhere strictly to the word count requirements for each section. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The economic system effectively incorporates and integrates {t['game_theory']}, {t['behavioral_economics']}, and {t['social_psychology']} throughout its design, with concrete examples provided for each concept",
            "The response demonstrates a deep understanding of game theory, behavioral economics, and social psychology, using relevant concepts and terminology accurately",
            "The economic system design is creative, logically consistent, and plausible, clearly differentiating itself from traditional economic models",
            "The incentive structure is well-developed, considers both intended and unintended consequences, and includes a specific example of its application",
            "The analysis of social dynamics is thorough, considers diverse social and cultural contexts, and provides a concrete example of its impact",
            "The implementation and transition plan is realistic, addresses potential challenges, and includes a hypothetical pilot program",
            "Ethical considerations are comprehensively explored with proposed mitigation strategies and an example of an ethical dilemma",
            "The proposed simulation and testing approach is well-reasoned, relevant to the system's evaluation, and includes a specific scenario to be tested",
            "Limitations and potential criticisms of the system are thoughtfully addressed, demonstrating critical thinking and awareness of diverse perspectives",
            "The response addresses all required sections with appropriate depth, provides concrete examples throughout, and adheres to the specified word count for each section",
            "The overall response demonstrates high-level interdisciplinary thinking, problem-solving skills, and innovative application of the given concepts"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
