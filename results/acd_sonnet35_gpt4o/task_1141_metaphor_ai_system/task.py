import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "time",
            "love",
            "justice",
            "knowledge",
            "power",
            "freedom"
        ]
        concrete_domains = [
            "nature",
            "technology",
            "food",
            "sports",
            "architecture",
            "music"
        ]
        applications = [
            "creative writing",
            "advertising",
            "education",
            "psychotherapy",
            "political communication",
            "scientific explanation"
        ]
        
        tasks = [
            {
                "abstract_concept": random.choice(abstract_concepts),
                "concrete_domain": random.choice(concrete_domains),
                "application": random.choice(applications)
            } for _ in range(2)
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating novel metaphors, focusing on the abstract concept of {t['abstract_concept']} using the concrete domain of {t['concrete_domain']}. Then, analyze its potential application in {t['application']}. Your response should include:

1. Metaphor AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for metaphor understanding and generation.
   b) Explain how your system integrates cognitive linguistics theories with machine learning techniques.
   c) Detail how the system processes and represents abstract concepts and concrete domains.
   d) Discuss any novel approaches you've incorporated to handle the complexities of metaphorical thinking.

2. Metaphor Generation Process (200-250 words):
   a) Explain the step-by-step process your AI system would use to generate a novel metaphor.
   b) Provide an example of a metaphor your system might generate for the given abstract concept and concrete domain.
   c) Discuss how your system ensures the generated metaphors are both novel and meaningful.

3. Metaphor Understanding Mechanism (200-250 words):
   a) Describe how your system would interpret and understand given metaphors.
   b) Explain how it handles ambiguity and context in metaphor interpretation.
   c) Discuss any limitations in your system's metaphor understanding capabilities.

4. Evaluation Metrics (150-200 words):
   a) Propose specific metrics to evaluate the quality, novelty, and appropriateness of generated metaphors.
   b) Describe how you would measure the system's metaphor understanding capabilities.
   c) Discuss the challenges in evaluating metaphor generation and understanding systems.

5. Application Analysis (200-250 words):
   a) Analyze how your Metaphor AI system could be applied in the field of {t['application']}.
   b) Provide specific examples of how it could be used in this field.
   c) Discuss potential benefits and challenges of using AI-generated metaphors in this context.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to AI systems that can generate and understand metaphors.
   b) Consider the societal implications of such systems, both positive and negative.
   c) Propose guidelines for the responsible development and use of metaphor AI systems.

7. Future Research Directions (100-150 words):
   a) Suggest two potential areas for further research to advance metaphor AI systems.
   b) Explain how these research directions could address current limitations or open up new possibilities.

Ensure your response demonstrates a deep understanding of cognitive linguistics, natural language processing, and machine learning. Use appropriate technical terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility.

Format your response using clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an AI system for understanding and generating metaphors related to {t['abstract_concept']} using {t['concrete_domain']}",
            f"The application of the system in {t['application']} must be thoroughly addressed",
            "The proposed AI system architecture should be scientifically plausible and clearly explained",
            "The response should demonstrate interdisciplinary knowledge integration",
            "Ethical implications must be thoughtfully considered",
            "The metaphor generation and understanding processes should be well-defined and logical",
            "Evaluation metrics for the system should be specific and relevant",
            "Future research directions should be relevant and well-justified",
            "The response should follow the specified format with clear headings for each section",
            "The response should be within the specified word count range (1300-1650 words)"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
