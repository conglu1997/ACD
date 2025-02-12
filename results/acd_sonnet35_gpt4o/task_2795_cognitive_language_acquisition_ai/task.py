import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_domains = [
            "memory",
            "attention",
            "reasoning",
            "social cognition"
        ]
        language_aspects = [
            "phonology",
            "syntax",
            "semantics",
            "pragmatics"
        ]
        development_stages = [
            "infancy",
            "early childhood",
            "middle childhood",
            "adolescence"
        ]
        return {
            "1": {
                "cognitive_domain": random.choice(cognitive_domains),
                "language_aspect": random.choice(language_aspects),
                "development_stage": random.choice(development_stages)
            },
            "2": {
                "cognitive_domain": random.choice(cognitive_domains),
                "language_aspect": random.choice(language_aspects),
                "development_stage": random.choice(development_stages)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates human cognitive development and language acquisition from infancy to adulthood, focusing on the cognitive domain of {t['cognitive_domain']}, the language aspect of {t['language_aspect']}, and the development stage of {t['development_stage']}. Then, analyze its potential applications and ethical implications. Your response should include the following sections:

1. AI System Architecture (300-350 words):
   a) Describe the key components of your AI system for modeling cognitive development and language acquisition.
   b) Explain how your system incorporates principles from developmental psychology, cognitive science, and linguistics.
   c) Detail how your system simulates the interaction between cognitive development and language acquisition.
   d) Describe how your system models the specific cognitive domain and language aspect for the given development stage.
   e) Include a simple diagram or flowchart of your system architecture (using ASCII art or a clear textual description).

2. Cognitive and Language Development Model (250-300 words):
   a) Explain how your system models the development of {t['cognitive_domain']} and {t['language_aspect']} during {t['development_stage']}.
   b) Describe the key variables and parameters your model considers.
   c) Discuss how your model accounts for individual differences and environmental factors in development.
   d) Explain how your model simulates the interaction between cognitive and language development.
   e) Provide an example of how a specific cognitive or linguistic skill might develop in your simulation.

3. Simulation Results and Analysis (250-300 words):
   a) Present a high-level summary of the simulated development for the given cognitive domain and language aspect.
   b) Identify any emerging patterns or unexpected outcomes in your simulation.
   c) Compare your results with established theories or empirical data on cognitive and language development.
   d) Analyze any discrepancies between your simulation and real-world observations.
   e) Explain how your results might inform or challenge our understanding of real-world developmental processes.

4. Potential Applications (150-200 words):
   a) Propose two potential applications of your cognitive language acquisition AI in fields such as education, therapy, or artificial general intelligence.
   b) Explain how these applications could benefit society or advance our understanding of human development.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of using AI to model and simulate human cognitive and language development.
   b) Address potential concerns about privacy, consent, and the use of developmental data in AI training.
   c) Analyze the ethical implications of using such simulations to inform educational or clinical practices.
   d) Propose guidelines for the responsible development and use of cognitive language acquisition AI systems.

6. Limitations and Future Improvements (150-200 words):
   a) Identify the main limitations of your current system.
   b) Suggest two potential improvements or extensions to your cognitive language acquisition AI.
   c) Propose a research question that could be explored using an advanced version of your system.

Ensure your response demonstrates a deep understanding of cognitive science, linguistics, developmental psychology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a sophisticated understanding of cognitive development and language acquisition, particularly in the domain of {t['cognitive_domain']} and aspect of {t['language_aspect']} during {t['development_stage']}.",
            "The proposed AI system architecture is innovative and plausibly capable of simulating human cognitive and language development.",
            "The simulation results are critically analyzed and compared with established theories or empirical data, showing depth in understanding both AI and developmental theories.",
            "The potential applications and ethical implications are thoroughly addressed, showing awareness of both benefits and potential issues in using such AI systems.",
            "The response is well-structured, coherent, and within the specified word limit."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
