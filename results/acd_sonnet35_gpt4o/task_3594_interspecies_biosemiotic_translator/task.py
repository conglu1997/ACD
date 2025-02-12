import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'species_pair': ('Humans', 'Dolphins'),
                'communication_context': 'Cooperative problem-solving in marine environments'
            },
            {
                'species_pair': ('Humans', 'Trees'),
                'communication_context': 'Forest ecosystem management and conservation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical system capable of interpreting and translating biological signals between {t['species_pair'][0]} and {t['species_pair'][1]}, focusing on the context of {t['communication_context']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your biosemiotic translation system.
   b) Explain how it incorporates principles from biosemiotics, information theory, and linguistics.
   c) Detail how the system processes and translates biological signals between the two species.
   d) Include a brief textual description of a diagram illustrating your system's architecture.

2. Signal Analysis and Interpretation (250-300 words):
   a) Explain how your system analyzes and interprets biological signals from each species.
   b) Describe any novel algorithms or methods used for signal processing and pattern recognition.
   c) Discuss how context and environmental factors are incorporated into the interpretation process.

3. Translation Mechanism (250-300 words):
   a) Detail the process by which your system translates signals from one species to the other.
   b) Explain how semantic and pragmatic aspects of communication are preserved across species.
   c) Discuss potential challenges in interspecies translation and how your system addresses them.

4. Application Scenario (200-250 words):
   a) Provide a specific example of how your system would facilitate communication between the two species in the given context.
   b) Explain the potential benefits and outcomes of this interspecies communication.
   c) Describe any limitations or potential misunderstandings that could arise.

5. Ethical Considerations (200-250 words):
   a) Discuss the ethical implications of enabling interspecies communication.
   b) Address concerns about potential misuse or unintended consequences of the technology.
   c) Propose guidelines for responsible development and use of interspecies communication systems.

6. Scientific and Philosophical Implications (200-250 words):
   a) Analyze how your system might advance our understanding of consciousness, intelligence, and communication.
   b) Discuss the potential impact on fields such as biology, cognitive science, and philosophy of mind.
   c) Consider how this technology might change our relationship with other species and the natural world.

7. Future Research Directions (100-150 words):
   a) Propose two novel research questions that arise from your system design.
   b) Suggest potential improvements or expansions to your system for future development.

Ensure your response demonstrates a deep understanding of biosemiotics, information theory, and interspecies communication. Be creative in your approach while maintaining scientific plausibility. Use appropriate terminology and provide clear explanations where necessary.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of biosemiotics, information theory, and linguistics.",
            "The proposed system architecture is innovative, well-explained, and scientifically plausible.",
            "The signal analysis and interpretation approach is clearly described and considers species-specific factors.",
            "The translation mechanism addresses the challenges of interspecies communication effectively.",
            "The application scenario is realistic and illustrates the system's potential clearly.",
            "Ethical considerations are thoroughly explored and addressed.",
            "The scientific and philosophical implications are insightful and well-reasoned.",
            "Future research directions are promising and well-justified.",
            "The overall response is creative, coherent, and demonstrates strong interdisciplinary knowledge integration."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
