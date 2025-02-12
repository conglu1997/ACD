import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        abstract_concepts = [
            'Entropy', 'Emergence', 'Fractals', 'Quantum Superposition',
            'Evolutionary Adaptation', 'Swarm Intelligence', 'Chaos Theory',
            'Neuroplasticity', 'Symbiosis', 'Resonance'
        ]
        problem_domains = [
            'Urban Planning', 'Climate Change Mitigation', 'Education Reform',
            'Healthcare Systems', 'Economic Inequality', 'Cybersecurity',
            'Sustainable Agriculture', 'Space Exploration', 'Renewable Energy',
            'Artificial General Intelligence'
        ]
        
        tasks = [
            {
                'concept1': random.choice(abstract_concepts),
                'concept2': random.choice(abstract_concepts),
                'problem_domain': random.choice(problem_domains)
            },
            {
                'concept1': random.choice(abstract_concepts),
                'concept2': random.choice(abstract_concepts),
                'problem_domain': random.choice(problem_domains)
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Analyze and blend the abstract concepts of '{t['concept1']}' and '{t['concept2']}' to generate an innovative solution for a complex problem in the domain of {t['problem_domain']}. Conceptual blending involves combining elements from different concepts to create a new, integrated concept that has emergent properties not present in the original concepts.

Your response should include the following sections:

1. Concept Analysis (200-250 words):
   a) Explain the key principles and characteristics of {t['concept1']} and {t['concept2']}.
   b) Identify any similarities, differences, or potential synergies between these concepts.
   c) Discuss how these concepts might be relevant to {t['problem_domain']}.

2. Conceptual Blending (250-300 words):
   a) Describe a novel framework or approach that combines elements of both concepts.
   b) Explain how this blended concept relates to {t['problem_domain']}.
   c) Discuss any emergent properties or insights that arise from this conceptual blend.
   d) Provide a visual representation of your conceptual blend using ASCII art or a clear textual description.

3. Problem Analysis (200-250 words):
   a) Identify a specific, complex problem within {t['problem_domain']}.
   b) Analyze the key challenges and current limitations in addressing this problem.
   c) Explain why traditional approaches might be insufficient.

4. Innovative Solution (300-350 words):
   a) Present a detailed, innovative solution to the identified problem using your blended conceptual framework.
   b) Explain how different elements of your solution correspond to aspects of {t['concept1']} and {t['concept2']}.
   c) Describe how your solution addresses the key challenges identified in the problem analysis.
   d) Discuss potential benefits and limitations of your proposed solution.
   e) Present your solution in the following format:
      - Problem statement
      - Solution overview
      - Key components (bullet points)
      - Implementation steps
      - Expected outcomes

5. Implementation and Evaluation (200-250 words):
   a) Outline steps for implementing your innovative solution in a real-world context.
   b) Propose methods for evaluating the effectiveness of your solution.
   c) Discuss potential challenges in implementation and how they might be addressed.

6. Broader Implications (150-200 words):
   a) Discuss how your conceptual blending approach might be applied to other problems or domains.
   b) Explore any ethical considerations or potential unintended consequences of your solution.
   c) Suggest areas for future research or development based on your conceptual blend.

Ensure your response demonstrates a deep understanding of the abstract concepts, the problem domain, and the process of conceptual blending. Be creative and innovative in your approach while maintaining logical consistency and practical feasibility. Use appropriate technical terminology and provide clear explanations for complex ideas.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1600 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['concept1']} and {t['concept2']}, accurately explaining their key principles and characteristics.",
            f"The conceptual blending effectively combines elements of {t['concept1']} and {t['concept2']} in a novel and meaningful way.",
            "The visual representation of the conceptual blend is clear and insightful.",
            f"The identified problem in {t['problem_domain']} is complex and well-analyzed.",
            "The proposed solution is innovative, directly applies the blended conceptual framework, and addresses the identified challenges.",
            "The solution is presented in the specified format with all required elements.",
            "The implementation and evaluation plan is feasible and well-thought-out.",
            "The discussion of broader implications is insightful and considers ethical aspects.",
            "The response is creative and demonstrates strong abstract reasoning and analogical thinking skills.",
            "The writing is clear, well-structured, and uses appropriate technical terminology.",
            "The response stays within the specified word count range of 1300-1600 words."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
