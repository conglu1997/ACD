import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'visual_complexity': 'high',
                'abstraction_level': 'metaphorical'
            },
            {
                'visual_complexity': 'medium',
                'abstraction_level': 'conceptual'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that generates abstract linguistic descriptions of visual scenes, with a focus on {t['visual_complexity']} complexity scenes and {t['abstraction_level']} level abstractions. Your task has the following components:

1. System Architecture (200-250 words):
   a) Describe the key components of your system for processing visual information and generating linguistic abstractions.
   b) Explain how your system integrates visual perception with language processing.
   c) Detail the mechanisms for extracting high-level concepts and relationships from visual input.
   d) Discuss how your system handles the specified level of visual complexity and abstraction.

2. Visual-Linguistic Mapping (200-250 words):
   a) Explain your approach to mapping visual elements to linguistic constructs.
   b) Describe how your system handles ambiguity and multiple interpretations in visual scenes.
   c) Discuss any novel techniques or algorithms used in this mapping process.

3. Abstraction Generation (200-250 words):
   a) Detail the process of generating {t['abstraction_level']} level abstractions from visual information.
   b) Explain how your system ensures coherence and relevance in its abstract descriptions.
   c) Discuss how cultural or contextual factors are considered in the abstraction process.

4. Example Analysis (200-250 words):
   Provide a specific example of how your system would process a {t['visual_complexity']} complexity visual scene:
   a) Describe a hypothetical visual scene in detail (no actual image is provided; use your imagination). Include at least 5-7 distinct elements or features in your scene description.
   b) Present the abstract linguistic description your system would generate for this scene.
   c) Explain the reasoning behind this description, highlighting key abstraction steps and how they relate to the scene elements.

5. Evaluation and Limitations (150-200 words):
   a) Propose methods for evaluating the effectiveness of your system's abstract descriptions.
   b) Discuss potential limitations or challenges in your approach.
   c) Compare your system's capabilities to human performance in similar tasks.

6. Cognitive and AI Implications (150-200 words):
   a) Discuss how your system relates to theories of human visual perception and language processing.
   b) Explore potential applications of your system in AI research or cognitive science.
   c) Propose a research question that arises from the development of this system.

Ensure your response demonstrates a deep understanding of visual perception, language processing, and abstract reasoning. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts.

IMPORTANT: Address all parts of each section thoroughly. Format your response with clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The system architecture effectively integrates visual perception and language processing for {t['visual_complexity']} complexity scenes.",
            f"The approach to generating {t['abstraction_level']} level abstractions is well-explained and innovative.",
            "The visual-linguistic mapping process is clearly described and addresses ambiguity in visual scenes.",
            "The example analysis includes a detailed hypothetical scene and demonstrates the system's ability to generate relevant and coherent abstract descriptions.",
            "The response includes a thoughtful discussion of evaluation methods, limitations, and comparisons to human performance.",
            "The cognitive and AI implications are insightful and demonstrate interdisciplinary thinking.",
            "All six required sections are present and adequately addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
