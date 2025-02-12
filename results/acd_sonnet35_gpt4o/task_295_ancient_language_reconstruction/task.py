import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            '1': {
                'language_name': 'Proto-Elamite',
                'known_information': {
                    'time_period': '3200-2700 BCE',
                    'location': 'Ancient Iran',
                    'writing_system': 'Pictographic and linear signs',
                    'corpus_size': 'Approximately 1600 tablets',
                    'deciphered_elements': ['Numerical system', 'Some common signs']
                },
                'sample_texts': [
                    '𒀝𒁉𒈨𒌍𒃻𒆠𒋫𒀀',
                    '𒀯𒁹𒌑𒃻𒂊𒈨𒌍𒋙'
                ],
                'modern_phrase': 'Digital communication'
            },
            '2': {
                'language_name': 'Linear A',
                'known_information': {
                    'time_period': '1800-1450 BCE',
                    'location': 'Minoan Crete',
                    'writing_system': 'Syllabic script',
                    'corpus_size': 'Approximately 1400 specimens',
                    'deciphered_elements': ['Some syllabic values', 'Numerical system']
                },
                'sample_texts': [
                    '𐘇𐘃𐘈𐘃',
                    '𐘞𐘀𐘁𐘅𐘅'
                ],
                'modern_phrase': 'Artificial intelligence'
            }
        }
        return {str(i): task for i, task in enumerate(random.sample(list(tasks.values()), len(tasks)), 1)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""You are a computational linguist specializing in ancient languages. Your task is to analyze and partially reconstruct the {t['language_name']} language using the limited information provided and AI-driven techniques. Complete the following steps:

1. Analysis (150-200 words):
   Analyze the given information about {t['language_name']}. Discuss potential relationships with known language families and any insights that can be drawn from the known elements. Provide a confidence level (0-100%) for your analysis.

2. Reconstruction Approach (200-250 words):
   Propose an AI-driven approach to further decipher and reconstruct {t['language_name']}. Explain how you would use machine learning techniques, pattern recognition, and comparative linguistics in your method. Be specific about the algorithms or models you would employ. Provide a confidence level (0-100%) for the potential success of your approach.

3. Sample Decipherment (100-150 words):
   Attempt a partial decipherment of one of the provided sample texts. Explain your reasoning and any patterns you identify. Clearly state when you are speculating. Provide a confidence level (0-100%) for your decipherment.

4. Linguistic Features (150-200 words):
   Based on your analysis and partial reconstruction, hypothesize about the potential linguistic features of {t['language_name']}. Consider aspects such as phonology, morphology, and syntax. Provide a confidence level (0-100%) for each major feature you propose.

5. Cultural Insights (100-150 words):
   Discuss what your reconstruction might reveal about the culture and society that used {t['language_name']}. Consider how the writing system and any deciphered content might reflect their way of life. Provide a confidence level (0-100%) for your cultural insights.

6. Challenges and Limitations (100-150 words):
   Identify the main challenges in reconstructing {t['language_name']} and any limitations of your proposed approach. Suggest directions for future research to overcome these obstacles.

7. Modern Translation (50-100 words):
   Based on your reconstruction and analysis, attempt to translate the modern phrase "{t['modern_phrase']}" into your hypothetical reconstruction of {t['language_name']}. Explain your reasoning and provide a confidence level (0-100%) for your translation.

Important Notes:
- Do not invent or assume any information not provided in the task description.
- Clearly state when you are speculating or making educated guesses.
- Use only the given information and your knowledge of linguistics and AI techniques.
- Provide confidence levels for each section as specified.

Format your response using clear headings for each section, and ensure that each section adheres to the specified word count. Your total response should be between 950-1200 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistic principles and computational approaches to language reconstruction.",
            "The proposed AI-driven approach is innovative, well-explained, and plausible given current technology.",
            "The analysis and hypotheses are logically sound and well-supported by the given information, without inventing or assuming additional data.",
            "The response shows creative problem-solving while remaining grounded in scientific principles.",
            "All required sections are present, adequately addressed, and adhere to the specified word count ranges.",
            "Speculations and educated guesses are clearly identified as such.",
            "Confidence levels are provided for each section as requested and seem reasonable given the information available.",
            "The modern phrase translation attempt demonstrates a coherent application of the proposed reconstruction.",
            "The response maintains a balance between creativity and scientific plausibility throughout all sections."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0