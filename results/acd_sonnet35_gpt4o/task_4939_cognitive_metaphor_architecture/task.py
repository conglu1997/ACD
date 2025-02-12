import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            'Time',
            'Consciousness',
            'Justice',
            'Knowledge',
            'Complexity'
        ]
        source_domains = [
            'Nature',
            'Technology',
            'Human body',
            'Architecture',
            'Music'
        ]
        
        tasks = {}
        for i in range(1, 3):
            concept = random.choice(abstract_concepts)
            domain = random.choice(source_domains)
            tasks[str(i)] = {
                'concept': concept,
                'domain': domain
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a cognitive architecture for metaphor generation and interpretation, then use it to create and analyze a novel metaphor for the abstract concept of {t['concept']} using the source domain of {t['domain']}. Your response should include:\n\n" \
               f"1. Cognitive Architecture Design (300-350 words):\n" \
               f"   a) Describe the key components of your cognitive architecture for metaphor processing.\n" \
               f"   b) Explain how your architecture models the cognitive processes involved in metaphor generation and interpretation.\n" \
               f"   c) Discuss how your system integrates knowledge from different domains to create meaningful metaphors.\n" \
               f"   d) Include a diagram or flowchart of your architecture (describe this textually).\n\n" \
               f"2. Metaphor Generation (200-250 words):\n" \
               f"   a) Use your cognitive architecture to generate a novel metaphor for {t['concept']} using {t['domain']} as the source domain.\n" \
               f"   b) Explain the step-by-step process your system follows to create this metaphor.\n" \
               f"   c) Discuss how your system ensures the metaphor is both novel and meaningful.\n\n" \
               f"3. Metaphor Analysis (250-300 words):\n" \
               f"   a) Analyze the generated metaphor, explaining its components and mappings.\n" \
               f"   b) Discuss the insights this metaphor provides about {t['concept']}.\n" \
               f"   c) Evaluate the metaphor's effectiveness in conveying abstract ideas.\n\n" \
               f"4. Cognitive Implications (200-250 words):\n" \
               f"   a) Discuss how your architecture's approach to metaphor processing compares to human cognition.\n" \
               f"   b) Analyze potential cognitive biases or limitations in your system's metaphor generation and interpretation.\n" \
               f"   c) Propose an experiment to test whether your system's metaphors enhance human understanding of abstract concepts.\n\n" \
               f"5. Ethical and Practical Implications (150-200 words):\n" \
               f"   a) Discuss ethical considerations in developing AI systems capable of generating and interpreting metaphors.\n" \
               f"   b) Explore potential applications of your cognitive architecture in fields such as education, creative writing, or scientific discovery.\n" \
               f"   c) Suggest guidelines for responsible development and use of metaphor-generating AI systems.\n\n" \
               f"Ensure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section. Your total response should be between 1100-1350 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence principles.",
            "The cognitive architecture design is comprehensive, innovative, and plausible.",
            f"The generated metaphor for {t['concept']} using {t['domain']} is novel and meaningful.",
            "The metaphor analysis is thorough and insightful.",
            "The discussion of cognitive implications shows a nuanced understanding of human cognition and AI limitations.",
            "The ethical and practical implications are thoughtfully considered.",
            "The response is well-structured, clear, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
