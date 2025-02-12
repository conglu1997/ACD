import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            {
                "concept": "Time",
                "domain": "Philosophy",
                "constraint": "Must incorporate elements of both linearity and cyclicality"
            },
            {
                "concept": "Democracy",
                "domain": "Political Science",
                "constraint": "Must represent both individual and collective aspects"
            },
            {
                "concept": "Consciousness",
                "domain": "Cognitive Science",
                "constraint": "Must depict both unity and multiplicity of experience"
            },
            {
                "concept": "Quantum Entanglement",
                "domain": "Physics",
                "constraint": "Must illustrate non-locality and instantaneous correlation"
            }
        ]
        return {
            "1": random.choice(concepts),
            "2": random.choice(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and interpreting abstract visual representations of complex ideas, focusing on the concept of {t['concept']} from the domain of {t['domain']}. Your system should mimic human use of metaphors and analogies in visual form. Address the following points in your response:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for generating and interpreting visual concept maps.
   b) Explain how your system integrates knowledge from {t['domain']} with principles of visual design and cognitive science.
   c) Detail how the system ensures that the generated visual representations are both abstract and meaningful.
   d) Address the following constraint in your design: {t['constraint']}

2. Visual Representation Generation (200-250 words):
   a) Explain the process your AI system uses to create a visual representation of {t['concept']}.
   b) Describe how the system incorporates metaphors and analogies in its visual output.
   c) Provide a textual description of the visual representation your system would generate for {t['concept']}.

3. Interpretation Mechanism (200-250 words):
   a) Detail how your AI system would interpret and extract meaning from the visual representation it generated.
   b) Explain how the system handles ambiguity and multiple possible interpretations.
   c) Describe a method for evaluating the accuracy and meaningfulness of the system's interpretations.

4. Cognitive Science Integration (150-200 words):
   a) Discuss how your system's approach relates to human cognitive processes for understanding abstract concepts.
   b) Explain how the system accounts for cultural and individual differences in conceptual understanding.
   c) Propose a method for comparing the system's visual representations with human-generated metaphors and analogies.

5. Practical Applications and Implications (150-200 words):
   a) Suggest two potential applications of your visual concept mapping AI system.
   b) Discuss the implications of such a system for fields like education, scientific research, or cross-cultural communication.
   c) Address potential ethical considerations or challenges in implementing and using this technology.

6. Future Developments (100-150 words):
   a) Propose an innovative extension or improvement to your AI system.
   b) Explain how this enhancement could overcome current limitations in AI understanding of abstract concepts.
   c) Speculate on how this technology might evolve and impact human-AI interaction in the next decade.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the chosen concept's domain. Use appropriate terminology and provide clear explanations for complex ideas. Be creative in your system design while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1050-1350 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of cognitive science, AI, and visual communication principles.",
            f"The proposed system architecture effectively integrates knowledge from {t['domain']} with visual design and cognitive science principles.",
            f"The visual representation generation process for {t['concept']} is well-explained and incorporates metaphors and analogies.",
            "The interpretation mechanism is clearly described, including methods for handling ambiguity and evaluating accuracy.",
            "The response effectively relates the system's approach to human cognitive processes and accounts for cultural differences.",
            "Practical applications and implications are thoughtfully discussed, including ethical considerations.",
            "The future developments section demonstrates foresight and creativity in extending the technology.",
            f"The design addresses the given constraint: {t['constraint']}",
            "The response is well-structured with clear headings for each section as requested."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
