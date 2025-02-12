import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        environments = [
            {
                "climate": "Arid",
                "population": "1 million",
                "main_challenge": "Water scarcity",
                "existing_tech": "Solar desalination",
                "local_ecosystem": "Desert scrubland"
            },
            {
                "climate": "Tropical",
                "population": "5 million",
                "main_challenge": "Biodiversity preservation",
                "existing_tech": "Vertical farming",
                "local_ecosystem": "Rainforest"
            },
            {
                "climate": "Temperate",
                "population": "10 million",
                "main_challenge": "Energy efficiency",
                "existing_tech": "Smart grid systems",
                "local_ecosystem": "Deciduous forest"
            }
        ]
        return {str(i+1): env for i, env in enumerate(random.sample(environments, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a futuristic urban ecosystem that integrates advanced technology with natural biological systems to create a self-sustaining city in a {t['climate']} climate with a population of {t['population']}, focusing on addressing the main challenge of {t['main_challenge']}. Consider the existing technology of {t['existing_tech']} and the local ecosystem of {t['local_ecosystem']} in your design. Your response should include the following sections:

1. Urban Ecosystem Design (250-300 words):
   a) Overall layout and key components
   b) Integration of technology with natural biological processes
   c) Addressing the main challenge

2. Technological Innovations (200-250 words):
   a) Two novel technologies crucial to your eco-urban system
   b) Interface between each technology and biological systems

3. Biological Systems Integration (200-250 words):
   a) Key biological systems in your urban ecosystem
   b) Interactions between biological and technological components

4. Sustainability Analysis (150-200 words):
   a) Long-term sustainability assessment
   b) Adaptation to changing environmental conditions

5. Societal Implications (150-200 words):
   a) Effects on human behavior and culture
   b) Potential economic impacts

6. Comparative Analysis (100-150 words):
   a) Comparison to current urban environments
   b) Main advantages and potential drawbacks

7. Trade-offs and Conflict Resolution (100-150 words):
   a) Identify one potential conflict between different aspects of your eco-urban system
   b) Propose a solution to resolve this conflict

8. Global Impact Assessment (100-150 words):
   a) Potential effects of widespread adoption of your eco-urban system on global climate and ecosystems

Optionally, you may include citations to fictional research studies or case studies to support your design choices and predictions. If you choose to do so, use the format (Author, Year) for in-text citations.

Ensure your response demonstrates a deep understanding of urban ecology, sustainable technology, and systems thinking. Use appropriate terminology from relevant fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific and practical plausibility.

Format your response with clear headings and subheadings for each section. Use numbered or bulleted lists where appropriate. Your total response should be between 1250-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must include a design of a futuristic urban ecosystem that integrates technology with biological systems, addressing the specified climate, population, main challenge, existing technology, and local ecosystem.",
            "The design should demonstrate at least two innovative and plausible technological solutions that interface with biological systems.",
            "The response must provide an explanation of how biological systems are integrated and enhanced in the urban environment, with at least one specific example.",
            "The sustainability analysis should consider long-term adaptability and ecological impact.",
            "The response should address societal implications of the eco-urban system, including at least one effect on human behavior or culture and one potential economic impact.",
            "The comparative analysis must provide at least one insightful comparison with current urban environments.",
            "The response must identify one potential conflict between different aspects of the eco-urban system and propose a plausible solution.",
            "The global impact assessment should consider environmental implications of widespread adoption of the eco-urban system.",
            "The response must demonstrate interdisciplinary knowledge integration, creative problem-solving, and systems thinking throughout, using appropriate terminology from at least two relevant fields.",
            "The response should adhere to the specified format, including clear headings and subheadings, and the overall word count (1250-1650 words)."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
