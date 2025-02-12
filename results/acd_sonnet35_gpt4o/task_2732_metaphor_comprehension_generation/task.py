import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        source_domains = [
            "quantum physics",
            "ecology",
            "economics",
            "music theory",
            "architecture",
            "celestial mechanics"
        ]
        target_domains = [
            "social media dynamics",
            "cognitive processes",
            "climate change",
            "artificial intelligence",
            "political systems",
            "emotional intelligence"
        ]
        abstract_problems = [
            "information overload",
            "wealth inequality",
            "cultural polarization",
            "ethical decision-making in AI",
            "sustainable resource management",
            "balancing innovation and tradition"
        ]
        return {
            "1": {
                "source_domain": random.choice(source_domains),
                "target_domain": random.choice(target_domains),
                "abstract_problem": random.choice(abstract_problems)
            },
            "2": {
                "source_domain": random.choice(source_domains),
                "target_domain": random.choice(target_domains),
                "abstract_problem": random.choice(abstract_problems)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of comprehending and generating novel metaphors across diverse domains, then use it to solve abstract problems and create innovative explanations for complex concepts. Your task has the following components:

1. Metaphor Processing System Design (300-350 words):
   a) Describe the architecture of your AI system for metaphor comprehension and generation.
   b) Explain how your system identifies and maps conceptual similarities across different domains.
   c) Detail the mechanisms for evaluating the aptness and novelty of generated metaphors.
   d) Discuss how your system integrates knowledge from various domains to create meaningful cross-domain analogies.

2. Metaphor Generation and Analysis (250-300 words):
   Source Domain: {t['source_domain']}
   Target Domain: {t['target_domain']}

   a) Use your AI system to generate a novel metaphor that explains a key concept or process in the target domain using elements from the source domain.
   b) Analyze the generated metaphor, explaining how it illuminates aspects of the target domain.
   c) Discuss potential limitations or misunderstandings that could arise from this metaphor.

3. Abstract Problem Solving (250-300 words):
   Abstract Problem: {t['abstract_problem']}

   a) Apply your metaphor-generating AI to create an innovative approach to addressing the given abstract problem.
   b) Explain how the metaphorical thinking led to this solution and its potential advantages.
   c) Identify any challenges in implementing this metaphor-inspired solution in the real world.

4. Cognitive Science Analysis (200-250 words):
   a) Compare your AI system's approach to metaphor processing with current understanding of human metaphor comprehension and generation.
   b) Discuss how your system might inform or be informed by cognitive theories of analogy and metaphor.
   c) Propose an experiment to test whether your AI system's metaphor capabilities match or exceed human performance.

5. Ethical and Societal Implications (150-200 words):
   a) Explore potential ethical concerns or societal impacts of widespread use of advanced metaphor-generating AI systems.
   b) Discuss how such systems might influence human creativity, communication, and problem-solving.
   c) Propose guidelines for responsible development and use of metaphor-generating AI.

6. Future Developments and Applications (150-200 words):
   a) Suggest potential improvements or extensions to your metaphor processing system.
   b) Propose two novel applications of your system in fields not mentioned in the given domains.
   c) Speculate on how advanced metaphor-generating AI might influence fields like education, scientific research, or artistic expression.

Ensure your response demonstrates a deep understanding of metaphor theory, cognitive science, and artificial intelligence. Use appropriate terminology and provide clear explanations where necessary. Be creative and innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response effectively designs an AI system for metaphor comprehension and generation, and applies it to the domains of {t['source_domain']} and {t['target_domain']}, as well as the abstract problem of {t['abstract_problem']}.",
            "The metaphor processing system design is well-explained, scientifically plausible, and demonstrates interdisciplinary integration.",
            "The generated metaphor and its analysis show creativity and insight in connecting the source and target domains.",
            "The approach to the abstract problem demonstrates innovative application of metaphorical thinking.",
            "The cognitive science analysis and ethical considerations show a deep understanding of the implications of the system.",
            "The response is creative and demonstrates a sophisticated understanding of metaphor theory, cognitive science, and artificial intelligence.",
            "The response follows the specified format and adheres to the word limit guidelines."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
