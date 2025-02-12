import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        dream_themes = [
            "flying",
            "falling",
            "being chased",
            "teeth falling out",
            "being unprepared for an exam"
        ]
        brain_regions = [
            "amygdala",
            "hippocampus",
            "prefrontal cortex",
            "visual cortex",
            "thalamus"
        ]
        cultures = [
            "Western",
            "East Asian",
            "African",
            "Middle Eastern",
            "Indigenous Australian"
        ]
        return {
            "1": {
                "dream_theme": random.choice(dream_themes),
                "brain_region": random.choice(brain_regions),
                "culture1": random.choice(cultures),
                "culture2": random.choice([c for c in cultures if c != "culture1"])
            },
            "2": {
                "dream_theme": random.choice(dream_themes),
                "brain_region": random.choice(brain_regions),
                "culture1": random.choice(cultures),
                "culture2": random.choice([c for c in cultures if c != "culture1"])
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that interprets and analyzes dreams based on neurolinguistic patterns (recurring language structures and metaphors in dream descriptions) and cultural symbolism, then use it to generate insights about cognitive processes. Your system should focus on the dream theme of {t['dream_theme']}, emphasize neural activity in the {t['brain_region']}, and compare interpretations between {t['culture1']} and {t['culture2']} cultures. For example, a snake in a dream might symbolize wisdom in one culture but danger in another. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI dream analysis system.
   b) Explain how it incorporates neurolinguistic patterns and cultural symbolism.
   c) Detail how the system accounts for the specified brain region's activity.
   d) Discuss any novel approaches or algorithms used in your design.
   e) Include a high-level diagram or flowchart of your system (describe it textually).

2. Dream Interpretation Process (250-300 words):
   a) Provide a step-by-step explanation of how your system interprets a dream with the given theme.
   b) Explain how neurolinguistic patterns are identified and analyzed.
   c) Describe how cultural symbolism is integrated into the interpretation.
   d) Discuss how your system handles ambiguity or conflicting interpretations.

3. Cross-Cultural Analysis (200-250 words):
   a) Compare and contrast how the specified dream theme might be interpreted in the two given cultures.
   b) Explain how your system accounts for these cultural differences.
   c) Discuss any challenges in maintaining cultural sensitivity and accuracy.

4. Cognitive Process Insights (200-250 words):
   a) Describe the types of insights about cognitive processes your system can generate.
   b) Explain how these insights are derived from the dream analysis.
   c) Discuss the potential implications of these insights for our understanding of the human mind.

5. Case Study (200-250 words):
   a) Present a hypothetical dream scenario related to the given theme.
   b) Walk through your system's analysis and interpretation of this dream.
   c) Compare the results between the two specified cultures.
   d) Discuss any insights about cognitive processes generated from this analysis.

6. Ethical Considerations and Limitations (150-200 words):
   a) Identify potential ethical issues related to AI-based dream analysis.
   b) Discuss how your system addresses privacy concerns and cultural sensitivities.
   c) Explain the limitations of your system and areas for future improvement.

Ensure your response demonstrates a deep understanding of neuroscience, linguistics, artificial intelligence, and cultural anthropology. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section and use subheadings (a, b, c, d) as specified above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of neuroscience, linguistics, AI, and cultural anthropology.",
            "The system design effectively integrates neurolinguistic patterns and cultural symbolism.",
            f"The system appropriately focuses on the dream theme of {t['dream_theme']} and neural activity in the {t['brain_region']}.",
            f"The cross-cultural analysis effectively compares interpretations between {t['culture1']} and {t['culture2']} cultures.",
            "The case study presents a plausible dream scenario and a thorough analysis using the proposed system.",
            "The response addresses ethical considerations and limitations of AI-based dream analysis.",
            "The writing is clear, well-structured, and adheres to the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
