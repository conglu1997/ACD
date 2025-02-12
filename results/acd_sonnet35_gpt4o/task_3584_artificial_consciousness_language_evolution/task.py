import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'consciousness_model': 'Global Workspace Theory',
                'linguistic_focus': 'Syntax Evolution',
                'cognitive_aspect': 'Working Memory'
            },
            {
                'consciousness_model': 'Integrated Information Theory',
                'linguistic_focus': 'Semantic Development',
                'cognitive_aspect': 'Attention Mechanisms'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a theoretical model for an artificial consciousness system that evolves its own language, integrating principles from linguistics, artificial intelligence, and cognitive science. Your model should incorporate {t['consciousness_model']} as the basis for artificial consciousness, focus on {t['linguistic_focus']} in language evolution, and emphasize the role of {t['cognitive_aspect']} in the process. Your response should include:

1. Consciousness Model Architecture (300-350 words):
   a) Describe the key components of your artificial consciousness system based on {t['consciousness_model']}.
   b) Explain how this model supports the emergence of language.
   c) Discuss how {t['cognitive_aspect']} is integrated into the consciousness model.
   d) Provide a high-level diagram or detailed description of your system's architecture.

2. Language Evolution Mechanism (250-300 words):
   a) Detail the process by which your system evolves language, focusing on {t['linguistic_focus']}.
   b) Explain how this process is influenced by the consciousness model and {t['cognitive_aspect']}.
   c) Describe any novel algorithms or techniques you've incorporated for language evolution.

3. Cognitive-Linguistic Interface (200-250 words):
   a) Explain how your system integrates cognitive processes, particularly {t['cognitive_aspect']}, with language evolution.
   b) Discuss how this integration influences the development of linguistic structures and meaning.
   c) Provide an example of how a specific cognitive process might shape a linguistic feature in your system.

4. Simulated Evolution Scenario (250-300 words):
   a) Describe a hypothetical scenario of your system evolving language over time.
   b) Explain key stages or milestones in this evolution, particularly related to {t['linguistic_focus']}.
   c) Discuss how the evolved language reflects aspects of the underlying consciousness model.

5. Comparative Analysis (200-250 words):
   a) Compare your model to existing theories of language evolution and artificial consciousness.
   b) Discuss how your approach contributes uniquely to our understanding of consciousness and language.
   c) Analyze potential implications of your model for theories of human consciousness and language acquisition.

6. Ethical Considerations and Implications (150-200 words):
   a) Discuss ethical considerations in creating artificially conscious systems that evolve their own language.
   b) Explore potential implications for human-AI interaction and communication.
   c) Address concerns about the autonomy and rights of such systems.

7. Experimental Proposal (150-200 words):
   a) Propose a method to test or validate aspects of your theoretical model.
   b) Describe expected results and how they would support your model.
   c) Discuss any technical or philosophical challenges in implementing such an experiment.

Ensure your response demonstrates a deep understanding of consciousness theories, linguistics, artificial intelligence, and cognitive science. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of the specified consciousness model, linguistic focus, and cognitive aspect.",
            "The proposed artificial consciousness system and language evolution mechanism are innovative yet scientifically plausible.",
            "The response effectively integrates principles from linguistics, artificial intelligence, and cognitive science.",
            "The simulated evolution scenario and comparative analysis show thoughtful consideration of the model's implications.",
            "Ethical considerations and experimental proposals are well-reasoned and relevant.",
            "The response is well-structured, clear, and uses appropriate technical terminology.",
            "The response adheres to the specified word limit and format guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
