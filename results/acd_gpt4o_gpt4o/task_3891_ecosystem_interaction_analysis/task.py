class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"scenario": "A tropical rainforest where deforestation is occurring rapidly. Explain how deforestation impacts the biodiversity, climate, and local human communities in this ecosystem."},
            "2": {"scenario": "A coral reef ecosystem experiencing bleaching events due to rising ocean temperatures. Explain the causes and consequences of coral bleaching on marine life and the broader oceanic environment."}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to analyze the given ecosystem scenario and explain the interactions within it. Ensure that your explanation is well-detailed, coherent, and includes specific observations that support your analysis. Use ecological terminology where appropriate. Provide your response in plain text format.\n\nScenario: {t['scenario']}\n\nResponse format:\n1. Biodiversity: [Detailed analysis of biodiversity impacts] (if applicable)\n2. Climate: [Detailed analysis of climate impacts] (if applicable)\n3. Human Communities: [Detailed analysis of impacts on local human communities] (if applicable)\n4. Causes: [Explanation of causes] (if applicable)\n5. Consequences: [Explanation of consequences] (if applicable)\n\nExample response:\nBiodiversity: Deforestation leads to habitat loss, which directly reduces species diversity. Many species are unable to adapt to the rapid changes and face extinction.\nClimate: The removal of trees reduces carbon sequestration, contributing to increased atmospheric CO2 levels and global warming.\nHuman Communities: Local communities dependent on the forest for resources and livelihood face economic and social challenges as their environment degrades.\nCauses: Deforestation is primarily caused by logging, agriculture, and urbanization.\nConsequences: The loss of biodiversity disrupts ecosystem services, affecting water cycles, soil fertility, and climate stability."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The explanation should be well-detailed and coherent.", "The explanation should include specific observations that support the analysis.", "The response should follow the specified format.", "The response should use appropriate ecological terminology."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
