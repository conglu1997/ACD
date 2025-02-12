import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        semantic_relations = ['synonymy', 'antonymy', 'hyponymy', 'meronymy']
        quantum_concepts = ['superposition', 'entanglement', 'interference', 'measurement']
        cognitive_processes = ['categorization', 'analogy-making', 'conceptual blending', 'metaphor comprehension']
        
        task1 = {
            "semantic_relation": random.choice(semantic_relations),
            "quantum_concept": random.choice(quantum_concepts),
            "cognitive_process": random.choice(cognitive_processes)
        }
        
        task2 = {
            "semantic_relation": random.choice([r for r in semantic_relations if r != task1["semantic_relation"]]),
            "quantum_concept": random.choice([q for q in quantum_concepts if q != task1["quantum_concept"]]),
            "cognitive_process": random.choice([c for c in cognitive_processes if c != task1["cognitive_process"]])
        }
        
        return {"1": task1, "2": task2}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing model for representing and manipulating semantic spaces, incorporating principles from distributional semantics and cognitive science. Your model should focus on the following elements:

Semantic Relation: {t['semantic_relation']}
Quantum Concept: {t['quantum_concept']}
Cognitive Process: {t['cognitive_process']}

Your response should include the following sections:

1. Quantum Semantic Space Model (300-350 words):
   a) Describe the key components of your quantum semantic space model.
   b) Explain how you incorporate the given quantum concept into your semantic representation.
   c) Detail how your model represents and processes the specified semantic relation.
   d) Discuss how your model simulates or relates to the given cognitive process.

2. Mathematical Formulation (250-300 words):
   a) Provide a mathematical description of your quantum semantic space model.
   b) Include key equations or formalisms that capture the integration of quantum principles and semantic structures.
   c) Explain how your mathematical framework relates to established models in distributional semantics or cognitive science.

3. Quantum Circuit Design (200-250 words):
   a) Describe a quantum circuit that implements a key operation in your semantic space model.
   b) Explain how this circuit processes semantic information using quantum operations.
   c) Discuss any advantages this quantum approach might have over classical methods.

4. Linguistic Analysis and Generation (250-300 words):
   a) Provide an example of how your model would analyze a given word or phrase in terms of the specified semantic relation.
   b) Describe how your model could generate novel linguistic expressions based on quantum semantic manipulations.
   c) Explain how the quantum nature of your model enhances linguistic processing compared to classical approaches.

5. Cognitive Implications (200-250 words):
   a) Discuss how your quantum semantic space model relates to theories of human cognition, particularly the specified cognitive process.
   b) Propose an experiment that could test whether human semantic processing exhibits quantum-like properties as suggested by your model.
   c) Speculate on the implications of your model for our understanding of the relationship between language, thought, and quantum phenomena.

6. Limitations and Future Directions (150-200 words):
   a) Identify potential limitations or challenges in implementing your model on current or near-term quantum hardware.
   b) Discuss any theoretical or empirical obstacles to validating your model.
   c) Propose future research directions or extensions of your model.

Ensure your response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science.",
            "The quantum semantic space model is innovative and well-explained.",
            "The mathematical formulation is sound and relevant to the model.",
            "The quantum circuit design is appropriate and well-described.",
            "The linguistic analysis and generation example is clear and relevant.",
            "The discussion of cognitive implications is insightful and well-reasoned.",
            "The limitations and future directions are thoughtfully considered.",
            "The response maintains scientific plausibility while being creative and innovative.",
            "The response follows the specified format with clear headings for each section.",
            "The total word count is within the specified range (1350-1650 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
