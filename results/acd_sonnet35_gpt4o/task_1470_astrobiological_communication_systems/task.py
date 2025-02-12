import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        phenomena = [
            "Gravitational waves",
            "Neutrino emissions",
            "Quantum entanglement",
            "Dark matter interactions",
            "Cosmic rays"
        ]
        environments = [
            "Neutron star surface",
            "Gas giant atmosphere",
            "Rogue planet",
            "Binary star system",
            "Galactic core"
        ]
        return {
            str(i+1): {
                "phenomenon": random.choice(phenomena),
                "environment": random.choice(environments)
            } for i in range(2)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical alien communication system based on {t['phenomenon']} in the context of a {t['environment']}. Your response should include:

1. Physical Basis (200-250 words):
   a) Explain the chosen physical phenomenon and its relevance to the given environment.
   b) Describe how this phenomenon could be harnessed for communication.
   c) Discuss any unique properties or limitations of this communication method.

2. Biological Adaptations (200-250 words):
   a) Propose biological features that would allow aliens to generate and detect these signals.
   b) Explain how these adaptations would function in the given environment.
   c) Discuss any potential evolutionary pathways that could lead to these adaptations.

3. Information Encoding (200-250 words):
   a) Describe a method for encoding information using this physical phenomenon.
   b) Explain how this encoding method optimizes information transfer in the given context.
   c) Compare the theoretical information capacity of this system to conventional electromagnetic communication.

4. Communication Network (150-200 words):
   a) Propose a structure for a civilization-wide communication network using this system.
   b) Discuss how this network would overcome challenges posed by the environment.
   c) Explain any unique capabilities or limitations of this network compared to conventional systems.

5. Detection and Analysis (150-200 words):
   a) Describe how humans could potentially detect and analyze these alien communications.
   b) Propose a method for decoding or interpreting the information content.
   c) Discuss any challenges in distinguishing these signals from natural phenomena.

6. Implications and Speculations (150-200 words):
   a) Discuss how the existence of such a communication system would impact our search for extraterrestrial intelligence.
   b) Speculate on how this form of communication might influence the evolution and culture of the alien civilization.
   c) Propose a novel scientific or technological advancement that could result from studying this communication system.

Ensure your response demonstrates a deep understanding of astrophysics, biology, and information theory. Use appropriate scientific terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Begin each section with the heading (e.g., '1. Physical Basis:') on a new line, followed by your response for that section. Your total response should be between 1050-1350 words, with each section adhering to the specified word count range."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a detailed description of a communication system based on {t['phenomenon']} in a {t['environment']}",
            "The physical basis of the communication system is clearly explained, including its relevance to the environment",
            "Biological adaptations for generating and detecting the signals are proposed, with explanations of their function and evolution",
            "A method for encoding information using the physical phenomenon is described, including its optimization and comparison to conventional methods",
            "A civilization-wide communication network structure is proposed, addressing environmental challenges and comparing it to conventional systems",
            "Methods for human detection and analysis of the alien communications are discussed, including decoding and distinguishing from natural phenomena",
            "The implications for SETI and alien civilization development are considered, along with potential scientific advancements",
            "The response demonstrates creativity while maintaining scientific plausibility",
            "Appropriate scientific terminology is used throughout the response",
            "The response is properly formatted with clear headings for each section",
            "Each section adheres to the specified word count range, and the total response is between 1050-1350 words"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
