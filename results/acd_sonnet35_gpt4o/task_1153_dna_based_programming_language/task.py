import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "biological_problem": "Gene regulation",
                "dna_bases": ["A", "T", "C", "G"],
                "example_sequence": "ATCG" * 5
            },
            "2": {
                "biological_problem": "Protein folding",
                "dna_bases": ["A", "T", "C", "G"],
                "example_sequence": "GCTA" * 5
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a programming language based on DNA sequences and use it to solve a problem in {t['biological_problem']}. Your task has the following components:

1. Language Design (250-300 words):
   a) Explain the key features of your DNA-based programming language.
   b) Describe how DNA bases ({', '.join(t['dna_bases'])}) are used as fundamental elements in your language.
   c) Provide examples of basic operations or functions in your language.
   d) Explain how your language incorporates biological principles related to DNA.

2. Problem Solution (200-250 words):
   a) Describe a specific problem in {t['biological_problem']} that your language is designed to address.
   b) Provide a code snippet in your DNA-based language that solves this problem.
   c) Explain how your solution leverages the unique properties of DNA sequences.

3. Execution Model (150-200 words):
   a) Describe how programs in your language would be executed.
   b) Explain any biological or chemical processes that could be used to 'run' the code.
   c) Discuss potential advantages of your execution model over traditional computing.

4. Analysis and Implications (200-250 words):
   a) Analyze the strengths and limitations of your DNA-based language for solving biological problems.
   b) Compare your language to traditional programming paradigms and existing computational biology tools.
   c) Discuss potential applications of your language in genetic engineering or synthetic biology.

5. Ethical Considerations (100-150 words):
   a) Discuss any ethical implications or concerns related to a programming language based on DNA.
   b) Propose guidelines for responsible development and use of such a language.

Ensure your response demonstrates a deep understanding of both computer science and molecular biology. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology from genetics, computer science, and related fields.

Format your response with clear headings for each section."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both computer science and molecular biology.",
            "The DNA-based programming language design is creative, plausible, and incorporates biological principles.",
            f"The proposed solution addresses a specific problem in {t['biological_problem']}.",
            "The execution model for the DNA-based language is explained clearly and relates to biological or chemical processes.",
            "The analysis includes a thoughtful comparison to traditional programming paradigms and discusses potential applications.",
            "Ethical considerations are addressed with proposed guidelines for responsible use."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
