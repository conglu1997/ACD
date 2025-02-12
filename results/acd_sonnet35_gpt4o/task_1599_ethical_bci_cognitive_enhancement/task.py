import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cognitive_functions = [
            "working memory",
            "attention control",
            "language processing",
            "decision making",
            "emotional regulation"
        ]
        target_populations = [
            "elderly individuals with cognitive decline",
            "children with learning disabilities",
            "adults with ADHD",
            "individuals with depression",
            "professionals in high-stress occupations"
        ]
        return {
            "1": {
                "cognitive_function": random.choice(cognitive_functions),
                "target_population": random.choice(target_populations)
            },
            "2": {
                "cognitive_function": random.choice(cognitive_functions),
                "target_population": random.choice(target_populations)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a brain-computer interface (BCI) system to enhance {t['cognitive_function']} for {t['target_population']}, and analyze its ethical implications and societal impact. A BCI is a direct communication pathway between the brain and an external device, allowing for the translation of neural signals into commands or the stimulation of specific brain regions.

Your response should include the following sections, with the specified word count for each:

1. BCI System Design (300-350 words):
   a) Describe the key components and functionality of your BCI system.
   b) Explain how it interfaces with the brain to enhance the specified cognitive function.
   c) Discuss any novel technologies or approaches incorporated in your design.
   d) Include a diagram or schematic representation of your BCI system (describe it textually).

2. Neuroscientific Basis (200-250 words):
   a) Explain the neuroscientific principles underlying your BCI system's approach to cognitive enhancement.
   b) Discuss how your system accounts for neural plasticity and long-term effects on brain function.
   c) Address any potential risks or side effects on brain health and function.
   d) Cite at least one relevant scientific study or paper to support your design or approach.

3. Ethical Analysis (250-300 words):
   a) Identify and analyze at least three ethical concerns raised by your BCI system.
   b) Discuss how these concerns might be addressed or mitigated in the system's design and implementation.
   c) Consider the broader implications for human autonomy, identity, and social equality.
   d) Cite at least one relevant ethical framework or philosophical perspective in your analysis.

4. Societal Impact (200-250 words):
   a) Analyze the potential benefits and risks of widespread adoption of your BCI system for the target population.
   b) Discuss how it might affect social dynamics, education, or workplace environments.
   c) Consider potential misuse scenarios and propose safeguards against them.
   d) Discuss potential cultural or societal differences in the acceptance and implementation of your BCI system.

5. Regulatory Framework (150-200 words):
   a) Propose guidelines for the responsible development, testing, and deployment of cognitive enhancement BCIs.
   b) Suggest how existing regulatory bodies might adapt to oversee this technology.
   c) Discuss the challenges in creating international standards for BCI regulation.

6. Future Research Directions (150-200 words):
   a) Propose two potential areas for future research based on your BCI system.
   b) Explain how these research directions could contribute to our understanding of brain function or AI-brain interfaces.
   c) Discuss any long-term implications for human evolution or the future of human-AI interaction.

Ensure your response demonstrates a deep understanding of neuroscience, artificial intelligence, and bioethics. Use technical terminology appropriately and provide explanations where necessary. Be creative in your approach while maintaining scientific plausibility and ethical responsibility.

Important notes:
- You must cite at least one scientific study or paper in the Neuroscientific Basis section and at least one ethical framework or philosophical perspective in the Ethical Analysis section.
- Format your response with clear headings for each section.
- Adhere to the specified word count for each section.
- Your total response should be between 1250-1550 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The BCI system must be designed to enhance {t['cognitive_function']} for {t['target_population']}.",
            "The response must include a clear description of the BCI system's components and functionality.",
            "The neuroscientific basis of the BCI system must be explained, including considerations of neural plasticity and potential risks.",
            "At least one relevant scientific study or paper must be cited to support the design or approach in the Neuroscientific Basis section.",
            "At least three ethical concerns must be identified and analyzed, with citation of at least one ethical framework or philosophical perspective in the Ethical Analysis section.",
            "The societal impact of widespread adoption of the BCI system must be discussed, including benefits, risks, and potential misuse scenarios.",
            "Potential cultural or societal differences in the acceptance and implementation of the BCI system must be considered.",
            "A regulatory framework for BCI development and deployment must be proposed.",
            "Two future research directions must be suggested, with explanations of their potential contributions.",
            "The response must demonstrate understanding of neuroscience, artificial intelligence, and bioethics.",
            "The response must be formatted with clear headings for each section and be between 1250-1550 words."
        ]
        return float(eval_with_llm_judge(instructions, submission, criteria))
