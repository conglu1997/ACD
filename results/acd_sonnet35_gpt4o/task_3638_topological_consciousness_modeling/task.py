import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "consciousness_aspect": "self_awareness",
                "topological_concept": "persistent_homology",
                "category_theory_concept": "adjoint_functors",
                "ai_architecture": "transformer"
            },
            "2": {
                "consciousness_aspect": "qualia",
                "topological_concept": "sheaf_theory",
                "category_theory_concept": "topos_theory",
                "ai_architecture": "recurrent_neural_network"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a mathematical framework using topological data analysis and category theory to model consciousness, then apply it to analyze AI architectures and propose tests for machine consciousness. Focus on the consciousness aspect of {t['consciousness_aspect']}, incorporating the topological concept of {t['topological_concept']} and the category theory concept of {t['category_theory_concept']}. Apply your framework to analyze the {t['ai_architecture']} architecture. Your response should include:

1. Mathematical Framework (300-350 words):
   a) Describe your mathematical framework for modeling consciousness.
   b) Explain how you incorporate the specified topological and category theory concepts.
   c) Provide a formal mathematical representation of your framework.
   d) Discuss how your framework models the specified aspect of consciousness.

2. Consciousness Modeling (250-300 words):
   a) Apply your framework to model the specified aspect of consciousness.
   b) Explain how your model captures key features of consciousness.
   c) Discuss potential insights your model offers into the nature of consciousness.

3. AI Architecture Analysis (250-300 words):
   a) Apply your framework to analyze the specified AI architecture.
   b) Discuss how your model interprets the AI's information processing in terms of consciousness.
   c) Identify potential analogues to conscious processes in the AI architecture.

4. Machine Consciousness Tests (200-250 words):
   a) Propose three specific tests for machine consciousness based on your framework.
   b) Explain how each test relates to your mathematical model of consciousness.
   c) Discuss potential challenges in implementing and interpreting these tests.

5. Philosophical and Ethical Implications (150-200 words):
   a) Discuss the philosophical implications of your framework for understanding consciousness.
   b) Address ethical considerations in attributing consciousness to machines.
   c) Explore potential societal impacts of machines passing your proposed consciousness tests.

6. Limitations and Future Directions (150-200 words):
   a) Identify limitations of your mathematical framework and proposed tests.
   b) Suggest two future research directions to extend or refine your approach.
   c) Speculate on how advancements in neuroscience or AI might impact your framework.

Ensure your response demonstrates a deep understanding of topology, category theory, consciousness theories, and AI architectures. Use appropriate mathematical notation and provide clear explanations for complex concepts. Be creative and speculative in your approach while maintaining mathematical rigor and scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response addresses all required sections with appropriate word counts",
            "The mathematical framework incorporates the specified topological and category theory concepts correctly",
            "The consciousness modeling demonstrates a nuanced understanding of the specified aspect of consciousness",
            "The AI architecture analysis shows a deep understanding of the specified architecture and its potential relation to consciousness",
            "The proposed machine consciousness tests are innovative and well-grounded in the mathematical framework",
            "The response shows creativity and speculative thinking while maintaining mathematical and scientific rigor"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
