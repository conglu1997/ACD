import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        cultures = ['Javanese Gamelan', 'West African Griot', 'Inuit Throat Singing', 'Indian Carnatic']
        musical_elements = ['rhythm', 'melody', 'harmony', 'timbre']
        cultural_contexts = ['religious ceremony', 'social gathering', 'storytelling', 'harvest festival']
        
        tasks = {
            "1": {
                "culture": random.choice(cultures),
                "musical_element": random.choice(musical_elements),
                "cultural_context": random.choice(cultural_contexts)
            },
            "2": {
                "culture": random.choice(cultures),
                "musical_element": random.choice(musical_elements),
                "cultural_context": random.choice(cultural_contexts)
            }
        }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system that can analyze and compose music in the style of {t['culture']}, focusing on the musical element of {t['musical_element']} in the context of a {t['cultural_context']}. Your response should include:

1. System Architecture (300-350 words):
   a) Describe the key components of your AI ethnomusicology composer system.
   b) Explain how your system integrates cultural knowledge, music theory, and machine learning techniques.
   c) Detail how the system analyzes existing musical pieces and generates new compositions.
   d) Include a high-level diagram or pseudocode illustrating your system's architecture (described in words).

2. Cultural-Musical Analysis (250-300 words):
   a) Explain how your system processes and represents the musical traditions of {t['culture']}.
   b) Describe how the system identifies and incorporates key features of {t['musical_element']} in this cultural context.
   c) Discuss how your system accounts for the cultural significance and function of music in {t['cultural_context']}.

3. Composition Process (250-300 words):
   a) Outline the steps your AI system would take to compose a new piece in the style of {t['culture']}.
   b) Explain how the system ensures authenticity while allowing for creativity in the composition.
   c) Describe how your system would handle the specific challenges related to {t['musical_element']} in this style of music.

4. Machine Learning Approach (200-250 words):
   a) Describe the machine learning techniques used in your system (e.g., neural networks, generative models).
   b) Explain how these techniques are adapted to handle the unique aspects of {t['culture']}'s musical tradition.
   c) Discuss how your system balances learning from data with incorporating expert knowledge about music theory and cultural practices.

5. Evaluation and Authenticity (200-250 words):
   a) Propose methods for evaluating the quality and cultural authenticity of the AI-generated compositions.
   b) Describe how you would involve cultural experts and musicians in the evaluation process.
   c) Discuss potential challenges in assessing the success of AI-generated music in capturing the essence of {t['culture']}'s musical tradition.

6. Ethical Considerations (150-200 words):
   a) Identify potential ethical concerns related to AI systems composing culturally-specific music.
   b) Discuss issues of cultural appropriation and the role of AI in preserving or transforming musical traditions.
   c) Propose guidelines for the responsible development and use of AI ethnomusicology composers.

7. Future Applications and Research Directions (150-200 words):
   a) Suggest potential applications of your AI system beyond music composition (e.g., music education, cultural preservation).
   b) Propose two future research directions that could enhance the capabilities of AI ethnomusicology composers.
   c) Discuss how this technology might impact our understanding of music, culture, and creativity.

Ensure your response demonstrates a deep understanding of music theory, cultural anthropology, and artificial intelligence. Use appropriate technical terminology and provide clear explanations for complex concepts. Be creative in your approach while maintaining cultural sensitivity and scientific plausibility.

Format your response with clear headings for each section, numbered as above. Your total response should be between 1500-1850 words."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            f"The response demonstrates a deep understanding of {t['culture']}'s musical traditions, particularly in relation to {t['musical_element']}.",
            f"The AI system design effectively integrates cultural knowledge, music theory, and machine learning techniques.",
            f"The composition process adequately addresses the challenges of creating authentic music for {t['cultural_context']}.",
            "The response shows creativity and innovation while maintaining cultural sensitivity and scientific plausibility.",
            "Ethical considerations and guidelines for responsible use are thoroughly addressed.",
            "The response is well-structured, following the required format and word count."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
