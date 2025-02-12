import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "math_concept": "prime numbers",
                "rhyme_scheme": "ABAB CDCD EFEF GG",
                "meter": "iambic pentameter"
            },
            "2": {
                "math_concept": "Fibonacci sequence",
                "rhyme_scheme": "ABBA ABBA CDC DCD",
                "meter": "iambic pentameter"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Compose a mathematical sonnet that adheres to the following rules:

1. The sonnet must be about {t['math_concept']}.
2. Follow the rhyme scheme: {t['rhyme_scheme']}.
3. Use {t['meter']} for each line (10 syllables per line, alternating unstressed and stressed syllables).
4. Incorporate at least three specific mathematical terms or concepts related to {t['math_concept']}. A mathematical term or concept is a word, phrase, or idea that has a precise meaning in mathematics (e.g., 'factor', 'sequence', 'infinity').
5. Include at least one mathematical symbol or equation, integrating it naturally into the verse.
6. The final couplet (last two lines) must contain a mathematical insight or conclusion about {t['math_concept']}.
7. Each quatrain (group of four lines) should focus on a different aspect or property of {t['math_concept']}.

Provide your response in the following format:

Sonnet:
[Line 1]
[Line 2]
...
[Line 14]

Mathematical terms/concepts used:
1. [Term/concept 1]
2. [Term/concept 2]
3. [Term/concept 3]

Quatrain focus (20-30 words each):
1st quatrain: [Brief description of focus]
2nd quatrain: [Brief description of focus]
3rd quatrain: [Brief description of focus]

Mathematical symbol/equation explanation (30-50 words):
[Explain how the mathematical symbol or equation is relevant to the sonnet's content]

Overall explanation (100-150 words):
[Your explanation of how you incorporated the mathematical concept, adhered to the sonnet structure, and maintained coherence and creativity]

Remember, in iambic pentameter, each line should have exactly 10 syllables with the stress pattern: unstressed, stressed, unstressed, stressed, and so on.

Scoring rubric:
- Adherence to rhyme scheme and meter (20%)
- Incorporation of three mathematical terms/concepts (20%)
- Integration of mathematical symbol/equation (15%)
- Distinct focus for each quatrain (15%)
- Mathematical insight in final couplet (10%)
- Relevance of mathematical symbol/equation to content (10%)
- Overall coherence and creativity (10%)"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The sonnet must be about {t['math_concept']} and incorporate at least three specific mathematical terms or concepts related to it.",
            f"The sonnet must follow the rhyme scheme: {t['rhyme_scheme']}.",
            f"Each line must be in {t['meter']} (10 syllables, alternating unstressed and stressed).",
            "The sonnet must include at least one mathematical symbol or equation integrated naturally into the verse.",
            "The final couplet must contain a mathematical insight or conclusion about the given concept.",
            "Each quatrain should focus on a different aspect or property of the mathematical concept.",
            "The response must include a list of the three mathematical terms/concepts used and a brief description (20-30 words) of each quatrain's focus.",
            "The response must include an explanation (30-50 words) of how the mathematical symbol or equation is relevant to the sonnet's content.",
            "The overall explanation (100-150 words) must accurately describe how the mathematical concept was incorporated, how the sonnet structure was followed, and how coherence and creativity were maintained."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
