import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenarios = [
            {
                'civilization': 'Minoan',
                'time_period': '2000 BCE',
                'artifact_type': 'clay tablets',
                'script_type': 'undeciphered pictographic',
                'archaeological_context': 'palace ruins'
            },
            {
                'civilization': 'Indus Valley',
                'time_period': '2500 BCE',
                'artifact_type': 'seals and amulets',
                'script_type': 'undeciphered symbolic',
                'archaeological_context': 'urban ruins'
            },
            {
                'civilization': 'Olmec',
                'time_period': '1000 BCE',
                'artifact_type': 'stone monuments',
                'script_type': 'early logographic',
                'archaeological_context': 'ceremonial centers'
            },
            {
                'civilization': 'Etruscan',
                'time_period': '750 BCE',
                'artifact_type': 'inscribed pottery',
                'script_type': 'partially deciphered alphabet',
                'archaeological_context': 'necropolises'
            }
        ]
        selected_scenarios = random.sample(scenarios, 2)
        for scenario in selected_scenarios:
            scenario['artifact_condition'] = random.choice(['well-preserved', 'partially damaged', 'heavily eroded'])
        return {str(i+1): scenario for i, scenario in enumerate(selected_scenarios)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a linguist and archaeologist tasked with reconstructing an ancient language and aspects of its associated culture based on limited evidence. The scenario is as follows:

Civilization: {t['civilization']}
Time Period: {t['time_period']}
Artifact Type: {t['artifact_type']} ({t['artifact_condition']})
Script Type: {t['script_type']}
Archaeological Context: {t['archaeological_context']}

Your task is to propose a reconstruction of the language and culture based on this limited information. Your response should include:

1. Linguistic Analysis (250-300 words):
   a) Propose a basic structure for the language, including its likely language family and typological features.
   b) Describe the writing system, including the estimated number of signs/symbols and their possible functions.
   c) Provide a hypothetical translation of a short phrase or sentence in this language, explaining your reasoning.

2. Cultural Reconstruction (200-250 words):
   a) Infer aspects of the society's social structure, economy, and religious beliefs based on the archaeological context.
   b) Propose at least two cultural practices or traditions that might have been significant in this society.
   c) Explain how the artifact type and script might reflect the society's priorities or values.

3. Comparative Analysis (200-250 words):
   a) Compare your reconstructed language to known ancient languages from similar time periods or regions.
   b) Discuss possible influences or connections with other contemporary civilizations.
   c) Explain how this language might have evolved or influenced later languages in the region.

4. Decipherment Methodology (150-200 words):
   a) Propose a step-by-step approach for attempting to decipher this script.
   b) Discuss potential challenges in the decipherment process and how you would address them.
   c) Suggest one innovative technique or technology that could aid in the decipherment effort.

5. Implications and Significance (150-200 words):
   a) Discuss the potential historical or cultural significance of deciphering this language.
   b) Explain how understanding this language and culture could impact our knowledge of ancient history.
   c) Propose one way in which this reconstruction could inform or challenge current archaeological or linguistic theories.

Ensure your response demonstrates a deep understanding of historical linguistics, archaeological methods, and cultural anthropology. Be creative and speculative in your reconstruction while maintaining scientific plausibility and consistency with the given evidence. Use appropriate terminology from relevant fields and provide clear reasoning for your hypotheses.

Format your response with clear headings for each section and number your paragraphs within each section. Your total response should be between 950-1200 words.

Important: For each major claim or hypothesis, provide at least one citation to a relevant academic source (real or hypothetical) to support your reasoning. Use a consistent citation format throughout your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of historical linguistics, archaeological methods, and cultural anthropology as applied to the {t['civilization']} civilization.",
            "The linguistic analysis and cultural reconstruction are creative yet plausible, with clear reasoning provided for all hypotheses.",
            "The comparative analysis shows a broad knowledge of ancient civilizations and languages.",
            "The proposed decipherment methodology is logical and innovative.",
            "The discussion of implications demonstrates an understanding of the broader context of archaeology and linguistics.",
            "The response includes appropriate citations to support major claims and hypotheses.",
            "The total word count falls within the specified range of 950-1200 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
