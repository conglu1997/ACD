import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        ai_types = [
            {
                'type': 'Neural Network',
                'focus': 'Pattern Recognition',
                'constraint': 'Parallel Processing'
            },
            {
                'type': 'Expert System',
                'focus': 'Decision Making',
                'constraint': 'Rule-Based Logic'
            },
            {
                'type': 'Reinforcement Learning Agent',
                'focus': 'Adaptive Behavior',
                'constraint': 'Reward Optimization'
            },
            {
                'type': 'Natural Language Processing Model',
                'focus': 'Language Understanding',
                'constraint': 'Contextual Interpretation'
            },
            {
                'type': 'Computer Vision System',
                'focus': 'Visual Analysis',
                'constraint': 'Spatial Reasoning'
            }
        ]
        
        tasks = [
            random.choice(ai_types),
            random.choice(ai_types)
        ]
        return {str(i+1): task for i, task in enumerate(tasks)}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a hypothetical internal language for a {t['type']} artificial intelligence system, focusing on {t['focus']} and constrained by {t['constraint']}. Then, analyze its potential efficacy and propose experiments to test it. Your response should include:

1. Language Design (250-300 words):
   a) Describe the basic structure and components of your AI internal language.
   b) Explain how it represents and processes information related to {t['focus']}.
   c) Detail how the language incorporates or addresses the constraint of {t['constraint']}.
   d) Provide an example of how a simple concept or operation would be represented in this language.
   e) Include a simple ASCII art or text-based diagram representing the structure of your language.

2. Information Processing Mechanisms (200-250 words):
   a) Explain how your language facilitates information storage, retrieval, and manipulation.
   b) Describe any novel features that make it particularly suited for {t['type']} systems.
   c) Discuss how the language might handle uncertainty or incomplete information.

3. Cognitive Architecture Integration (200-250 words):
   a) Describe how this internal language would integrate with the overall cognitive architecture of the AI system.
   b) Explain any potential advantages this language might offer over traditional data structures or representations.
   c) Discuss any potential limitations or challenges in implementing this language.

4. Comparative Analysis (150-200 words):
   a) Compare your AI internal language to human natural languages, highlighting key similarities and differences.
   b) Discuss how this comparison might inform our understanding of both artificial and human intelligence.

5. Experimental Design (200-250 words):
   Propose two experiments to test the efficacy of your AI internal language:
   a) Experiment 1: Design an experiment to test how well your language facilitates {t['focus']}.
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would validate (or invalidate) your language design.
   b) Experiment 2: Design an experiment to evaluate how your language handles the constraint of {t['constraint']}.
      - Describe the experimental setup, methodology, and expected results.
      - Explain how the results would demonstrate your language's effectiveness.

Ensure your response demonstrates a deep understanding of artificial intelligence, information processing, and linguistic principles. Be creative in your design while maintaining scientific plausibility. Use technical terminology appropriately and provide explanations where necessary.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1000-1300 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of AI systems, information processing, and linguistic principles.",
            "The language design is creative, plausible, and well-suited for the specified AI type and focus.",
            "The information processing mechanisms are clearly explained and appropriate for the AI system.",
            "The integration with cognitive architecture is well-reasoned and considers both advantages and limitations.",
            "The comparative analysis with human languages is insightful and informative.",
            "The proposed experiments are well-designed and would effectively test the language's efficacy.",
            "The response uses technical terminology appropriately and provides clear explanations.",
            "The overall response is well-structured, coherent, and adheres to the specified format and word count.",
            "The ASCII art or text-based diagram effectively represents the structure of the designed language."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
