import html2text
from stackoverflow_markdown.stackexchange import get_data

h = html2text.HTML2Text()
h.body_width = 0


def parse_question(title, body, author_name, author_link, question_link):
    return f"""# {title}

{body}

_Asked by:_ [{author_name}]({author_link})
[Question Link]({question_link})

---

"""


def parse_answer(body, author_name, author_link):
    return f"""## Answer

_Answered by:_ [{author_name}]({author_link})

{body}
"""


def parse_data(id):
    question, answer = get_data(id)

    question_title = h.handle(question["title"]).strip()
    question_body = h.handle(question["body"]).strip()

    question_text = parse_question(title=question_title, body=question_body, author_name=question['owner']
                                   ['display_name'], author_link=question['owner']['link'], question_link=question['link'])

    answer_body = h.handle(answer['body']).strip()
    answer_text = parse_answer(
        body=answer_body, author_name=answer['owner']['display_name'], author_link=answer['owner']['link'])

    return question_text + answer_text
