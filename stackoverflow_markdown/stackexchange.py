import requests
import pprint

QUESTION_URL = 'https://api.stackexchange.com/2.3/questions/{}?site=bitcoin.stackexchange&filter=withbody'
ANSWER_URL = 'https://api.stackexchange.com/2.3/answers/{}?site=bitcoin.stackexchange&filter=withbody'
ANSWER_LIST_URL = 'https://api.stackexchange.com/2.3/questions/{}/answers?site=bitcoin.stackexchange'


def get_question(id):
    """Fetch the question from stackoverflow.com and return the json data."""
    url = QUESTION_URL.format(id)
    try:
        response = requests.get(url).json()

        assert len(response['items']) == 1
        assert response['items'][0]['question_id'] == id

        return response['items'][0]
    except:
        print(f'Failed to fetch question {id}')
        raise


def get_answer_ids(id):
    """List of answer id's for the question."""
    url = ANSWER_LIST_URL.format(id)
    try:
        response = requests.get(url).json()

        return [r['answer_id'] for r in response['items']]
    except:
        print(f'Failed to fetch answers for question {id}')
        raise


def get_answer(id):
    """Fetch the answer of the id and return the json data"""
    url = ANSWER_URL.format(id)
    try:
        response = requests.get(url).json()

        assert len(response['items']) == 1
        assert response['items'][0]['answer_id'] == id

        return response['items'][0]
    except:
        print(f'Failed to fetch answer {id}')
        raise


def prompt_ids(id_list):
    """Prompt the user to select from the list of ids."""
    print('[!] There is no accepted answer, choose the answer you want to use.')
    for i, id in enumerate(id_list):
        print(f'{i+1}: {id}')

    while True:
        try:
            selection = int(input('> '))
            assert selection > 0 and selection <= len(id_list)
            return id_list[selection-1]
        except:
            print('Invalid selection !')


def get_data(id):
    question = get_question(id)
    if 'accepted_answer_id' in question:
        print('[*] Found an accepted answer')
        answer = get_answer(question["accepted_answer_id"])
    else:
        answer_ids = get_answer_ids(id)
        answer_id = prompt_ids(answer_ids)
        answer = get_answer(answer_id)

    return question, answer
