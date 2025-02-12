import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        scenes = [
            {
                "culture": "Japanese",
                "context": "A traditional tea ceremony",
                "elements": ["tatami mats", "tea utensils", "kimono-clad participants", "low table", "sliding doors"]
            },
            {
                "culture": "Indian",
                "context": "A typical street food market",
                "elements": ["food stalls", "colorful spices", "crowd of people", "auto-rickshaws", "street vendors"]
            },
            {
                "culture": "American",
                "context": "A high school prom night",
                "elements": ["decorated gymnasium", "formal attire", "corsages", "dance floor", "photo booth"]
            },
            {
                "culture": "Moroccan",
                "context": "A traditional wedding celebration",
                "elements": ["henna designs", "ornate clothing", "musical instruments", "elaborate feast", "decorative rugs"]
            }
        ]
        scene1 = random.choice(scenes)
        scene2 = random.choice([s for s in scenes if s != scene1])
        return {
            "1": {"main_scene": scene1, "comparison_culture": scene2["culture"]},
            "2": {"main_scene": scene2, "comparison_culture": scene1["culture"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        main_scene = t['main_scene']
        comparison_culture = t['comparison_culture']
        return f"""Imagine you are an AI system trained in visual scene interpretation and cross-cultural understanding. You are presented with a scene from {main_scene['culture']} culture in the context of {main_scene['context']}. The scene contains the following elements: {', '.join(main_scene['elements'])}.

1. Describe the scene in detail (100-150 words), explaining the significance and meaning of the elements within the cultural context.

2. Identify at least three cultural nuances or practices evident in the scene that might be misunderstood or misinterpreted by someone from a different cultural background. Explain these potential misunderstandings (100-150 words).

3. Compare and contrast this scene with a similar context in {comparison_culture} culture. Highlight key similarities and differences in practices, values, or social norms (100-150 words).

4. Propose how you would explain this scene to someone from {comparison_culture} culture to promote understanding and avoid stereotypes or oversimplification (100-150 words).

5. Reflect on how your interpretation and comparison might be influenced by your training data or potential biases in AI systems. Discuss any limitations or challenges in accurately interpreting and comparing cultural contexts (100-150 words).

Ensure your response is culturally sensitive, avoids stereotypes, and demonstrates a nuanced understanding of cultural practices and their significance."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately describes the scene and explains the cultural significance of the elements",
            "At least three cultural nuances or potential misunderstandings are identified and explained clearly",
            "The comparison with the other culture is insightful, highlighting key similarities and differences",
            "The proposed explanation for someone from the comparison culture is thoughtful and promotes understanding without stereotyping",
            "The reflection on AI limitations and biases shows critical thinking about the challenges of cultural interpretation and comparison",
            "The overall response demonstrates cultural sensitivity and avoids stereotypes or oversimplification"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
