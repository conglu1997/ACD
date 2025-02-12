class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "cognitive_process": "Working memory",
                "linguistic_structure": "Syntactic trees",
                "nlp_problem": "Ambiguity resolution in machine translation"
            },
            "2": {
                "cognitive_process": "Semantic memory",
                "linguistic_structure": "Conceptual frames",
                "nlp_problem": "Contextual word embedding for sentiment analysis"
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a quantum computing framework for modeling and manipulating linguistic structures based on cognitive processes, then apply it to solve a complex natural language processing problem. Focus on the cognitive process of {t['cognitive_process']}, the linguistic structure of {t['linguistic_structure']}, and apply your framework to the NLP problem of {t['nlp_problem']}.

Your response should include the following sections:

1. Quantum-Linguistic Framework (300-350 words):
   a) Describe the key components of your quantum computing framework for modeling linguistic structures.
   b) Explain how it incorporates principles from the specified cognitive process.
   c) Detail how quantum states or operations represent the given linguistic structure.
   d) Provide a formal notation or mathematical representation of your framework.

2. Cognitive-Linguistic Integration (200-250 words):
   a) Analyze how your framework models the interaction between the cognitive process and linguistic structure.
   b) Discuss potential insights this integration might offer into human language processing.
   c) Explain any novel emergent properties or behaviors in your quantum-linguistic system.

3. Quantum Operations (200-250 words):
   a) Describe at least three quantum operations in your framework and their linguistic interpretations.
   b) Explain how these operations manipulate the linguistic structures.
   c) Discuss any advantages these quantum operations might have over classical computational approaches.

4. NLP Problem Application (250-300 words):
   a) Apply your quantum-linguistic framework to the specified NLP problem.
   b) Provide a step-by-step explanation of how your framework processes and solves the problem.
   c) Discuss potential advantages and limitations of your approach compared to traditional methods.
   d) Propose a method for evaluating the performance of your quantum-linguistic NLP solution.

5. Technical Challenges and Future Directions (150-200 words):
   a) Identify at least two major technical challenges in implementing your framework on current or near-term quantum hardware.
   b) Propose potential solutions or research directions to address these challenges.
   c) Discuss how advancements in quantum computing might impact the future development of your framework.

Ensure your response demonstrates a deep understanding of quantum computing principles, linguistic theories, and cognitive science concepts. Be creative and innovative in your approach while maintaining scientific and mathematical rigor. Use appropriate notation, terminology, and provide clear explanations for complex ideas.

Format your response with clear headings for each section and subsection. Your total response should be between 1100-1350 words. Include a word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of quantum computing, linguistics, and cognitive science.",
            "The quantum-linguistic framework is innovative, well-explained, and integrates all required elements (cognitive process, linguistic structure, and quantum computing).",
            "The framework includes a clear formal notation or mathematical representation.",
            "At least three quantum operations are described with their linguistic interpretations and advantages over classical approaches.",
            "The application to the NLP problem is thorough, logical, and showcases the potential advantages of the quantum approach.",
            "The response addresses technical challenges and future directions thoughtfully.",
            "The overall response is well-structured, clear, and within the specified word count range (1100-1350 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
