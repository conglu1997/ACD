import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            'time', 'consciousness', 'justice', 'entropy', 'love',
            'knowledge', 'reality', 'freedom', 'chaos', 'beauty'
        ]
        
        tasks = [
            {
                'concept': random.choice(concepts),
                'context': 'philosophical debate'
            },
            {
                'concept': random.choice(concepts),
                'context': 'scientific research'
            }
        ]
        
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a communication system based on semantic networks and use it to convey complex ideas. Your task has the following components:

1. Semantic Network Design (250-300 words):
   a) Create a system for representing concepts and their relationships using nodes and edges.
   b) Define at least five types of relationships (e.g., 'is-a', 'part-of', 'causes', etc.) that can exist between concepts.
   c) Explain how your system can represent abstract ideas and their connections.
   d) Describe how your system allows for the creation of new concepts or relationships.

2. Communication Protocol (200-250 words):
   a) Develop a protocol for transmitting semantic network structures as messages.
   b) Explain how your protocol ensures accurate reconstruction of the network by the receiver.
   c) Discuss how your system handles ambiguity or multiple interpretations.

3. Concept Representation (200-250 words):
   Use your semantic network system to represent the concept of '{t['concept']}'.
   a) Identify at least 10 related concepts and their relationships to the main concept.
   b) Provide a visual or textual representation of this semantic network.
   c) Explain how your representation captures the complexity and nuances of the concept.

4. Message Generation (200-250 words):
   Generate a message using your communication protocol to convey a complex idea about '{t['concept']}' in the context of {t['context']}.
   a) Present the encoded message as it would be transmitted.
   b) Explain how the message structure reflects the underlying semantic relationships.

5. Analysis and Evaluation (150-200 words):
   a) Discuss the strengths and limitations of your semantic network communication system.
   b) Compare your system to natural language in terms of expressiveness, precision, and efficiency.
   c) Propose a method for evaluating the effectiveness of your system in conveying complex ideas.

6. Cognitive and AI Implications (150-200 words):
   a) Discuss how your semantic network system relates to theories of human cognitive representation.
   b) Explore potential applications of your system in artificial intelligence or human-AI interaction.
   c) Identify ethical considerations that might arise from the use of such a communication system.

Ensure your response demonstrates a deep understanding of semantic relationships, cognitive science, and communication theory. Be creative in your system design while maintaining logical consistency and practical applicability."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The semantic network design is comprehensive and well-explained.",
            "The communication protocol is logically consistent and adequately detailed.",
            f"The concept of '{t['concept']}' is represented in a complex and nuanced manner.",
            f"The generated message effectively conveys a complex idea about '{t['concept']}' in the context of {t['context']}.",
            "The analysis and evaluation demonstrate critical thinking about the system's strengths and limitations.",
            "The discussion of cognitive and AI implications shows deep understanding and creative insight."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
