import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_domains = [
            "Journey",
            "War",
            "Machine",
            "Container",
            "Balance"
        ]
        target_domains = [
            "Love",
            "Time",
            "Mind",
            "Life",
            "Argument"
        ]
        knowledge_fields = [
            "Psychology",
            "Economics",
            "Physics",
            "Biology",
            "Computer Science"
        ]
        
        tasks = [
            {
                "source_domain": source,
                "target_domain": target,
                "knowledge_field": field
            }
            for source in source_domains
            for target in target_domains
            for field in knowledge_fields
        ]
        
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of understanding and generating conceptual metaphors across different domains of knowledge. Then, apply your system to generate and analyze conceptual metaphors using the following parameters:

Source domain: {t['source_domain']}
Target domain: {t['target_domain']}
Knowledge field for novel metaphor generation: {t['knowledge_field']}

Your response should include:

1. Conceptual Metaphor AI System Design (300-350 words):
   a) Explain the key principles of conceptual metaphor theory.
   b) Describe the architecture of your AI system, including components for understanding, analyzing, and generating conceptual metaphors.
   c) Detail how your system represents and processes source and target domains.
   d) Explain how your system integrates knowledge from various fields to generate novel metaphors.

2. Metaphor Analysis (250-300 words):
   a) Analyze the given source-target domain pair ({t['source_domain']} - {t['target_domain']}).
   b) Identify and explain common conceptual metaphors that link these domains.
   c) Discuss how these metaphors shape our understanding of the target domain.
   d) Describe how your AI system would process and represent these metaphors.

3. Novel Metaphor Generation (250-300 words):
   a) Use your AI system to generate a novel conceptual metaphor that links the given target domain ({t['target_domain']}) with concepts from {t['knowledge_field']}.
   b) Explain the generated metaphor in detail, including its mappings and entailments.
   c) Discuss how this novel metaphor provides new insights into the target domain.
   d) Describe the process your AI system used to generate this metaphor.

4. Cross-domain Reasoning (200-250 words):
   a) Demonstrate how your AI system would use the generated metaphor to reason about a problem or concept in the target domain.
   b) Provide an example of how this metaphorical reasoning might lead to new hypotheses or solutions.
   c) Discuss the potential benefits and limitations of using such metaphorical reasoning in {t['knowledge_field']}.

5. Evaluation and Refinement (200-250 words):
   a) Propose a method for evaluating the quality and novelty of the generated metaphors.
   b) Describe how your AI system could refine and improve its metaphor generation based on feedback.
   c) Discuss potential challenges in evaluating metaphor quality across different cultures or knowledge domains.

6. Ethical and Societal Implications (150-200 words):
   a) Discuss potential ethical implications of an AI system capable of generating and analyzing conceptual metaphors.
   b) Consider how such a system might influence human creativity, language use, or problem-solving.
   c) Propose guidelines for responsible development and use of conceptual metaphor AI systems.

7. Conclusion (50-100 words):
   Summarize the key aspects of your conceptual metaphor AI system, its potential impact, and the most significant insights gained from applying it to the given scenario.

Ensure your response demonstrates a deep understanding of cognitive linguistics, artificial intelligence, and the specified knowledge field. Be creative and innovative while maintaining scientific rigor. Your total response should be between 1400-1750 words.

Format your response with clear headings for each section, numbered as above. Use appropriate subheadings where necessary to organize your thoughts clearly."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a comprehensive understanding of conceptual metaphor theory and AI system design.",
            "The analysis of the given source-target domain pair is thorough and insightful.",
            "The novel metaphor generated is creative, coherent, and effectively integrates concepts from the specified knowledge field.",
            "The cross-domain reasoning example is well-explained and demonstrates the potential of metaphorical thinking in problem-solving.",
            "The evaluation method and refinement process for the AI system are well-thought-out and practical.",
            "The discussion of ethical and societal implications is balanced and considers multiple perspectives.",
            "The overall response is well-structured, clear, and demonstrates interdisciplinary knowledge integration.",
            "The conclusion effectively summarizes the key aspects of the system and its potential impact."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0