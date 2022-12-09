import pytest
import json


def test_create_summary(test_app_with_db):
    payload = json.dumps({'url': 'https://aboba.com'})
    response = test_app_with_db.post('/summaries/', data=payload)

    assert response.status_code == 201
    assert response.json()['url'] == 'https://aboba.com'


def test_create_summaries_invalid_json(test_app):
    invalid_payload = json.dumps({})
    response = test_app.post('/summaries/', data=invalid_payload)

    assert response.status_code == 422
    assert response.json() == {
        'detail': [
            {
                'loc': ['body', 'url'],
                'msg': 'field required',
                'type': 'value_error.missing'
            }
        ]
    }


def test_read_summary(test_app_with_db):
    payload = json.dumps({'url': 'https://aboba.com'})
    response = test_app_with_db.post('/summaries/', data=payload)
    expected_summary_id = response.json()['id']

    response = test_app_with_db.get(f'/summaries/{expected_summary_id}/')

    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict['id'] == expected_summary_id
    assert response_dict['url'] == 'https://aboba.com'
    assert response_dict['summary']
    assert response_dict['created_at']


def test_read_all_summaries(test_app_with_db):
    ids = []
    for i in range(3):
        response = test_app_with_db.post(
            '/summaries/', data=json.dumps({'url': f'https://aboba{i+1}.com'}))
        assert response.status_code == 201
        ids.append(response.json()['id'])

    response = test_app_with_db.get('/summaries/')
    assert response.status_code == 200

    response_list = response.json()
    filtered_list = [e for e in response_list if e['id'] in ids]
    assert len(filtered_list) == len(ids)