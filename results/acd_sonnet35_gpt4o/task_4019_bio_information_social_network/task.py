import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'biological_basis': 'DNA-based computation',
                'network_structure': 'Small-world network',
                'information_processing': 'Distributed consensus mechanisms',
                'societal_application': 'Global decision-making system'
            },
            {
                'biological_basis': 'Protein-based signaling',
                'network_structure': 'Scale-free network',
                'information_processing': 'Swarm intelligence algorithms',
                'societal_application': 'Adaptive resource allocation'
            }
        ]
        return {str(i+1): scenario for i, scenario in enumerate(scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical biological information processing system inspired by social networks, based on the following scenario:

Biological basis: {t['biological_basis']}
Network structure: {t['network_structure']}
Information processing mechanism: {t['information_processing']}
Potential societal application: {t['societal_application']}

Your response should include the following sections:

1. System Design (300-350 words):
   a) Describe the key components of your bio-information social network.
   b) Explain how the biological basis is utilized for information processing.
   c) Detail how the network structure influences information flow and processing.
   d) Discuss how the specified information processing mechanism is implemented.
   e) Include a diagram using ASCII art or Unicode characters (max 20 lines x 80 characters) illustrating the system architecture or a key process.
   f) Provide a pseudocode snippet (5-10 lines) demonstrating a core algorithm or process in your system.

2. Biological Feasibility (200-250 words):
   a) Analyze the biological plausibility of your system.
   b) Discuss any challenges in implementing this system using current biotechnology.
   c) Propose potential solutions or future advancements needed to realize this system.
   d) Provide a concrete example of a similar biological process or system in nature.

3. Information Theory Analysis (200-250 words):
   a) Explain how information is encoded, transmitted, and processed in your system.
   b) Discuss the efficiency and robustness of your system from an information theory perspective.
   c) Compare your system's information processing capabilities to existing biological or technological systems.
   d) Reference at least one relevant information theory concept or principle.

4. Social Network Parallels (200-250 words):
   a) Draw parallels between your bio-information system and human social networks.
   b) Analyze how principles from social network theory apply to your system.
   c) Discuss any novel insights your system provides about social network dynamics.
   d) Provide a specific scenario illustrating how your system mimics or improves upon a social network phenomenon.

5. Societal Application (250-300 words):
   a) Describe in detail how your system could be applied to {t['societal_application']}.
   b) Analyze the potential benefits and risks of implementing this system in society.
   c) Discuss any ethical considerations related to the use of this technology.
   d) Propose guidelines for responsible development and deployment of such systems.
   e) Provide a hypothetical case study demonstrating the system's application and impact.

6. Future Implications (150-200 words):
   a) Speculate on how this technology might evolve over the next 50 years.
   b) Discuss potential long-term impacts on society, culture, and human evolution.
   c) Propose two potential research directions that could emerge from this work.
   d) Reference at least one relevant scientific theory or concept in your speculation.

Ensure your response demonstrates a deep understanding of biology, information theory, network science, and social systems. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Strictly adhere to the word count for each section. Your total response should be between 1300-1600 words. Cite at least three relevant scientific sources or theories throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['biological_basis']}, {t['network_structure']}, and {t['information_processing']}.",
            f"The proposed system effectively integrates principles from biology, information theory, and social network science.",
            f"The societal application of {t['societal_application']} is thoroughly explored, including potential benefits, risks, and ethical considerations.",
            "The response includes a clear diagram using ASCII art or Unicode characters and a pseudocode snippet as requested.",
            "The biological feasibility of the system is critically analyzed, with challenges and potential solutions discussed.",
            "The information theory analysis demonstrates a solid understanding of information encoding, transmission, and processing.",
            "The response draws meaningful parallels between the proposed system and human social networks.",
            "Future implications and research directions are thoughtfully considered and plausible.",
            "The response is well-structured, clear, and strictly adheres to the specified word count for each section and overall.",
            "At least three relevant scientific sources or theories are cited throughout the response.",
            "Concrete examples, scenarios, or case studies are provided to illustrate key points in each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
