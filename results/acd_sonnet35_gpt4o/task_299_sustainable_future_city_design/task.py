import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        challenges = [
            {
                "challenge": "rising sea levels",
                "location": "coastal region",
                "population": "2 million",
                "year": 2100
            },
            {
                "challenge": "extreme heat waves",
                "location": "desert area",
                "population": "1.5 million",
                "year": 2080
            }
        ]
        return {str(i+1): challenge for i, challenge in enumerate(challenges)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a sustainable city of the future that addresses the challenge of {t['challenge']} in a {t['location']} with a population of {t['population']} in the year {t['year']}. Your design should incorporate innovative solutions to environmental issues while ensuring a high quality of life for its inhabitants.

1. City Layout and Infrastructure (250-300 words):
   a) Describe the overall layout and key infrastructure elements of your city.
   b) Explain how the design addresses the specific environmental challenge.
   c) Discuss how the infrastructure supports sustainability and resilience.

2. Energy and Resource Management (200-250 words):
   a) Outline the city's energy production and distribution systems.
   b) Describe water management and conservation strategies.
   c) Explain waste management and recycling approaches.

3. Transportation and Mobility (200-250 words):
   a) Detail the city's transportation systems and networks.
   b) Discuss how the design promotes sustainable and efficient mobility.
   c) Explain any innovative transportation technologies incorporated.

4. Green Spaces and Biodiversity (150-200 words):
   a) Describe the integration of nature and green spaces in the city.
   b) Explain strategies for maintaining biodiversity.
   c) Discuss the benefits of these green elements for the inhabitants and the environment.

5. Social and Economic Considerations (200-250 words):
   a) Outline how the city design promotes social equity and community well-being.
   b) Describe the economic model that supports the city's sustainability.
   c) Discuss how the design accommodates future population growth or changes.

6. Technological Innovations (150-200 words):
   a) Describe two key technological innovations in your city design.
   b) Explain how these innovations contribute to sustainability and quality of life.
   c) Discuss any potential challenges in implementing these technologies.

Ensure your response demonstrates a deep understanding of urban planning, environmental science, and futuristic technologies. Use appropriate terminology and provide clear, logical explanations for your design choices. Be creative in your approach while maintaining scientific and practical plausibility."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The design must specifically address the challenge of {t['challenge']} in a {t['location']}.",
            "The response should cover all six required sections with appropriate detail.",
            "The city design must incorporate innovative and plausible solutions to environmental issues.",
            "The proposal should demonstrate interdisciplinary knowledge application, particularly in urban planning, environmental science, and technology.",
            "The design should balance sustainability with quality of life for the city's inhabitants.",
            "The response should be creative while maintaining scientific and practical plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
