import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        mathematical_concepts = [
            "topology",
            "group theory",
            "complex analysis",
            "differential geometry",
            "category theory",
            "algebraic geometry",
            "functional analysis",
            "chaos theory"
        ]
        application_domains = [
            "quantum computing",
            "evolutionary biology",
            "climate modeling",
            "cognitive neuroscience",
            "financial modeling",
            "artificial intelligence",
            "cryptography",
            "network science"
        ]
        return {
            "1": {
                "math_concept": random.choice(mathematical_concepts),
                "application": random.choice(application_domains)
            },
            "2": {
                "math_concept": random.choice(mathematical_concepts),
                "application": random.choice(application_domains)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a novel symbolic language based on concepts from {t['math_concept']}, then use it to represent and solve a complex problem in {t['application']}. Your task has the following components:

1. Symbolic Language Design (250-300 words):
   a) Define the basic elements and rules of your symbolic language, incorporating key concepts from {t['math_concept']}.
   b) Explain how your language represents mathematical operations and structures relevant to {t['math_concept']}.
   c) Provide examples of how complex ideas in {t['math_concept']} are expressed in your language.
   d) Describe how your language can be extended to represent concepts in {t['application']}.
   e) Ensure your symbolic language is original and not a reproduction of existing systems.

   Example: If designing a language based on topology, you might use symbols to represent open sets, continuous functions, and homeomorphisms, such as '◯' for open set, '→' for continuous function, and '≅' for homeomorphism.

2. Problem Formulation (150-200 words):
   a) State a complex problem in {t['application']} that could benefit from the mathematical framework of {t['math_concept']}.
   b) Explain why this problem is particularly suited for analysis using your symbolic language.

3. Problem Representation (200-250 words):
   a) Translate the problem into your symbolic language.
   b) Explain each step of the translation process, highlighting how your language captures the essence of both the mathematical and applied aspects of the problem.

4. Solution Process (250-300 words):
   a) Use your symbolic language to solve the problem step-by-step.
   b) For each step, provide both the symbolic representation and an explanation of its meaning.
   c) Highlight how your language facilitates insights or simplifies the problem-solving process.

5. Interpretation and Analysis (150-200 words):
   a) Interpret the solution in the context of {t['application']}.
   b) Discuss any novel insights or perspectives gained through the use of your symbolic language.
   c) Analyze the strengths and limitations of your approach compared to traditional methods in {t['application']}.

6. Potential Extensions (100-150 words):
   a) Propose two ways your symbolic language could be extended or applied to other problems in {t['application']} or related fields.
   b) Briefly describe how these extensions could lead to new research directions or methodologies.

Ensure your response demonstrates a deep understanding of both {t['math_concept']} and {t['application']}. Be creative and original in your language design and problem-solving approach while maintaining mathematical and scientific rigor. Use appropriate terminology from both fields and provide clear explanations where necessary.

Format your response using clear headings for each section. Your total response should be between 1100-1400 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a deep understanding of both {t['math_concept']} and {t['application']}.",
            "The symbolic language design should be creative, coherent, original, and effectively incorporate the specified mathematical concepts.",
            "The problem formulation and representation should be clear and well-suited to the symbolic language.",
            "The solution process should be logical, well-explained, and make effective use of the symbolic language.",
            "The interpretation and analysis should provide meaningful insights and a critical evaluation of the approach.",
            "The proposed extensions should be innovative and demonstrate the potential for broader applications of the symbolic language.",
            "The overall response should be well-structured, adhere to the word count guidelines, and demonstrate exceptional interdisciplinary knowledge and creative problem-solving."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
