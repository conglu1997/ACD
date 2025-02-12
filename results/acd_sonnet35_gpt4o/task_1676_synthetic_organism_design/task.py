import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'environmental_challenge': 'Plastic pollution in oceans',
                'genetic_source': 'Extremophile bacteria',
                'novel_capability': 'Rapid plastic decomposition'
            },
            {
                'environmental_challenge': 'Atmospheric carbon dioxide levels',
                'genetic_source': 'Photosynthetic algae',
                'novel_capability': 'Enhanced CO2 sequestration'
            },
            {
                'environmental_challenge': 'Soil contamination with heavy metals',
                'genetic_source': 'Hyperaccumulator plants',
                'novel_capability': 'Accelerated phytoremediation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system for creating synthetic organisms with novel capabilities, then use it to propose a specific organism for environmental remediation. Use the following specifications:

Environmental Challenge: {t['environmental_challenge']}
Genetic Source: {t['genetic_source']}
Novel Capability: {t['novel_capability']}

Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the main components of your AI system for synthetic organism design.
   b) Explain how your system integrates genetic databases, metabolic pathway modeling, and evolutionary algorithms.
   c) Detail any novel features that make your system particularly suited for designing organisms with the specified novel capability.
   d) Optionally, include a simple diagram or ASCII representation of your system architecture.

2. Synthetic Organism Design Process (200-250 words):
   a) Outline the step-by-step process your AI system would follow to design the synthetic organism.
   b) Explain how your system would incorporate the genetic source material and engineer the novel capability.
   c) Describe any computational models or simulations used to predict the organism's behavior and environmental impact.

3. Proposed Synthetic Organism (250-300 words):
   a) Describe the key features and capabilities of your proposed synthetic organism.
   b) Explain how it addresses the specified environmental challenge.
   c) Discuss any potential risks or unintended consequences associated with releasing this organism into the environment.
   d) Propose safety measures or genetic safeguards to mitigate these risks.

4. Ethical and Regulatory Considerations (200-250 words):
   a) Discuss the ethical implications of creating and releasing synthetic organisms for environmental remediation.
   b) Propose a framework for assessing the risks and benefits of such organisms.
   c) Suggest regulatory guidelines for the development, testing, and deployment of synthetic organisms.

5. Future Directions and Societal Impact (150-200 words):
   a) Speculate on potential future applications of your AI system beyond environmental remediation.
   b) Discuss how widespread use of synthetic organisms might impact society and the environment in the long term.
   c) Propose areas of research or technological development that could enhance the safety and efficacy of synthetic organism design.

Ensure your response demonstrates a deep understanding of genetic engineering, artificial intelligence, and environmental science. Be innovative in your approach while maintaining scientific plausibility and addressing ethical concerns. Use appropriate terminology from all relevant fields and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above (1, 2, 3, 4, 5). Begin each section with the heading on a new line, followed by your response for that section. Maintain scientific accuracy and ethical considerations throughout your response.

Your total response should be between 1050-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of genetic engineering, artificial intelligence, and environmental science.",
            "The AI system architecture is well-designed and clearly explained, with a focus on integrating genetic databases, metabolic pathway modeling, and evolutionary algorithms.",
            "The synthetic organism design process is logically outlined and incorporates the specified genetic source and novel capability.",
            "The proposed synthetic organism is described in detail, addressing the environmental challenge while considering potential risks and safety measures.",
            "Ethical and regulatory considerations are thoroughly discussed, with a proposed framework for risk assessment and suggested guidelines.",
            "Future directions and societal impacts are thoughtfully explored, demonstrating foresight and critical thinking.",
            "The response is innovative while maintaining scientific plausibility and addressing ethical concerns.",
            "Appropriate terminology is used throughout, with clear explanations provided where necessary.",
            "The response is well-formatted with clear headings and falls within the specified word count range."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
