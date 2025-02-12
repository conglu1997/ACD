import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "organism": "Termite mounds",
                "challenge": "Energy-efficient climate control in buildings"
            },
            {
                "organism": "Lotus leaf",
                "challenge": "Water management and flood prevention"
            },
            {
                "organism": "Mycorrhizal networks",
                "challenge": "Efficient resource distribution in urban areas"
            },
            {
                "organism": "Coral reefs",
                "challenge": "Resilient coastal urban development"
            }
        ]
        return {
            "1": random.choice(challenges),
            "2": random.choice(challenges)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze an urban system or structure inspired by {t['organism']}, addressing the urban sustainability challenge of {t['challenge']}. Your response should include:

1. Biological Analysis (200-250 words):
   a) Describe the key features and functions of {t['organism']}.
   b) Explain how these features contribute to the organism's survival or efficiency.
   c) Identify specific mechanisms or principles that could be applicable to urban design.

2. Urban System Design (250-300 words):
   a) Propose an urban system or structure inspired by {t['organism']}.
   b) Describe its key components and how they mimic or adapt the biological features.
   c) Explain how your design addresses {t['challenge']}.
   d) Include a basic schematic or diagram of your design (describe it textually).

3. Implementation Analysis (200-250 words):
   a) Discuss the potential benefits of your biomimetic design compared to conventional approaches.
   b) Identify possible challenges in implementing your design and propose solutions.
   c) Describe how your design might be scaled or adapted for different urban contexts.

4. Sustainability Impact (150-200 words):
   a) Analyze the potential environmental impacts of your design.
   b) Discuss how it contributes to urban sustainability beyond addressing the primary challenge.
   c) Identify any potential negative consequences and how they might be mitigated.

5. Interdisciplinary Connections (100-150 words):
   a) Explain how your design integrates knowledge from biology, engineering, and urban planning.
   b) Discuss how this interdisciplinary approach enhances the solution's effectiveness.

6. Future Developments (100-150 words):
   a) Propose potential future research or innovations that could further enhance your biomimetic urban design.
   b) Speculate on how this approach might influence urban planning and sustainability practices in the next 50 years.

Ensure your response demonstrates a deep understanding of biological principles, urban planning concepts, and sustainability issues. Be creative in your design while maintaining scientific plausibility and addressing potential limitations or challenges.

Format your response with clear headings for each section. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response accurately describes the key features and functions of {t['organism']} and their relevance to urban design.",
            f"The proposed urban system or structure clearly addresses {t['challenge']} through biomimetic design.",
            "The design demonstrates creative problem-solving and interdisciplinary knowledge application.",
            "The implementation analysis and sustainability impact assessment are thorough and well-reasoned.",
            "The response shows a deep understanding of biological principles, urban planning concepts, and sustainability issues.",
            "The future developments section provides insightful speculation on the long-term implications of the biomimetic approach."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
