import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        species = ['Homo sapiens', 'Canis lupus familiaris', 'Apis mellifera', 'Zea mays']
        genetic_modifications = [
            'Enhanced intelligence',
            'Increased lifespan',
            'Disease resistance',
            'Environmental adaptation'
        ]
        ecological_contexts = [
            'Urban environment',
            'Agricultural ecosystem',
            'Marine ecosystem',
            'Tropical rainforest'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'species': random.choice(species),
                'genetic_modification': random.choice(genetic_modifications),
                'ecological_context': random.choice(ecological_contexts)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can simulate and analyze the ethical implications of genetic engineering across different species, with a focus on long-term ecological and evolutionary consequences. Apply your system to the following scenario:

Species: {t['species']}
Genetic Modification: {t['genetic_modification']}
Ecological Context: {t['ecological_context']}

Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for simulating and analyzing genetic modifications.
   b) Explain how your system integrates genetic, ecological, and ethical models.
   c) Discuss any novel AI techniques or algorithms used in your system.
   d) Include a high-level diagram or flowchart of your AI system's architecture.

2. Genetic Modification Simulation (250-300 words):
   a) Explain how your AI system simulates the given genetic modification in the specified species.
   b) Describe the key parameters and variables considered in the simulation.
   c) Discuss how your system accounts for genetic interactions and epigenetic factors.

3. Ecological Impact Analysis (250-300 words):
   a) Detail how your AI system models the long-term ecological consequences of the genetic modification.
   b) Explain how it considers interactions with other species in the given ecological context.
   c) Describe any predictive models used for long-term evolutionary impacts.

4. Ethical Implications Assessment (300-350 words):
   a) Explain how your AI system evaluates the ethical implications of the genetic modification.
   b) Discuss the ethical frameworks or principles incorporated into your system.
   c) Describe how your system balances potential benefits against risks and ethical concerns.
   d) Provide a sample ethical analysis output from your AI system for this scenario.

5. Uncertainty and Limitations (200-250 words):
   a) Discuss how your AI system accounts for uncertainties in genetic engineering and ecological modeling.
   b) Explain any limitations of your approach and potential areas for improvement.
   c) Propose methods for validating and refining your AI system's predictions and ethical assessments.

6. Societal and Policy Implications (200-250 words):
   a) Analyze how your AI system could inform policy decisions on genetic engineering.
   b) Discuss potential societal impacts of using AI for ethical assessment of genetic modifications.
   c) Propose guidelines for the responsible use of your AI system in real-world scenarios.

Ensure your response demonstrates a deep understanding of artificial intelligence, genetics, ecology, and ethics. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility and ethical rigor.

Format your response with clear headings for each section and use bullet points or numbered lists where appropriate. Your total response should be between 1500-1800 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections comprehensively",
            "The AI system design demonstrates innovation and interdisciplinary integration",
            "The genetic modification simulation and ecological impact analysis are scientifically sound",
            "The ethical implications assessment shows depth of reasoning and consideration of multiple perspectives",
            "The response acknowledges uncertainties and limitations appropriately",
            "The discussion of societal and policy implications is thoughtful and well-reasoned",
            "The overall response demonstrates a high level of expertise across AI, genetics, ecology, and ethics"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
