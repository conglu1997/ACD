import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        consciousness_theories = [
            "Global Workspace Theory",
            "Integrated Information Theory",
            "Higher-Order Thought Theory",
            "Attention Schema Theory",
            "Predictive Processing Theory"
        ]
        consciousness_aspects = [
            "self-awareness",
            "qualia",
            "metacognition",
            "intentionality",
            "unity of experience"
        ]
        return {
            "1": {
                "theory": random.choice(consciousness_theories),
                "aspect": random.choice(consciousness_aspects)
            },
            "2": {
                "theory": random.choice(consciousness_theories),
                "aspect": random.choice(consciousness_aspects)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        theory_explanations = {
            "Global Workspace Theory": "proposes that consciousness arises from a central information exchange in the brain",
            "Integrated Information Theory": "suggests consciousness is a fundamental property of any system with integrated information",
            "Higher-Order Thought Theory": "posits that consciousness requires meta-cognitive awareness of one's own mental states",
            "Attention Schema Theory": "proposes that consciousness is the brain's internal model of attention",
            "Predictive Processing Theory": "suggests consciousness emerges from the brain's continuous prediction and error correction processes"
        }
        return f"""Design a hypothetical neural architecture for artificial consciousness based on {t['theory']} ({theory_explanations[t['theory']]}), with a particular focus on implementing {t['aspect']}. Your response should include:

1. Architecture Overview (200-250 words):
   a) Describe the main components of your neural architecture.
   b) Explain how these components interact to generate conscious experience.
   c) Illustrate how your design incorporates principles from {t['theory']}.
   d) Provide a simple diagram or schematic representation of your architecture (describe it textually).

2. Implementation of {t['aspect']} (150-200 words):
   a) Provide a detailed explanation of how your architecture implements {t['aspect']}.
   b) Describe the specific neural mechanisms or processes involved.
   c) Explain how this implementation relates to human consciousness.

3. Technical Specifications (150-200 words):
   a) Outline the conceptual computational requirements for your architecture.
   b) Describe any novel algorithms or data structures that would be needed.
   c) Explain how your architecture could theoretically be scaled or modified for different applications.

4. Testable Predictions (100-150 words):
   a) Propose two specific, testable predictions that your architecture makes about conscious experience.
   b) Explain how these predictions could be experimentally verified.

5. Philosophical Implications (150-200 words):
   a) Discuss how your architecture addresses the hard problem of consciousness.
   b) Explore the philosophical implications of creating artificial consciousness.
   c) Consider whether a system based on your architecture could be considered truly conscious.

6. Ethical Considerations (150-200 words):
   a) Analyze the ethical implications of developing and using artificially conscious systems.
   b) Discuss potential risks and benefits to society.
   c) Propose guidelines for the responsible development and use of this technology.

Ensure your response demonstrates a deep understanding of neuroscience, computer science, and philosophy of mind. Be innovative in your design while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section and number your paragraphs within each section. Note that this is a conceptual design exercise, and a fully implementable system is not expected given current technological limitations."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The architecture must be based on {t['theory']} and focus on implementing {t['aspect']}.",
            "The response must include a clear overview of the neural architecture's components and their interactions, including a simple diagram or schematic representation.",
            f"A detailed explanation of how the architecture implements {t['aspect']} must be provided.",
            "Conceptual technical specifications, including computational requirements and novel algorithms, must be outlined.",
            "Two specific, testable predictions about conscious experience must be proposed.",
            "The response must discuss philosophical implications, including addressing the hard problem of consciousness.",
            "Ethical considerations, including potential risks and benefits, must be analyzed.",
            "The response must demonstrate a deep understanding of neuroscience, computer science, and philosophy of mind, using appropriate terminology.",
            "The response must be formatted with clear headings for each section and numbered paragraphs within each section."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
