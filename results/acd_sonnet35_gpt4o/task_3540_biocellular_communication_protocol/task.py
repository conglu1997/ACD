import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        signaling_pathways = [
            "G protein-coupled receptor signaling",
            "Tyrosine kinase receptor signaling",
            "Ion channel receptor signaling",
            "Nuclear receptor signaling"
        ]
        networking_problems = [
            "Distributed consensus in unreliable networks",
            "Efficient routing in dynamic topologies",
            "Secure communication in adversarial environments",
            "Load balancing in heterogeneous systems"
        ]
        return {
            "1": {
                "signaling_pathway": random.choice(signaling_pathways),
                "networking_problem": random.choice(networking_problems)
            },
            "2": {
                "signaling_pathway": random.choice(signaling_pathways),
                "networking_problem": random.choice(networking_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication protocol inspired by the {t['signaling_pathway']} pathway, then apply it to solve the networking problem of {t['networking_problem']}. Your response should include the following sections:

1. Biological Basis (200-250 words):
   a) Explain the key components and mechanisms of the {t['signaling_pathway']} pathway.
   b) Discuss how this pathway facilitates efficient and reliable cellular communication.
   c) Identify specific features of this pathway that could be applicable to computer networking.

2. Protocol Design (250-300 words):
   a) Describe your bio-inspired communication protocol, detailing its main components and processes.
   b) Explain how your protocol translates biological mechanisms into networking concepts.
   c) Discuss any novel algorithms or data structures in your protocol.
   d) Provide a high-level diagram or flowchart of your protocol using ASCII art or clear textual description.

3. Application to Networking Problem (250-300 words):
   a) Analyze the challenge of {t['networking_problem']}.
   b) Explain how your bio-inspired protocol addresses this problem.
   c) Describe the specific advantages your approach offers over traditional solutions.
   d) Provide a step-by-step explanation of how your protocol would operate in this scenario.

4. Performance Analysis (200-250 words):
   a) Discuss the expected performance characteristics of your protocol.
   b) Compare your approach to existing solutions for {t['networking_problem']}.
   c) Identify potential limitations or trade-offs in your bio-inspired approach.
   d) Propose a method to empirically evaluate your protocol's effectiveness.

5. Broader Implications (150-200 words):
   a) Explore potential applications of your bio-inspired protocol beyond the given problem.
   b) Discuss how this approach might impact our understanding of both biological and artificial communication systems.
   c) Consider any ethical implications or potential misuses of your protocol.

6. Future Directions (100-150 words):
   a) Propose at least two ways to further develop or expand your bio-inspired networking approach.
   b) Suggest a research question that arises from your protocol design.

Ensure your response demonstrates a deep understanding of both cellular biology and computer networking principles. Use appropriate terminology from both fields and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific and technical plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed explanation of the {t['signaling_pathway']} pathway and its relevance to networking.",
            "The bio-inspired communication protocol should be clearly described with its main components and processes.",
            f"The application of the protocol to {t['networking_problem']} must be thoroughly explained.",
            "A performance analysis comparing the bio-inspired approach to existing solutions should be included.",
            "The response should discuss broader implications and future directions for the bio-inspired networking approach.",
            "The submission should demonstrate deep understanding of both cellular biology and computer networking principles.",
            "The response should be between 1150-1450 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
