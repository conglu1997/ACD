import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        poetic_elements = ['rhythm', 'rhyme', 'alliteration', 'metaphor', 'imagery']
        mathematical_structures = ['group', 'ring', 'field', 'vector space', 'lattice']
        
        tasks = {
            "1": {
                "poetic_element": random.choice(poetic_elements),
                "mathematical_structure": random.choice(mathematical_structures)
            },
            "2": {
                "poetic_element": random.choice(poetic_elements),
                "mathematical_structure": random.choice(mathematical_structures)
            }
        }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an algebraic system for analyzing and generating poetry based on the poetic element of {t['poetic_element']} using the mathematical structure of a {t['mathematical_structure']}. Then, apply your system to analyze and generate poetry. Your response should include:

1. System Design (250-300 words):
   a) Define the elements and operations of your algebraic system.
   b) Explain how your system models the poetic element of {t['poetic_element']}.
   c) Describe how the properties of a {t['mathematical_structure']} are utilized in your system.
   d) Provide at least one formal definition or theorem in your system.

2. Poetry Analysis (200-250 words):
   a) Choose a short poem (4-6 lines) and analyze it using your algebraic system.
   b) Explain how your analysis reveals insights about the poem's use of {t['poetic_element']}.
   c) Discuss any limitations of your system in analyzing this poem.

3. Poetry Generation (200-250 words):
   a) Use your algebraic system to generate a new poem (4-6 lines) that emphasizes {t['poetic_element']}.
   b) Explain the generation process, referencing specific elements and operations in your system.
   c) Analyze the generated poem using your system, highlighting its use of {t['poetic_element']}.

4. Comparative Analysis (150-200 words):
   a) Compare your algebraic approach to traditional methods of poetry analysis and generation.
   b) Discuss potential advantages and limitations of your system.

5. Interdisciplinary Connections (100-150 words):
   a) Explore how your system connects abstract algebra with linguistics and poetics.
   b) Propose a novel research question that arises from this connection.

Ensure your response demonstrates a deep understanding of both the mathematical concepts and poetic principles. Use appropriate technical terminology and provide clear explanations of complex ideas. Be innovative in your approach while maintaining mathematical rigor and poetic sensibility.

Format your answer with clear headings for each section. Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of the mathematical structure of a {t['mathematical_structure']} and how it can be applied to model the poetic element of {t['poetic_element']}.",
            "The algebraic system design is well-defined, with clear elements, operations, and at least one formal definition or theorem.",
            "The poetry analysis and generation sections effectively apply the designed system to real and created poems, providing insights into the use of the specified poetic element.",
            "The comparative analysis and interdisciplinary connections show depth of thought and creativity in bridging mathematics and poetry.",
            "The response is well-structured, adheres to the word count guidelines, and effectively communicates complex ideas."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
