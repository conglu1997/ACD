import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "problem_domain": "Data Compression",
                "biological_principle": "DNA Codon Redundancy"
            },
            {
                "problem_domain": "Error Correction",
                "biological_principle": "DNA Repair Mechanisms"
            },
            {
                "problem_domain": "Secure Communication",
                "biological_principle": "Genetic Recombination"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bio-inspired information encoding system based on DNA principles, focusing on the biological principle of {t['biological_principle']}, and use it to solve a complex problem in the domain of {t['problem_domain']}. Your response should include:

1. System Design (300-350 words):
   a) Describe the key components of your DNA-inspired encoding system.
   b) Explain how your system incorporates the principle of {t['biological_principle']}.
   c) Discuss how your system translates between conventional digital data and DNA-like sequences.
   d) Provide an example of how a simple piece of information would be encoded in your system.

2. Biological Foundations (200-250 words):
   a) Explain the relevant aspects of {t['biological_principle']} in actual DNA systems.
   b) Discuss how you've abstracted or modified these principles for use in your encoding system.
   c) Address any limitations or simplifications in your bio-inspired approach.

3. Problem-Solving Application (250-300 words):
   a) Describe a specific problem in {t['problem_domain']} that your system is particularly suited to address.
   b) Provide a detailed solution to this problem using your DNA-inspired encoding system.
   c) Explain how the bio-inspired features of your system contribute to solving the problem.
   d) Compare your approach to traditional methods in {t['problem_domain']}.

4. Theoretical Analysis (200-250 words):
   a) Provide a mathematical or information-theoretical analysis of your encoding system.
   b) Discuss the efficiency, robustness, and scalability of your approach.
   c) Address any potential limitations or trade-offs in your system.

5. Broader Implications (150-200 words):
   a) Discuss potential applications of your DNA-inspired encoding system beyond {t['problem_domain']}.
   b) Explore how your system might contribute to advancements in synthetic biology or biocomputing.
   c) Address any ethical considerations or potential misuses of your encoding system.

Ensure your response demonstrates a deep understanding of molecular biology, information theory, and the specific problem domain. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide explanations for complex concepts where necessary.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words. Adhere strictly to the word count guidelines for each section and use the section headings as provided above."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must demonstrate a clear understanding of {t['biological_principle']} and how it can be applied to {t['problem_domain']}.",
            "The DNA-inspired encoding system should be innovative, logically consistent, and well-explained.",
            "The problem-solving application should be detailed and demonstrate clear advantages over traditional methods.",
            "The theoretical analysis should be sound and demonstrate a good understanding of information theory.",
            "The response must thoughtfully address broader implications and ethical considerations of the proposed system.",
            "The response should follow the specified format with clear section headings and adhere to the word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
