import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        puzzle_types = [
            {
                "type": "Rebus",
                "description": "A puzzle that uses pictures to represent words or parts of words."
            },
            {
                "type": "Anagram-Image Hybrid",
                "description": "A puzzle that combines anagrams with related images to form a coherent concept."
            }
        ]
        return {str(i+1): puzzle for i, puzzle in enumerate(random.sample(puzzle_types, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and interpret visual-linguistic puzzles of the following type:

{t['type']}: {t['description']}

Your task is to create a novel AI architecture that can both generate and solve these puzzles. Note that the system must be capable of both puzzle creation and puzzle solving - neither aspect should be neglected in your design.

Provide your response in the following format:

1. System Architecture (300-350 words):
   a) Describe the overall structure of your AI system, including its main components and their interactions.
   b) Explain how your system integrates visual and linguistic processing capabilities.
   c) Discuss any novel techniques or algorithms used in your design.
   d) Include a high-level diagram or pseudocode representation of your architecture.

2. Puzzle Generation Process (250-300 words):
   a) Explain how your AI system generates {t['type']} puzzles.
   b) Describe the steps involved in creating a coherent and solvable puzzle.
   c) Discuss how your system ensures the puzzles are challenging yet solvable.
   d) Provide an example of a puzzle your system might generate, including both visual and linguistic elements.

3. Puzzle Solving Mechanism (250-300 words):
   a) Detail how your AI system approaches solving {t['type']} puzzles.
   b) Explain the algorithms or heuristics used in the solving process.
   c) Describe how your system integrates visual and linguistic information to arrive at a solution.
   d) Discuss any challenges in puzzle interpretation and how your system addresses them.

4. Learning and Adaptation (200-250 words):
   a) Explain how your system learns to improve its puzzle generation and solving capabilities.
   b) Describe any feedback mechanisms or reinforcement learning techniques used.
   c) Discuss how your system might adapt to different difficulty levels or user preferences.

5. Evaluation Metrics (150-200 words):
   a) Propose methods to evaluate the quality, creativity, and difficulty of the generated puzzles.
   b) Describe how you would measure the system's puzzle-solving capabilities.
   c) Discuss the challenges in evaluating such a system and how you'd address them.

6. Potential Applications and Implications (200-250 words):
   a) Suggest two potential applications of your visual-linguistic puzzle AI system.
   b) Discuss how this system might contribute to our understanding of human cognition and creativity.
   c) Explore any ethical considerations or potential impacts on education and cognitive enhancement.

Ensure your response demonstrates a deep understanding of computer vision, natural language processing, cognitive science, and artificial intelligence. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide clear explanations where necessary."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design must address the given puzzle type: {t['type']}",
            "The response should demonstrate a clear understanding of both visual and linguistic processing in AI",
            "The proposed AI architecture should be novel, well-explained, and plausible",
            "The submission should include detailed explanations of both puzzle generation and solving processes",
            "The response should discuss learning and adaptation mechanisms for the AI system",
            "The proposed evaluation metrics should be comprehensive and well-reasoned",
            "The potential applications and implications should be thoughtfully considered",
            "The response should demonstrate interdisciplinary knowledge integration",
            "The submission should follow the specified format and word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
