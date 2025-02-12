import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            "Time",
            "Causality",
            "Consciousness",
            "Infinity",
            "Emergence",
            "Complexity",
            "Entropy",
            "Duality",
            "Symmetry",
            "Recursion"
        ]
        concrete_domains = [
            "Oceanography",
            "Architecture",
            "Music Theory",
            "Botany",
            "Culinary Arts",
            "Textile Manufacturing",
            "Urban Planning",
            "Geology",
            "Meteorology",
            "Horology"
        ]
        problem_areas = [
            "Climate Change Mitigation",
            "Interstellar Travel",
            "Quantum Computing",
            "Artificial General Intelligence",
            "Sustainable Energy",
            "Nanotechnology",
            "Biotechnology",
            "Space Colonization",
            "Cybersecurity",
            "Cognitive Enhancement"
        ]
        
        tasks = {}
        for i in range(2):
            concept = random.choice(abstract_concepts)
            domain = random.choice(concrete_domains)
            problem = random.choice(problem_areas)
            
            tasks[str(i+1)] = {
                "concept": concept,
                "domain": domain,
                "problem": problem
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can generate and interpret complex metaphors, then apply this capability to solve abstract problems. Metaphorical reasoning involves understanding and expressing abstract ideas in terms of more concrete concepts, often drawing connections between seemingly unrelated domains.

Your task has the following components:

1. Metaphor Generation and Interpretation (250-300 words):
   a) Design an AI system that can generate complex metaphors relating the abstract concept of {t['concept']} to the concrete domain of {t['domain']}.
   b) Explain how your system would interpret and extract meaning from these metaphors.
   c) Describe the key components and mechanisms of your AI system, including any novel neural network architectures or algorithms.

2. Cognitive Linguistics Analysis (200-250 words):
   a) Analyze how your AI system's approach to metaphor generation and interpretation relates to theories in cognitive linguistics.
   b) Discuss how your system might shed light on human cognitive processes involved in metaphorical thinking.
   c) Explain any assumptions or simplifications your model makes about human cognition.

3. Problem-Solving Application (250-300 words):
   a) Describe how your AI system would apply its metaphorical reasoning capability to address the problem of {t['problem']}.
   b) Provide at least two specific examples of metaphor-inspired solutions or insights your system might generate.
   c) Explain how these solutions differ from traditional approaches to the problem.

4. Evaluation and Limitations (200-250 words):
   a) Propose a method to evaluate the effectiveness and creativity of your AI system's metaphorical reasoning.
   b) Discuss potential limitations or biases in your system's approach.
   c) Suggest how these limitations might be addressed in future iterations.

5. Ethical Implications (150-200 words):
   a) Discuss the ethical implications of developing AI systems capable of advanced metaphorical reasoning.
   b) Consider potential risks and benefits to society.
   c) Propose guidelines for responsible development and use of such systems.

6. Interdisciplinary Connections (150-200 words):
   a) Explain how your AI system integrates knowledge from cognitive science, linguistics, and artificial intelligence.
   b) Discuss any novel insights or approaches that emerge from this interdisciplinary integration.
   c) Suggest how this approach might impact future research in these fields.

Ensure your response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, and the specific domains involved. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and speculative in your design while maintaining scientific plausibility.

Format your response with clear headings for each section, exactly as numbered above. Begin each section with the heading (e.g., '1. Metaphor Generation and Interpretation:') on a new line, followed by your response for that section. Your total response should be between 1200-1500 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, and the specified domains",
            "The AI system design for metaphor generation and interpretation is innovative and well-explained",
            "The application of metaphorical reasoning to the given problem is creative and insightful",
            "The evaluation method and discussion of limitations show critical thinking",
            "The ethical implications are thoroughly considered",
            "The interdisciplinary connections are well-articulated and demonstrate integrative thinking",
            "The response follows the specified format with clear headings for each section"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
