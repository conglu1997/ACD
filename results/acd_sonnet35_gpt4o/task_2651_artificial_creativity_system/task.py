import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = [
            'Visual Arts',
            'Music Composition',
            'Scientific Discovery',
            'Technological Innovation',
            'Literary Creation',
            'Culinary Arts',
            'Architectural Design',
            'Game Design'
        ]
        creativity_theories = [
            'Divergent Thinking',
            'Conceptual Blending',
            'Cognitive Flexibility',
            'Associative Hierarchy',
            'Incubation and Insight',
            'Flow State',
            'Bisociation'
        ]
        tasks = [
            {
                'domain': random.choice(domains),
                'creativity_theory': random.choice(creativity_theories),
                'constraint': 'Ethical implications'
            },
            {
                'domain': random.choice(domains),
                'creativity_theory': random.choice(creativity_theories),
                'constraint': 'Resource limitations'
            }
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        theory_explanations = {
            'Divergent Thinking': 'the ability to generate multiple unique ideas',
            'Conceptual Blending': 'combining distinct concepts to create new ideas',
            'Cognitive Flexibility': 'adapting thinking strategies to new situations',
            'Associative Hierarchy': 'forming connections between disparate ideas',
            'Incubation and Insight': 'subconscious problem-solving leading to sudden realizations',
            'Flow State': 'a state of heightened focus and productivity',
            'Bisociation': 'perceiving a situation in two incompatible frames of reference'
        }
        return f"""Design an artificial creativity system capable of generating and evaluating novel ideas in the domain of {t['domain']}, incorporating principles from the creativity theory of {t['creativity_theory']} ({theory_explanations[t['creativity_theory']]}), while considering the constraint of {t['constraint']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your artificial creativity system.
   b) Explain how it incorporates the specified creativity theory.
   c) Detail how the system generates and evaluates ideas in the given domain.
   d) Include a diagram or flowchart of your system architecture (describe it textually).

2. Creativity Mechanisms (250-300 words):
   a) Explain the specific mechanisms your system uses to generate novel ideas.
   b) Describe how it evaluates the creativity and value of generated ideas.
   c) Discuss how your system balances novelty with usefulness in the given domain.

3. Domain-Specific Application (200-250 words):
   a) Provide an example of how your system would generate a creative idea in the specified domain.
   b) Explain how the system would evaluate and refine this idea.
   c) Discuss how domain-specific knowledge is integrated into the creative process.

4. Constraint Handling (150-200 words):
   a) Explain how your system addresses the specified constraint.
   b) Describe any trade-offs or challenges this constraint presents.
   c) Propose a method for adapting the system to different constraints.

5. Comparative Analysis (200-250 words):
   a) Compare your system to human creativity in the specified domain.
   b) Discuss potential advantages and limitations of your artificial approach.
   c) Analyze how your system might complement or enhance human creativity.

6. Ethical Considerations (150-200 words):
   a) Discuss ethical implications of deploying your artificial creativity system.
   b) Propose guidelines for responsible use and development of creative AI.
   c) Explore potential societal impacts of widespread adoption of such systems.

7. Future Directions (150-200 words):
   a) Suggest potential improvements or expansions to your system.
   b) Discuss how it could be adapted to other domains or creativity theories.
   c) Propose a novel research question arising from your design.

Ensure your response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specified domain and creativity theory. Use appropriate technical terminology and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Use precise language and avoid unnecessary repetition. Your total response should be between 1400-1750 words.

IMPORTANT: Adhere strictly to the section headings and word counts provided. Present your ideas clearly and concisely, focusing on the most crucial aspects of your artificial creativity system design."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of cognitive science, artificial intelligence, and the specified domain and creativity theory.",
            "The artificial creativity system design is innovative, scientifically plausible, and effectively incorporates the specified creativity theory.",
            "The system architecture and creativity mechanisms are well-explained and logically sound.",
            "The domain-specific application and example are relevant and demonstrate the system's creative capabilities.",
            "The handling of the specified constraint is thoughtful and well-integrated into the system design.",
            "The comparative analysis with human creativity is insightful and balanced.",
            "Ethical considerations are thoroughly explored with responsible guidelines proposed.",
            "Future directions and potential improvements are creative and well-reasoned.",
            "The response shows strong integration of knowledge from multiple disciplines.",
            "The response adheres to the specified word limits for each section and overall length."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
