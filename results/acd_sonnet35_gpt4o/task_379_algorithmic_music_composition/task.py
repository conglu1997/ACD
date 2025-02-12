import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "composition_type": "Minimalist",
                "mathematical_concept": "Fibonacci sequence",
                "musical_element": "Rhythm"
            },
            {
                "composition_type": "Serialist",
                "mathematical_concept": "Prime numbers",
                "musical_element": "Pitch"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an algorithmic music composition system that generates a {t['composition_type']} piece based on the {t['mathematical_concept']}, focusing primarily on the musical element of {t['musical_element']}. Your task is to:

1. System Design (250-300 words):
   - Describe the core components and functioning of your algorithmic composition system.
   - Explain how it incorporates the specified mathematical concept into the musical composition process.
   - Discuss how it applies music theory principles relevant to the given composition type.
   - Detail how the system focuses on the specified musical element.

2. Algorithm Explanation (200-250 words):
   - Provide a step-by-step explanation of how your algorithm generates a musical piece.
   - Include at least one mathematical formula or pseudo-code snippet that illustrates a key part of your algorithm.
   - Explain how your algorithm ensures musical coherence and adheres to the principles of the specified composition type.

3. Sample Output Analysis (200-250 words):
   - Describe a hypothetical musical passage that your system might generate.
   - Analyze this passage in terms of its musical structure, adherence to the composition type, and use of the mathematical concept.
   - Explain how the specified musical element is particularly highlighted in this passage.

4. Creative Extensions (150-200 words):
   - Propose two creative ways to extend your system, such as incorporating additional mathematical concepts, musical elements, or compositional techniques.
   - Briefly explain how each extension would enhance the system's capabilities or the resulting compositions.

Ensure your response is well-structured, using clear headings for each section. Your analysis should be creative yet grounded in music theory and mathematical principles, demonstrating a deep understanding of both domains and their potential interactions in computational creativity.

Your total response should be between 800-1000 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must design an algorithmic music composition system for a {t['composition_type']} piece based on the {t['mathematical_concept']}, focusing on {t['musical_element']}",
            "The system design should be innovative, musically sound, and clearly explained",
            "The algorithm explanation should include at least one mathematical formula or pseudo-code snippet",
            "The sample output analysis should demonstrate a deep understanding of music theory and the specified composition type",
            "The creative extensions should be original and well-reasoned",
            "The overall response should show a balance between musical creativity and mathematical rigor",
            "All four sections (System Design, Algorithm Explanation, Sample Output Analysis, and Creative Extensions) must be adequately addressed",
            "The response should be between 800-1000 words in total"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
