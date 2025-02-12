import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_architectures = [
            {
                "name": "ACT-R (Adaptive Control of Thought-Rational)",
                "key_feature": "modular cognitive architecture with a central production system"
            },
            {
                "name": "SOAR (State, Operator, and Result)",
                "key_feature": "problem-solving and learning architecture based on production rules"
            },
            {
                "name": "Global Workspace Theory",
                "key_feature": "conscious cognition as a global workspace for information integration"
            }
        ]
        abstract_domains = [
            "Time",
            "Emotions",
            "Knowledge",
            "Life",
            "Power"
        ]
        tasks = {}
        for i in range(2):
            architecture = random.choice(cognitive_architectures)
            domain = random.choice(abstract_domains)
            tasks[str(i+1)] = {
                "architecture": architecture,
                "domain": domain
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a metaphor generation system based on the {t['architecture']['name']} cognitive architecture, focusing on the abstract domain of {t['domain']}. Then, analyze and evaluate the metaphors produced by this system. Follow these steps:

1. System Design (300-350 words):
   a) Explain how you would implement a metaphor generation system using the key features of {t['architecture']['name']}: {t['architecture']['key_feature']}.
   b) Describe the specific components or modules of your system and how they interact to generate metaphors.
   c) Explain how your system represents and processes the abstract domain of {t['domain']}.
   d) Discuss any specific techniques or algorithms you would use for metaphor creation within this architecture.

2. Metaphor Generation (200-250 words):
   a) Provide three example metaphors that your system might generate for the concept of {t['domain']}.
   b) For each metaphor, explain the cognitive process that led to its creation within your architectural framework.
   c) Discuss how these metaphors reflect the strengths and limitations of the {t['architecture']['name']} architecture.

3. Evaluation and Analysis (250-300 words):
   a) Propose a method to evaluate the quality and creativity of the generated metaphors.
   b) Analyze the strengths and weaknesses of your system in terms of metaphor comprehension and generation.
   c) Compare your system's approach to human cognitive processes in metaphor creation.
   d) Discuss potential biases or limitations in the metaphors produced by your system.

4. Cognitive Architecture Comparison (200-250 words):
   a) Briefly describe how two other cognitive architectures might approach this task differently.
   b) Analyze the potential advantages and disadvantages of your chosen architecture compared to these alternatives for metaphor generation.

5. Implications and Future Directions (200-250 words):
   a) Discuss the implications of your system for our understanding of human cognition and creativity.
   b) Explore potential applications of your metaphor generation system in fields such as creative writing, education, or AI-human interaction.
   c) Propose two specific research questions or experiments to further develop or test your system.

Ensure your response demonstrates a deep understanding of the chosen cognitive architecture, metaphor theory, and computational linguistics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must accurately describe and apply the {t['architecture']['name']} cognitive architecture",
            f"The metaphor generation system must focus on the abstract domain of {t['domain']}",
            "The response should include three example metaphors with explanations",
            "The analysis should demonstrate a deep understanding of cognitive architectures and metaphor theory",
            "The response should be creative yet scientifically plausible",
            "The response should follow the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
