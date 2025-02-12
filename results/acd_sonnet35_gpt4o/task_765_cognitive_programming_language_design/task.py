import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_processes = [
            "Analogical reasoning",
            "Conceptual blending",
            "Mental model manipulation",
            "Associative memory retrieval",
            "Embodied cognition",
            "Metacognition",
            "Cognitive load management",
            "Perceptual simulation"
        ]
        problem_domains = [
            "Natural language understanding",
            "Visual pattern recognition",
            "Decision making under uncertainty",
            "Creative idea generation",
            "Emotion recognition and processing",
            "Spatial reasoning and navigation",
            "Multimodal learning",
            "Adaptive problem-solving"
        ]
        return {
            "1": {"process": random.choice(cognitive_processes), "domain": random.choice(problem_domains)},
            "2": {"process": random.choice(cognitive_processes), "domain": random.choice(problem_domains)}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical programming language based on the cognitive process of {t['process']} and apply it to solve a complex problem in the domain of {t['domain']}. Your response should include:

1. Language Design (300-350 words):
   a) Describe the key features and syntax of your cognitive programming language.
   b) Explain how it incorporates the specified cognitive process.
   c) Provide at least 3 code snippets demonstrating unique aspects of your language.
   d) Discuss how your language differs from traditional programming paradigms.
   e) Include a visual representation or diagram of your language design (describe it textually).

2. Cognitive Foundations (200-250 words):
   a) Explain the cognitive science principles underlying your language design.
   b) Discuss how your language might influence or change programmers' thought processes.
   c) Address potential cognitive benefits and challenges of using your language.

3. Problem-Solving Application (250-300 words):
   a) Describe a complex problem in the specified domain that your language is particularly suited to solve.
   b) Provide a high-level algorithm or pseudocode in your language to address this problem.
   c) Explain how the cognitive process-based features of your language contribute to solving the problem.

4. Implementation Considerations (200-250 words):
   a) Discuss potential challenges in implementing an interpreter or compiler for your language.
   b) Propose approaches to overcome these challenges.
   c) Explore how existing hardware or software architectures might need to be adapted for your language.

5. Broader Implications (150-200 words):
   a) Discuss how your cognitive programming language might impact software development practices.
   b) Explore potential applications in artificial intelligence or cognitive modeling.
   c) Address any ethical considerations or potential misuses of your language.

Ensure your response demonstrates a deep understanding of both cognitive science and computer science principles. Be creative in your approach while maintaining scientific and technological plausibility. Use appropriate terminology and provide explanations where necessary. Adhere to the word limits for each section.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The language design is based on the cognitive process of {t['process']}",
            f"The language is applied to solve a problem in the domain of {t['domain']}",
            "The response includes at least 3 code snippets demonstrating unique aspects of the language",
            "A visual representation or diagram of the language design is described",
            "The cognitive science principles underlying the language design are clearly explained",
            "A complex problem and its solution using the designed language are described",
            "Implementation challenges and potential solutions are discussed",
            "The broader implications of the language are explored",
            "The response demonstrates deep understanding of both cognitive science and computer science",
            "The response adheres to the specified word limits for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
