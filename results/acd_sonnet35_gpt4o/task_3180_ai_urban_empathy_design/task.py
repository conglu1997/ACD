import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        urban_challenges = [
            "reducing social isolation in high-density areas",
            "improving cross-cultural understanding in diverse neighborhoods",
            "enhancing community engagement in urban renewal projects",
            "mitigating the psychological impact of gentrification",
            "fostering intergenerational connections in age-diverse communities"
        ]
        urban_elements = [
            "public spaces",
            "transportation systems",
            "housing layouts",
            "community centers",
            "green areas"
        ]
        psychological_factors = [
            "social identity theory",
            "environmental psychology",
            "intergroup contact theory",
            "place attachment",
            "collective efficacy"
        ]
        
        return {
            "1": {
                "challenge": random.choice(urban_challenges),
                "urban_element": random.choice(urban_elements),
                "psych_factor": random.choice(psychological_factors)
            },
            "2": {
                "challenge": random.choice(urban_challenges),
                "urban_element": random.choice(urban_elements),
                "psych_factor": random.choice(psychological_factors)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that analyzes urban environments and human behavior to optimize city layouts for increased empathy and social cohesion, then apply it to solve the specific urban challenge of {t['challenge']}. Your system should focus on the urban element of {t['urban_element']} and incorporate the psychological factor of {t['psych_factor']}. Your response should include:

1. AI System Architecture (250-300 words):
   a) Describe the key components of your AI system for urban empathy design.
   b) Explain how it integrates data from urban environments, human behavior, and social interactions.
   c) Detail how the system incorporates the specified psychological factor.
   d) Discuss any novel AI techniques or algorithms used in your design.

2. Data Collection and Analysis (200-250 words):
   a) Outline the types of data your system would collect and analyze.
   b) Explain how you would ensure privacy and ethical data usage.
   c) Describe how your system would process and interpret this data to inform urban design decisions.
   d) Discuss how you would validate the accuracy and relevance of the insights generated.

3. Urban Design Optimization (250-300 words):
   a) Explain how your AI system would optimize the specified urban element to address the given challenge.
   b) Provide specific examples of design recommendations your system might generate.
   c) Describe how these optimizations would promote empathy and social cohesion.
   d) Discuss potential trade-offs or conflicting priorities in your design approach.

4. Implementation and Impact Assessment (200-250 words):
   a) Propose a method for implementing your AI-generated design recommendations in real urban environments.
   b) Describe how you would measure the impact of these changes on empathy and social cohesion.
   c) Discuss potential challenges in implementation and how you would address them.
   d) Explain how your system would continuously learn and adapt based on observed outcomes.

5. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues or unintended consequences of using AI for urban empathy design.
   b) Discuss how your system would address issues of bias, equity, and cultural sensitivity.
   c) Explain limitations of your approach and areas for future improvement.

6. Broader Implications (100-150 words):
   a) Discuss how your AI urban empathy design system could impact urban planning practices and policies.
   b) Speculate on potential long-term effects on society if such systems become widely adopted.
   c) Propose future research directions in the intersection of AI, urban design, and social psychology.

Ensure your response demonstrates a deep understanding of AI, urban planning, and social psychology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of AI, urban planning, and social psychology.",
            "The AI system design is innovative and well-explained, with clear integration of the specified urban element and psychological factor.",
            "The proposed solution effectively addresses the given urban challenge while promoting empathy and social cohesion.",
            "The response considers ethical implications, limitations, and future directions of AI-driven urban design.",
            "The submission is well-structured, within the specified word count, and uses appropriate technical terminology."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
