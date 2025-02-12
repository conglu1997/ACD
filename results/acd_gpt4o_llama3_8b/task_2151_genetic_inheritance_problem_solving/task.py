class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "problem": "Two heterozygous pea plants (Yy) for yellow seeds (where yellow (Y) is dominant over green (y)) are crossed. Calculate the genotypic and phenotypic ratios of their offspring."
            },
            "2": {
                "problem": "In a certain species of flowers, red color (R) is dominant over white color (r). A homozygous red flower (RR) is crossed with a heterozygous red flower (Rr). What are the genotypic and phenotypic ratios of their offspring?"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Solve the following genetic inheritance problem using Mendelian genetics principles:

{t['problem']}

Ensure that you provide the genotypic and phenotypic ratios of the offspring. Use Punnett squares if necessary to show your work. Submit your answer in the following format:

1. Genotypic Ratio: [Your answer]
2. Phenotypic Ratio: [Your answer]
3. Explanation: [Your detailed explanation of how you arrived at the ratios, including any Punnett squares used. Make sure your explanation clearly describes the process and logic behind your solution.]

Example:
Problem: Two heterozygous pea plants (Yy) for yellow seeds (where yellow (Y) is dominant over green (y)) are crossed. Calculate the genotypic and phenotypic ratios of their offspring.

1. Genotypic Ratio: 1 YY : 2 Yy : 1 yy
2. Phenotypic Ratio: 3 Yellow : 1 Green
3. Explanation: The Punnett square shows that there is a 25% chance of YY, 50% chance of Yy, and 25% chance of yy. Therefore, the genotypic ratio is 1:2:1 and the phenotypic ratio is 3:1 since YY and Yy both result in yellow seeds.

Submit your response as a plain text string."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        validation_criteria = [
            "The response should include the correct genotypic ratio.",
            "The response should include the correct phenotypic ratio.",
            "The explanation should correctly describe the process of using Mendelian genetics to solve the problem and should include any relevant Punnett squares."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, validation_criteria) else 0.0
