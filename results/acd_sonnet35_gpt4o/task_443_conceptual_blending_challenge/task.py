import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "domain1": "Music",
                "domain2": "Architecture",
                "blend_context": "Design a musical instrument"
            },
            {
                "domain1": "Biology",
                "domain2": "Computer Science",
                "blend_context": "Describe a new type of artificial intelligence"
            },
            {
                "domain1": "Cuisine",
                "domain2": "Chemistry",
                "blend_context": "Invent a novel cooking technique"
            },
            {
                "domain1": "Psychology",
                "domain2": "Physics",
                "blend_context": "Explain a new theory of human motivation"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create and analyze a novel conceptual blend combining the domains of {t['domain1']} and {t['domain2']} in the context of {t['blend_context']}. Follow these steps:

1. Conceptual Blend Creation (150-200 words):
   a) Identify key concepts or elements from both {t['domain1']} and {t['domain2']}.
   b) Describe how these concepts can be combined in a novel and meaningful way.
   c) Explain your conceptual blend, focusing on how it addresses {t['blend_context']}.

2. Cognitive Linguistics Analysis (150-200 words):
   a) Discuss the mental spaces involved in your conceptual blend.
   b) Explain the mapping and projection processes between the input spaces.
   c) Identify emergent structure in the blended space that isn't present in either input space.

3. Implications and Applications (100-150 words):
   a) Explore potential real-world applications or implications of your conceptual blend.
   b) Discuss how this blend might lead to new insights or innovations in either or both domains.

4. Reflection on Creativity (100-150 words):
   a) Analyze the creative process you used to generate this conceptual blend.
   b) Discuss how this exercise relates to human cognitive processes and creativity.

Ensure your response demonstrates a deep understanding of both domains, cognitive linguistics principles, and creative thinking. Use clear, concise language and provide specific examples to illustrate your points."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response creates a novel and meaningful conceptual blend combining {t['domain1']} and {t['domain2']} in the context of {t['blend_context']}.",
            "The cognitive linguistics analysis demonstrates a clear understanding of mental spaces, mapping processes, and emergent structure.",
            "The implications and applications of the conceptual blend are insightful and well-reasoned.",
            "The reflection on creativity shows a deep understanding of cognitive processes and their relation to conceptual blending."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
