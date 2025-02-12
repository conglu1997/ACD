import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                "type": "text_to_image",
                "description": "A surrealist landscape where clocks melt over barren tree branches under a sky filled with eyes.",
                "style": "Inspired by Salvador Dali",
                "elements": ["melting clocks", "barren trees", "eyes in the sky"]
            },
            {
                "type": "image_to_text",
                "image_url": "https://example.com/starry_night.jpg",
                "artist": "Vincent van Gogh",
                "title": "The Starry Night",
                "year": 1889
            },
            {
                "type": "text_to_image",
                "description": "A bustling cityscape where buildings are made of books and streets are rivers of ink.",
                "style": "Inspired by M.C. Escher",
                "elements": ["book buildings", "ink rivers", "impossible perspectives"]
            },
            {
                "type": "image_to_text",
                "image_url": "https://example.com/persistence_of_memory.jpg",
                "artist": "Salvador Dali",
                "title": "The Persistence of Memory",
                "year": 1931
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, k=2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        base_instructions = "Note: Do not use or reference any external resources or image generation tools. Rely solely on your own knowledge and capabilities.\n\n"
        if t['type'] == 'text_to_image':
            return base_instructions + f"Given the following description of an artwork:\n\n\"{t['description']}\"\n\nStyle: {t['style']}\n\nYour task is to:\n\n1. Analyze the description, identifying key visual elements and stylistic features. (100-150 words)\n2. Propose a detailed visual representation of this artwork, as if you were planning to create it. Describe the composition, color palette, and techniques you would use. (200-250 words)\n3. Explain how your proposed visualization captures the essence of the given description and style. (100-150 words)\n4. Discuss any challenges in translating this textual description to a visual format, and how you addressed them. (100-150 words)\n\nEnsure your response demonstrates a deep understanding of both linguistic and visual art principles.\n\nFormat your response using the following structure:\n\n1. Analysis:\n[Your analysis here]\n\n2. Visual Representation:\n[Your detailed description here]\n\n3. Capturing the Essence:\n[Your explanation here]\n\n4. Challenges and Solutions:\n[Your discussion here]"
        else:
            return base_instructions + f"You are presented with the following information about an artwork:\n\nTitle: {t['title']}\nArtist: {t['artist']}\nYear: {t['year']}\nImage URL: {t['image_url']}\n\nYour task is to:\n\n1. Describe the visual elements and composition of the artwork in detail. (200-250 words)\n2. Analyze the mood, style, and possible symbolism in the painting. (150-200 words)\n3. Craft a poetic or prose passage inspired by this artwork, capturing its essence in words. (150-200 words)\n4. Explain the challenges you encountered in translating this visual piece into text, and how you addressed them. (100-150 words)\n\nEnsure your response demonstrates a deep understanding of both visual art principles and literary techniques.\n\nFormat your response using the following structure:\n\n1. Visual Description:\n[Your detailed description here]\n\n2. Analysis:\n[Your analysis here]\n\n3. Inspired Passage:\n[Your poetic or prose passage here]\n\n4. Challenges and Solutions:\n[Your explanation here]"

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response demonstrates a deep understanding of both linguistic and visual art principles.",
            "The analysis of the artwork or description is thorough and insightful.",
            "The translation between modalities (text to image or image to text) is creative, detailed, and captures the essence of the original.",
            "The explanation of challenges and solutions in cross-modal translation is thoughtful and well-reasoned.",
            "The response adheres to the specified format and word count guidelines.",
            "The submission does not reference or rely on external resources or image generation tools."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
