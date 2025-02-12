import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        algorithms = [
            {
                "name": "Quicksort",
                "description": "A divide-and-conquer algorithm that selects a 'pivot' element and partitions the array around it, then recursively sorts the sub-arrays."
            },
            {
                "name": "PageRank",
                "description": "An algorithm used by search engines to rank web pages in their search engine results, based on the importance of web pages."
            }
        ]
        return {str(i+1): algorithm for i, algorithm in enumerate(algorithms)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that translates natural language instructions into a novel visual programming language, then use it to represent the {t['name']} algorithm. A visual programming language uses visual elements (such as shapes, colors, and connections) to represent programming concepts and logic, making it more intuitive and accessible than traditional text-based code.

Your response should include:

1. Visual Language Design (250-300 words):
   a) Describe the key elements of your visual programming language (e.g., shapes, colors, connections).
   b) Explain how these elements represent basic programming concepts (e.g., variables, loops, conditionals).
   c) Provide at least 2 example 'statements' in your visual language with their corresponding natural language and traditional code equivalents.
   d) Include a simple diagram or sketch of a basic programming concept (e.g., a loop or conditional statement) in your visual language. Describe this diagram briefly.

2. Translation System and Algorithm Representation (300-350 words):
   a) Outline the main components of your translation system.
   b) Explain the process of converting natural language to your visual programming language.
   c) Provide a high-level description of how the {t['name']} algorithm would be represented in your visual programming language.
   d) Explain how your visual representation captures the key steps and logic of the algorithm.
   e) Discuss any challenges in representing this algorithm visually and how your system addresses them.

3. Analysis and Future Work (200-250 words):
   a) Compare your visual programming language to an existing visual programming language (e.g., Scratch, LabVIEW).
   b) Analyze potential cognitive benefits of using your visual programming language for understanding complex algorithms.
   c) Identify any limitations of your visual programming language or translation system.
   d) Propose potential improvements or extensions to your system.

Ensure your response demonstrates understanding of linguistics, computer science, and visual design principles. Be innovative while maintaining clarity and logical consistency. Use appropriate technical terminology and provide clear explanations where necessary.

Your total response should be between 750-900 words. Format your response with clear headings for each section and number your paragraphs for easy reference. Remember to provide a coherent and well-structured response that addresses all parts of the task."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The visual language design is described with at least 2 examples of how it represents programming concepts.",
            "A simple diagram or sketch of a basic programming concept in the visual language is included and described.",
            "The translation system and algorithm representation section covers the main points requested in the instructions.",
            f"The representation of the {t['name']} algorithm captures key steps and logic in the visual programming language.",
            "The response includes a comparison with an existing visual programming language.",
            "The response includes an analysis of potential cognitive benefits.",
            "The limitations and future work section shows some critical thinking about the system.",
            "The response demonstrates interdisciplinary knowledge across linguistics, computer science, and visual design.",
            "The response adheres to the specified word count range (750-900 words)."
        ]
        met_criteria = sum([eval_with_llm_judge(instructions, submission, [criterion]) for criterion in criteria])
        return 1.0 if met_criteria >= len(criteria) - 1 else met_criteria / len(criteria)
