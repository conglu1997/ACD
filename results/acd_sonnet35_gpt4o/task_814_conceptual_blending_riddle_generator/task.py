import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'domain1': 'Music',
                'domain2': 'Architecture',
                'blending_focus': 'Structure and Harmony'
            },
            {
                'domain1': 'Biology',
                'domain2': 'Computer Science',
                'blending_focus': 'Information Processing and Adaptation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and solves riddles using conceptual blending between {t['domain1']} and {t['domain2']}, focusing on the aspect of {t['blending_focus']}. Your response should include:

1. System Design (250-300 words):
   a) Describe the architecture of your AI system, including main components and their functions.
   b) Explain how your system implements conceptual blending to generate riddles.
   c) Detail the specific techniques or algorithms used for riddle generation and solving.

2. Riddle Generation and Solution (200-250 words):
   a) Generate an example riddle using your proposed system that blends concepts from {t['domain1']} and {t['domain2']}.
   b) Provide the solution to the riddle.
   c) Explain how the riddle demonstrates conceptual blending and the focus on {t['blending_focus']}.

3. Cognitive Process Analysis (150-200 words):
   a) Analyze how your system's riddle generation process parallels human cognitive processes in conceptual blending.
   b) Discuss any limitations of your system compared to human creativity in riddle generation.

4. Evaluation Method (100-150 words):
   a) Propose a method to evaluate the creativity and coherence of the generated riddles.
   b) Describe specific metrics or criteria you would use for this evaluation.

5. Potential Applications (100-150 words):
   a) Discuss potential applications of your conceptual blending riddle generator in fields such as education, cognitive science research, or creative writing.
   b) Explain how these applications could benefit from the unique capabilities of your system.

Ensure your response demonstrates a deep understanding of conceptual blending theory, cognitive science, and AI technologies. Be creative in your approach while maintaining scientific and technological plausibility.

Format your response using clear headings for each section and subsections where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of conceptual blending between {t['domain1']} and {t['domain2']}",
            "The system design is coherent and plausible",
            "The generated riddle effectively blends concepts from both domains",
            "The cognitive process analysis shows insight into human creativity",
            "The evaluation method and potential applications are well-reasoned"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
