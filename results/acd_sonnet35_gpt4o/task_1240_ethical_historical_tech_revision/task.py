import random

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        tasks = [
            {
                'technology': 'Printing Press',
                'inventor': 'Johannes Gutenberg',
                'year': 1440,
                'ethical_consideration': 'Information privacy and censorship'
            },
            {
                'technology': 'Steam Engine',
                'inventor': 'James Watt',
                'year': 1769,
                'ethical_consideration': 'Environmental sustainability and labor rights'
            },
            {
                'technology': 'Telephone',
                'inventor': 'Alexander Graham Bell',
                'year': 1876,
                'ethical_consideration': 'Communication privacy and surveillance'
            },
            {
                'technology': 'Nuclear Fission',
                'inventor': 'Otto Hahn and Fritz Strassmann',
                'year': 1938,
                'ethical_consideration': 'Weapons proliferation and energy safety'
            },
            {
                'technology': 'World Wide Web',
                'inventor': 'Tim Berners-Lee',
                'year': 1989,
                'ethical_consideration': 'Digital divide and online misinformation'
            }
        ]
        return {str(i+1): task for i, task in enumerate(random.sample(tasks, 2))}

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Reimagine the development of the {t['technology']} (invented by {t['inventor']} in {t['year']}) with modern ethical considerations, focusing on {t['ethical_consideration']}. Your response should include the following sections, each with its own heading and subheadings:

1. Historical Context (150-200 words):
   a) Original development
   b) Historical significance and impact
   c) Ethical landscape at the time of invention

2. Ethical Analysis (200-250 words):
   a) Modern ethical implications
   b) Relevance of {t['ethical_consideration']}
   c) Potential negative consequences

3. Ethical Reimagination (250-300 words):
   a) Alternative development proposal
   b) Key features of ethically-revised version
   c) Mitigation of identified ethical issues

4. Historical Impact Assessment (200-250 words):
   a) Potential alterations to historical course
   b) Positive and negative consequences
   c) Unintended effects on progress or society

5. Modern Implementation (150-200 words):
   a) Application to current or future technologies
   b) Ethical framework for technological development

6. Reflection (100-150 words):
   a) Challenges of applying modern ethics to historical innovations
   b) Balance between progress and ethical considerations

Ensure your response demonstrates a deep understanding of the historical context, technological principles, and ethical reasoning. Be creative in your reimagination while maintaining historical and scientific plausibility. Use clear headings and subheadings as specified above.

Include at least three relevant citations or references to support your historical and ethical analysis. These should be numbered and listed at the end of your response, not included in the word count for each section. A valid citation should include the author's name, publication year, and title of the work (for books or articles) or the name of the website (for online sources).

Your entire response (excluding citations) should be between 1050-1350 words. Provide a word count at the end of each section (rounded to the nearest whole number) and a total word count at the end of your response."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = [
            "The response accurately describes the historical context and significance of the specified technology, with reference to the inventor and year provided.",
            "The ethical analysis thoroughly examines the implications of the technology from a modern perspective, with a clear focus on the specified ethical consideration.",
            "The reimagined version of the technology creatively and plausibly addresses the ethical concerns while maintaining technological feasibility and historical context.",
            "The historical impact assessment provides a well-reasoned analysis of potential alternate historical outcomes, considering both positive and negative consequences.",
            "The modern implementation suggestions are practical, relevant, and demonstrate an understanding of current technological trends and ethical frameworks.",
            "The reflection shows critical thinking about the challenges of applying modern ethics to historical innovations and thoughtfully discusses the balance between progress and ethics.",
            "The response follows the specified format with clear headings and subheadings for each of the six required sections.",
            "At least three relevant citations or references are provided, formatted correctly with author name, year, and title or website name.",
            "Each section adheres to the specified word count range (as indicated by the word counts provided), and the total response (excluding citations) is between 1050-1350 words.",
            "The writing demonstrates clear interdisciplinary knowledge integration, creative problem-solving, and a nuanced understanding of the interplay between technology, ethics, and historical context."
        ]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
