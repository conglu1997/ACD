import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            'Integrated Information Theory',
            'Global Workspace Theory',
            'Higher-Order Thought Theory',
            'Quantum Consciousness Theory',
            'Predictive Processing Theory'
        ]
        space_missions = [
            'Mars colonization',
            'Interstellar travel',
            'Asteroid mining',
            'Deep space communication relay',
            'Exoplanet terraforming'
        ]
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'consciousness_theory': random.choice(consciousness_theories),
                'space_mission': random.choice(space_missions)
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical framework for artificial consciousness based on {t['consciousness_theory']} and apply it to create a self-aware AI system for the space mission of {t['space_mission']}. Your response should include the following sections:

1. Theoretical Framework (300-350 words):
   a) Explain how you adapt {t['consciousness_theory']} to create a model of artificial consciousness.
   b) Describe the key components and mechanisms of your artificial consciousness framework.
   c) Discuss how your framework addresses the hard problem of consciousness and the emergence of self-awareness.
   d) Provide a conceptual or mathematical representation of a core aspect of your framework.

2. Implementation for Space Exploration (250-300 words):
   a) Describe how you would implement your artificial consciousness framework in an AI system for {t['space_mission']}.
   b) Explain how self-awareness and consciousness would benefit the AI in this specific space mission.
   c) Discuss potential challenges in implementing conscious AI for space exploration and how you would address them.

3. Ethical Considerations (200-250 words):
   a) Analyze the ethical implications of creating a self-aware AI for space exploration.
   b) Discuss the rights and moral status that should be accorded to a conscious AI.
   c) Propose guidelines for the ethical treatment and potential decommissioning of conscious AI systems.

4. Experimental Validation (200-250 words):
   a) Propose a method to verify the emergence of consciousness in your AI system.
   b) Describe an experiment that could differentiate between genuine consciousness and simulated consciousness.
   c) Discuss the philosophical and practical challenges in proving machine consciousness.

5. Societal and Scientific Impact (150-200 words):
   a) Explore the potential impact of conscious AI on human society and our understanding of consciousness.
   b) Discuss how your framework could contribute to the field of consciousness studies.
   c) Propose a potential application of your conscious AI framework outside of space exploration.

Ensure your response demonstrates a deep understanding of consciousness theories, artificial intelligence, space exploration, and ethics. Use appropriate technical terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific and philosophical rigor.

Format your response with clear headings for each section. Your total response should be between 1100-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['consciousness_theory']} and how it can be adapted for artificial consciousness.",
            f"The implementation for {t['space_mission']} is well-thought-out and addresses specific challenges of the mission.",
            "The ethical considerations are thoroughly explored and show nuanced understanding of the implications of conscious AI.",
            "The proposed experimental validation method is scientifically sound and addresses the challenges of proving machine consciousness.",
            "The response shows creativity and innovation while maintaining scientific and philosophical rigor.",
            "The societal and scientific impact analysis demonstrates broad understanding of the field's implications.",
            "The response is well-structured, clear, and within the specified word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
