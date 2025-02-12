import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_principles = [
            "chunking",
            "visual processing",
            "phonological loop",
            "semantic networks",
            "dual coding theory"
        ]
        writing_aspects = [
            "alphabet design",
            "word formation",
            "sentence structure",
            "text organization",
            "reading direction"
        ]
        tasks = {}
        for i in range(1, 3):
            principle = random.choice(cognitive_principles)
            aspect = random.choice(writing_aspects)
            tasks[str(i)] = {"principle": principle, "aspect": aspect}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a novel writing system based on the cognitive principle of {t['principle']}, focusing on the aspect of {t['aspect']}. Your task is to:\n\n1. Explain the chosen cognitive principle and its relevance to writing systems (2-3 sentences).\n2. Describe your innovative writing system, detailing how it incorporates the cognitive principle into the specified aspect (4-5 sentences).\n3. Provide a concrete example of how your writing system would represent a simple sentence or concept (2-3 sentences).\n4. Analyze potential advantages and limitations of your writing system compared to existing systems (3-4 sentences).\n5. Discuss how your writing system might influence cognitive processes or learning in its users (3-4 sentences).\n6. Propose an experiment to test the effectiveness or cognitive impact of your writing system (2-3 sentences).\n\nEnsure your response is creative yet grounded in cognitive science and linguistic principles. Organize your answer using clear headings for each section."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the chosen cognitive principle and its application to writing systems",
            "The proposed writing system is innovative and logically incorporates the cognitive principle into the specified aspect",
            "The example provided clearly illustrates how the writing system works",
            "The analysis of advantages and limitations is thoughtful and grounded in cognitive science",
            "The discussion of cognitive influences is insightful and well-reasoned",
            "The proposed experiment is relevant and well-designed to test the writing system's effectiveness or impact"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0