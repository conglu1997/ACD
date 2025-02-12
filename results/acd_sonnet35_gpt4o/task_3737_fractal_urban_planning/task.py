import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cities = [
            "Tokyo, Japan",
            "Sao Paulo, Brazil",
            "Lagos, Nigeria",
            "New York City, USA",
            "Mumbai, India",
            "Moscow, Russia"
        ]
        fractal_types = [
            "Sierpinski triangle",
            "Menger sponge",
            "Koch snowflake",
            "Mandelbrot set",
            "Lyapunov fractal",
            "Apollonian gasket"
        ]
        tasks = {}
        for i in range(2):
            city = random.choice(cities)
            fractal = random.choice(fractal_types)
            tasks[str(i+1)] = {"city": city, "fractal": fractal}
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a fractal-based urban planning system for {t['city']} using the {t['fractal']} as inspiration. Your task is to create a comprehensive proposal that addresses the following aspects:

1. Fractal System Design (300-350 words):
   a) Explain how you would adapt the {t['fractal']} to create an urban planning framework.
   b) Describe the key features of your fractal-based system and how they relate to urban planning principles.
   c) Discuss how your system scales from individual buildings to neighborhood and city-wide planning.
   d) Provide a visual description or diagram of your fractal urban plan.

2. Environmental Considerations (250-300 words):
   a) Analyze how your fractal-based system could improve environmental sustainability in {t['city']}.
   b) Discuss potential impacts on green spaces, energy efficiency, and resource management.
   c) Address any environmental challenges specific to {t['city']} and how your system might mitigate them.

3. Social and Economic Impact (250-300 words):
   a) Evaluate the potential social implications of implementing your fractal-based urban plan in {t['city']}.
   b) Discuss how the system might affect housing, transportation, and community spaces.
   c) Analyze potential economic benefits and challenges of implementing this system.

4. Implementation and Adaptation (200-250 words):
   a) Propose a phased approach for implementing your fractal-based urban plan in {t['city']}.
   b) Discuss how existing infrastructure could be adapted to fit your system.
   c) Address potential resistance or challenges to implementation and how they might be overcome.

5. Mathematical Analysis (200-250 words):
   a) Provide a mathematical description of how your fractal system scales and grows.
   b) Analyze the efficiency of your system in terms of space utilization and resource distribution.
   c) Discuss any novel mathematical properties or insights that emerge from your fractal urban plan.

6. Ethical Considerations and Future Prospects (200-250 words):
   a) Discuss ethical implications of implementing a fractal-based urban planning system.
   b) Address potential issues of equity and accessibility in your design.
   c) Speculate on how this approach to urban planning might evolve over time and influence future city development.

Ensure your response demonstrates a deep understanding of fractal mathematics, urban planning principles, and the specific context of {t['city']}. Be creative and innovative in your approach while considering practical constraints and ethical implications. Use clear headings for each section of your response.

Your total response should be between 1400-1700 words. Include relevant citations or references where appropriate."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the {t['fractal']} and its application to urban planning",
            f"The fractal-based urban plan is well-adapted to the specific context of {t['city']}",
            "The proposal addresses environmental, social, and economic factors comprehensively",
            "The mathematical analysis of the fractal system is sound and insightful",
            "The response shows creativity and innovation in urban planning approaches",
            "Ethical considerations and future implications are thoroughly discussed",
            "The overall response is well-structured, coherent, and within the specified word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
