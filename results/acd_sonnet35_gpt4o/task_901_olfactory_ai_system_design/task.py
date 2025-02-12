import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {"domain": "Environmental Monitoring", "application": "Air Quality Assessment", "sample_odors": ["benzene", "formaldehyde", "ozone"]},
            {"domain": "Food Industry", "application": "Quality Control in Wine Production", "sample_odors": ["ethanol", "acetic acid", "vanillin"]},
            {"domain": "Medical Diagnostics", "application": "Disease Detection through Breath Analysis", "sample_odors": ["acetone", "ammonia", "nitric oxide"]},
            {"domain": "Forensic Science", "application": "Crime Scene Investigation", "sample_odors": ["chloroform", "gunpowder residue", "decomposition compounds"]},
            {"domain": "Cosmetics Industry", "application": "Perfume Formulation", "sample_odors": ["limonene", "linalool", "benzyl acetate"]}
        ]
        return {
            "1": random.choice(scenarios),
            "2": random.choice(scenarios)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system inspired by the human olfactory system to process and interpret complex odor data, then apply it to {t['domain']} for {t['application']}. You have 90 minutes to complete this task. Your response will be evaluated based on its completeness, accuracy, creativity, and adherence to the instructions. Each section contributes equally to your overall score. Your response should include the following sections:

1. Olfactory System Analysis (200-250 words):
   a) Describe the key components and processes of the human olfactory system.
   b) Explain how these elements contribute to odor perception and discrimination.
   c) Identify specific features that could be valuable for AI implementation.
   d) Include a simple diagram illustrating the olfactory pathway.

2. AI System Architecture (250-300 words):
   a) Design an AI architecture that mimics the human olfactory system.
   b) Explain how each component corresponds to biological counterparts.
   c) Describe the data processing flow in your system.
   d) Discuss any novel AI techniques or algorithms you've incorporated.
   e) Provide a flowchart or block diagram of your AI system.

3. Odor Data Representation (200-250 words):
   a) Propose a method for encoding complex odor data in your AI system.
   b) Explain how this representation captures the multidimensional nature of odors.
   c) Discuss how your system handles odor mixtures and intensity variations.
   d) Provide a mathematical or visual representation of your odor encoding method.

4. Application to {t['domain']} ({t['application']}) (250-300 words):
   a) Describe how your AI system would be applied to this specific scenario.
   b) Explain the potential benefits and challenges of using your system in this context.
   c) Provide an example of how the system would process and interpret the following odor samples: {', '.join(t['sample_odors'])}.
   d) Discuss any modifications needed to adapt your system to this application.

5. Performance Evaluation (200-250 words):
   a) Propose a method for evaluating your AI system's performance in odor processing and interpretation.
   b) Compare your system's capabilities to human olfactory performance.
   c) Suggest metrics for measuring accuracy, sensitivity, and discrimination in odor analysis.
   d) Design a hypothetical experiment to test your system's performance, including control groups and statistical analysis.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical concerns related to AI systems that can process and interpret odors.
   b) Explore the societal impacts of deploying such systems in various domains.
   c) Propose guidelines for responsible development and use of olfactory AI systems.
   d) Address potential privacy concerns related to odor data collection and analysis.

Ensure your response demonstrates a deep understanding of both neuroscience and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1250-1550 words.

Format your response with clear headings for each section. Include at least one diagram or visual representation in your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the human olfactory system and its relevance to AI design, including a clear diagram of the olfactory pathway.",
            "The AI system architecture is well-designed, plausibly mimics the human olfactory system, and is illustrated with a flowchart or block diagram.",
            "The proposed odor data representation method is innovative, captures the complexity of olfactory information, and includes a mathematical or visual representation.",
            f"The application to {t['domain']} for {t['application']} is well-explained, demonstrates practical understanding, and includes specific examples using the provided sample odors: {', '.join(t['sample_odors'])}.",
            "The performance evaluation method is appropriate, well-reasoned, and includes a detailed hypothetical experiment design.",
            "The discussion of ethical and societal implications is thoughtful, comprehensive, and addresses privacy concerns related to odor data.",
            "The overall solution is creative while maintaining scientific and technological plausibility.",
            "The response adheres to the specified word limit (1250-1550 words), uses clear headings for each section, and includes at least one diagram or visual representation."
        ]
        return float(sum([eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria]) / len(criteria))
