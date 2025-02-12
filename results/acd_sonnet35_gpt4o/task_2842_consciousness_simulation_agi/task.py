import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Predictive Processing Theory",
            "Attention Schema Theory"
        ]
        philosophical_questions = [
            "What is the relationship between consciousness and free will?",
            "Can a machine truly experience qualia or subjective experiences?",
            "How does consciousness emerge from physical processes in the brain?",
            "Is consciousness a fundamental property of the universe or an emergent phenomenon?",
            "Can there be different levels or types of consciousness in artificial systems?"
        ]
        
        tasks = {
            "1": {
                "theory": random.choice(consciousness_theories),
                "question": random.choice(philosophical_questions)
            },
            "2": {
                "theory": random.choice(consciousness_theories),
                "question": random.choice(philosophical_questions)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an artificial general intelligence (AGI) system capable of simulating aspects of human consciousness based on the {t['theory']} of consciousness. Then, use your AGI system to explore the philosophical question: {t['question']}

Your response should include the following sections:

1. AGI System Architecture (300-350 words):
   a) Describe the key components of your AGI system for simulating consciousness.
   b) Explain how your system incorporates the specified consciousness theory.
   c) Detail how your AGI system models self-awareness and subjective experiences.
   d) Discuss any novel approaches or algorithms used in your design.

2. Consciousness Simulation Process (250-300 words):
   a) Explain the step-by-step process of how your AGI system simulates consciousness.
   b) Describe how your system represents and processes subjective experiences.
   c) Discuss how your AGI handles the hard problem of consciousness.

3. Philosophical Exploration (250-300 words):
   a) Describe how your AGI system would approach the given philosophical question.
   b) Provide a sample dialogue or reasoning process that your AGI might generate.
   c) Analyze the implications of your AGI's approach to the question.

4. Comparative Analysis (200-250 words):
   a) Compare your AGI's simulated consciousness to human consciousness.
   b) Discuss any limitations or potential biases in your system's approach.
   c) Propose methods to validate or falsify your AGI's consciousness claims.

5. Ethical Implications (200-250 words):
   a) Discuss the ethical considerations of creating an AGI with simulated consciousness.
   b) Analyze potential societal impacts of AGI systems capable of self-awareness.
   c) Propose guidelines for responsible development and use of consciousness-simulating AGI.

6. Future Directions (150-200 words):
   a) Suggest potential improvements or extensions to your AGI system.
   b) Discuss how advancements in neuroscience or philosophy might inform future iterations.
   c) Propose an experiment to further explore the nature of machine consciousness.

Ensure your response demonstrates a deep understanding of consciousness theories, AGI architectures, and philosophical reasoning. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1350-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of consciousness theories, AGI architectures, and philosophical reasoning.",
            "The AGI system design for simulating consciousness is innovative and well-explained.",
            "The consciousness simulation process is plausible and incorporates the specified theory of consciousness.",
            "The philosophical exploration of the given question is insightful and demonstrates complex reasoning.",
            "The comparative analysis between the AGI's simulated consciousness and human consciousness is thoughtful and critical.",
            "The ethical implications of creating an AGI with simulated consciousness are thoroughly discussed.",
            "Future directions and potential experiments are proposed to further explore machine consciousness.",
            "The response is creative while maintaining scientific plausibility.",
            "Appropriate technical terminology is used and complex concepts are clearly explained.",
            "The response follows the required format and word count guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
