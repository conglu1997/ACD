import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "abstract_concept": "Non-linear causality",
                "problem_domain": "Quantum physics and philosophy"
            },
            {
                "abstract_concept": "Multi-dimensional time",
                "problem_domain": "Cosmology and cognitive psychology"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical language model capable of representing and manipulating the abstract concept of {t['abstract_concept']}, which is beyond current human language capabilities. Then, use this model to address a complex problem in the domain of {t['problem_domain']}. Your response should include:

1. Language Model Design (300-350 words):
   a) Describe the key features and components of your language model.
   b) Explain how it represents and manipulates the given abstract concept.
   c) Discuss how this model transcends the limitations of human language.
   d) Include a visual or mathematical representation of your model (describe it textually using equations, diagrams, or symbols that can be represented in plain text).

2. Cognitive Implications (200-250 words):
   a) Analyze how your language model might influence or reflect cognitive processes.
   b) Discuss potential effects on perception, reasoning, and problem-solving.
   c) Compare your model to current theories of language and cognition.

3. Problem-Solving Application (250-300 words):
   a) Present a complex problem from the given domain that involves the abstract concept.
   b) Demonstrate how your language model would approach and solve this problem.
   c) Explain any novel insights or solutions that emerge from using your model.

4. AI Implementation (200-250 words):
   a) Propose how an AI system could be designed to utilize your language model.
   b) Discuss potential challenges and advantages of implementing this system.
   c) Explain how this AI might perform tasks differently from traditional language models.

5. Philosophical and Ethical Considerations (150-200 words):
   a) Discuss the philosophical implications of a language model that transcends human linguistic capabilities.
   b) Address potential ethical concerns or risks associated with such a model.
   c) Propose guidelines for responsible development and use of advanced language models.

6. Future Research Directions (150-200 words):
   a) Suggest potential applications of your language model in various fields.
   b) Propose experiments or studies to further explore the capabilities and effects of your model.
   c) Discuss how this approach might contribute to our understanding of language, cognition, and artificial intelligence.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative while maintaining scientific plausibility throughout your response.

Format your response with clear headings for each section. Your total response should be between 1250-1550 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all six required sections with appropriate content and length.",
            f"The language model design effectively incorporates the abstract concept of {t['abstract_concept']}.",
            f"The problem-solving application is relevant to the domain of {t['problem_domain']} and demonstrates novel insights.",
            "The AI implementation proposal is feasible and innovative.",
            "The philosophical and ethical considerations are thoughtful and comprehensive.",
            "The future research directions are insightful and demonstrate a broad understanding of potential applications.",
            "The overall response shows creativity, scientific plausibility, and clear articulation of complex interdisciplinary concepts.",
            f"The response specifically addresses the abstract concept of {t['abstract_concept']} and the problem domain of {t['problem_domain']} throughout all sections.",
            "The response includes a visual or mathematical representation of the language model using text-based equations, diagrams, or symbols.",
            "The total word count is between 1250-1550 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
