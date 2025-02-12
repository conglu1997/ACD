import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        musical_traditions = [
            "Western classical",
            "Indian classical (Hindustani)",
            "Chinese traditional",
            "West African",
            "Arabic maqam",
            "Japanese gagaku",
            "Javanese gamelan"
        ]
        musical_elements = [
            "rhythm and meter",
            "melody and scale systems",
            "harmony and tonality",
            "form and structure",
            "instrumentation and timbre"
        ]
        fusion_themes = [
            "nature and seasons",
            "urban life",
            "spiritual journey",
            "cultural exchange",
            "technological progress"
        ]
        return {
            "1": {
                "tradition1": random.choice(musical_traditions),
                "tradition2": random.choice(musical_traditions),
                "musical_element": random.choice(musical_elements),
                "fusion_theme": random.choice(fusion_themes)
            },
            "2": {
                "tradition1": random.choice(musical_traditions),
                "tradition2": random.choice(musical_traditions),
                "musical_element": random.choice(musical_elements),
                "fusion_theme": random.choice(fusion_themes)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""As a music theorist and composer, your task is to analyze, compare, and creatively fuse elements from different musical traditions. Focus on the musical element of {t['musical_element']} in the context of {t['tradition1']} and {t['tradition2']} traditions. Then, propose a short piece that combines these elements around the theme of {t['fusion_theme']}. Your response should include:

1. Comparative Analysis (300-400 words):
   a) Describe how {t['musical_element']} is approached in {t['tradition1']} and {t['tradition2']} traditions. Use specific music theory terms and concepts relevant to each tradition.
   b) Identify at least three key similarities and three key differences between these approaches. Provide concrete examples for each.
   c) Explain how these approaches reflect the cultural and historical contexts of each tradition. Reference relevant historical periods or cultural practices.

2. Composition Proposal (300-400 words):
   a) Describe a short musical piece (1-2 minutes) that fuses {t['musical_element']} from both {t['tradition1']} and {t['tradition2']} traditions, inspired by the theme of {t['fusion_theme']}.
   b) Explain how your composition incorporates specific elements from both traditions. Mention at least two distinct features from each tradition.
   c) Discuss how the theme of {t['fusion_theme']} is expressed through your fusion of {t['musical_element']}. Provide at least one specific musical example.
   d) Address any challenges in merging these traditions and how you resolve them. Discuss any compromises or innovations you've made.

3. Notation and Representation (200-300 words):
   a) Describe how you would notate a key section of your composition that best demonstrates the fusion of traditions. If traditional Western notation is insufficient, propose a hybrid notation system.
   b) Explain any non-standard notations or symbols you would use to accurately represent elements from both traditions.
   c) Provide a brief example of how a specific musical phrase or pattern would be notated in your system.

4. Cultural and Artistic Implications (200-300 words):
   a) Discuss the potential reception of your piece by audiences familiar with {t['tradition1']} and {t['tradition2']} traditions. Consider both positive reactions and potential criticisms.
   b) Explore how your composition might contribute to cross-cultural understanding or musical innovation. Provide at least one specific example.
   c) Address any ethical considerations in fusing distinct musical traditions. Discuss how you've approached cultural sensitivity in your composition.

Ensure your response demonstrates a deep understanding of music theory, cultural analysis, and creative composition. Use appropriate musical terminology and provide clear explanations for complex concepts. Be innovative in your approach while respecting the integrity of the musical traditions involved.

Format your response with clear headings for each section, and include a brief introduction and conclusion. Your total response should be between 1000-1400 words.

Example structure (replace with your own content):

Introduction: [Brief overview of your approach]

1. Comparative Analysis:
   [Your analysis here]

2. Composition Proposal:
   [Your proposal here]

3. Notation and Representation:
   [Your notation description here]

4. Cultural and Artistic Implications:
   [Your discussion here]

Conclusion: [Brief summary of key points]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The comparative analysis accurately describes {t['musical_element']} in both {t['tradition1']} and {t['tradition2']} traditions, including at least three similarities and three differences with concrete examples.",
            f"The composition proposal clearly incorporates at least two distinct elements from both traditions and expresses the theme of {t['fusion_theme']} with a specific musical example.",
            "The notation description demonstrates a thoughtful approach to representing the fusion of traditions, including an example of a specific musical phrase or pattern.",
            "The response discusses cultural and artistic implications, including potential reception, cross-cultural contributions, and ethical considerations with specific examples.",
            "The submission demonstrates understanding of music theory and cultural analysis, using appropriate terminology throughout.",
            "The response is creative and innovative while respecting musical traditions and addressing challenges in merging them.",
            "The submission follows the specified format, including an introduction, conclusion, and clear headings for each section, within the given word count range."
        ]
        return float(sum(eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria) / len(criteria))
