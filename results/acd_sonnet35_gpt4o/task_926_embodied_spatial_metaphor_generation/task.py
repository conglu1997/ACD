import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Quantum Physics",
            "Economic Theory",
            "Social Psychology",
            "Environmental Science"
        ]
        spatial_relations = [
            "containment",
            "path",
            "force",
            "balance"
        ]
        return {
            str(i+1): {
                'domain': random.choice(domains),
                'spatial_relation': random.choice(spatial_relations)
            } for i in range(2)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that generates and interprets spatial metaphors based on principles of embodied cognition, then apply it to explain abstract concepts in the domain of {t['domain']} using the spatial relation of {t['spatial_relation']}. Your response should include:

1. Theoretical Framework (200-250 words):
   a) Explain the key principles of embodied cognition relevant to spatial reasoning and metaphor generation.
   b) Describe how the spatial relation of {t['spatial_relation']} is typically experienced and conceptualized in human cognition.
   c) Discuss how embodied experiences of {t['spatial_relation']} might influence abstract thinking in the domain of {t['domain']}.

2. AI System Design (250-300 words):
   a) Outline the architecture of your AI system, including its main components and their interactions.
   b) Explain how your system incorporates principles of embodied cognition and spatial reasoning.
   c) Describe the process of generating spatial metaphors, including any constraints or guidelines.
   d) Detail how your system would interpret and evaluate the generated metaphors.
   e) Include a high-level diagram or pseudocode to illustrate your system's architecture.

3. Metaphor Generation and Application (200-250 words):
   a) Use your AI system to generate three distinct spatial metaphors based on {t['spatial_relation']} to explain abstract concepts in {t['domain']}.
   b) Present each metaphor and provide a brief explanation of how it relates to the abstract concept.
   c) Analyze how each metaphor reflects principles of embodied cognition and spatial reasoning.

4. Cross-domain Implications (150-200 words):
   a) Discuss how spatial metaphors based on {t['spatial_relation']} might influence understanding and problem-solving in {t['domain']}.
   b) Explore potential benefits and limitations of using these spatial metaphors in the given domain.
   c) Propose an experiment to test whether exposure to these spatial metaphors affects problem-solving in {t['domain']}.

5. Ethical and Cognitive Considerations (150-200 words):
   a) Discuss potential biases or limitations in using embodied spatial metaphors for abstract concepts.
   b) Explore how cultural differences in spatial experiences might affect the universality of these metaphors.
   c) Consider the ethical implications of using AI-generated embodied metaphors in education or decision-making processes.

6. Future Directions and Expansions (150-200 words):
   a) Propose two ways to expand your AI system to incorporate other aspects of embodied cognition.
   b) Suggest how your system could be adapted to generate metaphors for multimodal or sensory experiences.
   c) Discuss the potential implications of this research for developing more human-like AI systems.

Ensure your response demonstrates a deep understanding of embodied cognition, spatial reasoning, and the chosen domain. Use appropriate terminology and provide clear explanations where necessary. Be creative in your approach while maintaining scientific plausibility. Your total response should be between 1100-1400 words.
"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of embodied cognition, spatial reasoning, and the specified domain",
            "The AI system design is clearly explained and incorporates principles of embodied cognition and spatial reasoning",
            "The generated spatial metaphors are creative, relevant to the domain, and reflect the specified spatial relation",
            "The cross-domain implications and ethical considerations are thoroughly explored",
            "The response shows creativity and speculative thinking while maintaining scientific plausibility"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
