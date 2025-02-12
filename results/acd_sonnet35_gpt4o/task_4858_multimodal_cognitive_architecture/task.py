import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        problems = [
            {
                'domain': 'Scientific Discovery',
                'problem': 'Proposing a new fundamental particle in physics',
                'constraint': 'Must be consistent with existing Standard Model'
            },
            {
                'domain': 'Artistic Creation',
                'problem': 'Designing a new musical instrument',
                'constraint': 'Must be playable by human hands'
            },
            {
                'domain': 'Technological Innovation',
                'problem': 'Inventing a new form of sustainable energy generation',
                'constraint': 'Must be scalable to meet global energy demands'
            },
            {
                'domain': 'Social Engineering',
                'problem': 'Designing a new form of democratic governance',
                'constraint': 'Must be resistant to corruption and manipulation'
            }
        ]
        return {str(i+1): problem for i, problem in enumerate(random.sample(problems, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a novel cognitive architecture that integrates multiple modes of thought and representation, including verbal, visual, and conceptual processing. Then, apply this architecture to solve the following complex problem in the domain of {t['domain']}:Problem: {t['problem']}Constraint: {t['constraint']}Your response should include the following sections:1. Cognitive Architecture Design (300-350 words):   a) Describe the overall structure and key components of your cognitive architecture.   b) Explain how verbal, visual, and conceptual processing are integrated within the system.   c) Detail any novel features or mechanisms in your architecture.   d) Provide a diagram or pseudocode representation of your architecture (describe it textually).   e) Cite at least two relevant scientific papers to support your design choices.2. Information Processing and Representation (250-300 words):   a) Explain how information is encoded, stored, and retrieved in your architecture.   b) Describe how different types of information (verbal, visual, conceptual) interact and influence each other.   c) Discuss how your architecture handles ambiguity and context-dependent meanings.3. Problem-Solving Approach (300-350 words):   a) Describe how your cognitive architecture would approach the given problem.   b) Explain how different modes of processing contribute to the solution.   c) Detail the steps your architecture would take to generate and evaluate potential solutions.   d) Discuss how the architecture ensures the solution meets the given constraint.4. Comparative Analysis (200-250 words):   a) Compare your architecture to existing cognitive models or AI systems.   b) Discuss potential advantages and limitations of your approach.   c) Explain how your architecture might provide insights into human cognition or inspire new AI techniques.5. Ethical Considerations and Societal Impact (150-200 words):   a) Discuss potential ethical implications of implementing such a cognitive architecture in AI systems.   b) Explore possible societal impacts of using this architecture for complex problem-solving.   c) Propose guidelines for responsible development and use of advanced cognitive architectures.6. Future Research Directions (150-200 words):   a) Suggest two specific research directions to enhance or extend your cognitive architecture.   b) Discuss potential applications of your architecture beyond the given problem domain.   c) Speculate on how this approach might influence our understanding of intelligence and consciousness.7. Limitations and Challenges (200-250 words):   a) Identify and discuss at least three potential limitations or challenges in implementing your proposed cognitive architecture.   b) Suggest possible approaches to address or mitigate these limitations.Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specific problem domain. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.Format your response with clear headings for each section. Your total response should be between 1550-1900 words. Include a word count at the end of your response.Cite all references using APA format. Include a 'References' section at the end of your response (not counted in the word limit) with full citations for all papers mentioned."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science and AI principles, supported by relevant scientific citations.",
            "The proposed cognitive architecture is innovative, well-explained, and effectively integrates verbal, visual, and conceptual processing.",
            "The problem-solving approach using the architecture is logical, detailed, and adequately addresses the given constraint.",
            "The comparative analysis shows critical thinking and awareness of the architecture's position within the field.",
            "The discussion of ethical considerations and societal impact demonstrates a thoughtful approach to responsible AI development.",
            "The identified limitations and challenges show a realistic understanding of the difficulties in implementing advanced cognitive architectures.",
            "The response is well-structured, coherent, and within the specified word count.",
            "The proposed future research directions are innovative and well-reasoned."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
