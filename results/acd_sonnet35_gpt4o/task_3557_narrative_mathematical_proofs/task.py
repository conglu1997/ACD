import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        topics = [
            "climate change",
            "artificial intelligence ethics",
            "space exploration",
            "quantum computing"
        ]
        math_concepts = [
            "calculus",
            "linear algebra",
            "number theory",
            "graph theory"
        ]
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'topic': random.choice(topics),
                'math_concept': random.choice(math_concepts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Create a mathematical proof that, when read aloud, forms a coherent narrative or argument related to {t['topic']}. Your proof should incorporate concepts from {t['math_concept']}. Follow these guidelines:\n\n1. Proof Structure (300-350 words):\n   a) Begin with a clear theorem statement that relates to the given topic.\n   b) Provide a step-by-step proof using valid mathematical reasoning.\n   c) Ensure that each step, when read aloud, contributes to a coherent narrative or argument about the topic.\n   d) Use appropriate mathematical notation, symbols, and equations.\n\n2. Mathematical Content (200-250 words):\n   a) Incorporate at least three distinct concepts or techniques from {t['math_concept']}.\n   b) Explain how these mathematical concepts relate to or illuminate aspects of {t['topic']}.\n   c) Ensure that the mathematical reasoning is sound and logically consistent.\n\n3. Narrative Coherence (200-250 words):\n   a) When read aloud, the proof should form a clear and engaging narrative or argument about {t['topic']}.\n   b) Use creative language and analogies to link mathematical concepts to real-world aspects of the topic.\n   c) Maintain grammatical correctness and narrative flow throughout the proof.\n\n4. Conclusion and Implications (150-200 words):\n   a) Conclude your proof with a clear statement of what has been demonstrated.\n   b) Discuss the implications of your mathematical argument for {t['topic']}.\n   c) Suggest potential real-world applications or further areas of study based on your proof.\n\n5. Reflection (100-150 words):\n   a) Briefly discuss the challenges you encountered in creating this narrative proof.\n   b) Explain how this approach to mathematical proofs might enhance understanding or communication of complex topics.\n\nEnsure your response demonstrates a deep understanding of both the mathematical concepts and the chosen topic. Be creative in your approach while maintaining mathematical rigor and narrative coherence. Use appropriate terminology from both mathematics and the relevant field of study.\n\nFormat your response with clear headings for each section. Your total response should be between 950-1200 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The proof incorporates concepts from {t['math_concept']} correctly and relevantly",
            f"The narrative or argument coherently addresses the topic of {t['topic']}",
            "The mathematical reasoning is sound and logically consistent",
            "The proof, when read aloud, forms a clear and engaging narrative",
            "The response demonstrates creativity in linking mathematical concepts to real-world aspects of the topic"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
