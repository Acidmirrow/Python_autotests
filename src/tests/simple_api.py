import requests

def test_get_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    print("userId = "+str(response.json()['userId']))
    print("id = "+str(response.json()['id']))
    print("title = "+response.json()['title'])
    print("body = "+response.json()['body'])


def test_get_array_from_json():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data=response.json()

    posts = data["posts"]
    assert isinstance(posts, list), "'posts' is not a list"

    for post in posts :
        print(post)