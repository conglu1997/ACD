import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Ancient Greek', 'Medieval European', 'Classical Chinese', 'Modern American']
        time_periods = ['Ancient (800 BCE - 500 CE)', 'Medieval (500 CE - 1500 CE)', 'Early Modern (1500 CE - 1800 CE)', 'Contemporary (1800 CE - present)']
        metaphor_domains = ['Love', 'Time', 'Power', 'Knowledge']
        cognitive_processes = ['Conceptual blending', 'Image schema', 'Embodied cognition', 'Analogical reasoning']
        linguistic_features = ['Syntax', 'Semantics', 'Pragmatics', 'Phonology']
        
        tasks = {}
        for i in range(2):
            source_culture = random.choice(cultures)
            target_culture = random.choice([c for c in cultures if c != source_culture])
            time_period = random.choice(time_periods)
            metaphor_domain = random.choice(metaphor_domains)
            cognitive_process = random.choice(cognitive_processes)
            linguistic_feature = random.choice(linguistic_features)
            
            tasks[str(i+1)] = {
                'source_culture': source_culture,
                'target_culture': target_culture,
                'time_period': time_period,
                'metaphor_domain': metaphor_domain,
                'cognitive_process': cognitive_process,
                'linguistic_feature': linguistic_feature
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that simulates and analyzes the evolution of linguistic metaphors across different cultures and time periods, then apply it to a specific scenario. Your task is to focus on the metaphor domain of {t['metaphor_domain']}, analyzing its evolution from {t['source_culture']} culture during the {t['time_period']} to the {t['target_culture']} culture in the contemporary period. Your system should incorporate the cognitive process of {t['cognitive_process']} in its analysis and pay special attention to the linguistic feature of {t['linguistic_feature']}. Your response should include the following sections:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI system for metaphor evolution simulation and analysis.
   b) Explain how it integrates linguistic, cultural, and cognitive science knowledge.
   c) Detail how your system incorporates the {t['cognitive_process']} process and {t['linguistic_feature']} in its analysis.
   d) Discuss any novel techniques or algorithms used in your design.
   e) Include a simple diagram or flowchart of your system's architecture (describe it textually).

2. Metaphor Representation and Evolution (250-300 words):
   a) Explain how your system represents metaphors and their cultural/historical context.
   b) Describe the process by which your system simulates metaphor evolution across time and cultures.
   c) Discuss how your system accounts for cultural and linguistic differences in metaphor use and interpretation.
   d) Provide an example of how your system would represent a specific metaphor in the {t['metaphor_domain']} domain.

3. Case Study Analysis (300-350 words):
   a) Apply your system to analyze the evolution of metaphors in the domain of {t['metaphor_domain']} from {t['source_culture']} culture during the {t['time_period']} to {t['target_culture']} culture in the contemporary period.
   b) Provide at least three specific examples of metaphors and how they changed over time and across cultures.
   c) Explain how the {t['cognitive_process']} process influences this metaphor evolution.
   d) Discuss how changes in the {t['linguistic_feature']} affect the metaphor's structure or interpretation.
   e) Identify any surprising or counterintuitive findings from your analysis.

4. Cognitive Science Integration (200-250 words):
   a) Elaborate on how your system's approach aligns with current theories in cognitive linguistics.
   b) Explain how the incorporation of {t['cognitive_process']} enhances your system's analysis.
   c) Discuss potential implications of your system's findings for our understanding of human cognition and language use.
   d) Propose a hypothesis about the relationship between {t['cognitive_process']} and metaphor evolution that your system could test.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the accuracy and cultural sensitivity of your system's outputs.
   b) Describe how you would validate your system's findings against existing linguistic and historical data.
   c) Discuss potential challenges in verifying the authenticity of simulated metaphor evolution.
   d) Suggest a novel metric for measuring the 'cultural distance' between metaphors in different contexts.

6. Ethical Considerations and Future Directions (150-200 words):
   a) Identify potential ethical implications of simulating and analyzing cultural metaphors.
   b) Suggest guidelines for responsible development and use of such AI systems in linguistic and cultural studies.
   c) Propose two potential extensions or applications of your system for future research.
   d) Discuss how your system could be adapted to address potential biases in metaphor analysis.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, cultural studies, and AI. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining scientific and cultural accuracy.

Format your response with clear headings for each section and number your examples and points for clarity. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response includes a well-designed AI system architecture that incorporates {t['cognitive_process']} and addresses metaphor evolution simulation and analysis, with attention to {t['linguistic_feature']}",
            f"The system effectively represents and simulates metaphor evolution across time and cultures, with a focus on {t['metaphor_domain']} metaphors, providing a specific example",
            f"The case study analysis provides at least three specific examples of metaphor evolution from {t['source_culture']} during {t['time_period']} to contemporary {t['target_culture']} culture, explaining the influence of {t['cognitive_process']} and changes in {t['linguistic_feature']}",
            "The response demonstrates a deep understanding of cognitive linguistics, effectively integrates cognitive science principles, and proposes a testable hypothesis",
            "The proposed evaluation and validation methods are well-reasoned, address potential challenges, and include a novel metric for measuring 'cultural distance' between metaphors",
            "The response considers ethical implications, suggests responsible guidelines for AI use in linguistic and cultural studies, and discusses adaptation to address potential biases",
            "The overall response shows creativity, interdisciplinary knowledge integration, and strong analytical reasoning within the specified word limits and formatting guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
