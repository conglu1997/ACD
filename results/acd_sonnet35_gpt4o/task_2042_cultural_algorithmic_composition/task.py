import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        traditions = [
            {
                'tradition': 'Javanese Gamelan',
                'key_elements': ['Slendro and Pelog scales', 'Cyclic structures', 'Interlocking patterns'],
                'instruments': ['Metallophones', 'Gongs', 'Drums'],
                'cultural_context': 'Traditional Indonesian ensemble music'
            },
            {
                'tradition': 'North Indian Classical',
                'key_elements': ['Raga (melodic framework)', 'Tala (rhythmic cycle)', 'Alap-Jor-Jhala structure'],
                'instruments': ['Sitar', 'Tabla', 'Tanpura'],
                'cultural_context': 'Ancient classical tradition of the Indian subcontinent'
            },
            {
                'tradition': 'Renaissance Polyphony',
                'key_elements': ['Modal system', 'Cantus firmus technique', 'Imitative counterpoint'],
                'instruments': ['Human voices', 'Lute', 'Viol'],
                'cultural_context': 'European sacred and secular music of the 15th-16th centuries'
            }
        ]
        return {str(i+1): tradition for i, tradition in enumerate(random.sample(traditions, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel algorithmic composition system based on the {t['tradition']} musical tradition. Your system should be original and not simply describe an existing composition system. Your task includes:

1. System Design (300-350 words):
   a) Describe the key components of your algorithmic composition system.
   b) Explain how your system incorporates the key elements of {t['tradition']}: {', '.join(t['key_elements'])}.
   c) Discuss how your algorithm represents and generates musical structures specific to this tradition.
   d) Provide a high-level pseudocode (15-20 lines) of your composition algorithm. Use clear variable names and comments to explain each step.

2. Mathematical Foundation (200-250 words):
   a) Explain the mathematical or computational principles underlying your system.
   b) Describe any formal models or data structures used to represent musical elements.
   c) Discuss how your system handles the generation of coherent musical patterns.

3. Cultural Integration (200-250 words):
   a) Analyze how your system reflects the cultural context of {t['tradition']}: {t['cultural_context']}.
   b) Discuss any challenges in translating cultural musical concepts into algorithmic processes.
   c) Explain how your system maintains cultural authenticity while allowing for creative variation.

4. Composition Generation (250-300 words):
   a) Use your system to generate a short musical piece (describe it in words).
   b) Explain the step-by-step process of how your algorithm created this piece.
   c) Discuss how the generated piece reflects the characteristics of {t['tradition']}.
   d) Provide a short musical example (8-16 measures) in standard Western notation or appropriate tablature for {', '.join(t['instruments'])}. If using non-standard notation, provide a clear explanation of how to read it.

5. Analysis and Evaluation (200-250 words):
   a) Analyze the strengths and limitations of your algorithmic composition system.
   b) Propose a method for evaluating the cultural authenticity and musical quality of the generated pieces.
   c) Discuss how your system could be extended or modified for music pedagogy or cross-cultural musical analysis.

6. Ethical and Cultural Considerations (150-200 words):
   a) Discuss the ethical implications of using algorithms to generate music from specific cultural traditions.
   b) Propose guidelines for the respectful use and attribution of culturally-specific musical algorithms.
   c) Explore the potential impact of such systems on the preservation and evolution of musical traditions.

Ensure your response demonstrates a deep understanding of music theory, cultural musicology, and algorithmic composition techniques. Use appropriate musical and technical terminology, providing clear explanations where necessary. Be creative in your approach while maintaining cultural sensitivity and musical plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words, not including the pseudocode and musical notation."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['tradition']} musical tradition and accurately incorporates its key elements: {', '.join(t['key_elements'])}.",
            "The algorithmic composition system is novel, well-designed, and clearly explained with appropriate pseudocode.",
            "The mathematical foundation is sound and thoroughly explained, with clear connections to the musical tradition.",
            "The cultural integration section shows a nuanced understanding of the tradition's context and addresses challenges thoughtfully.",
            "The composition generation process is clearly described, and the provided musical example accurately reflects the tradition's characteristics.",
            "The analysis and evaluation section provides insightful commentary on the system's strengths, limitations, and potential applications.",
            "The ethical and cultural considerations are thoughtfully addressed, showing awareness of the broader implications of the technology.",
            "The response is well-structured, adheres to the specified word count for each section, and includes all required elements (pseudocode, musical notation/tablature)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
