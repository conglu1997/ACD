class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        import random

        environments = [
            "low-gravity gas giant moon",
            "tidally-locked planet orbiting a red dwarf star",
            "underground cavern system on a rogue planet",
            "methane ocean world",
            "planet with a highly elliptical orbit causing extreme seasonal changes"
        ]

        energy_sources = [
            "bioluminescent radiation",
            "geothermal vents",
            "exotic particle emissions",
            "crystallized time",
            "quantum fluctuations"
        ]

        tasks = [
            {
                "environment": random.choice(environments),
                "energy_source": random.choice(energy_sources)
            } for _ in range(2)
        ]

        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an ecosystem of imaginary lifeforms on a fictional planet with the following characteristics:

        Environment: {t['environment']}
        Primary energy source: {t['energy_source']}

        Your task has the following parts:

        1. Ecosystem Overview (200-250 words):
           a) Describe the general characteristics of your imaginary ecosystem.
           b) Explain how the environment and energy source influence the ecosystem's development.
           c) Outline the main ecological niches present in your ecosystem.

        2. Dominant Lifeform Design (250-300 words):
           a) Create a detailed description of the dominant lifeform in your ecosystem.
           b) Explain its biological adaptations to the environment and energy source.
           c) Describe its life cycle, reproductive strategy, and role in the ecosystem.
           d) Include a simple diagram or sketch of this lifeform (described in words).

        3. Ecological Interactions (200-250 words):
           a) Describe at least two other lifeforms in your ecosystem and their relationships with the dominant lifeform.
           b) Explain a unique symbiotic relationship present in your ecosystem.
           c) Discuss how energy flows through your ecosystem's food web.

        4. Evolutionary History (150-200 words):
           a) Propose a plausible evolutionary history for your ecosystem.
           b) Explain how key adaptations might have developed over time.
           c) Discuss any potential future evolutionary trends.

        5. Scientific Analysis (200-250 words):
           a) Analyze the scientific plausibility of your imaginary ecosystem.
           b) Discuss any principles from Earth's biology that you've extrapolated or modified.
           c) Propose a hypothesis about your ecosystem that future explorers could test.

        6. Potential Applications (100-150 words):
           a) Suggest two potential scientific or technological applications inspired by your imaginary ecosystem.
           b) Briefly explain how these applications could benefit human society.

        Ensure your response demonstrates creativity in designing a coherent and unique ecosystem while maintaining scientific plausibility. Use appropriate terminology from biology, ecology, and related fields. Your total response should be between 1100-1400 words.
        """

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates creativity in designing a unique and coherent ecosystem.",
            "The ecosystem and lifeforms are scientifically plausible and consistent with the given environment and energy source.",
            "The response shows a deep understanding of biological and ecological principles, extrapolating from Earth's science.",
            "The evolutionary history and future trends are logically explained and consistent with the ecosystem design.",
            "The proposed scientific applications are innovative and well-connected to the imaginary ecosystem.",
            "The response is well-structured, comprehensive, and adheres to the word count guidelines for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
