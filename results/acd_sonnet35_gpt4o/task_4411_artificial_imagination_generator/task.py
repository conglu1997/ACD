class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = {
            "1": {
                "global_challenge": "climate change mitigation",
                "creative_domains": ["biotechnology", "urban design", "energy systems"]
            },
            "2": {
                "global_challenge": "interplanetary colonization",
                "creative_domains": ["nanotechnology", "psychology", "ecosystem engineering"]
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating novel creative concepts, then use it to propose and evaluate imaginative solutions to the global challenge of {t['global_challenge']}, drawing inspiration from the following creative domains: {', '.join(t['creative_domains'])}.

Your response should include:

1. AI System Design (350-400 words):
   a) Describe the key components and architecture of your artificial imagination system.
   b) Provide an ASCII art or text-based diagram representing your system's architecture.
   c) Explain how your system integrates knowledge from diverse domains to generate novel concepts.
   d) Detail any novel algorithms or techniques used for creative idea generation and evaluation.
   e) Discuss how your system balances novelty with feasibility in its creative output.
   f) Provide a brief example of how your system would generate a creative concept, step by step.

2. Comparative Analysis (200-250 words):
   a) Compare your proposed AI system with existing approaches to artificial creativity.
   b) Highlight the novel aspects of your design and how they address limitations in current systems.
   c) Discuss potential limitations or weaknesses of your proposed system.

3. Creative Solution Generation (300-350 words):
   a) Use your AI system to generate three highly imaginative solutions to the given global challenge.
   b) For each solution, provide a detailed description of the concept and its potential implementation.
   c) Explain how each solution draws inspiration from the specified creative domains.
   d) Discuss how these solutions differ from current approaches to the challenge.

4. Feasibility and Impact Analysis (250-300 words):
   a) Evaluate the potential effectiveness of each proposed solution in addressing the global challenge.
   b) Assess the technical feasibility of implementing each solution, considering current and near-future technologies.
   c) Analyze potential unintended consequences or ethical concerns for each solution.
   d) Rank the solutions based on their overall potential impact and feasibility.

5. Interdisciplinary Implications (150-200 words):
   a) Discuss how the proposed solutions might influence or advance research in related fields.
   b) Explore potential applications of these creative concepts beyond the initial global challenge.
   c) Propose a research agenda to further develop the most promising solution.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical issues related to the development or implementation of your AI imagination system.
   b) Discuss the broader implications of using AI for creative problem-solving in addressing global challenges.
   c) Propose guidelines for responsible development and use of artificial imagination technologies.

Ensure your response demonstrates a deep understanding of AI, the specified creative domains, and the global challenge. Be highly creative and speculative in your approach while maintaining scientific plausibility. Use appropriate technical terminology and provide clear explanations for complex concepts.

Format your response with clear headings for each section. Adhere strictly to the word count limits for each section as specified above. Your total response should be between 1400-1700 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI systems and the specified creative domains.",
            "The proposed AI system for generating creative concepts is innovative and well-explained.",
            "The visual representation (ASCII art or text-based diagram) effectively illustrates the system's architecture.",
            "The comparative analysis shows a good understanding of existing approaches and highlights novel aspects of the proposed system.",
            "The generated solutions are highly imaginative and draw clear inspiration from the specified domains.",
            "The feasibility and impact analysis is thorough and considers multiple factors.",
            "The response explores interdisciplinary implications and proposes meaningful research directions.",
            "Ethical considerations are thoughtfully addressed and guidelines are proposed.",
            "The overall response is well-structured, coherent, and within the specified word limit.",
            "The proposed solutions demonstrate a high level of creativity and novelty in addressing the global challenge."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
