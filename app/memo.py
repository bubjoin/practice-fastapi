from fastapi import APIRouter

memo_router = APIRouter()

memo_list = list()


@memo_router.get("/memo")
async def retrieve_memos() -> dict:
    return {
        "memos": memo_list
    }

@memo_router.post("/memo")
async def add_memo(memo: dict) -> dict:
    memo_list.append(memo)
    return {
        "message": "Memo added"
    }

# using a url bar in browsers always results in GET
#
# How to Send Post by Using Requests
# import requests
# import json
# # res = requests.get('http://localhost/memo')
# data = {'20231130':'Today I am going to Seoul!'}
# res = requests.post('http://localhost/memo', data=json.dumps(data))
# print(res.content)