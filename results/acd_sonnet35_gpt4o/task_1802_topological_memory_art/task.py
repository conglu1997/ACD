import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        memory_processes = [
            "Encoding",
            "Consolidation",
            "Retrieval",
            "Reconsolidation"
        ]
        topological_concepts = [
            "Homotopy",
            "Homology",
            "Manifold",
            "Fiber bundle"
        ]
        artistic_styles = [
            "Abstract expressionism",
            "Cubism",
            "Surrealism",
            "Digital art"
        ]
        
        tasks = {}
        for i in range(2):
            memory_process = random.choice(memory_processes)
            topological_concept = random.choice(topological_concepts)
            artistic_style = random.choice(artistic_styles)
            
            tasks[str(i+1)] = {
                "memory_process": memory_process,
                "topological_concept": topological_concept,
                "artistic_style": artistic_style
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a system that maps the human memory process of {t['memory_process']} to the topological concept of {t['topological_concept']}, then translate this mapping into an abstract art piece in the style of {t['artistic_style']}. Your response should include:

1. Topological Memory Mapping (300-350 words):
   a) Explain how you would represent the {t['memory_process']} process using {t['topological_concept']}.
   b) Describe the key features of your topological representation and how they correspond to aspects of the memory process.
   c) Discuss any novel mathematical insights this mapping might provide about memory formation or cognitive processes.

2. Artistic Translation (250-300 words):
   a) Describe how you would translate your topological memory mapping into a {t['artistic_style']} art piece.
   b) Explain your choice of visual elements, colors, or forms and how they represent specific aspects of the topological structure and memory process.
   c) Discuss how this artistic representation might enhance understanding of both the mathematical concept and the cognitive process.

3. Cognitive-Mathematical Analysis (200-250 words):
   a) Analyze how your topological representation of {t['memory_process']} aligns with current cognitive theories.
   b) Identify any potential new hypotheses about memory processes that arise from this mathematical modeling.
   c) Discuss how this interdisciplinary approach might contribute to both cognitive science and topology.

4. Artistic-Scientific Interpretation (200-250 words):
   a) Explain how your {t['artistic_style']} representation might be interpreted or analyzed by:
      - A cognitive scientist
      - A mathematician
      - An art critic
   b) Discuss how these different perspectives might contribute to a holistic understanding of the memory-topology relationship.

5. Practical Applications and Implications (150-200 words):
   a) Propose a potential practical application of your topological memory art system in fields such as education, therapy, or scientific visualization.
   b) Discuss any ethical considerations or potential societal impacts of representing cognitive processes through abstract mathematical and artistic means.

Ensure your response demonstrates a deep understanding of topology, cognitive science, and artistic principles. Be creative in your approach while maintaining scientific and mathematical plausibility. Use appropriate terminology from all relevant fields and provide clear explanations where necessary.

Format your response with clear headings for each section and include the word count for each section in parentheses at the end of the section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of the topological concept {t['topological_concept']} and how it can be applied to model the memory process of {t['memory_process']}",
            f"The artistic translation effectively represents the topological-cognitive mapping in the style of {t['artistic_style']}",
            "The cognitive-mathematical analysis provides novel insights or hypotheses about memory processes",
            "The response shows creativity and innovation while maintaining scientific and mathematical plausibility",
            "The practical application proposed is feasible and potentially impactful",
            "The response adheres to the specified word count for each section and the overall word limit"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
