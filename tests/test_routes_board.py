from app.models.board import Board
import pytest



# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_cards_one_saved_boards(client, one_board):
    # Act
    response = client.get("/boards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    print(response_body)
    assert response_body == [
        {
            "id": 1,
            "title": "Ada is great",
            "owner": "Nina"
        }
    ]

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_board(client, one_board):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "Ada is great",
            "owner": "Nina"
        }
    }

# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_board_not_found(client):
    # Act
    response = client.get("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body=={"message": "board 1 not found"}



# @pytest.mark.skip(reason="No way to test this feature yet")
def test_create_board(client):
    # Act
    response = client.post("/boards", json={
        "title": "A Brand New board",
        "owner": "Marlyn"
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "A Brand New board",
            "owner": "Marlyn"
        }
    }
    new_board = Board.query.get(1)
    assert new_board
    assert new_board.title == "A Brand New board"
    assert new_board.owner == "Marlyn"


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_put_board_not_found(client):
    # Act
    response = client.put("/boards/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body=={"message": "board 1 not found"}


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_update_board(client, one_board):
    # Act
    response = client.put("/boards/1", json={
        "title": "Updated board title"
    })
    response_body = response.get_json()
    print(response_body)

    # Assert
    assert response.status_code == 200
    assert "board" in response_body
    assert response_body == {
        "board": {
            "id": 1,
            "title": "Updated board title",
            "owner": "Nina"
        }
    }
    board = Board.query.get(1)
    assert board.title == "Updated board title"
    assert board.owner == "Nina"


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_cards_for_specific_board_no_board(client):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message":"board 1 not found"}


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_cards_for_specific_board_no_cards(client, one_board):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "cards" in response_body
    assert len(response_body["cards"]) == 0
    assert response_body == {
        "id": 1,
        "title": "Ada is great",
        "owner": "Nina",
        "cards": []
    }


# @pytest.mark.skip(reason="No way to test this feature yet")
def test_get_cards_for_specific_board(client, one_card_belongs_to_one_board):
    # Act
    response = client.get("/boards/1/cards")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert "cards" in response_body
    assert len(response_body["cards"]) == 1
    assert response_body == {
        "id": 1,
        "title": "Ada is great",
        "owner": "Nina",
        "cards": [
            {
                "id": 1,
                "board_id": 1,
                "message":"Be happy",
                "likes_count":0
            }
        ]
    }
