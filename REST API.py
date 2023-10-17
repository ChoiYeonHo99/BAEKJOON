import requests
import json

# GET
# 127.0.0.1은 localhost로 대체 가능 
url = "http://127.0.0.1:3000/todos" # 전체 todos 데이터 받아오기
url_items = "http://localhost:3000/todos/1" # todos의 1번째 데이터 받아오기

response = requests.get(url_items)

print(response.text) # 전체 response 결과
print(response.json()["content"]) # response에서 content에 해당하는 결과

# 응답(Response) 데이터가 JSON 형식이므로 바로 파이썬 객체로 변환
data = response.json()

# 모든 사용자(user) 정보를 확인하며 이름 정보만 삽입
name_list = []
for user in data:
    name_list.append(user['name'])
print(name_list)

# 다른 표현법
for i in range(len(data)):
    print(data[i]['name'])



#POST
# 127.0.0.1은 localhost로 대체 가능 
url = "http://127.0.0.1:3000/todos" # todos에 데이터 추가

# 추가할 데이터 생성
newItem = {
    "id": 4,
    "content": "Python",
    "completed": True
}

# 데이터 추가
response = requests.post(url_items, data=json.dumps(newItem))

# response 결과 확인
print("response.text: ", response.text)