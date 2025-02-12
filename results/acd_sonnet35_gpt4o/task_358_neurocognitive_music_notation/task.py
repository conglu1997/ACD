import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'musical_element': 'rhythm',
                'cognitive_process': 'working memory'
            },
            {
                'musical_element': 'pitch',
                'cognitive_process': 'auditory processing'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel musical notation system focused on {t['musical_element']}, based on principles of {t['cognitive_process']} from cognitive neuroscience. Your task is to create a notation system that could potentially enhance music learning and performance. Provide your response in the following format:

1. Notation System Overview (150-200 words):
   Briefly describe your notation system and how it aims to enhance {t['musical_element']} learning and performance through {t['cognitive_process']}.

2. Key Features (list 4-5 points):
   Describe the main features of your notation system, explaining how each relates to {t['musical_element']} and {t['cognitive_process']}.

3. Visual Representation (150-200 words):
   Describe in detail how your notation system would visually represent {t['musical_element']}. Explain why this representation might be more intuitive or effective than traditional notation.

4. Neurological Basis (200-250 words):
   Explain the neurological principles behind your notation system. How does it leverage our understanding of {t['cognitive_process']} to potentially enhance music learning and performance?

5. Sample Notation (provide 2 examples):
   Describe two examples of how specific musical phrases or concepts would be notated in your system. Explain how these examples demonstrate the system's advantages.

6. Potential Benefits (150-200 words):
   Discuss how your notation system might enhance music education, performance, or composition. Consider both cognitive and practical benefits.

7. Implementation Challenges (150-200 words):
   Address potential difficulties in adopting this new notation system and propose strategies to overcome them.

8. Comparative Analysis (200-250 words):
   Compare your notation system to traditional Western notation and at least one other alternative notation system (e.g., graphic scores, tablature). Discuss the relative strengths and weaknesses of each approach.

Ensure your notation system design is creative, theoretically grounded in both music theory and neuroscience, and clearly demonstrates how it could potentially enhance music learning and performance."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed design of a novel musical notation system focused on {t['musical_element']}, based on principles of {t['cognitive_process']}.",
            "The notation system overview clearly explains how it aims to enhance music learning and performance.",
            "Key features of the notation system are well-described and relate to both the musical element and cognitive process.",
            "The visual representation of the notation system is described in detail and its potential effectiveness is explained.",
            "The neurological basis of the notation system is thoroughly explained, demonstrating understanding of the specified cognitive process.",
            "Two clear examples of musical notation in the new system are provided and explained.",
            "Potential benefits of the notation system are discussed, considering both cognitive and practical aspects.",
            "Implementation challenges are addressed with proposed strategies to overcome them.",
            "A comparative analysis is provided, contrasting the new system with traditional Western notation and at least one other alternative system."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
