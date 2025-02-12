import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_schemas = [
            {
                "schema": "Script schema",
                "description": "Represents sequences of events or actions",
                "example": "The process of ordering food at a restaurant"
            },
            {
                "schema": "Categorization schema",
                "description": "Organizes objects or concepts into categories",
                "example": "Classifying animals into mammals, reptiles, birds, etc."
            },
            {
                "schema": "Spatial schema",
                "description": "Represents spatial relationships and navigation",
                "example": "Mental map of your hometown"
            },
            {
                "schema": "Causal schema",
                "description": "Represents cause-and-effect relationships",
                "example": "Understanding how weather patterns affect crop growth"
            }
        ]
        
        cognitive_problems = [
            "Implement a decision-making algorithm for an autonomous robot",
            "Design a system for natural language understanding in AI",
            "Create a model for emotion recognition in human-computer interaction",
            "Develop an adaptive learning system for personalized education"
        ]
        
        return {
            "1": {
                "schema": random.choice(cognitive_schemas),
                "problem": random.choice(cognitive_problems)
            },
            "2": {
                "schema": random.choice(cognitive_schemas),
                "problem": random.choice(cognitive_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a programming language based on the cognitive schema of {t['schema']['schema']} ({t['schema']['description']}). Then, use your language to solve the following problem in artificial cognition: {t['problem']}\n\nProvide your response in the following format:\n\n1. Language Design (300-350 words):\n   a) Describe the key features and syntax of your programming language, including at least three unique constructs that reflect the {t['schema']['schema']}.\n   b) Explain how your language incorporates the principles of the {t['schema']['schema']}, providing specific examples of how cognitive processes are represented.\n   c) Provide a code snippet (5-10 lines) demonstrating a basic operation in your language, with comments explaining each line.\n   d) Discuss how your language differs from traditional programming languages, highlighting at least two major distinctions.\n\n2. Problem Solution (250-300 words):\n   a) Present a high-level algorithm or pseudocode (at least 10 steps) to solve the given problem using your language.\n   b) Explain how your solution leverages at least two unique features of your language.\n   c) Discuss any challenges you anticipate in implementing this solution and propose approaches to overcome them.\n\n3. Cognitive Analysis (200-250 words):\n   a) Analyze how your language might influence problem-solving and cognitive processes, providing at least one concrete example.\n   b) Discuss two potential advantages and two limitations of using a schema-based language for artificial cognition.\n   c) Propose a detailed experiment to test the cognitive effects of using your language, including hypothesis, methodology, and expected outcomes.\n\n4. Interdisciplinary Implications (150-200 words):\n   a) Explore how your language might be applied in two other fields (e.g., psychology, education, or neuroscience), providing specific use cases.\n   b) Discuss at least two potential ethical considerations in developing cognitive schema-based programming languages.\n   c) Suggest a future research direction that could emerge from this work, outlining potential objectives and methodologies.\n\nEnsure your response demonstrates a deep understanding of cognitive science, programming language design, and artificial intelligence. Be creative and innovative while maintaining scientific and technical plausibility."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design effectively incorporates principles of the {t['schema']['schema']}, with at least three unique constructs clearly explained.",
            "The code snippet provided is coherent, relevant, and well-commented.",
            "The problem solution presents a detailed algorithm or pseudocode that clearly applies the designed language to the given artificial cognition problem.",
            "The cognitive analysis provides insightful understanding of the potential impacts and implications of the language design, with concrete examples.",
            "The proposed experiment to test cognitive effects is well-structured and scientifically sound.",
            "The interdisciplinary implications are thoughtfully explored, with specific use cases and ethical considerations.",
            "The response exhibits creativity and innovation while maintaining scientific and technical plausibility throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
