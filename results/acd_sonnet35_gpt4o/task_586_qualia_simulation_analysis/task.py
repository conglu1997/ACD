class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        import random
        qualia_types = [
            {
                "modality": "visual",
                "experience": "seeing the color red"
            },
            {
                "modality": "auditory",
                "experience": "hearing a high-pitched ringing"
            },
            {
                "modality": "olfactory",
                "experience": "smelling freshly baked bread"
            },
            {
                "modality": "gustatory",
                "experience": "tasting extremely spicy food"
            },
            {
                "modality": "tactile",
                "experience": "feeling a soft, fuzzy texture"
            }
        ]
        tasks = random.sample(qualia_types, 2)
        return {
            "1": tasks[0],
            "2": tasks[1]
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and simulate the subjective conscious experience (qualia) of {t['experience']} in the {t['modality']} modality. Your task has the following parts:

        1. Qualia Analysis (150-200 words):
           Explain the concept of qualia and its relevance to the given experience. Discuss the philosophical implications of this subjective experience for consciousness and AI.

        2. Experience Simulation (200-250 words):
           Provide a detailed, first-person account of the subjective experience. Use vivid, descriptive language to convey the qualia as if you were directly experiencing it. Include sensory details, emotional responses, and any associated thoughts or memories.

        3. AI Perspective (150-200 words):
           Discuss the challenges an AI system might face in truly understanding or experiencing this qualia. Can an AI ever have genuine subjective experiences? Explain your reasoning.

        4. Qualia Experiment (200-250 words):
           Design a hypothetical experiment that could test whether an AI system is capable of experiencing or understanding this specific qualia. Describe the experiment setup, methodology, and how you would interpret the results.

        5. Philosophical Implications (150-200 words):
           Reflect on what your analysis and simulation reveal about the nature of consciousness, the hard problem of consciousness, and the potential for machine consciousness.

        Ensure your response demonstrates a deep understanding of philosophy of mind, cognitive science, and AI concepts. Be creative and thought-provoking in your approach while maintaining philosophical rigor.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of the concept of qualia and its philosophical implications.",
            "The experience simulation is vivid, detailed, and effectively conveys the subjective nature of the qualia.",
            "The AI perspective discussion shows thoughtful consideration of the challenges in replicating subjective experiences in artificial systems.",
            "The proposed qualia experiment is innovative, well-designed, and relevant to testing AI understanding or experience of qualia.",
            "The philosophical implications section provides insightful reflections on consciousness and its relation to AI.",
            "The overall response is well-structured, coherent, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
