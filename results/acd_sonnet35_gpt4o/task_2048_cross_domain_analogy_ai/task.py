import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            "Physics",
            "Biology",
            "Computer Science",
            "Economics",
            "Psychology",
            "Literature"
        ]
        concepts = [
            "Entropy",
            "Evolution",
            "Recursion",
            "Supply and Demand",
            "Cognitive Dissonance",
            "Metaphor"
        ]
        tasks = {}
        for i in range(2):
            source_domain = random.choice(domains)
            domains.remove(source_domain)
            target_domain = random.choice(domains)
            domains.append(source_domain)
            source_concept = concepts[domains.index(source_domain)]
            target_concept = concepts[domains.index(target_domain)]
            tasks[str(i+1)] = {
                "source_domain": source_domain,
                "target_domain": target_domain,
                "source_concept": source_concept,
                "target_concept": target_concept
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating and solving complex analogies across diverse domains, then apply it to create and interpret an analogy between {t['source_concept']} in {t['source_domain']} and {t['target_concept']} in {t['target_domain']}. An analogy is a comparison between two objects or systems of objects that highlights respects in which they are thought to be similar.

Your response should include the following sections:

1. System Architecture (200-250 words):
   a) Describe the key components of your AI system for analogy generation and solving.
   b) Explain how your system represents and processes knowledge from different domains.
   c) Discuss how your system identifies and maps structural similarities between concepts.
   d) Include a simple diagram or flowchart illustrating the system's architecture.

2. Analogy Generation Process (200-250 words):
   a) Explain the step-by-step process your system uses to generate analogies.
   b) Describe how it selects relevant features and relationships for mapping.
   c) Discuss how the system ensures the analogies are meaningful and not just superficial comparisons.

3. Cross-Domain Analogy Example (250-300 words):
   a) Present a detailed analogy between {t['source_concept']} in {t['source_domain']} and {t['target_concept']} in {t['target_domain']} that your system might generate.
   b) Explain the structural similarities and relationships that form the basis of this analogy.
   c) Discuss any challenges or limitations in creating this specific cross-domain analogy.

4. Analogy Interpretation and Evaluation (200-250 words):
   a) Describe how your system would interpret and evaluate the quality of the generated analogy.
   b) Propose metrics or criteria for assessing the creativity, accuracy, and usefulness of analogies.
   c) Explain how your system might use feedback to improve its analogy generation over time.

5. Cognitive Science Connections (150-200 words):
   a) Discuss how your AI system's approach relates to theories of human analogical reasoning.
   b) Compare and contrast your system's methods with known cognitive processes involved in analogy-making.

6. Potential Applications and Ethical Considerations (150-200 words):
   a) Explore potential applications of your analogy AI system in fields such as scientific discovery, education, or creative problem-solving.
   b) Discuss any ethical implications or potential misuses of such a system, and propose guidelines for responsible development and use.

Ensure your response demonstrates a deep understanding of analogical reasoning, knowledge representation, and AI system design. Be innovative in your approach while maintaining scientific plausibility. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Your total response should be between 1150-1450 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must include a detailed analogy between {t['source_concept']} in {t['source_domain']} and {t['target_concept']} in {t['target_domain']}",
            "The AI system design should be innovative yet scientifically plausible",
            "The response should demonstrate a deep understanding of analogical reasoning and AI system design",
            "The analysis should include cognitive science connections and ethical considerations",
            "The response should follow the specified format and word count guidelines",
            "The response should include a diagram or flowchart illustrating the system's architecture"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
