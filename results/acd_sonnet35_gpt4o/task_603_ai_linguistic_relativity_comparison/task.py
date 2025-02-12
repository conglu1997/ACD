import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        programming_paradigms = [
            "Functional",
            "Object-Oriented",
            "Logic",
            "Array-based",
            "Symbolic"
        ]
        problem_domains = [
            "Natural Language Processing",
            "Computer Vision",
            "Automated Reasoning",
            "Data Analysis",
            "Game Playing"
        ]
        cognitive_biases = [
            "Confirmation Bias",
            "Anchoring Bias",
            "Availability Heuristic",
            "Framing Effect",
            "Dunning-Kruger Effect"
        ]
        
        tasks = {}
        for i in range(2):
            paradigm1, paradigm2 = random.sample(programming_paradigms, 2)
            domain = random.choice(problem_domains)
            bias = random.choice(cognitive_biases)
            
            tasks[str(i+1)] = {
                "paradigm1": paradigm1,
                "paradigm2": paradigm2,
                "domain": domain,
                "bias": bias
            }
        
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design and analyze two AI systems exhibiting linguistic relativity based on different 'native' programming paradigms. Compare their approaches to a specific problem-solving scenario. Your task has the following components:

1. System Design (300-350 words):
   a) Describe two AI systems: one primarily based on the {t['paradigm1']} programming paradigm, and another based on the {t['paradigm2']} paradigm.
   b) Explain how each paradigm shapes its respective AI's 'thought processes' and problem-solving approaches.
   c) Detail how each system would approach problems in the domain of {t['domain']}.

2. Linguistic Relativity Analysis (250-300 words):
   a) Analyze how each chosen programming paradigm might create different cognitive biases or limitations in its AI system.
   b) Compare and contrast how these biases could manifest in the AIs' problem-solving strategies or outputs.
   c) Draw parallels to how human languages can shape thought patterns and cognitive biases.

3. Problem-Solving Scenario (250-300 words):
   Describe a specific problem-solving scenario in the {t['domain']} domain. Analyze how each AI system would approach and potentially solve this problem differently due to its 'native' paradigm. Include a brief pseudocode or code snippet (5-10 lines) for each paradigm to illustrate key differences.

4. Bias Demonstration (200-250 words):
   a) Provide a specific example of how each AI system might exhibit {t['bias']} due to its 'native' programming paradigm.
   b) Explain how this bias might manifest differently in each system when tackling the problem-solving scenario.

5. Mitigation Strategies (200-250 words):
   a) Propose methods to mitigate the identified biases for each system while maintaining the benefits of their respective paradigms.
   b) Discuss the challenges and potential trade-offs of these mitigation strategies.

6. Implications and Future Research (200-250 words):
   a) Discuss the broader implications of linguistic relativity in AI systems for the field of artificial intelligence.
   b) Propose a research agenda to further explore the effects of 'native' programming languages on AI cognition.
   c) Speculate on how understanding these effects could influence future AI development and human-AI interaction.

Ensure your response demonstrates a deep understanding of programming paradigms, cognitive science, and artificial intelligence. Use technical terminology appropriately and provide explanations where necessary. Be creative in your analysis while maintaining scientific plausibility.

Format your response with clear headings for each section, adhering to the word count guidelines provided. Your total response should be between 1400-1700 words. Use concise, clear language and avoid unnecessary repetition to meet these guidelines."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a clear understanding of both the {t['paradigm1']} and {t['paradigm2']} programming paradigms and their potential effects on AI cognition",
            "The analysis of linguistic relativity in AI systems is thorough, comparative, and draws valid parallels to human cognition",
            f"The problem-solving scenario in the {t['domain']} domain is well-described, and the analysis of each AI system's approach is insightful and paradigm-specific",
            "The provided pseudocode or code snippets effectively illustrate key differences between the paradigms",
            f"The examples of {t['bias']} demonstration are specific, plausible, and clearly linked to the given programming paradigms and problem-solving scenario",
            "Proposed mitigation strategies are creative, address the identified biases for each system, and consider potential trade-offs",
            "The discussion of implications and future research directions is insightful and demonstrates a broad understanding of AI development challenges",
            "The response follows the specified format with clear headings and adheres to the provided word count guidelines"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
