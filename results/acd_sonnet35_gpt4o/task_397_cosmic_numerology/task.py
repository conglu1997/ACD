import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = [
            {
                "name": "Celestians",
                "base": 12,
                "cosmology": "A universe with 12 celestial spheres",
                "problem": "Calculate the area of a triangle with sides 5, 8, and 10"
            },
            {
                "name": "Primordials",
                "base": 5,
                "cosmology": "A world built on 5 elemental forces",
                "problem": "Find the sum of the first 20 numbers in this system"
            },
            {
                "name": "Cyclics",
                "base": 7,
                "cosmology": "A reality governed by 7 cosmic cycles",
                "problem": "Multiply 13 by 16 in this system"
            }
        ]
        selected = random.sample(cultures, 2)
        return {"1": selected[0], "2": selected[1]}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an original and creative number system for the {t['name']} culture based on their cosmology of {t['cosmology']}. Then, use this system to solve a mathematical problem and analyze its cultural implications. Follow these steps:

(Note: A base-n number system uses n unique digits to represent numbers. For example, our decimal system is base-10, using digits 0-9.)

1. Number System Design (200-250 words):
   a) Describe your unique number system, explaining how it's inspired by the {t['name']} cosmology.
   b) Explain how this system represents numbers in base-{t['base']}.
   c) Provide examples of how basic mathematical operations (addition, subtraction, multiplication, division) work in this system.
   d) Include a conversion method between your system and base-10.

   Example (do not use this directly): In a base-4 system inspired by four seasons, you might use symbols ❄️, 🌱, ☀️, 🍁 to represent 0, 1, 2, 3 respectively.

2. Problem Solving (200-250 words):
   a) Solve the following problem using your number system: {t['problem']}
   b) Show your work step-by-step, explaining each stage of the calculation.
   c) Convert your final answer back to base-10 and verify its correctness.

3. Cultural Analysis (200-250 words):
   a) Explain how this number system reflects the {t['name']} culture's worldview and values.
   b) Discuss how this system might influence the {t['name']}' approach to mathematics, science, and everyday life.
   c) Compare this system to our base-10 system, highlighting potential advantages and limitations.

4. Practical Applications (150-200 words):
   a) Propose two practical applications of this number system within the {t['name']} society.
   b) Explain how these applications might shape their technological or scientific development.

5. Intercultural Communication (100-150 words):
   a) Describe a potential challenge in explaining this number system to someone from a base-10 culture.
   b) Suggest a method to facilitate understanding between cultures with different number systems.

Ensure your response demonstrates a deep understanding of number systems, mathematical problem-solving, and cultural analysis. Be creative and original in your approach while maintaining mathematical accuracy and cultural sensitivity.

Format your response with clear headings for each section, numbered as above. Your total response should be between 850-1100 words. Manage your time wisely to address all sections thoroughly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed description of an original number system based on the {t['name']} cosmology and using base-{t['base']}",
            "The number system design includes unique symbols or representations for numbers",
            "The design includes examples of all four basic mathematical operations (addition, subtraction, multiplication, division)",
            "A conversion method between the new system and base-10 is provided",
            f"The mathematical problem '{t['problem']}' is correctly solved using the designed number system, with clear step-by-step explanations",
            "The cultural analysis demonstrates how the number system reflects the culture's worldview and influences their approach to mathematics, science, and everyday life",
            "The response proposes two practical and innovative applications of the number system within the given society",
            "The response addresses specific challenges in intercultural communication regarding different number systems and suggests a creative method to facilitate understanding",
            "The response is well-structured with clear, numbered headings and is between 850-1100 words",
            "The overall response demonstrates creativity, originality, and a deep understanding of the interdisciplinary nature of the task"
        ]
        scores = [eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria]
        return sum(scores) / len(criteria)
