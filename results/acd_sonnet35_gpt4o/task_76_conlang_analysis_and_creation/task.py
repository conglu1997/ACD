import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        conlangs = [
            {
                'name': 'Klingon',
                'features': 'OVS word order, agglutinative morphology, guttural phonology'
            },
            {
                'name': 'Dothraki',
                'features': 'SVO word order, agglutinative morphology, extensive case system'
            }
        ]
        
        new_lang_params = [
            {
                'phonology': 'Tonal language with 4 tones',
                'morphology': 'Highly isolating',
                'syntax': 'VSO word order'
            },
            {
                'phonology': 'Consonant clusters allowed, no voiced consonants',
                'morphology': 'Fusional',
                'syntax': 'Free word order with case marking'
            }
        ]
        
        tasks = [
            {
                'conlang': random.choice(conlangs),
                'new_lang_params': new_lang_params[0]
            },
            {
                'conlang': random.choice(conlangs),
                'new_lang_params': new_lang_params[1]
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""This task has two parts:

1. Analyze the constructed language (conlang) {t['conlang']['name']}. Your analysis should include:
   a) A brief overview of the language's purpose and background (1-2 sentences)
   b) An explanation of its key features: {t['conlang']['features']} (3-4 sentences)
   c) An example sentence in the language with its English translation and a breakdown of its grammatical structure

2. Create a new constructed language based on the following parameters:
   Phonology: {t['new_lang_params']['phonology']}
   Morphology: {t['new_lang_params']['morphology']}
   Syntax: {t['new_lang_params']['syntax']}

   Your new language should include:
   a) A name for the language
   b) A brief explanation of its phonemic inventory (2-3 sentences)
   c) An overview of its morphological and syntactic features (3-4 sentences)
   d) An example sentence in the new language with its English translation and a breakdown of its grammatical structure

Format your response as follows:

Part 1: {t['conlang']['name']} Analysis
[Your analysis here]

Part 2: New Conlang
Name: [Your conlang's name]
[Your conlang description and example here]
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The analysis of {t['conlang']['name']} is accurate and addresses all required points.",
            "The new constructed language adheres to the given parameters and is internally consistent.",
            "Both parts demonstrate a deep understanding of linguistic principles and creative language design.",
            "The example sentences are provided and correctly analyzed for both languages."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
