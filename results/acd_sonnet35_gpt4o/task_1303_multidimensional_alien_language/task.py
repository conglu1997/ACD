import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        concepts = [
            'The interconnectedness of all things across spacetime',
            'The simultaneous experience of past, present, and future'
        ]
        return {
            str(i+1): {'concept': concept}
            for i, concept in enumerate(concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel communication system for an advanced alien civilization capable of perceiving and manipulating multiple dimensions, then use it to translate the complex abstract concept: '{t['concept']}'. Your response should include the following sections:

1. Communication System Design (300-350 words):
   a) Describe the key features of your multidimensional communication system.
   b) Explain how it incorporates extra-dimensional perception and manipulation.
   c) Detail at least three unique aspects of the system that differ from human language.
   d) Provide a brief example of how a simple message would be conveyed in this system.

2. Linguistic and Cognitive Principles (200-250 words):
   a) Explain the linguistic and cognitive principles underlying your communication system.
   b) Discuss how these principles relate to the aliens' multidimensional nature.
   c) Compare and contrast these principles with those found in human languages and cognition.

3. Concept Translation (250-300 words):
   a) Translate the given abstract concept into your alien communication system.
   b) Explain the translation process and any challenges encountered.
   c) Describe how the multidimensional aspects of the system enhance the expression of this concept.
   d) Provide at least one concrete example or metaphor to illustrate the translated concept.

4. Implications and Analysis (200-250 words):
   a) Discuss the implications of this communication system for the aliens' society and thought processes.
   b) Analyze how this system might influence the aliens' understanding of the universe.
   c) Explore potential misunderstandings that could arise in human-alien communication using this system.

5. Scientific and Philosophical Significance (150-200 words):
   a) Explain how this communication system could inform human understanding of language, cognition, and the nature of reality.
   b) Propose an experiment or study that could validate or explore aspects of your communication system.

Ensure your response demonstrates a deep understanding of linguistics, cognitive science, and physics. Use appropriate terminology and provide clear explanations. Be creative in your approach while maintaining scientific plausibility. Format your response using clear headings for each section, numbered as above.

Your total response should be between 1100-1350 words. You will be scored based on the creativity, coherence, and scientific plausibility of your response, with a maximum score of 1.0 for exceptional answers."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of linguistics, cognitive science, and physics.",
            "The communication system design is innovative, coherent, and plausibly incorporates multidimensional aspects.",
            "The linguistic and cognitive principles are well-explained and logically connected to the system design.",
            "The concept translation effectively uses the designed communication system and addresses the challenges involved.",
            "The implications and analysis section provides insightful discussion on the impact of the communication system.",
            "The scientific and philosophical significance is thoughtfully explored with a plausible experimental proposal.",
            "The response is well-structured, following the specified format and word count guidelines.",
            "The proposed system is creative and novel while maintaining scientific plausibility.",
            "The response effectively addresses the specific abstract concept given in the task.",
            "Concrete examples or metaphors are used to illustrate the translated concept."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
