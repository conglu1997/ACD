class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"narrative": "In 1776, the American Declaration of Independence was signed, marking the beginning of the United States. In 1787, the United States Constitution was drafted, establishing the framework for the federal government. In 1861, the Civil War began, a conflict primarily over states' rights and slavery. In 1865, the Civil War ended, and slavery was abolished with the Thirteenth Amendment. In 1920, women gained the right to vote with the passage of the Nineteenth Amendment. In 1969, the first man landed on the moon, a significant achievement in space exploration. In 1989, the Berlin Wall fell, symbolizing the end of the Cold War and the reunification of Germany.", "questions": ["What major event happened between the drafting of the Constitution and the start of the Civil War?", "What was the significant event in 1920?"]},
            "2": {"narrative": "In 1492, Columbus reached the Americas, opening the way for European exploration and colonization. In 1607, the first permanent English settlement was established in Jamestown, Virginia. In 1775, the American Revolutionary War began, a conflict between the thirteen American colonies and Great Britain. In 1783, the war ended with the Treaty of Paris, which recognized American independence. In 1803, the Louisiana Purchase doubled the size of the United States, acquiring territory from France. In 1848, gold was discovered in California, leading to the Gold Rush and a massive influx of settlers. In 1869, the Transcontinental Railroad was completed, connecting the east and west coasts and facilitating commerce and travel.", "questions": ["What event marked the end of the American Revolutionary War?", "What was the significant event in 1848?"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to create a timeline of events based on the following narrative and then answer the questions provided:

Narrative: {t['narrative']}

Questions:
{chr(10).join(t['questions'])}

Ensure that your timeline is accurate and that your answers to the questions are based on the timeline you created. Provide your response in plain text format.

1. Timeline of events
2. Answers to the questions

Be sure to address each question clearly and accurately based on the timeline."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        criteria = ["The timeline should be accurate and complete.", "The answers to the questions should be based on the created timeline.", "The response should be clear and logically structured."]
        return 1.0 if eval_with_llm_judge(instructions, submission, criteria) else 0.0
