import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        domains = ['art', 'science', 'technology', 'social issues']
        blend_types = ['mirror', 'single-scope', 'double-scope', 'megablend']
        applications = ['product design', 'scientific discovery', 'storytelling', 'problem-solving']
        
        tasks = {
            "1": {
                "domain": random.choice(domains),
                "blend_type": random.choice(blend_types),
                "application": random.choice(applications)
            },
            "2": {
                "domain": random.choice(domains),
                "blend_type": random.choice(blend_types),
                "application": random.choice(applications)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that uses conceptual blending techniques from cognitive linguistics to generate novel ideas and solve creative problems in the domain of {t['domain']}, focusing on the blend type '{t['blend_type']}', and analyze its potential application in {t['application']}. 

Conceptual blending is a cognitive theory that explains how humans combine different mental spaces to create new, emergent structures. This process is fundamental to human creativity and innovation.

Your response should include the following sections and subsections:

1. Conceptual Blending Theory (200-250 words):
   a) Key principles of conceptual blending theory
   b) Characteristics of the specified blend type
   c) Relationship between conceptual blending and human creativity
   d) Proposal for a novel blend type not mentioned in the existing list

2. AI System Architecture (250-300 words):
   a) Overall system design
   b) Representation and manipulation of conceptual spaces
   c) Algorithms for conceptual blending
   d) Evaluation and selection of blended concepts

3. Domain-Specific Implementation (200-250 words):
   a) Adaptation to the given domain
   b) Example of novel idea generation
   c) Domain-specific challenges

4. Creative Output Analysis (200-250 words):
   a) Description of a hypothetical AI-generated output
   b) Analysis of novelty, usefulness, and coherence
   c) Comparison with human-generated ideas

5. Application in {t['application']} (150-200 words):
   a) Potential uses in the specified application
   b) Benefits and limitations
   c) Specific use case or scenario

6. Comparative Analysis (200-250 words):
   a) Comparison with existing creative AI systems
   b) Unique features and advantages of your proposed system
   c) Potential areas for integration or synergy with other AI approaches

7. Cross-Domain Applications (150-200 words):
   a) Identification of potential applications in domains other than the initially specified one
   b) Explanation of how the system could be adapted for these new domains
   c) Potential challenges and benefits of cross-domain application

8. Ethical Considerations and Societal Impact (150-200 words):
   a) Potential ethical issues
   b) Impact on human creativity and innovation
   c) Guidelines for responsible development and use

9. Future Research Directions (150-200 words):
   a) Potential improvements or extensions
   b) Proposal for a novel experiment
   c) Contributions to understanding human cognition and creativity

Ensure your response demonstrates a deep understanding of conceptual blending theory, cognitive linguistics, and artificial intelligence. Use appropriate terminology from these fields and provide clear explanations where necessary. Include examples or analogies to illustrate complex concepts. Be innovative in your approach while maintaining scientific and ethical rigor.

Format your response with clear headings for each section and subheadings for subsections. Your total response should be between 1650-2100 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of conceptual blending theory, cognitive linguistics, and artificial intelligence.",
            "The AI system architecture is well-designed and clearly explains how conceptual blending is implemented.",
            "The domain-specific implementation is thoughtfully adapted to the given domain and blend type.",
            "The creative output analysis is insightful and critically evaluates the AI-generated ideas.",
            "The application of the AI system to the specified area is well-explained and includes a concrete use case.",
            "The comparative analysis effectively contrasts the proposed system with existing creative AI systems.",
            "Cross-domain applications are identified and explained convincingly.",
            "Ethical considerations and societal impacts are thoroughly addressed.",
            "Future research directions are innovative and well-reasoned.",
            "The response is creative and demonstrates interdisciplinary knowledge integration.",
            "The response follows the required format, including section headings and subheadings, and adheres to the word count guidelines.",
            "Complex concepts are illustrated with clear examples or analogies.",
            "A novel blend type is proposed and explained coherently."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
