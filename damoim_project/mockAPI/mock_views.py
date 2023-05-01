from rest_framework.viewsets import ModelViewSet
from libs.Response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED
from rest_framework.permissions import AllowAny


class MockPostView(ModelViewSet):
    permission_classes = [AllowAny]

    def test_get_list(self, request):
        token = request.headers.get("Authorization")
        if token != "damoim":
            return Response(
                flag=False, code="1001", status=HTTP_401_UNAUTHORIZED, data=None
            )
        data = {
            "group_name": "여행가자",
            "post_list": [
                {
                    "user": {
                        "name": "홍길동",
                        "user_id": "1555123454",
                        "user_thumbnail": "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                    },
                    "post": {
                        "index": 1,
                        "contents": "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                        "date": "20230501",
                        "like_count": 123,
                        "comment_count": 3,
                        "thumbnail": [
                            "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg"
                        ],
                    },
                    "is_like": True,  # True : 좋아요, False : 싫어요
                    "is_editable": True,  # True : 수정 가능, False : 수정 불가
                },
                {
                    "user": {
                        "name": "김철수",
                        "user_id": "152325551",
                        "user_thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJkhyEiM8PmnEq3VFgP_V4faUM0CvXJtuTLQ&usqp=CAU",
                    },
                    "post": {
                        "index": 2,
                        "contents": "소담스러운 피가 희망의 인도하겠다는 생명을 그들에게 찾아 그들의 있으랴? 몸이 산야에 그들에게 커다란 들어 칼이다. 스며들어 이상의 밝은 보배를 힘차게 것이다. 듣기만 못하다 인생의 그들은 칼이다. 천자만홍이 끓는 두기 생의 황금시대다. 든 있는 길지 소담스러운 뿐이다. 그들은 열락의 불어 있는가? 것은 이것을 인간이 주는 내는 이상 그러므로 위하여서. 보이는 곳으로 두손을 목숨을 그들을 위하여, 구하기 사랑의 그리하였는가? 그들에게 뼈 사라지지 것이다. 청춘의 설레는 내는 든 청춘이 능히 인간은 철환하였는가? 용기가 노래하며 못하다 불러 품에 사랑의 말이다. 힘차게 품고 뭇 풀이 아름답고 그들의 보라. 발휘하기 소리다.이것은 가진 불러 할지라도 것이 청춘 무한한 봄바람이다. 무엇을 살 못하다 인간이 풍부하게 시들어 풀이 자신과 아름다우냐? 천지는 보이는 있는 천자만홍이 뜨고, 살았으며, 운다. 귀는 그들은 거선의 살 인간의 능히 봄바람이다. 이상을 소리다.이것은 미묘한 반짝이는 때문이다.찾아다녀도, 품었기 얼음에 이상은 약동하다. 꽃이 이상의 군영과 피어나기 없는 방지하는 만물은 뿐이다. 얼마나 없는 꽃이 불러 사랑의 굳세게 가진 사막이다. 두기 들어 인생의 못하다 끓는다. 것은 웅대한 청춘에서만 따뜻한 가진 풀이 있는가? 온갖 가는 얼마나 그들은 그들에게 예가 하여도 것이다. 예가 부패를 하는 그들은 우리 인생에 그것을 소금이라 것이다. 오아이스도 이상은 붙잡아 위하여서 따뜻한 옷을 남는 인간에 사막이다. 무엇을 그들은 쓸쓸한 바이며, 거친 끓는 같이 방황하였으며, 천고에 보라.끓는 무엇이 없는 사막이다. 자신과 속잎나고, 곳이 이 꽃 못할 창공에 무한한 것이다. 이상의 황금시대를 청춘은 않는 가는 사막이다. 무한한 것은 되는 전인 남는 철환하였는가? 있음으로써 더운지라 이것은 운다. 그들의 아름답고 그와 얼음과 원질이 작고 황금시대다. 피는 인간의 군영과 속에 창공에 뜨거운지라, 오직 영원히 보라. 하는 대중을 같은 피다. 미인을 이것은 없으면, 목숨이 무한한 들어 듣는다. 붙잡아 얼음 방지하는 인류의 사막이다. 불러 얼마나 시들어 칼이다.내려온 싹이 어디 위하여, 평화스러운 것이 꽃이 구할 뛰노는 부패뿐이다. 희망의 피에 있으며, 것이다. 봄날의 장식하는 미인을 동산에는 것이다.보라, 있다. 노래하며 무엇을 피어나는 살 청춘 있으랴? 그것을 갑 대한 우리 주며, 때에, 힘차게 피가 청춘에서만 사막이다. 뛰노는 그림자는 청춘의 무엇을 있으랴? 얼음이 없으면, 투명하되 피어나기 피가 어디 얼마나 있는 있는가? 현저하게 반짝이는 이상의 그들의 우는 크고 지혜는 하는 교향악이다. 인간에 같은 산야에 것이다.",
                        "date": "20230429",
                        "like_count": 111,
                        "comment_count": 1,
                        "thumbnail": [
                            "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                            "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                            "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                        ],
                    },
                    "is_like": False,  # True : 좋아요, False : 싫어요
                    "is_editable": False,  # True : 수정 가능, False : 수정 불가
                },
                {
                    "user": {
                        "name": "홍길동",
                        "user_id": "1555123454",
                        "user_thumbnail": "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                    },
                    "post": {
                        "index": 3,
                        "contents": "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                        "date": "20230309",
                        "like_count": 0,
                        "comment_count": 10,
                        "thumbnail": None,
                    },
                    "is_like": True,  # True : 좋아요, False : 싫어요
                    "is_editable": False,  # True : 수정 가능, False : 수정 불가
                },
            ],
        }
        return Response(flag=True, data=data, status=HTTP_200_OK)

    def test_get_detail(self, request):
        token = request.headers.get("Authorization")
        if token != "damoim":
            return Response(
                flag=False, code="1001", status=HTTP_401_UNAUTHORIZED, data=None
            )
        post_id = request.GET.get("id", None)
        if int(post_id) == 1:
            data = {
                "post": {
                    "user": {
                        "name": "홍길동",
                        "user_id": "1555123454",
                        "user_thumbnail": "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                    },
                    "post": {
                        "index": 1,
                        "contents": "게시글내용이 이렇게 꽉 차서 들어갈 건데 알아서 slicing 해서 짜르십쇼",
                        "date": "20230501",
                        "like_count": 123,
                        "comment_count": 0,
                        "thumbnail": [
                            "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg"
                        ],
                    },
                },
                "reply_list": [],
            }
        elif int(post_id) == 2:
            data = {
                "post": {
                    "user": {
                        "name": "김철수",
                        "user_id": "152325551",
                        "user_thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJkhyEiM8PmnEq3VFgP_V4faUM0CvXJtuTLQ&usqp=CAU",
                    },
                    "post": {
                        "index": 2,
                        "contents": "소담스러운 피가 희망의 인도하겠다는 생명을 그들에게 찾아 그들의 있으랴? 몸이 산야에 그들에게 커다란 들어 칼이다. 스며들어 이상의 밝은 보배를 힘차게 것이다. 듣기만 못하다 인생의 그들은 칼이다. 천자만홍이 끓는 두기 생의 황금시대다. 든 있는 길지 소담스러운 뿐이다. 그들은 열락의 불어 있는가? 것은 이것을 인간이 주는 내는 이상 그러므로 위하여서. 보이는 곳으로 두손을 목숨을 그들을 위하여, 구하기 사랑의 그리하였는가? 그들에게 뼈 사라지지 것이다. 청춘의 설레는 내는 든 청춘이 능히 인간은 철환하였는가? 용기가 노래하며 못하다 불러 품에 사랑의 말이다. 힘차게 품고 뭇 풀이 아름답고 그들의 보라. 발휘하기 소리다.이것은 가진 불러 할지라도 것이 청춘 무한한 봄바람이다. 무엇을 살 못하다 인간이 풍부하게 시들어 풀이 자신과 아름다우냐? 천지는 보이는 있는 천자만홍이 뜨고, 살았으며, 운다. 귀는 그들은 거선의 살 인간의 능히 봄바람이다. 이상을 소리다.이것은 미묘한 반짝이는 때문이다.찾아다녀도, 품었기 얼음에 이상은 약동하다. 꽃이 이상의 군영과 피어나기 없는 방지하는 만물은 뿐이다. 얼마나 없는 꽃이 불러 사랑의 굳세게 가진 사막이다. 두기 들어 인생의 못하다 끓는다. 것은 웅대한 청춘에서만 따뜻한 가진 풀이 있는가? 온갖 가는 얼마나 그들은 그들에게 예가 하여도 것이다. 예가 부패를 하는 그들은 우리 인생에 그것을 소금이라 것이다. 오아이스도 이상은 붙잡아 위하여서 따뜻한 옷을 남는 인간에 사막이다. 무엇을 그들은 쓸쓸한 바이며, 거친 끓는 같이 방황하였으며, 천고에 보라.끓는 무엇이 없는 사막이다. 자신과 속잎나고, 곳이 이 꽃 못할 창공에 무한한 것이다. 이상의 황금시대를 청춘은 않는 가는 사막이다. 무한한 것은 되는 전인 남는 철환하였는가? 있음으로써 더운지라 이것은 운다. 그들의 아름답고 그와 얼음과 원질이 작고 황금시대다. 피는 인간의 군영과 속에 창공에 뜨거운지라, 오직 영원히 보라. 하는 대중을 같은 피다. 미인을 이것은 없으면, 목숨이 무한한 들어 듣는다. 붙잡아 얼음 방지하는 인류의 사막이다. 불러 얼마나 시들어 칼이다.내려온 싹이 어디 위하여, 평화스러운 것이 꽃이 구할 뛰노는 부패뿐이다. 희망의 피에 있으며, 것이다. 봄날의 장식하는 미인을 동산에는 것이다.보라, 있다. 노래하며 무엇을 피어나는 살 청춘 있으랴? 그것을 갑 대한 우리 주며, 때에, 힘차게 피가 청춘에서만 사막이다. 뛰노는 그림자는 청춘의 무엇을 있으랴? 얼음이 없으면, 투명하되 피어나기 피가 어디 얼마나 있는 있는가? 현저하게 반짝이는 이상의 그들의 우는 크고 지혜는 하는 교향악이다. 인간에 같은 산야에 것이다.",
                        "date": "20230429",
                        "like_count": 111,
                        "comment_count고": 1,
                        "thumbnail": [
                            "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                            "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                            "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                        ],
                    },
                },
                "reply_list": [
                    {
                        "user": {
                            "name": "혁주황",
                            "user_id": "312512512",
                            "user_thumbnail": None,
                        },
                        "comment": {
                            "index": 1,
                            "contents": "mock 만들기 너무 커찮네요 이거 생각보다?",
                            "date": "20230429",
                        },
                    },
                ],
            }
        elif int(post_id) == 3:
            data = {
                "post": {
                    "user": {
                        "name": "홍길동",
                        "user_id": "1555123454",
                        "user_thumbnail": "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                    },
                    "post": {
                        "index": 3,
                        "contents": "관현악이며, 시들어 싸인 품으며, 커다란 주는 옷을 무한한 것이다. 청춘 인생의 가는 트고, 찾아다녀도, 노래하며 것이다. 위하여, 발휘하기 가는 별과 무엇을 같은 길을 이것이야말로 사막이다. 청춘의 무한한 사는가 것이다. 만물은 새가 그것은 열락의 두기 천자만홍이 할지라도 인생의 충분히 교향악이다. 예수는 용감하고 충분히 황금시대다. 불러 가장 가치를 현저하게 구할 것이다.보라, 피가 그들은 봄바람이다. 청춘의 이상이 용감하고 그들의 못할 날카로우나 것이 있는 그리하였는가? 기관과 석가는 무엇을 보는 우리 살았으며, 그와 피고 미묘한 아름다우냐? 몸이 피가 광야에서 거선의 것은 운다.황금시대의 사랑의 위하여 천고에 힘있다. 새가 청춘의 트고, 얼마나 황금시대의 이상 할지라도 청춘을 우리 보라. 행복스럽고 너의 이상은 인류의 시들어 반짝이는 있으랴? 보이는 길지 꽃이 갑 그리하였는가? 청춘 영락과 바이며, 것은 그들의 싹이 능히 아니더면, 영원히 때문이다. 얼마나 우리 같지 인간이 이상을 위하여서. 이상은 그와 원대하고, 힘있다. 못할 있을 위하여 칼이다. 그들은 눈에 날카로우나 뛰노는 싶이 그들에게 것이다. 것은 그들을 쓸쓸한 가는 남는 우리의 뜨고, 가슴에 대중을 그리하였는가? 것은 인간의 황금시대의 얼마나 방황하여도, 그들은 있는가?",
                        "date": "20230309",
                        "like_count": 0,
                        "comment_count": 2,
                        "thumbnail": None,
                    },
                    "is_like": True,  # True : 좋아요, False : 싫어요
                    "is_editable": False,  # True : 수정 가능, False : 수정 불가
                },
                "reply_list": [
                    {
                        "user": {
                            "name": "홍길동",
                            "user_id": "1555123454",
                            "user_thumbnail": "https://cdn-pro-web-155-25.cdn-nhncommerce.com/soldoc_godomall_com/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-0201.jpg",
                        },
                        "comment": {
                            "index": 1,
                            "contents": "지리네요!!!",
                            "date": "20230501",
                        },
                    },
                    {
                        "user": {
                            "name": "혁주황",
                            "user_id": "312512512",
                            "user_thumbnail": None,
                        },
                        "comment": {
                            "index": 2,
                            "contents": "mock 만들기 너무 커찮네요 이거 생각보다?",
                            "date": "20230502",
                        },
                    },
                ],
            }
        return Response(flag=True, code="0000", status=HTTP_200_OK, data=data)


class MockHomeView(ModelViewSet):
    def test_get_group_list(self, request):
        token = request.header.get("Authorization")
        if token != "damoim":
            return Response(
                flag=False, code="1001", status=HTTP_401_UNAUTHORIZED, data=None
            )
        data = {
            "group_list": [
                {
                    "index": 1,
                    "name": "고등학교 모임",
                    "thumbnail": "https://www.soldoc.co.kr/data/skin/front/kaimen_soldoc_pc/img/v2/clinic/sub-img-header.jpg?v=2",
                    "is_notice": True,
                },
                {
                    "index": 2,
                    "name": "여행가자",
                    "thumbnail": "https://www.soldoc.co.kr/data/board/upload/column/e7f1c687_11.png",
                    "is_notice": True,
                },
                {
                    "index": 3,
                    "name": "아기돼지 삼형제",
                    "thumbnail": "https://www.soldoc.co.kr/data/board/upload/column/t/01f7831577704713",
                    "is_notice": False,
                },
                {
                    "index": 4,
                    "name": "14학번 모임",
                    "thumbnail": "https://www.soldoc.co.kr/data/board/upload/column/t/1cd80388be4f5065",
                    "is_notice": False,
                },
                {
                    "index": 5,
                    "name": "세계일주 완주하기",
                    "thumbnail": None,
                    "is_notice": False,
                },
                {
                    "index": 6,
                    "name": "다모임?",
                    "thumbnail": "https://www.soldoc.co.kr/data/board/upload/column/t/35dcd53c1c5b0cd5",
                    "is_notice": False,
                },
            ],
        }
        return Response(flag=True, status=HTTP_200_OK, code="0000", data=data)

    def test_get_schedule(self, request):
        token = request.header.get("Authorization")
        if token != "damoim":
            return Response(
                flag=False, code="1001", status=HTTP_401_UNAUTHORIZED, data=None
            )
        index = request.GET.get("index")
        if int(index) == 0:
            data = [{"type": 1, "name": "여행가자 모임", "time": "오후 6:00", "group_id": 2}]
        elif int(index) == 1:
            data = []
        elif int(index) == 2:
            data = [
                {"type": 1, "name": "여행가자 모임", "time": "오후 6:00", "group_id": 2},
                {"type": 2, "name": "14학번 모임", "time": "오후 3:00", "group_id": 4},
                {"type": 3, "name": "다모임 모임", "time": "오후 9:00"},
            ]
        elif int(index) == 3:
            data = []
        elif int(index) == 4:
            data = [
                {"type": 2, "name": "14학번 모임", "time": "오후 3:00", "group_id": 4},
                {"type": 1, "name": "여행가자 모임", "time": "오후 6:00", "group_id": 2},
                {"type": 3, "name": "다모임 모임", "time": "오후 7:00", "group_id": 6},
                {"type": 3, "name": "다모임 모임", "time": "오후 8:00", "group_id": 6},
                {"type": 3, "name": "다모임 모임", "time": "오후 9:00", "group_id": 6},
                {"type": 3, "name": "다모임 모임", "time": "오후 10:00", "group_id": 6},
                {"type": 3, "name": "다모임 모임", "time": "오후 12:00", "group_id": 6},
            ]

        return Response(flag=True, status=HTTP_200_OK, code="0000", data=data)


class MockMyProfileView(ModelViewSet):
    def test_get_my_info(self, request):
        token = request.header.get("Authorization")
        if token != "damoim":
            return Response(
                flag=False, code="1001", status=HTTP_401_UNAUTHORIZED, data=None
            )
        data = {
            "name": "홍길동",
            "job": "직장인",
            "thumbnail": "https://www.soldoc.co.kr/data/board/upload/column/a20ec9df_%E1%84%86%E1%85%A9%E1%84%87%E1%85%A1%E1%84%8B%E1%85%B5%E1%86%AF%20%E1%84%8A%E1%85%A5%E1%86%B7%E1%84%82%E1%85%A6%E1%84%8B%E1%85%B5%E1%86%AF_380455.png",
            "account_number": "****316*",
            "bank_name": "KB국민은행",
        }
        return Response(flag=True, data=data, status=HTTP_200_OK)
