from sqlalchemy.testing.plugin.plugin_base import generate_sub_tests


def test_create_genre(client):
    genre_data = {
        'name': 'Disco polo'
    }

    response = client.post('/genres', json=genre_data)

    assert response.status_code == 201
    data = response.json()
    assert data['name'] == 'Disco polo'
    assert 'id' in data
    assert isinstance(data['id'], int)


def test_get_genres_empty(client):
    response = client.get('/genres')

    assert response.status_code == 200
    data = response.json()
    assert data == []


def test_get_genres_with_data(client):
    client.post('/genres', json={'name': 'Disco polo'})

    response = client.get('/genres')

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == 'Disco polo'
    assert 'id' in data[0]


def test_crete_genre_without_name(client):
    genre_name = {}
    response = client.post('/genres', json=genre_name)

    assert response.status_code == 422


def test_update_genre(client):
    create_response = client.post('/genres', json={'name': 'Disco polo'})
    genre_id = create_response.json()['id']

    update_response = client.put(f'/genres/{genre_id}', json={'name': 'Super Disco polo'})
    assert update_response.status_code == 200
    data = update_response.json()
    assert data['name'] == 'Super Disco polo'


def test_delete_genre(client):
    create_response = client.post('/genres', json={'name': 'Disco polo'})
    genre_id = create_response.json()['id']

    delete_response = client.delete(f'/genres/{genre_id}')
    assert delete_response.status_code == 204

    all_genres = client.get('/genres')
    assert all_genres.status_code == 200
    assert len(all_genres.json()) == 0