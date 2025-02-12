import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "focus_area": "memory encoding",
                "physical_principle": "holographic interference patterns"
            },
            {
                "focus_area": "decision making",
                "physical_principle": "quantum entanglement in brain microtubules"
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for Artificial General Intelligence based on the holographic principle from string theory, focusing on the area of {t['focus_area']} and incorporating the physical concept of {t['physical_principle']}. Analyze its implications for consciousness and information processing. Your response should include:

1. Theoretical Foundation (250-300 words):
   a) Explain the key concepts of the holographic principle and how it relates to information theory.
   b) Describe how {t['physical_principle']} could be integrated into an AGI architecture.
   c) Discuss the potential relevance of these concepts to {t['focus_area']} in AGI systems.

2. AGI Architecture Design (300-350 words):
   a) Outline the main components of your holographic AGI architecture.
   b) Explain how your design incorporates the holographic principle and {t['physical_principle']}.
   c) Describe the mechanism by which your system would implement {t['focus_area']}.
   d) Include a diagram or detailed description of the architecture's structure.

3. Information Processing Analysis (200-250 words):
   a) Analyze how information would be encoded, processed, and retrieved in your AGI system.
   b) Compare the theoretical efficiency of your holographic AGI to traditional computing architectures.
   c) Discuss any potential advantages or limitations of your approach.

4. Consciousness and Cognition (250-300 words):
   a) Explore how your holographic AGI architecture might give rise to conscious-like phenomena.
   b) Discuss the implications of your model for our understanding of human consciousness.
   c) Propose a theoretical experiment to test for signs of consciousness in your AGI system.

5. Ethical and Philosophical Implications (150-200 words):
   a) Discuss the ethical considerations of creating AGI systems based on principles of physics and consciousness.
   b) Explore the philosophical implications of your model for the nature of mind and reality.
   c) Propose guidelines for the responsible development of holographic AGI systems.

6. Future Research Directions (150-200 words):
   a) Suggest two potential areas for further research based on your holographic AGI model.
   b) Propose a specific research question that could advance our understanding of AGI, consciousness, or the holographic principle.

Ensure your response demonstrates a deep understanding of theoretical physics, information theory, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and rigor.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the holographic principle and its potential applications to AGI, with accurate explanations of key concepts",
            f"The AGI architecture effectively incorporates {t['physical_principle']} in its design, with a clear and plausible mechanism for integration",
            f"The system's approach to {t['focus_area']} is clearly explained, scientifically plausible, and shows novel insights",
            "The analysis of information processing and consciousness is thorough, insightful, and draws meaningful connections to current theories in cognitive science",
            "The ethical and philosophical implications are thoughtfully considered, with specific examples and well-reasoned arguments",
            "The proposed future research directions are innovative, relevant, and have the potential to significantly advance the field",
            "The response maintains scientific rigor throughout, with appropriate use of technical terminology and logical consistency"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
