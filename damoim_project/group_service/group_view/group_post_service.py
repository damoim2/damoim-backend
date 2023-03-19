from rest_framework import viewsets


"""
# 글목록 불러오기
{
    "is_success": flag,
    "code": code,
    "data": {
        "post_list" :[
            {
                "user" : {
                    "name": "홍길동",
                    "user_id" "12",
                    "user_thumbnail" : "BASE64CODE"
                },
                "post" : {
                    "contents" : "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                    "date" : "20230303",
                    "like_count" : 0,
                    "comment_count" : 0,
                    "thumbnail" : "Base64 Code"
                }
                "is_like" : True, # True : 좋아요, False : 싫어요
                "is_editable" : True # True : 수정 가능, False : 수정 불가
            }
        ]
    }
}
"""

"""
# 글 디테일 불러오기
{
    "is_success": True,
    "code": code,
    "data": {
        "post":
            {
                "user" : {
                    "name": "홍길동",
                    "user_id" "12",
                    "user_thumbnail" : "BASE64CODE",
                },
                "post" : {
                    "contents" : "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                    "date" : "20230303",
                    "like_count" : 0,
                    "thumbnail_list" : ["Base64 Code"]
                }
            }
        
        "reply_list" :[
            {
                "user" : {
                    "name": "홍길동",
                    "user_id" "12",
                    "user_thumbnail" : "BASE64CODE",
                },
                "comment" : {
                    "contents" : "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                    "date" : "20230303",
                }
            }
        ]
    }
} 

"""


# 댓글작성하기
# 좋아요 하기
# 사진 첨부하기
