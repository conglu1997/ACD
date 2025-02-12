import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_periods = ['Renaissance', 'Baroque', 'Impressionism', 'Modernism', 'Contemporary']
        cultural_regions = ['Western Europe', 'East Asia', 'South Asia', 'Middle East', 'Africa']
        analysis_focuses = ['Iconography', 'Stylistic elements', 'Materials and techniques', 'Socio-political context', 'Religious symbolism']
        
        tasks = {}
        for i in range(1, 3):
            tasks[str(i)] = {
                'art_period': random.choice(art_periods),
                'cultural_region': random.choice(cultural_regions),
                'analysis_focus': random.choice(analysis_focuses)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system to analyze historical artworks, detect cross-cultural influences, and generate insights about artistic evolution. Focus on the {t['art_period']} period in {t['cultural_region']}, with particular attention to {t['analysis_focus']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI art history analyzer.
   b) Explain how your system integrates computer vision, natural language processing, and knowledge representation.
   c) Detail the data inputs and outputs of your system.
   d) Discuss how your AI learns and adapts its analysis over time.
   e) Include a high-level diagram or pseudocode snippet illustrating a key aspect of your system.

2. Cross-cultural Analysis Approach (200-250 words):
   a) Explain how your system detects and analyzes cross-cultural influences in artworks.
   b) Describe the methods used to compare artistic elements across different cultures and periods.
   c) Discuss how your system handles ambiguity and uncertainty in cultural attributions.

3. {t['analysis_focus']} Analysis (200-250 words):
   a) Detail how your system specifically analyzes {t['analysis_focus']} in artworks.
   b) Explain any specialized algorithms or techniques used for this analysis.
   c) Provide an example of how your system might interpret a specific artwork feature related to {t['analysis_focus']}.

4. Historical Context Integration (150-200 words):
   a) Describe how your system incorporates historical and cultural context into its analysis.
   b) Explain how it accounts for changes in artistic conventions and societal norms over time.
   c) Discuss any challenges in applying modern AI techniques to historical art analysis.

5. Insights Generation (150-200 words):
   a) Explain how your system generates novel insights about artistic evolution.
   b) Describe the types of patterns or trends it might identify across cultures and periods.
   c) Discuss how these insights could contribute to art historical scholarship.

6. Ethical Considerations and Limitations (200-250 words):
   a) Address potential biases in your AI system and how you would mitigate them.
   b) Discuss ethical implications of using AI for cultural heritage analysis.
   c) Explain how your system handles sensitive cultural content or contested interpretations.
   d) Describe the limitations of your approach and areas for future improvement.

Ensure your response demonstrates a deep understanding of AI technologies, art history, and cultural analysis. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of AI technologies, art history, and cultural analysis, particularly focusing on the {t['art_period']} period in {t['cultural_region']} and {t['analysis_focus']}.",
            "The proposed AI system architecture is well-designed, integrating computer vision, natural language processing, and knowledge representation effectively.",
            "The cross-cultural analysis approach is innovative and well-explained, with clear methods for comparing artistic elements across cultures and periods.",
            f"The analysis of {t['analysis_focus']} is detailed and includes specialized techniques or algorithms.",
            "The system's approach to generating insights about artistic evolution is clearly explained and potentially valuable for art historical scholarship.",
            "Ethical considerations and limitations are thoroughly addressed, including potential biases and handling of sensitive cultural content.",
            "The response is well-structured, uses appropriate technical terminology, and provides clear explanations for complex concepts."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
