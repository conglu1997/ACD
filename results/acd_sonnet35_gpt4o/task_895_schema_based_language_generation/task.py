import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            {
                "name": "Restaurant dining",
                "key_concepts": ["menu", "waiter", "order", "cuisine", "bill"],
                "relationships": ["customer-waiter", "food-price", "ambiance-satisfaction"]
            },
            {
                "name": "Academic conference",
                "key_concepts": ["presentation", "networking", "research", "Q&A", "proceedings"],
                "relationships": ["speaker-audience", "research-feedback", "collaboration-innovation"]
            }
        ]
        
        tasks = {}
        for i in range(2):
            domain = random.choice(domains)
            tasks[str(i+1)] = {
                "domain": domain["name"],
                "key_concepts": domain["key_concepts"],
                "relationships": domain["relationships"]
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a cognitive schema for the domain of {t['domain']} and use it to generate and analyze language. Your task has three parts:

1. Schema Design (200-250 words):
   a) Create a detailed cognitive schema for the {t['domain']} domain.
   b) Include the key concepts: {', '.join(t['key_concepts'])}.
   c) Incorporate the relationships: {', '.join(t['relationships'])}.
   d) Add at least three additional concepts and two relationships that fit this domain.
   e) Explain how your schema represents typical expectations and knowledge structures in this domain.

2. Language Generation (200-250 words):
   a) Use your schema to generate a coherent paragraph (5-7 sentences) describing a typical scenario in the {t['domain']} domain.
   b) Ensure your generated text incorporates at least 7 concepts and 3 relationships from your schema.
   c) Explain how your schema guided the generation process and how it ensures contextual relevance.

3. Language Analysis (200-250 words):
   a) Analyze the following text using your cognitive schema:
      [Insert a 3-4 sentence text related to the domain]
   b) Identify which concepts and relationships from your schema are present in the text.
   c) Discuss any deviations or unexpected elements in the text that don't fit your schema.
   d) Explain how your schema helps in understanding and interpreting the given text.

Ensure your response demonstrates a deep understanding of cognitive schemas and their application to language processing. Be creative in your schema design while maintaining logical consistency within the given domain.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a well-designed cognitive schema for the {t['domain']} domain",
            "The schema should incorporate all given key concepts and relationships, plus additional relevant ones",
            "The generated paragraph should coherently use the schema elements in a typical scenario",
            "The language analysis should demonstrate how the schema aids in understanding and interpreting text",
            "The overall response should show a deep understanding of cognitive schemas and their application to language processing"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
