def test_create_album(client):
    artist_response = client.post('/artists', json={
        'name': 'Pink Floyd',
        'description': 'British rock band'
    })
    artist_id = artist_response.json()['id']

    genre_response = client.post('/genres', json={
        'name': 'Rock'
    })
    genre_id = genre_response.json()['id']

    album_data = {
        'artist_id': artist_id,
        'genre_id': genre_id,
        'title': 'The Wall',
        'release_year': 1979
    }

    response = client.post('/albums', json=album_data)

    assert response.status_code == 201
    data = response.json()
    assert data['title'] == 'The Wall'
    assert data['release_year'] == 1979
    assert 'id' in data


def test_get_albums_empty(client):
    response = client.get('/albums')

    assert response.status_code == 200
    assert response.json() == []


def test_get_albums_with_data(client):
    artist = client.post('/artists', json={'name': 'Pink Floyd'})
    artist_id = artist.json()['id']

    genre = client.post('/genres', json={'name': 'Rock'})
    genre_id = genre.json()['id']

    client.post('/albums', json={
        'artist_id': artist_id,
        'genre_id': genre_id,
        'title': 'The Wall',
        'release_year': 1979
    })

    response = client.get('/albums')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['title'] == 'The Wall'
    assert data[0]['artist'] == 'Pink Floyd'
    assert data[0]['genre'] == 'Rock'


def test_get_album_by_id(client):
    artist = client.post('/artists', json={'name': 'Pink Floyd'})
    artist_id = artist.json()['id']

    genre = client.post('/genres', json={'name': 'Rock'})
    genre_id = genre.json()['id']

    create_response = client.post('/albums', json={
        'artist_id': artist_id,
        'genre_id': genre_id,
        'title': 'The Wall',
        'release_year': 1979
    })
    album_id = create_response.json()['id']

    response = client.get(f'/albums/{album_id}')

    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'The Wall'
    assert data['artist_id'] == artist_id
    assert data['genre_id'] == genre_id


def test_update_album(client):
    artist = client.post('/artists', json={'name': 'Pink Floyd'})
    artist_id = artist.json()['id']

    genre = client.post('/genres', json={'name': 'Rock'})
    genre_id = genre.json()['id']

    create_response = client.post('/albums', json={
        'artist_id': artist_id,
        'genre_id': genre_id,
        'title': 'The Wall',
        'release_year': 1979
    })
    album_id = create_response.json()['id']

    update_data = {
        'artist_id': artist_id,
        'genre_id': genre_id,
        'title': 'The Wall - Remastered',
        'release_year': 2011
    }
    response = client.put(f'/albums/{album_id}', json=update_data)

    assert response.status_code == 200
    data = response.json()
    assert data['title'] == 'The Wall - Remastered'
    assert data['release_year'] == 2011


def test_delete_album(client):
    artist = client.post('/artists', json={'name': 'Pink Floyd'})
    artist_id = artist.json()['id']

    genre = client.post('/genres', json={'name': 'Rock'})
    genre_id = genre.json()['id']

    create_response = client.post('/albums', json={
        'artist_id': artist_id,
        'genre_id': genre_id,
        'title': 'The Wall',
        'release_year': 1979
    })
    album_id = create_response.json()['id']

    response = client.delete(f'/albums/{album_id}')
    assert response.status_code == 204

    all_albums = client.get('/albums')
    assert all_albums.status_code == 200
    assert len(all_albums.json()) == 0