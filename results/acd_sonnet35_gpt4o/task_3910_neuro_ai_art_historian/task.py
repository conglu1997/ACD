import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_periods = [
            {
                "period": "Renaissance",
                "key_features": "perspective, realism, religious themes"
            },
            {
                "period": "Impressionism",
                "key_features": "light effects, loose brushwork, everyday scenes"
            },
            {
                "period": "Cubism",
                "key_features": "geometric shapes, multiple perspectives, fragmentation"
            },
            {
                "period": "Surrealism",
                "key_features": "dreamlike imagery, juxtaposition, symbolism"
            }
        ]
        
        neuroscience_principles = [
            {
                "principle": "Visual hierarchies",
                "description": "The brain processes visual information in a hierarchical manner, from simple features to complex objects"
            },
            {
                "principle": "Gestalt principles",
                "description": "The brain tends to perceive objects as organized patterns and groups"
            },
            {
                "principle": "Emotional processing",
                "description": "The amygdala and other brain regions process emotional responses to visual stimuli"
            },
            {
                "principle": "Neuroaesthetics",
                "description": "Specific neural mechanisms underlie aesthetic experiences and judgments"
            }
        ]
        
        return {
            "1": {
                "art_period": random.choice(art_periods),
                "neuroscience_principle": random.choice(neuroscience_principles)
            },
            "2": {
                "art_period": random.choice(art_periods),
                "neuroscience_principle": random.choice(neuroscience_principles)
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and generate art in the style of the {t['art_period']['period']} period, incorporating the neuroscientific principle of {t['neuroscience_principle']['principle']}. Your response should include the following sections:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system for art analysis and generation.
   b) Explain how your system incorporates the specified neuroscientific principle.
   c) Detail how the system processes and analyzes visual information.
   d) Discuss any novel algorithms or techniques used in your system.

2. Art Period Integration (200-250 words):
   a) Explain how your system captures the key features of the {t['art_period']['period']} period ({t['art_period']['key_features']}).
   b) Describe the specific techniques or models used to recognize and generate these features.
   c) Discuss how your system handles the unique challenges of this art period.

3. Neuroscientific Basis (200-250 words):
   a) Elaborate on the principle of {t['neuroscience_principle']['principle']} and its relevance to art perception and creation.
   b) Explain how this principle is implemented in your AI system's architecture or algorithms.
   c) Discuss any insights from cognitive neuroscience that inform your system's design.

4. Art Generation Process (250-300 words):
   a) Describe the step-by-step process your system uses to generate new artworks.
   b) Explain how it balances adherence to the art period's style with creative innovation.
   c) Provide an example of how a specific artwork might be generated, detailing the system's decision-making process.

5. Evaluation and Validation (150-200 words):
   a) Propose methods to evaluate the authenticity and quality of the generated artworks.
   b) Describe how you would validate the system's understanding of the art period and neuroscientific principles.
   c) Discuss potential challenges in evaluating AI-generated art.

6. Ethical and Cultural Implications (150-200 words):
   a) Discuss the potential impact of AI-generated art on human artists and the art world.
   b) Address concerns about cultural appropriation or misrepresentation in AI art generation.
   c) Propose guidelines for the responsible development and use of AI in art creation.

7. Future Directions (100-150 words):
   a) Suggest potential extensions or improvements to your system.
   b) Discuss how this technology might evolve with advancements in neuroscience and AI.

Ensure your response demonstrates a deep understanding of art history, neuroscience, and artificial intelligence. Use appropriate terminology from all fields and provide clear explanations for complex concepts. Be innovative in your approach while maintaining scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1300-1650 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response must propose a detailed AI system for analyzing and generating art in the style of the {t['art_period']['period']} period, incorporating the neuroscientific principle of {t['neuroscience_principle']['principle']}.",
            "The proposed system should demonstrate a clear understanding of art history, neuroscience, and artificial intelligence, integrating concepts from all three fields in a plausible manner.",
            "The submission must include all seven required sections, adequately addressing each topic.",
            "The response should demonstrate creativity and innovation in the proposed AI system while maintaining scientific plausibility.",
            "The analysis of ethical implications and future directions should be insightful and well-reasoned.",
            "The response must show a deep understanding of the specified art period and neuroscientific principle, using appropriate terminology from all fields.",
            "The proposed evaluation methods and future research directions should be relevant and potentially feasible."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
