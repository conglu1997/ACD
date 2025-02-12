import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        quantum_concepts = [
            {
                'concept': 'Superposition',
                'description': 'The ability of a quantum system to exist in multiple states simultaneously'
            },
            {
                'concept': 'Entanglement',
                'description': 'A quantum phenomenon where particles become correlated and share properties'
            }
        ]
        cognitive_processes = [
            {
                'process': 'Semantic memory',
                'description': 'The memory of meanings, understandings, and other concept-based knowledge'
            },
            {
                'process': 'Working memory',
                'description': 'The cognitive system responsible for temporarily holding and manipulating information'
            }
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'quantum_concept': random.choice(quantum_concepts),
                'cognitive_process': random.choice(cognitive_processes)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical quantum-inspired natural language processing model that incorporates the quantum mechanical concept of {t['quantum_concept']['concept']} and the cognitive process of {t['cognitive_process']['process']}. Your task has the following parts:

1. Model Concept (200-250 words):
   a) Explain how you would integrate {t['quantum_concept']['concept']} ({t['quantum_concept']['description']}) with {t['cognitive_process']['process']} ({t['cognitive_process']['description']}) in a language processing model.
   b) Describe the key components and structure of your model.
   c) Explain how this integration might enhance or change traditional NLP approaches.

2. Theoretical Framework (150-200 words):
   a) Provide a theoretical justification for your model, drawing on relevant literature from quantum mechanics, cognitive science, and linguistics.
   b) Discuss any existing theories or models that support or inspire your approach.
   c) Propose a novel hypothesis about language processing that your model could test.

3. Mathematical Formulation (150-200 words):
   a) Present a mathematical representation of a key aspect of your model.
   b) Explain the variables, operators, or functions in your formulation.
   c) Describe how this mathematical representation captures the integration of quantum and cognitive principles.

4. Potential Applications (100-150 words):
   a) Suggest two potential applications of your model in natural language processing tasks.
   b) Explain how these applications might outperform classical NLP approaches.

5. Implementation Challenges (100-150 words):
   a) Identify potential challenges in implementing your model.
   b) Propose approaches to overcome these challenges.
   c) Discuss any ethical considerations related to your model.

6. Experimental Design (150-200 words):
   a) Propose an experiment to test a key feature of your model.
   b) Describe the data you would need and how you would collect or generate it.
   c) Outline your methodology and explain how you would analyze the results.

Ensure your response demonstrates a deep understanding of quantum mechanics, cognitive science, and natural language processing. Be creative in your approach while maintaining scientific plausibility and coherence across all sections of your response.

Your total response should be between 850-1150 words.

Format your response with clear headings for each section, as follows:

1. Model Concept:
   [Your content here]

2. Theoretical Framework:
   [Your content here]

3. Mathematical Formulation:
   [Your content here]

4. Potential Applications:
   [Your content here]

5. Implementation Challenges:
   [Your content here]

6. Experimental Design:
   [Your content here]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The Model Concept integrates {t['quantum_concept']['concept']} and {t['cognitive_process']['process']} in a novel and coherent way.",
            "The Theoretical Framework is well-justified and draws on relevant literature.",
            "The Mathematical Formulation is clear and relevant to the model.",
            "The Potential Applications are innovative and well-explained.",
            "Implementation Challenges and ethical considerations are thoughtfully addressed.",
            "The proposed Experimental Design is well-constructed and appropriate for testing the model.",
            "The response demonstrates a deep understanding of quantum mechanics, cognitive science, and NLP.",
            "The ideas presented are creative while maintaining scientific plausibility.",
            "The response follows the specified format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
