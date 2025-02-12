import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'initial_alphabet': 'ABCD',
                'initial_rules': ['A -> AB', 'B -> C', 'C -> D', 'D -> DA'],
                'generations': 3,
                'operation': 'substitution'
            },
            {
                'initial_alphabet': '01',
                'initial_rules': ['0 -> 01', '1 -> 10'],
                'generations': 4,
                'operation': 'xor'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""In this task, you will create and evolve a mathematical language system. This process models how languages can evolve based on simple rules, similar to how cellular automata or L-systems work in mathematics and computer science.

Initial alphabet: {t['initial_alphabet']}
Initial evolution rules: {t['initial_rules']}
Number of generations: {t['generations']}
Operation: {t['operation']}

1. Start with the given initial alphabet.
2. Apply the initial evolution rules for the specified number of generations. In each generation, apply all rules simultaneously to the result of the previous generation.
   Example: If the alphabet is 'AB' and the rules are ['A -> AB', 'B -> A'], then:
   Generation 0: AB
   Generation 1: ABA
   Generation 2: ABAAB
3. After applying the rules, perform the specified operation on the result:
   - If 'substitution', replace each character with its ASCII value.
     Example: 'ABC' becomes '65 66 67'
   - If 'xor', perform bitwise XOR operation on the binary representation of each character with the binary representation of its position (1-indexed).
     Example: 'AB' becomes '65 64' because:
     A (ASCII 65) in binary is 01000001, position 1 in binary is 00000001, XOR result is 01000000 (64 in decimal)
     B (ASCII 66) in binary is 01000010, position 2 in binary is 00000010, XOR result is 01000000 (64 in decimal)
   Note: If spaces or punctuation appear in the evolved language, treat them as regular characters.
4. Based on the final result, create new evolution rules that would generate an interesting pattern if applied repeatedly. Your new rules should follow the format 'X -> Y' where X is a single character and Y is a string of one or more characters. An 'interesting' pattern could be one that grows in a non-trivial way, creates symmetry, or demonstrates some form of self-similarity.
5. Describe a potential real-world application or implication of your evolved language system. Consider one of the following fields:
   a) Cryptography: How could this system be used to encode or decode messages?
   b) Data compression: How might this system compress or expand data?
   c) Artificial Intelligence: How could this system model or generate language-like structures?

Provide your response in the following format:

Evolution Process:
[Show each generation of the language evolution]

Final Result:
[The result after applying the specified operation]

New Evolution Rules:
[List your new rules, one per line]

Explanation:
[Explain your reasoning for the new rules and why the resulting pattern would be interesting]

Potential Application:
[Describe a potential real-world application in one of the specified fields]

Note: Strictly adhere to this format in your response. Each section should be clearly labeled and contain the requested information."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The evolution process is correctly applied for the specified number of generations.",
            "The specified operation (substitution or xor) is correctly performed on the final result.",
            "The new evolution rules are creative, follow the specified format, and would generate an interesting pattern as defined in the instructions.",
            "The explanation for the new rules demonstrates understanding of the underlying patterns and potential for interesting evolution.",
            "The potential real-world application is innovative, logically connected to the evolved language system, and specifically addresses one of the fields mentioned in the instructions (cryptography, data compression, or artificial intelligence).",
            "The response strictly follows the specified format with clear section labels."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
