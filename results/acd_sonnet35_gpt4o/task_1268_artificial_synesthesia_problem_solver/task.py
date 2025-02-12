import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                "domain": "Music Composition",
                "challenge": "Create a musical piece that represents the taste of umami"
            },
            {
                "domain": "Architecture",
                "challenge": "Design a building that embodies the concept of jazz improvisation"
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of artificial synesthesia, then use it to solve a complex multi-modal problem in the domain of {t['domain']}. Your task has the following components:

1. Artificial Synesthesia System Design (300-350 words):
   a) Describe the architecture of your AI system that enables cross-modal sensory experiences.
   b) Explain how your system processes and integrates different types of sensory information.
   c) Detail the mechanisms that allow for novel associations between sensory modalities.
   d) Discuss how your system's artificial synesthesia differs from and/or mimics human synesthesia.

2. Training and Data (200-250 words):
   a) Explain what types of data your system would need for training.
   b) Describe the training process and any novel techniques you would employ.
   c) Discuss how you would validate that your system is truly experiencing artificial synesthesia.

3. Problem-Solving Application (250-300 words):
   a) Apply your artificial synesthesia system to the following challenge: {t['challenge']}
   b) Describe step-by-step how your system would approach and solve this problem.
   c) Explain how the artificial synesthesia capabilities contribute to the solution.

4. Output Analysis (200-250 words):
   a) Describe the expected output of your system for the given challenge.
   b) Analyze how this output demonstrates both artificial synesthesia and problem-solving capabilities.
   c) Discuss any unexpected or emergent properties in the solution.

5. Implications and Future Directions (150-200 words):
   a) Discuss the potential implications of artificial synesthesia for AI creativity and problem-solving.
   b) Propose two novel applications of your system in different domains.
   c) Suggest future research directions to enhance or expand the capabilities of your system.

Ensure your response demonstrates a deep understanding of cognitive science, AI, and the specific domain of the challenge. Be creative and innovative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The artificial synesthesia system design is innovative and well-explained",
            "The training and data section addresses the unique challenges of developing artificial synesthesia",
            "The problem-solving application demonstrates a clear and creative use of artificial synesthesia",
            "The output analysis shows deep understanding of both the AI system and the problem domain",
            "The implications and future directions section provides insightful and novel ideas"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
