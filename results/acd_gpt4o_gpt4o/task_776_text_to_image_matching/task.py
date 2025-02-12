class TaskFamily:
    @staticmethod
    def get_tasks() -> dict[str, dict]:
        return {
            "1": {"descriptions": ["A red apple on a wooden table with a rustic background.", "A group of children playing soccer in a green park.", "A black cat sitting on a windowsill with a city skyline view."], "images": ["img1.jpg", "img2.jpg", "img3.jpg"]},
            "2": {"descriptions": ["A beach with golden sand and tall palm trees.", "A snowy mountain landscape with a wooden cabin and smoke coming from the chimney.", "A city skyline at night with brightly illuminated skyscrapers and a reflection in the river.", "A bustling market with colorful stalls and people shopping."], "images": ["img4.jpg", "img5.jpg", "img6.jpg", "img7.jpg"]}
        }

    @staticmethod
    def get_instructions(t: dict) -> str:
        return f"""Your task is to match the following textual descriptions to the correct images from the provided set:

Descriptions:
{t['descriptions']}

Images:
{t['images']}

Provide your matches in the format: 'description_index:image_filename'. For example, '1:img1.jpg, 2:img2.jpg, 3:img3.jpg'. Ensure each description is matched to one image only. Double-check your matches to ensure accuracy."""

    @staticmethod
    def score(t: dict, submission: str) -> float | None:
        correct_matches = {
            "1": {"1:img1.jpg", "2:img2.jpg", "3:img3.jpg"},
            "2": {"1:img4.jpg", "2:img5.jpg", "3:img6.jpg", "4:img7.jpg"}
        }
        submitted_matches = set(submission.split(', '))
        task_id = "1" if t['descriptions'][0] == "A red apple on a wooden table with a rustic background." else "2"
        return 1.0 if submitted_matches == correct_matches[task_id] else 0.0
