import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        art_movements = ['Impressionism', 'Surrealism', 'Abstract Expressionism', 'Cubism', 'Pop Art']
        literary_styles = ['Romantic poetry', 'Modernist prose', 'Haiku', 'Stream of consciousness', 'Magical realism']
        cultural_contexts = ['Renaissance Italy', 'Edo period Japan', 'Harlem Renaissance', '1960s counterculture', 'Ancient Greece']
        sample_texts = [
            "In the depths of night, stars whisper secrets to the moon, painting dreams across the velvet sky.",
            "Fractured memories dance on the edge of reality, each shard a window to forgotten worlds."
        ]
        
        tasks = {}
        for i in range(2):
            tasks[str(i+1)] = {
                'art_movement': random.choice(art_movements),
                'literary_style': random.choice(literary_styles),
                'cultural_context': random.choice(cultural_contexts),
                'sample_text': sample_texts[i]
            }
        return tasks

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design an AI system capable of generating visual art based on complex linguistic inputs, incorporating cultural and historical context. This task is inspired by the concept of ekphrasis, which is the verbal description of a visual work of art.

Your system should be able to create art in the style of {t['art_movement']} based on text written in the style of {t['literary_style']}, while considering the cultural context of {t['cultural_context']}. Your response should include:

1. System Architecture (250-300 words):
   a) Describe the key components of your AI system, including modules for text analysis, cultural-historical context processing, and visual generation.
   b) Explain how these components interact to produce the final artistic output.
   c) Detail any novel approaches or technologies used in your system.

2. Linguistic-Visual Translation Process (200-250 words):
   a) Explain how your system interprets and extracts key elements from the input text.
   b) Describe the process of mapping linguistic features to visual elements.
   c) Discuss how the system incorporates the specified literary style into its visual interpretation.

3. Cultural and Historical Integration (200-250 words):
   a) Detail how your system incorporates knowledge of {t['cultural_context']}.
   b) Explain how this cultural-historical context influences the artistic output.
   c) Discuss any challenges in accurately representing cultural elements and how your system addresses them.

4. Artistic Style Implementation (200-250 words):
   a) Describe how your system replicates the style of {t['art_movement']}.
   b) Explain any specific techniques or algorithms used to generate art in this style.
   c) Discuss how the system balances adherence to the artistic style with creative interpretation of the input.

5. Output Analysis (150-200 words):
   a) Provide a detailed description of the output your system would generate for the following input text:
      "{t['sample_text']}"
   b) Analyze how this output reflects the input text, cultural context, and artistic style.
   c) Discuss any unexpected or creative elements in the generated art.

6. Evaluation and Ethical Considerations (150-200 words):
   a) Propose a method for evaluating the quality and accuracy of your system's outputs.
   b) Discuss potential biases in your system and how they might be mitigated.
   c) Address ethical considerations related to AI-generated art and cultural representation.

Ensure your response demonstrates a deep understanding of art history, literary analysis, cultural studies, and AI technologies. Be innovative in your approach while maintaining scientific and cultural plausibility. Your total response should be between 1150-1500 words.

Format your response with clear headings for each section (e.g., '1. System Architecture', '2. Linguistic-Visual Translation Process', etc.) and use subheadings (a, b, c) within each section as outlined above. Addressing all parts of the task is crucial for a complete response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response must address all six sections outlined in the instructions with appropriate headings and subheadings",
            "The system architecture must include detailed descriptions of modules for text analysis, cultural-historical context processing, and visual generation",
            "The response must explain how the system incorporates the specified art movement ({0}), literary style ({1}), and cultural context ({2})".format(t['art_movement'], t['literary_style'], t['cultural_context']),
            "The output analysis must provide a detailed description of the hypothetical output for the given sample text",
            "The response must discuss specific ethical considerations and potential biases in AI-generated art",
            "The proposed system must demonstrate innovative approaches to integrating linguistic, visual, and cultural information",
            "The response should be within the specified word count range (1150-1500 words)"
        ]
        
        # Check word count
        word_count = len(submission.split())
        if word_count < 1150 or word_count > 1500:
            return 0.0
        
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0