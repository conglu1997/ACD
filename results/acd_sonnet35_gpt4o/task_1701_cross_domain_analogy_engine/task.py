import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            ("quantum mechanics", "social networks"),
            ("evolutionary biology", "economic systems"),
            ("fluid dynamics", "information flow in organizations"),
            ("celestial mechanics", "political power structures"),
            ("thermodynamics", "urban development"),
            ("neural networks", "ecosystem interactions")
        ]
        problems = [
            "resource allocation",
            "pattern recognition",
            "system optimization",
            "predictive modeling",
            "adaptive learning",
            "emergent behavior"
        ]
        return {
            "1": {
                "source_domain": random.choice(domains)[0],
                "target_domain": random.choice(domains)[1],
                "problem": random.choice(problems)
            },
            "2": {
                "source_domain": random.choice(domains)[0],
                "target_domain": random.choice(domains)[1],
                "problem": random.choice(problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system capable of understanding and generating complex analogies across different domains of knowledge, then use it to solve an interdisciplinary problem. Your task has the following parts:\n\n1. Analogy Engine Design (300-350 words):\n   a) Describe the key components and architecture of your cross-domain analogy engine.\n   b) Explain how your system represents and maps concepts from different domains.\n   c) Detail the process of generating and evaluating analogies.\n   d) Discuss any novel techniques or approaches used in your design.\n\n2. Knowledge Integration (200-250 words):\n   a) Explain how your system integrates knowledge from diverse domains, specifically {t['source_domain']} and {t['target_domain']}.\n   b) Describe the data sources and types you would use to train your system.\n   c) Discuss challenges in combining knowledge from these disparate fields and how you address them.\n\n3. Analogy Generation (250-300 words):\n   a) Use your system to generate a complex analogy between {t['source_domain']} and {t['target_domain']}.\n   b) Explain the key mappings and relationships in your generated analogy.\n   c) Analyze the strengths and limitations of this analogy.\n\n4. Problem Solving Application (250-300 words):\n   a) Apply your generated analogy to address the problem of {t['problem']} in the {t['target_domain']} domain.\n   b) Explain how insights from {t['source_domain']} contribute to solving this problem.\n   c) Discuss any novel solutions or perspectives that emerge from this cross-domain approach.\n\n5. Evaluation and Refinement (200-250 words):\n   a) Propose metrics to evaluate your system's performance in generating useful analogies and solving problems.\n   b) Describe how you would refine and improve your system based on these evaluations.\n   c) Discuss potential biases or limitations in your approach and how you might address them.\n\n6. Ethical and Societal Implications (150-200 words):\n   a) Discuss potential ethical implications of using AI for cross-domain analogical reasoning.\n   b) Explore the broader societal impacts of systems that can generate novel solutions through unexpected analogies.\n   c) Propose guidelines for responsible development and use of such systems.\n\nEnsure your response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.\n\nFormat your response with clear headings for each section. Your total response should be between 1350-1650 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system for cross-domain analogy generation and problem-solving, specifically addressing {t['source_domain']} and {t['target_domain']}.",
            f"The generated analogy between {t['source_domain']} and {t['target_domain']} is complex, insightful, and well-explained.",
            f"The application of the analogy to solve the problem of {t['problem']} in {t['target_domain']} is creative and well-reasoned.",
            "The response demonstrates a deep understanding of cognitive science, linguistics, and artificial intelligence concepts.",
            "The ethical and societal implications of the proposed system are thoughtfully considered.",
            "The response is well-structured, following the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
