import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_challenges = [
            "traffic congestion",
            "air pollution",
            "social isolation",
            "mental health",
            "resource scarcity"
        ]
        biotech_approaches = [
            "engineered microorganisms",
            "synthetic plant systems",
            "bio-responsive materials",
            "gene-edited urban fauna",
            "bioremediation networks"
        ]
        psychological_factors = [
            "collective stress levels",
            "community cohesion",
            "individual well-being",
            "cultural identity",
            "social equity"
        ]
        return {
            "1": {
                "urban_challenge": random.choice(urban_challenges),
                "biotech_approach": random.choice(biotech_approaches),
                "psychological_factor": random.choice(psychological_factors)
            },
            "2": {
                "urban_challenge": random.choice(urban_challenges),
                "biotech_approach": random.choice(biotech_approaches),
                "psychological_factor": random.choice(psychological_factors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a bioadaptive urban system that addresses the urban challenge of {t['urban_challenge']} using {t['biotech_approach']} while considering the psychological factor of {t['psychological_factor']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your bioadaptive urban system.
   b) Explain how it integrates synthetic biology, urban planning, and social psychology.
   c) Detail how the system responds to and modifies the urban environment.
   d) Include a high-level diagram or pseudocode illustrating the system's architecture.

2. Biotechnology Integration (250-300 words):
   a) Explain how {t['biotech_approach']} is used to address {t['urban_challenge']}.
   b) Describe the biological mechanisms involved in sensing and responding to urban conditions.
   c) Discuss any potential risks or challenges in implementing this biotechnology in an urban setting.

3. Psychological Impact Analysis (200-250 words):
   a) Analyze how your system affects {t['psychological_factor']}.
   b) Describe the methods used to measure and monitor psychological states of city inhabitants.
   c) Explain how the system adapts its responses based on psychological data.

4. Urban Planning Implications (200-250 words):
   a) Discuss how your bioadaptive system influences traditional urban planning approaches.
   b) Describe any necessary changes to city infrastructure to support your system.
   c) Explain how your system promotes sustainable urban development.

5. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to your bioadaptive urban system.
   b) Discuss issues of privacy, consent, and individual autonomy.
   c) Propose guidelines for responsible development and use of such technology.

6. Future Scenarios and Adaptability (200-250 words):
   a) Describe two potential future scenarios where your system would need to adapt.
   b) Explain how your bioadaptive urban system would evolve to meet changing needs.
   c) Discuss the long-term implications of your system for urban development and human society.

7. Code Snippet (50-100 words + code):
   Provide a brief Python code snippet or pseudocode (10-20 lines) that illustrates a key aspect of your bioadaptive system, such as data processing or decision-making. Explain what the code does and how it relates to your overall system design.

Ensure your response demonstrates a deep understanding of synthetic biology, urban planning principles, and social psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Include at least 5 references to relevant scientific literature to support your proposed system design. Use in-text citations in the format (Author, Year) and provide a brief bibliography at the end of your response.

Format your response with clear headings for each section. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of synthetic biology, urban planning, and social psychology, using appropriate terminology from all fields.",
            f"The bioadaptive urban system effectively addresses the specified urban challenge ({t['urban_challenge']}) using the given biotech approach ({t['biotech_approach']}) while considering the psychological factor ({t['psychological_factor']}).",
            "The system design is innovative, scientifically plausible, and thoroughly explained.",
            "The response addresses all required sections with appropriate depth and insight.",
            "The proposed system shows a clear integration of biotechnology, urban planning, and social psychology in a novel and coherent manner.",
            "The response includes at least 5 relevant scientific references and a code snippet or pseudocode as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
