import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            'Physics',
            'Biology',
            'Economics',
            'Psychology',
            'Mathematics',
            'Art',
            'Music',
            'Technology'
        ]
        abstract_concepts = [
            'Complexity',
            'Balance',
            'Growth',
            'Transformation',
            'Connectivity',
            'Harmony',
            'Entropy',
            'Emergence'
        ]
        tasks = [
            {
                'source_domain': random.choice(domains),
                'target_domain': random.choice(domains),
                'abstract_concept': random.choice(abstract_concepts)
            },
            {
                'source_domain': random.choice(domains),
                'target_domain': random.choice(domains),
                'abstract_concept': random.choice(abstract_concepts)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of developing and using abstract reasoning in language understanding and generation, then apply it to analyze and create conceptual metaphors across different domains. Your system should demonstrate the ability to understand and generate novel conceptual metaphors that bridge disparate domains through abstract concepts.

For this task, apply your system to the following scenario:

Source Domain: {t['source_domain']}
Target Domain: {t['target_domain']}
Abstract Concept to Bridge: {t['abstract_concept']}

Your response should include the following sections:

1. Abstract Reasoning Framework (250-300 words):
   a) Explain your AI system's approach to developing abstract reasoning capabilities.
   b) Describe how your system represents and manipulates abstract concepts.
   c) Detail the cognitive processes your system employs for abstract reasoning in language.

2. Conceptual Metaphor Generation (250-300 words):
   a) Outline your AI system's process for generating conceptual metaphors across domains.
   b) Explain how your system utilizes abstract reasoning in this process.
   c) Provide an example of a conceptual metaphor your system would generate for the given scenario, bridging the source and target domains through the specified abstract concept.
   d) Analyze the generated metaphor, explaining its structure and implications.

3. Linguistic Analysis and Interpretation (200-250 words):
   a) Describe how your AI system would analyze and interpret existing conceptual metaphors.
   b) Explain how this analysis contributes to the system's understanding of abstract concepts and domain relationships.
   c) Discuss potential challenges in interpreting metaphors across diverse domains and how your system addresses them.

4. Abstract Reasoning Evaluation (200-250 words):
   a) Propose methods for evaluating your AI system's abstract reasoning capabilities in language tasks.
   b) Describe specific metrics or tests you would use to assess the quality and novelty of generated conceptual metaphors.
   c) Explain how you would measure the system's ability to transfer abstract concepts across domains.

5. Cognitive and Linguistic Implications (200-250 words):
   a) Discuss the potential insights your system could provide into human cognitive processes related to abstract reasoning and metaphor creation.
   b) Explore how your system's approach might inform or challenge current theories in cognitive linguistics.
   c) Consider potential applications of your system in fields such as education, creative writing, or scientific discovery.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical concerns related to AI systems capable of abstract reasoning and metaphor generation.
   b) Discuss limitations of your approach and areas for future improvement.
   c) Propose guidelines for the responsible development and use of such AI systems.

Ensure your response demonstrates a deep understanding of abstract reasoning, cognitive linguistics, and AI system design. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of abstract reasoning, cognitive linguistics, and AI system design.",
            "The proposed AI system shows innovative approaches to developing abstract reasoning capabilities in language tasks.",
            "The conceptual metaphor generated for the given scenario effectively bridges the source and target domains through the specified abstract concept.",
            "The response includes a thorough analysis of the generated metaphor and its implications.",
            "The proposed evaluation methods and metrics for assessing abstract reasoning are well-thought-out and relevant.",
            "The discussion of cognitive and linguistic implications shows insight into human cognitive processes and current theories in cognitive linguistics.",
            "Ethical considerations and limitations are thoughtfully addressed.",
            "The response is well-structured, clear, and within the specified word count for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
