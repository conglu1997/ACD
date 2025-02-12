import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "cognitive_task": "Natural language understanding",
                "embodied_principle": "Sensorimotor grounding"
            },
            {
                "cognitive_task": "Spatial navigation",
                "embodied_principle": "Proprioception and spatial awareness"
            },
            {
                "cognitive_task": "Emotion recognition",
                "embodied_principle": "Interoception and physiological feedback"
            },
            {
                "cognitive_task": "Problem-solving in dynamic environments",
                "embodied_principle": "Situated cognition"
            }
        ]
        return {
            "1": random.choice(tasks),
            "2": random.choice(tasks)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design an AI system that incorporates principles of embodied cognition to perform the cognitive task of {t['cognitive_task']}, focusing on the embodied principle of {t['embodied_principle']}. Your response should include:\n\n1. Theoretical Foundation (200-250 words):\n   a) Explain the concept of embodied cognition and its relevance to AI.\n   b) Describe how the specified embodied principle relates to the given cognitive task.\n   c) Discuss potential advantages of an embodied approach for this task.\n\n2. AI System Architecture (250-300 words):\n   a) Design an AI system that incorporates the specified embodied principle for the given cognitive task.\n   b) Describe the key components of your system and how they interact.\n   c) Explain how your system simulates or implements the embodied principle.\n   d) Include a high-level diagram or pseudocode to illustrate your architecture.\n\n3. Learning and Adaptation Process (200-250 words):\n   a) Describe how your AI system would learn and adapt using the embodied approach.\n   b) Provide a specific example of how it would perform the given cognitive task.\n   c) Explain how the system's embodied nature contributes to its learning process.\n\n4. Comparative Analysis (200-250 words):\n   a) Compare your embodied AI approach to traditional disembodied AI methods for the given cognitive task.\n   b) Discuss potential advantages and limitations of your approach.\n   c) Propose a method to evaluate the effectiveness of your system compared to existing AI approaches.\n\n5. Ethical Considerations and Future Directions (150-200 words):\n   a) Discuss any ethical implications of using embodied AI for the given cognitive task.\n   b) Propose two potential applications of your system beyond the specified task.\n   c) Suggest one area for future research or improvement in embodied AI.\n\nEnsure your response demonstrates a deep understanding of embodied cognition, AI principles, and the specified cognitive task. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of embodied cognition and its relevance to AI.",
            "The AI system design effectively incorporates the specified embodied principle for the given cognitive task.",
            "The learning and adaptation process is well-explained and clearly leverages the embodied approach.",
            "The comparative analysis provides insightful comparisons between the embodied AI approach and traditional methods.",
            "The response addresses ethical considerations and future directions thoughtfully.",
            "The overall design is creative, scientifically plausible, and demonstrates interdisciplinary knowledge synthesis."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
