import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        exoplanets = [
            {
                "name": "Kepler-186f",
                "type": "Rocky super-Earth",
                "atmosphere": "Thin, possibly CO2-rich",
                "surface": "Potentially water and land",
                "star": "M-dwarf (red dwarf)"
            },
            {
                "name": "TRAPPIST-1e",
                "type": "Earth-sized rocky planet",
                "atmosphere": "Unknown, possibly hydrogen-rich",
                "surface": "Tidally locked, permanent day and night sides",
                "star": "Ultra-cool dwarf"
            },
            {
                "name": "HD 40307g",
                "type": "Super-Earth or mini-Neptune",
                "atmosphere": "Thick, possibly hydrogen and helium-rich",
                "surface": "Unknown, potentially no solid surface",
                "star": "K-type orange dwarf"
            }
        ]
        return {str(i+1): planet for i, planet in enumerate(random.sample(exoplanets, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a set of experiments to detect potential life on the exoplanet {t['name']}. Consider the planet's characteristics and the limitations of current technology. Your response should include:

1. Experimental Design (300-350 words):
   - Propose three distinct experiments to detect signs of life on {t['name']}.
   - For each experiment, describe the scientific principle it's based on, the type of data it would collect, and how it would be conducted.
   - Explain how each experiment takes into account the specific characteristics of {t['name']} (type, atmosphere, surface, star).

2. Technology and Instrumentation (200-250 words):
   - Describe the technology and instruments required for your experiments.
   - Discuss any modifications or innovations needed to adapt existing technology for use in the extreme conditions of space and on {t['name']}.

3. Data Analysis and Interpretation (200-250 words):
   - Explain how the data from each experiment would be analyzed.
   - Discuss potential challenges in interpreting the results and how you would address them.
   - Describe what would constitute a positive result for each experiment and why.

4. Limitations and Alternative Approaches (150-200 words):
   - Identify potential limitations of your proposed experiments.
   - Suggest alternative approaches or experiments that could complement or verify your results.

5. Ethical Considerations (100-150 words):
   - Discuss any ethical considerations related to the search for life on {t['name']}.
   - Address potential impacts of discovering (or not discovering) life on this exoplanet.

Ensure your response is well-structured, using clear headings for each section. Your experiments should be creative yet grounded in scientific principles, demonstrating a deep understanding of astrobiology, planetary science, and the challenges of space exploration. Use appropriate technical terminology and provide clear explanations for a scientifically literate audience."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must propose three distinct and scientifically plausible experiments to detect life on {t['name']}.",
            f"Each experiment should take into account the specific characteristics of {t['name']} as provided in the task description.",
            "The technology and instrumentation section should discuss realistic adaptations or innovations for space exploration.",
            "The data analysis and interpretation section must include a clear explanation of what would constitute a positive result for each experiment.",
            "The response should demonstrate a high level of interdisciplinary knowledge in astrobiology, planetary science, and related fields.",
            "The proposed experiments and analysis should be creative while remaining grounded in current scientific understanding.",
            "Ethical considerations related to the search for extraterrestrial life must be addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
