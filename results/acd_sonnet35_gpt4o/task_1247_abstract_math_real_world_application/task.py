import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        math_concepts = [
            "topology",
            "group theory",
            "complex analysis",
            "category theory",
            "non-Euclidean geometry"
        ]
        application_domains = [
            "urban planning",
            "climate modeling",
            "social network analysis",
            "cryptography",
            "music composition"
        ]
        return {
            "1": {
                "math_concept": random.choice(math_concepts),
                "application_domain": random.choice(application_domains)
            },
            "2": {
                "math_concept": random.choice(math_concepts),
                "application_domain": random.choice(application_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Apply the mathematical concept of {t['math_concept']} to solve or analyze a problem in the domain of {t['application_domain']}. Your response should include:

1. Concept Overview (100-150 words):
   a) Briefly explain the key principles of {t['math_concept']}.
   b) Discuss its typical applications in pure mathematics.

2. Domain Analysis (100-150 words):
   a) Provide an overview of current challenges or interesting problems in {t['application_domain']}.
   b) Explain why traditional approaches might be insufficient to address these challenges.

3. Novel Application (250-300 words):
   a) Propose an innovative way to apply {t['math_concept']} to a specific problem in {t['application_domain']}.
   b) Explain how this application leverages the unique properties of the mathematical concept.
   c) Describe the potential benefits of this approach compared to conventional methods.

4. Implementation Outline (200-250 words):
   a) Provide a high-level description of how your proposed application could be implemented.
   b) Discuss any technical challenges that might arise and how they could be addressed.
   c) If applicable, suggest any new tools or frameworks that would need to be developed.

5. Implications and Future Directions (150-200 words):
   a) Discuss the broader implications of your proposed application for both {t['application_domain']} and mathematics.
   b) Suggest potential future research directions or extensions of your idea.
   c) Speculate on how this cross-disciplinary approach might lead to new discoveries or innovations.

Ensure your response demonstrates a deep understanding of both the mathematical concept and the application domain. Be creative in your approach while maintaining scientific and mathematical rigor. Use appropriate terminology and provide clear explanations for complex ideas.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['math_concept']} and its potential applications.",
            f"The proposed application to {t['application_domain']} must be innovative and well-reasoned.",
            "The response should show how the mathematical concept can provide unique insights or solutions in the application domain.",
            "The implementation outline must be logically sound and address potential challenges.",
            "The discussion of implications and future directions should be insightful and demonstrate broad thinking.",
            "The overall response must showcase creativity in connecting abstract mathematics with real-world applications."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
