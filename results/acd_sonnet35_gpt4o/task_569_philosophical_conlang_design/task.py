import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        philosophical_concepts = [
            {
                'concept': 'Solipsism',
                'description': 'The view that the self is all that can be known to exist'
            },
            {
                'concept': 'Eternalism',
                'description': 'The view that all points in time are equally real'
            }
        ]
        
        texts_to_translate = [
            "The only true wisdom is in knowing you know nothing.",
            "I think, therefore I am."
        ]
        
        return {
            str(i+1): {
                'philosophical_concept': concept,
                'text_to_translate': random.choice(texts_to_translate)
            } for i, concept in enumerate(philosophical_concepts)
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Design a constructed language (conlang) based on the philosophical concept of {t['philosophical_concept']['concept']}: {t['philosophical_concept']['description']}. Then use your conlang to translate and analyze the following text: "{t['text_to_translate']}"

Your response should include:

1. Conlang Design (250-300 words):
   a) Describe the key features of your conlang, including its phonology, morphology, and syntax.
   b) Explain how these features reflect the given philosophical concept.
   c) Provide at least three example sentences in your conlang with translations.

2. Philosophical Analysis (150-200 words):
   a) Discuss how your conlang's structure embodies the given philosophical concept.
   b) Explain any challenges you encountered in aligning the language with the philosophy.
   c) Analyze how using this language might influence a speaker's thought patterns or worldview.

3. Text Translation (100-150 words):
   a) Translate the given text into your conlang.
   b) Provide a word-for-word gloss and a free translation back into English.
   c) Explain any difficulties in translation and how you resolved them.

4. Linguistic Analysis (200-250 words):
   a) Analyze how the translated text's meaning changes or is reframed in your conlang.
   b) Discuss any nuances or implications that emerge in the translation process.
   c) Explain how the philosophical basis of your conlang affects the interpretation of the text.

5. Cultural Implications (150-200 words):
   a) Hypothesize about a culture that might use this language as their primary mode of communication.
   b) Discuss how this language might shape their literature, art, or social structures.
   c) Propose an experiment to test the influence of your conlang on cognitive processes or decision-making.

Ensure your response demonstrates a deep understanding of linguistics, philosophy, and their intersections. Be creative in your language design while maintaining internal consistency and philosophical alignment. Use appropriate linguistic terminology and provide clear explanations for your choices."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The conlang design is creative, detailed, and clearly reflects the given philosophical concept",
            "The philosophical analysis demonstrates a deep understanding of the concept and its linguistic implications",
            "The text translation is complete and accompanied by a thorough linguistic analysis",
            "The cultural implications are well-reasoned and show innovative thinking about language and society",
            "The response uses appropriate linguistic terminology and provides clear explanations throughout"
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
