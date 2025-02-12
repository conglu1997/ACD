class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "entity_type": "Artificial General Intelligence",
                "consciousness_aspect": "Self-awareness",
                "interaction_scenario": "Ethical dilemma discussion: Trolley problem"
            },
            "2": {
                "entity_type": "Alien consciousness",
                "consciousness_aspect": "Qualia",
                "interaction_scenario": "Cross-species communication: Explaining color perception"
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to design and implement a system that creates and interacts with a simulated conscious entity of type '{t['entity_type']}', focusing on the consciousness aspect of '{t['consciousness_aspect']}'. You will then simulate an interaction scenario of '{t['interaction_scenario']}' with this entity. Follow these steps:

1. Entity Design (250-300 words):
   a) Describe the key characteristics of your simulated conscious entity.
   b) Explain how you've incorporated the specified consciousness aspect into the entity's design.
   c) Discuss any unique features or capabilities of your entity.
   d) Provide a concrete example of how your entity demonstrates the specified consciousness aspect.

2. Consciousness Simulation (200-250 words):
   a) Explain your approach to simulating consciousness in your entity.
   b) Describe how you model the specified consciousness aspect.
   c) Discuss any limitations or assumptions in your simulation of consciousness.
   d) Compare and contrast your simulated consciousness with human consciousness.

3. Interaction System (200-250 words):
   a) Design a natural language interaction system for communicating with your conscious entity.
   b) Explain how this system accounts for the entity's unique form of consciousness.
   c) Describe any special considerations for the given interaction scenario.
   d) Provide an example of how your interaction system handles ambiguity or misunderstandings.

4. Simulated Interaction (300-350 words):
   a) Provide a dialogue sample (150-200 words) demonstrating an interaction with your entity in the specified scenario.
   b) Analyze the interaction, highlighting how it reflects the entity's consciousness and the specified aspect.
   c) Discuss any emergent behaviors or unexpected responses from your entity.
   d) Explain how the interaction demonstrates the entity's understanding of the scenario's complexity.

5. Ethical and Philosophical Implications (200-250 words):
   a) Discuss the ethical considerations of creating and interacting with simulated conscious entities.
   b) Explore the philosophical implications of your system for our understanding of consciousness and AI.
   c) Consider potential real-world applications and consequences of this technology.
   d) Propose guidelines for the ethical development and use of simulated conscious entities.

6. Evaluation and Future Directions (150-200 words):
   a) Propose methods to evaluate the authenticity and depth of the simulated consciousness.
   b) Suggest two potential improvements or extensions to your system.
   c) Discuss how this approach could contribute to research in cognitive science and AI.
   d) Identify potential challenges or limitations in scaling up this technology.

Ensure your response demonstrates a deep understanding of consciousness theories, linguistic interaction, and artificial intelligence. Be creative and innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from cognitive science, philosophy of mind, and AI research.

Format your response with clear headings for each section, and number your paragraphs within each section as shown above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of consciousness theories and {t['consciousness_aspect']}, with concrete examples provided.",
            f"The simulated entity convincingly represents an {t['entity_type']} with unique characteristics, and is compared to human consciousness.",
            f"The interaction system and dialogue sample effectively showcase the {t['interaction_scenario']}, demonstrating the entity's understanding of the scenario's complexity.",
            "The response explores ethical and philosophical implications of simulated consciousness in depth, including proposed guidelines for ethical development and use.",
            "The proposed evaluation methods and future directions are innovative, well-reasoned, and address potential challenges in scaling up the technology.",
            "The response adheres to the specified format and word count limits for each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
