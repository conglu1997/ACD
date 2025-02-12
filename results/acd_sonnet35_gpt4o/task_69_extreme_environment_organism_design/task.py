import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "name": "Supercritical CO2 Ocean",
                "description": "A planet with oceans of supercritical carbon dioxide at 100 atmospheres of pressure and 100°C"
            },
            {
                "name": "Neutron Star Surface",
                "description": "The surface of a neutron star with extreme gravity (10^11 times Earth's) and intense magnetic fields"
            },
            {
                "name": "Plasma Storm",
                "description": "A gas giant's upper atmosphere with constant plasma storms and temperatures reaching 10,000°C"
            }
        ]
        return {str(i+1): env for i, env in enumerate(random.sample(environments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical organism adapted to survive in the following extreme environment:

Environment: {t['name']}
Description: {t['description']}

Your task is to:

1. Design an organism that could theoretically survive in this environment. Describe its key biological features and adaptations (4-5 sentences).

2. Explain how each of the organism's adaptations addresses a specific challenge posed by the environment (3-4 sentences).

3. Describe the organism's primary method of obtaining energy in this environment (2-3 sentences).

4. Propose a unique sensory or communication system this organism might use, considering the environmental constraints (2-3 sentences).

5. Discuss potential limitations or vulnerabilities of your designed organism (2-3 sentences).

6. Suggest how studying such an organism (if it existed) might advance our understanding of biology or contribute to technological innovations (2-3 sentences).

Ensure your response is creative yet grounded in scientific principles. Organize your answer using clear headings for each section. Your total response should not exceed 500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The organism must be specifically adapted to the {t['name']} environment",
            "The biological features and adaptations should be scientifically plausible and creative",
            "The response should clearly explain how adaptations address environmental challenges",
            "The energy acquisition method should be suitable for the given environment",
            "The proposed sensory or communication system should be unique and appropriate for the environment",
            "The discussion of limitations and potential scientific/technological contributions should be insightful",
            "The response should be well-organized with clear headings for each section",
            "The total response should not exceed 500 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
