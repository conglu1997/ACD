import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_domains = ['SPACE', 'TEMPERATURE', 'BALANCE', 'MACHINE', 'CONTAINER']
        target_domains = ['TIME', 'EMOTION', 'MORALITY', 'MIND', 'LIFE']
        developmental_stages = ['Early Childhood', 'Middle Childhood', 'Adolescence', 'Adulthood']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'source_domain': random.choice(source_domains),
                'target_domain': random.choice(target_domains),
                'developmental_stage': random.choice(developmental_stages)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a computational model that simulates the acquisition and evolution of conceptual metaphors in artificial agents, focusing on the metaphor {t['source_domain']} IS {t['target_domain']} during the {t['developmental_stage']} stage. Your response should include:

1. Theoretical Foundation (200-250 words):
   a) Explain the cognitive linguistics theory of conceptual metaphors.
   b) Describe how conceptual metaphors typically develop during the {t['developmental_stage']} stage.
   c) Discuss the relevance of the {t['source_domain']} IS {t['target_domain']} metaphor in human cognition.

2. Model Architecture (250-300 words):
   a) Describe the key components of your computational model.
   b) Explain how your model represents and processes conceptual metaphors.
   c) Detail how your model simulates the acquisition and evolution of the {t['source_domain']} IS {t['target_domain']} metaphor.
   d) Include a simple diagram or flowchart of your model's architecture using ASCII art or a structured text description.

3. Learning Mechanism (200-250 words):
   a) Explain the learning algorithm(s) used in your model.
   b) Describe how your model learns from environmental inputs and experiences.
   c) Discuss how your model handles the transition between literal and metaphorical understanding.
   d) Provide a specific example of how your model would learn and apply the {t['source_domain']} IS {t['target_domain']} metaphor.

4. Developmental Progression (200-250 words):
   a) Outline how your model simulates the progression of metaphor acquisition through different developmental stages.
   b) Explain how the model's understanding of the {t['source_domain']} IS {t['target_domain']} metaphor changes from {t['developmental_stage']} to other stages.
   c) Discuss any critical periods or developmental milestones in your model.
   d) Provide a scenario demonstrating how your model's metaphor understanding evolves across two developmental stages.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate your model's performance in acquiring and using conceptual metaphors.
   b) Suggest experiments to validate your model against human developmental data.
   c) Discuss potential challenges in comparing artificial and human metaphor acquisition.

6. Implications and Applications (150-200 words):
   a) Discuss the potential implications of your model for understanding human cognitive development.
   b) Explore possible applications of your model in AI, education, or cognitive therapy.
   c) Propose a novel research question that could be investigated using your model.

Ensure your response demonstrates a deep understanding of cognitive linguistics, developmental psychology, and artificial intelligence. Use appropriate terminology and provide clear explanations. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of conceptual metaphor theory and its application to the {t['source_domain']} IS {t['target_domain']} metaphor, with clear explanations of how this metaphor develops during the {t['developmental_stage']} stage.",
            "The model architecture is well-designed and clearly presented, including a comprehensible diagram or flowchart.",
            f"The learning mechanism and developmental progression are explained in detail, with specific examples related to the {t['source_domain']} IS {t['target_domain']} metaphor.",
            "The response shows creative problem-solving in integrating concepts from cognitive linguistics, developmental psychology, and AI, proposing innovative yet plausible solutions.",
            "The proposed evaluation methods, implications, and future research directions are thoughtful, scientifically sound, and demonstrate a broad understanding of the field.",
            "The response is well-structured, clear, and adheres to the specified format and word count, with all required sections adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
