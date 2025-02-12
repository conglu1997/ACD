import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        linguistic_concepts = [
            "metaphor",
            "polysemy",
            "syntactic ambiguity",
            "semantic field",
            "phonological rule"
        ]
        visual_elements = [
            "shape",
            "color",
            "size",
            "position",
            "orientation"
        ]
        puzzle_types = [
            "translation",
            "transformation",
            "combination"
        ]
        return {
            "1": {
                "concept": random.choice(linguistic_concepts),
                "visual_element": random.choice(visual_elements),
                "puzzle_type": random.choice(puzzle_types)
            },
            "2": {
                "concept": random.choice(linguistic_concepts),
                "visual_element": random.choice(visual_elements),
                "puzzle_type": random.choice(puzzle_types)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""In this task, you will create an abstract visual representation of a linguistic concept and use it to solve a language-based puzzle. Follow these steps:

1. Visual Representation (200-250 words):
   a) Create an abstract visual representation of the linguistic concept '{t['concept']}' using the visual element of '{t['visual_element']}'.
   b) Explain how your visual representation captures the key aspects of the linguistic concept.
   c) Describe how variations in the '{t['visual_element']}' correspond to variations in the linguistic concept.
   Note: Provide your visual representation in text format, describing it in detail.

2. Mapping Rules (150-200 words):
   a) Define a set of rules for mapping between the visual representation and linguistic expressions.
   b) Provide examples of how these rules work for at least three different linguistic expressions related to the concept.

3. Puzzle Design (200-250 words):
   a) Create a '{t['puzzle_type']}' puzzle using your visual-linguistic mapping.
   b) Clearly state the puzzle objective and any constraints.
   c) Provide the necessary visual and linguistic elements for solving the puzzle.

   Puzzle types:
   - Translation: Convert between visual and linguistic representations
   - Transformation: Modify visual or linguistic elements to change meaning
   - Combination: Merge multiple visual-linguistic mappings to create new meanings

4. Puzzle Solution (200-250 words):
   a) Present a step-by-step solution to your puzzle.
   b) Explain how each step utilizes the visual-linguistic mapping.
   c) Discuss any insights or challenges that arise during the solving process.

5. Analysis and Reflection (150-200 words):
   a) Analyze the strengths and limitations of your visual-linguistic mapping approach.
   b) Discuss how this method might reveal new insights about the linguistic concept or language processing in general.
   c) Propose an extension or variation of your approach that could be applied to other linguistic phenomena.

Ensure your response demonstrates a deep understanding of the linguistic concept, creativity in visual representation, and logical consistency in the mapping and puzzle design. Use clear headings for each section and number your paragraphs within each section.

Your total response should be between 900-1150 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the given linguistic concept.",
            "The visual representation is creative and effectively captures the key aspects of the linguistic concept.",
            "The mapping rules are clear, logical, and consistently applied.",
            "The puzzle design is original, challenging, and properly utilizes the visual-linguistic mapping.",
            "The puzzle solution is clear, step-by-step, and demonstrates the effectiveness of the visual-linguistic mapping.",
            "The analysis and reflection show insight into the strengths and limitations of the approach.",
            "The response is well-structured, coherent, and adheres to the specified word limits."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
