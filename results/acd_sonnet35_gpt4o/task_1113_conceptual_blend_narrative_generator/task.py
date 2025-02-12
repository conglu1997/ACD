import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        narrative_elements = [
            {
                "input_space_1": "Time travel",
                "input_space_2": "Ecosystem",
                "blending_goal": "Create a narrative where changes in the past affect the evolution of species"
            },
            {
                "input_space_1": "Artificial Intelligence",
                "input_space_2": "Ancient mythology",
                "blending_goal": "Develop a story where AI systems embody roles of mythological gods"
            }
        ]
        return {
            "1": random.choice(narrative_elements),
            "2": random.choice(narrative_elements)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"Design a system that uses conceptual blending theory to generate novel narrative structures, then create a story using this system. Your task has the following parts:\n\n1. Conceptual Blending System Design (300-350 words):\n   a) Explain the key principles of conceptual blending theory.\n   b) Describe how your system would implement these principles to generate narrative structures.\n   c) Detail the components of your system and how they interact.\n   d) Explain how your system ensures coherence and novelty in the generated narratives.\n\n2. Narrative Generation Process (250-300 words):\n   a) Using your system, blend the following input spaces: \"{t['input_space_1']}\" and \"{t['input_space_2']}\".\n   b) Describe the blended space that results from this combination.\n   c) Explain how your system would use this blended space to generate a narrative structure.\n   d) Discuss any challenges in this blending process and how your system addresses them.\n\n3. Story Creation (400-450 words):\n   Create a short story (or a detailed story outline) based on the blended space and narrative structure you generated. Your story should:\n   a) Clearly reflect elements from both input spaces.\n   b) Demonstrate the blending goal: {t['blending_goal']}.\n   c) Showcase a coherent plot structure with a beginning, middle, and end.\n   d) Include at least one character and one conflict derived from the conceptual blend.\n\n4. Analysis and Reflection (200-250 words):\n   a) Analyze how your story demonstrates the principles of conceptual blending.\n   b) Reflect on how this approach to narrative generation differs from traditional storytelling methods.\n   c) Discuss potential applications of your system in fields such as creative writing, game design, or AI-assisted storytelling.\n\n5. Ethical Considerations (100-150 words):\n   Discuss potential ethical implications of using AI systems for creative tasks like story generation, considering issues such as copyright, authorship, and the impact on human creativity.\n\nEnsure your response demonstrates a deep understanding of conceptual blending theory, creative problem-solving in system design, and skilled application of interdisciplinary knowledge in narrative creation. Use appropriate terminology and provide clear explanations where necessary.\n\nFormat your response with clear headings for each section. Your total response should be between 1250-1500 words."

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a clear understanding of conceptual blending theory and its application to narrative generation.",
            "The proposed system design is coherent, innovative, and well-explained.",
            f"The generated story successfully blends elements from both \"{t['input_space_1']}\" and \"{t['input_space_2']}\".",
            f"The story effectively addresses the blending goal: {t['blending_goal']}.",
            "The response includes thoughtful analysis, reflection, and consideration of ethical implications.",
            "The overall submission is well-structured, coherent, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
