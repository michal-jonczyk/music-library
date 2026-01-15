def test_create_artist(client):
    artist_data = {
        'name': 'Pink Floyd',
        'description': 'British rock band'
    }

    response = client.post('/artists',json=artist_data)

    assert response.status_code == 201

    data = response.json()
    assert data['name'] == 'Pink Floyd'
    assert data['description'] == 'British rock band'
    assert 'id' in data
    assert isinstance(data['id'], int)


def test_get_artists_empty(client):

    response = client.get('/artists')

    assert response.status_code == 200
    assert response.json() == []


def test_get_artists_with_data(client):

    client.post('/artists', json={
        'name': 'Pink Floyd',
        'description': 'British rock band'
    })


    response = client.get('/artists')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == 'Pink Floyd'


def test_create_artist_without_name(client):

    artist_data = {
        'description': 'Rock band'
    }

    response = client.post('/artists', json=artist_data)

    assert response.status_code == 422


def test_get_artist_by_id(client):

    create_response = client.post('/artists', json={
        'name': 'Pink Floyd',
        'description': 'British rock band'
    })
    artist_id = create_response.json()["id"]

    response = client.get(f'/artists/{artist_id}')

    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Pink Floyd'
    assert data['id'] == artist_id


def test_update_artist(client):

    create_response = client.post('/artists', json={
        'name': 'Pink Floyd',
        'description': 'British rock band'
    })
    artist_id = create_response.json()['id']

    update_data = {
        'name': 'Pink Floyd',
        'description': 'Legendary British rock band'
    }
    response = client.put(f'/artists/{artist_id}', json=update_data)

    assert response.status_code == 200
    data = response.json()
    assert data['description'] == 'Legendary British rock band'


def test_delete_artist(client):

    create_response = client.post('/artists', json={
        'name': 'Pink Floyd',
        'description': 'British rock band'
    })
    artist_id = create_response.json()['id']

    response = client.delete(f'/artists/{artist_id}')

    assert response.status_code == 204

    get_response = client.get(f'/artists/{artist_id}')
    assert get_response.status_code == 404