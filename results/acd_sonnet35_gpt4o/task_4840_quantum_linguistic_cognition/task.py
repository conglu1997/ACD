import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "quantum_principle": "Superposition",
                "linguistic_feature": "Polysemy",
                "cognitive_process": "Semantic memory retrieval",
                "nlp_task": "Word sense disambiguation"
            },
            {
                "quantum_principle": "Entanglement",
                "linguistic_feature": "Syntactic dependencies",
                "cognitive_process": "Working memory",
                "nlp_task": "Parsing"
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework that applies the quantum principle of {t['quantum_principle']} to the linguistic feature of {t['linguistic_feature']}, considering the cognitive process of {t['cognitive_process']}. Then, use this framework to develop a novel approach to the NLP task of {t['nlp_task']}. Your response should include:

1. Theoretical Framework (300-350 words):
   a) Explain how the quantum principle of {t['quantum_principle']} can be applied to linguistic cognition, specifically in relation to {t['linguistic_feature']}.
   b) Describe how this quantum-linguistic model interfaces with the cognitive process of {t['cognitive_process']}.
   c) Provide a visual representation (described in text) of your theoretical framework.
   d) Discuss potential implications of this framework for our understanding of language and cognition.

2. Quantum-Linguistic Model (250-300 words):
   a) Develop a formal model that represents linguistic entities and processes using quantum-inspired mathematics.
   b) Explain how your model captures the key aspects of {t['linguistic_feature']} using quantum principles.
   c) Describe how your model accounts for the role of {t['cognitive_process']} in language processing.

3. NLP Application (300-350 words):
   a) Apply your quantum-linguistic framework to the NLP task of {t['nlp_task']}.
   b) Describe a novel algorithm or approach for this task based on your framework.
   c) Explain how your approach differs from classical methods for {t['nlp_task']}.
   d) Discuss potential advantages and challenges of your quantum-inspired approach.

4. Experimental Design (200-250 words):
   a) Propose an experiment to test the effectiveness of your quantum-linguistic approach to {t['nlp_task']}.
   b) Describe your methodology, including data collection and analysis techniques.
   c) Discuss how you would compare your approach to state-of-the-art classical methods.

5. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the ethical implications of applying quantum principles to understanding human language and cognition.
   b) Explore the philosophical questions raised by your framework, particularly regarding the nature of meaning and understanding.
   c) Consider potential societal impacts of advanced quantum-inspired NLP systems.

Ensure your response demonstrates a deep understanding of quantum physics, linguistics, cognitive science, and natural language processing. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1250-1500 words. Include a word count at the end of your submission."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response includes all five required sections with appropriate content and length.",
            f"The theoretical framework effectively integrates the quantum principle of {t['quantum_principle']} with the linguistic feature of {t['linguistic_feature']} and the cognitive process of {t['cognitive_process']}.",
            "The quantum-linguistic model is formally described and clearly relates to the specified linguistic and cognitive elements.",
            f"The NLP application presents a novel approach to {t['nlp_task']} based on the quantum-linguistic framework.",
            "The experimental design is well-thought-out and appropriate for testing the proposed approach.",
            "The ethical and philosophical implications are thoughtfully considered and relevant to the proposed framework.",
            "The response demonstrates a deep understanding of quantum physics, linguistics, cognitive science, and natural language processing.",
            "The ideas presented are innovative while maintaining scientific plausibility."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
