import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "field": "Quantum Physics",
                "abstract": "We report on the observation of a quantum spin liquid state in a kagome antiferromagnet. Using inelastic neutron scattering, we find evidence for fractionalized excitations in a single crystal of ZnCu3(OH)6Cl2 (herbertsmithite). The low-energy magnetic density of states displays a power-law dependence on energy, a hallmark of spin liquid behavior."
            },
            {
                "field": "Neuroscience",
                "abstract": "This study investigates the role of neuroplasticity in recovery from traumatic brain injury (TBI). Using a combination of fMRI and cognitive testing, we demonstrate that targeted cognitive training can lead to significant improvements in neural connectivity and cognitive function in TBI patients, even years after the initial injury."
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Create a constructed language (conlang) based on the field of {t['field']} and use it to translate the following research abstract:

"{t['abstract']}"

Your task involves the following steps:

1. Conlang Creation (200-250 words):
   a) Develop a phonetic inventory inspired by key concepts in {t['field']}.
   b) Create basic grammatical rules that reflect fundamental principles of the field.
   c) Generate a lexicon of at least 20 words/phrases crucial to expressing ideas in {t['field']}.

2. Translation (no word limit):
   Translate the given abstract into your conlang. Provide both the translation and a word-for-word or phrase-for-phrase back-translation to English.

3. Explanation (150-200 words):
   Justify how your conlang's features (phonetics, grammar, lexicon) represent key aspects of {t['field']}.

4. Analysis (100-150 words):
   Discuss any challenges you faced in translating specific scientific concepts and how you addressed them.

Ensure your conlang is consistent, your translation accurate, and your explanations clear and insightful."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The conlang's features (phonetics, grammar, lexicon) clearly reflect key concepts and principles of {t['field']}.",
            "The conlang is consistent and well-developed, with at least 20 words/phrases in the lexicon.",
            "The translation of the abstract into the conlang is complete and appears to accurately represent the original text.",
            "The back-translation to English demonstrates that the conlang can express complex scientific ideas from the original abstract.",
            "The explanation effectively justifies how the conlang's features represent key aspects of the scientific field.",
            "The analysis insightfully discusses challenges in translating scientific concepts and how they were addressed."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
