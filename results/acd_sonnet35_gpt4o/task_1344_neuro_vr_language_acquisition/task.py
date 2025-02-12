import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        languages = [
            {"name": "Mandarin Chinese", "feature": "tonal system"},
            {"name": "Arabic", "feature": "root-based morphology"},
            {"name": "Swahili", "feature": "noun class system"}
        ]
        return {str(i+1): lang for i, lang in enumerate(random.sample(languages, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a neuroscience-based virtual reality system for accelerated acquisition of {t['name']}, focusing on its {t['feature']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the overall structure of your VR language acquisition system.
   b) Explain how it incorporates neuroscientific principles to enhance learning.
   c) Detail how the system specifically targets the language's {t['feature']}.

2. Neuroscientific Basis (200-250 words):
   a) Explain the key neuroscientific principles underlying your system's design.
   b) Discuss how these principles are expected to accelerate language acquisition.
   c) Propose a method for monitoring brain activity during the VR experience.

3. VR Environment Design (200-250 words):
   a) Describe the virtual environment(s) used in your system.
   b) Explain how the VR design elements support language acquisition.
   c) Detail specific activities or exercises focused on the {t['feature']}.

4. Adaptive Learning Algorithm (150-200 words):
   a) Propose an algorithm that adapts the VR experience based on the user's progress.
   b) Explain how this algorithm integrates neurofeedback data.
   c) Discuss how it optimizes learning of the {t['feature']}.

5. Potential Cognitive Effects (150-200 words):
   a) Analyze potential short-term and long-term cognitive effects of using this system.
   b) Discuss how learning {t['name']} through this method might affect other cognitive processes.
   c) Propose a longitudinal study to investigate these effects.

6. Ethical Considerations (100-150 words):
   a) Identify potential ethical concerns related to using this technology for language acquisition.
   b) Propose guidelines for responsible development and use of neuroscience-based VR learning systems.

Ensure your response demonstrates a deep understanding of neuroscience, virtual reality technology, and language acquisition theories. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, virtual reality technology, and language acquisition theories",
            f"The system design specifically targets the {t['feature']} of {t['name']}",
            "The proposed system integrates neuroscientific principles in a plausible and innovative way",
            "The response includes a detailed analysis of potential cognitive effects and ethical considerations",
            "The answer is well-structured, clear, and within the specified word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
