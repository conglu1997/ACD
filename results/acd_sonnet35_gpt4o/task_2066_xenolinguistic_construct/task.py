import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        biological_principles = [
            'photosynthesis',
            'echolocation',
            'symbiosis',
            'bioluminescence'
        ]
        physical_principles = [
            'quantum entanglement',
            'gravitational waves',
            'dark matter',
            'plasma dynamics'
        ]
        scientific_concepts = [
            'climate change',
            'genetic engineering',
            'artificial intelligence',
            'space colonization'
        ]
        
        def generate_task():
            base_principle = random.choice(biological_principles + physical_principles)
            concept = random.choice(scientific_concepts)
            return {
                'base_principle': base_principle,
                'scientific_concept': concept
            }
        
        return {
            "1": generate_task(),
            "2": generate_task()
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) based on the principle of {t['base_principle']}, then use it to communicate the concept of {t['scientific_concept']}. A constructed language is an artificial language designed for a specific purpose, in this case to reflect a biological or physical principle.

Your response should be entirely your own original work and not copied from existing constructed languages or other sources. Ensure that your language design is internally consistent and coherent. Your response will be evaluated based on the criteria provided at the end of these instructions.

Include the following sections, with the specified word counts:

1. Language Design (300-350 words):
   a) Explain how the principle of {t['base_principle']} informs the structure and features of your constructed language.
   b) Describe the phonology, morphology, and syntax of your language, providing examples.
   c) Explain any novel linguistic features that arise from the base principle.
   d) Discuss how this language might be produced or perceived by its hypothetical speakers.

2. Vocabulary Generation (200-250 words):
   a) Create 5-10 key words or phrases in your constructed language that are relevant to {t['scientific_concept']}.
   b) Provide their English translations and etymologies based on your language's structure.
   c) Explain how these words reflect both the base principle and the scientific concept.

3. Concept Translation (300-350 words):
   a) Provide a brief explanation of {t['scientific_concept']} in English (50-75 words).
   b) Write a short paragraph (3-5 sentences) explaining {t['scientific_concept']} in your constructed language.
   c) Provide an English translation of this paragraph.
   d) Analyze how your language's features influence the expression of this scientific concept.
   e) Discuss any challenges or novel insights that arose from this translation process.

4. Linguistic Analysis (200-250 words):
   a) Compare your constructed language to existing human languages, noting similarities and differences.
   b) Discuss how your language might influence or reflect the thought patterns of its speakers.
   c) Speculate on how this language might evolve over time, given its unusual basis.

5. Implications and Applications (200-250 words):
   a) Discuss potential applications of your language design process in linguistics or cognitive science.
   b) Explore how this exercise might inform our understanding of the relationship between language, thought, and physical reality.
   c) Propose an experiment to test whether aspects of your language could enhance understanding of {t['scientific_concept']}.
   d) Discuss potential limitations or challenges of your constructed language and how they might be addressed.

Ensure your response demonstrates a deep understanding of linguistics, the specified base principle, and the scientific concept. Be creative in your approach while maintaining scientific plausibility. Use clear headings for each section of your response. Your total response should be between 1200-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed language design based on {t['base_principle']}, with clear explanations of its phonology, morphology, and syntax.",
            f"The response must generate at least 5 vocabulary items relevant to {t['scientific_concept']} in the constructed language, with translations and etymologies.",
            f"The response must include a brief explanation of {t['scientific_concept']} in English, followed by a translation into the constructed language and back to English.",
            "The response must provide a linguistic analysis comparing the constructed language to existing human languages and speculating on its potential evolution.",
            "The response must discuss implications, applications, and limitations of the language design process, including a proposed experiment.",
            "The overall response must demonstrate creativity, scientific plausibility, and a deep understanding of linguistics and the given scientific concept.",
            "The language design must be internally consistent and coherent.",
            "The response must be original work and not copied from existing constructed languages or other sources."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
