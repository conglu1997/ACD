class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "passage": "In the late 19th century, the industrial revolution brought about significant changes in the social and economic structures of many Western countries. Factories began to emerge, leading to urbanization as people moved from rural areas to cities in search of work. This shift resulted in both positive outcomes, such as increased production and innovation, and negative consequences, like overcrowded living conditions and exploitation of workers. Labor unions began to form as workers sought to improve their conditions, leading to significant social and political reforms.",
                "questions": [
                    {
                        "question": "Which of the following best summarizes the main idea of the passage?",
                        "choices": [
                            "A) The industrial revolution led to the emergence of factories.",
                            "B) The industrial revolution had both positive and negative impacts on society.",
                            "C) Labor unions formed to improve worker conditions.",
                            "D) Urbanization was a direct result of the industrial revolution."
                        ],
                        "answer": "B"
                    },
                    {
                        "question": "What was one negative consequence of the industrial revolution mentioned in the passage?",
                        "choices": [
                            "A) Increased production.",
                            "B) Urbanization.",
                            "C) Overcrowded living conditions.",
                            "D) Formation of labor unions."
                        ],
                        "answer": "C"
                    }
                ]
            },
            "2": {
                "passage": "The theory of relativity, developed by Albert Einstein in the early 20th century, revolutionized the field of physics. It introduced the concepts of spacetime and the equivalence of mass and energy, encapsulated in the famous equation E=mc^2. This theory challenged the classical mechanics established by Newton and provided new insights into the nature of gravity, leading to the understanding that massive objects can warp the fabric of spacetime. The implications of relativity have been profound, influencing not only scientific thought but also technology, such as GPS systems that rely on relativistic calculations for accuracy.",
                "questions": [
                    {
                        "question": "What is one key concept introduced by the theory of relativity according to the passage?",
                        "choices": [
                            "A) The laws of motion.",
                            "B) The nature of gravity.",
                            "C) The concept of spacetime.",
                            "D) The importance of classical mechanics."
                        ],
                        "answer": "C"
                    },
                    {
                        "question": "How has the theory of relativity influenced modern technology?",
                        "choices": [
                            "A) By establishing the laws of motion.",
                            "B) Through the development of GPS systems.",
                            "C) By challenging classical mechanics.",
                            "D) By providing new insights into gravity."
                        ],
                        "answer": "B"
                    }
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Read the following passage carefully and answer the multiple-choice questions based on it. Select the option that best answers each question and provide explanations for your choices in the following format: Question 1: [Your Answer] - Explanation: [Your Explanation] Question 2: [Your Answer] - Explanation: [Your Explanation]

Passage: {t['passage']}"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        answers = [q['answer'] for q in t['questions']]
        submitted_answers = submission.split('\n')
        submitted_answers = [ans.split(': ')[1].split(' - Explanation: ')[0] for ans in submitted_answers if ': ' in ans]
        if len(submitted_answers) != len(answers):
            return 0.0
        return 1.0 if all(sa == a for sa, a in zip(submitted_answers, answers)) else 0.0
