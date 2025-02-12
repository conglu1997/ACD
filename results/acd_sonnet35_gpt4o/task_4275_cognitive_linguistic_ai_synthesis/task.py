import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_domains = ['spatial reasoning', 'temporal concepts', 'emotion', 'causality', 'social relationships']
        metaphor_types = ['orientational', 'ontological', 'structural', 'image schema']
        reasoning_tasks = ['analogy completion', 'concept categorization', 'inferential reasoning', 'pattern recognition']
        example_metaphors = {
            'spatial reasoning': 'Life is a journey',
            'temporal concepts': 'Time is money',
            'emotion': 'Anger is a hot fluid in a container',
            'causality': 'Ideas are plants',
            'social relationships': 'Love is a battlefield'
        }
        
        tasks = {}
        for i in range(1, 3):
            cognitive_domain = random.choice(cognitive_domains)
            tasks[str(i)] = {
                "cognitive_domain": cognitive_domain,
                "metaphor_type": random.choice(metaphor_types),
                "reasoning_task": random.choice(reasoning_tasks),
                "example_metaphor": example_metaphors[cognitive_domain]
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that integrates cognitive linguistics principles to generate and analyze complex metaphorical language in the domain of {t['cognitive_domain']}, focusing on {t['metaphor_type']} metaphors. Then, apply this system to solve a {t['reasoning_task']} problem. An example metaphor in this domain is '{t['example_metaphor']}'. Your response should include:\n\n" \
               f"1. Cognitive-Linguistic Framework (250-300 words):\n" \
               f"   a) Describe the key components of your AI system for generating and analyzing metaphorical language.\n" \
               f"   b) Explain how your system incorporates principles from cognitive linguistics and metaphor theory.\n" \
               f"   c) Discuss how your system models the relationship between {t['cognitive_domain']} and language.\n\n" \
               f"2. Metaphor Generation and Analysis (250-300 words):\n" \
               f"   a) Provide three examples of {t['metaphor_type']} metaphors your system would generate for {t['cognitive_domain']}.\n" \
               f"   b) Explain how your system analyzes and interprets these metaphors.\n" \
               f"   c) Discuss any challenges in computationally representing and processing these metaphors.\n\n" \
               f"3. Application to {t['reasoning_task']} (300-350 words):\n" \
               f"   a) Describe a specific {t['reasoning_task']} problem related to {t['cognitive_domain']}.\n" \
               f"   b) Explain how your system would approach this problem using metaphorical reasoning.\n" \
               f"   c) Provide a step-by-step example of your system solving the problem, including sample metaphors generated and analyzed.\n\n" \
               f"4. Cognitive Science Implications (200-250 words):\n" \
               f"   a) Discuss how your system's approach relates to theories of human cognition and language processing.\n" \
               f"   b) Propose a testable hypothesis about metaphor comprehension or generation that could be investigated using your system.\n" \
               f"   c) Suggest an experiment design to validate your hypothesis.\n\n" \
               f"5. Ethical Considerations and Limitations (150-200 words):\n" \
               f"   a) Discuss potential ethical implications of using AI systems for metaphor generation and analysis.\n" \
               f"   b) Address any limitations or potential biases in your system's approach to metaphorical reasoning.\n" \
               f"   c) Propose guidelines for the responsible development and use of cognitive-linguistic AI systems.\n\n" \
               f"Ensure your response demonstrates a deep understanding of cognitive linguistics, metaphor theory, and AI. Use appropriate terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\n" \
               f"Format your response with clear headings for each section and subsections labeled a, b, c as appropriate. Your total response should be between 1150-1400 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of cognitive linguistics and metaphor theory, particularly in relation to {t['cognitive_domain']} and {t['metaphor_type']} metaphors.",
            "The AI system design is innovative and integrates cognitive linguistics principles effectively.",
            f"Three appropriate {t['metaphor_type']} metaphors are provided for the {t['cognitive_domain']}.",
            f"The application to the {t['reasoning_task']} problem is well-explained with a clear step-by-step example.",
            "The cognitive science implications are discussed with a testable hypothesis and experiment design.",
            "Ethical considerations and limitations are thoroughly addressed with proposed guidelines.",
            "The response is well-structured, within the specified word limit, and uses appropriate terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
