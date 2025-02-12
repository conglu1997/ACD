import pandas as pd

class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {
                "data": "Year,Population,GDP\n2000,282162411,10252345\n2001,284968955,10581820\n2002,287625193,10936480\n2003,290107933,11458220\n2004,292805298,12213750\n2005,295516599,13036640\n2006,298379912,13814620\n2007,301231207,14451870\n2008,304093966,14712850\n2009,306771529,14448900\n2010,309321666,14992050",
                "questions": [
                    "What was the GDP in 2005?",
                    "Which year had the highest population growth?"
                ]
            },
            "2": {
                "data": "City,Temperature,Humidity\nNew York,30,65\nLos Angeles,25,50\nChicago,20,70\nHouston,35,80\nPhoenix,40,20",
                "questions": [
                    "Which city had the highest temperature?",
                    "What was the average humidity?"
                ]
            }
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Interpret the following dataset and answer the specific questions provided.

Dataset:
{t['data']}

Questions:
1. {t['questions'][0]}
2. {t['questions'][1]}

Submit your answers as a plain text string in the following format:

Answer 1: [Your answer to question 1]
Answer 2: [Your answer to question 2]"""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        from src.eval_helper import eval_with_llm_judge
        instructions = TaskFamily.get_instructions(t)
        return 1.0 if eval_with_llm_judge(instructions, submission) else 0.0
