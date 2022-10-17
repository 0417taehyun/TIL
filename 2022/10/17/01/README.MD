---
title: "게으름과 부지런함(Lazy vs Eager)"
description: "머신 러닝, 웹, ORM(Obejct Relational Mapping), 그리고 함수형 프로그래밍에서의 지연(Lazy)"
date: "2022-10-17"
---

# 게으름과 부지런함(Lazy vs Eager)

## 목차

- [도입](#도입)
- [머신러닝에서의 게으름과 부지런함](#머신러닝에서의-게으름과-부지런함)
  - [머신러닝의 학습과 테스트](#머신러닝의-학습과-테스트)
  - [게으른 학습(Lazy Learning)](#게으른-학습lazy-learning)
  - [즉각적인 학습(Eager Learning)](#즉각적인-학습eager-learning)
- [웹에서의 게으름과 부지런함](#웹에서의-게으름과-부지런함)
  - [지연 로딩(Lazy Loading)](#지연-로딩lazy-loading)
  - [구현 방법](#구현-방법)
- [ORM에서의 게으름과 부지런함](#orm에서의-게으름과-부지런함)
  - [ORM(Object-Relational Mapping)](#ormobject-relatinoal-mapping)
  - [장고(Django)의 쿼리셋(QuerySet)](#쟝고django의-쿼리셋queryset)
  - [N+1 문제](#n1-문제)
  - [기타 다른 프레임워크](#기타-다른-프레임워크)
- [함수형 프로그래밍에서의 게으름과 부지런함](#함수형-프로그래밍에서의-게으름과-부지런함)
  - [함수형 프로그래밍(Functional Programming)](#함수형-프로그래밍functional-programming)
  - [지연 평가(Lazy Evaluation)](#지연-평가lazy-evaluation)
  - [피보나치 수열](#피보나치-수열)
- [결론](#결론)
- [참고](#참고)

## 도입

머신 러닝을 배우는데 게으른 학습(Lazy Learning)과 즉각적인 학습(Eager Learning)이라는 내용이 나왔다. (Eager를 '즉각적인'으로 번역한 건 아래 다른 프로그래밍 용어에서 주로 지연과 즉각으로 번역하기 때문에 선택한 용어다.)

어디선가 많이 들어본 용어라는 생각이 들었다. 지연 로딩(Lazy Loading)이라는 용어도 생각났고 지연 평가(Lazy Evaluation)라는 용어도 생각났다. 용어 간의 추상적인 연관성이 있을 수 있으나 함께 떠오른 김에 정리해두면 좋을 것 같아서 정리해본다.

## 머신러닝에서의 게으름과 부지런함

### 머신러닝의 학습과 테스트

머신러닝은 기본적으로 기존의 데이터를 가지고 학습을 시켜 모델을 만든 뒤 새로운 데이터가 들어오면 이를 구축한 모델을 통해 예측하는 방법이라 요약할 수 있는데 이때 구축한 모델이 올바르게 작동하는지 알게 하기 위해서는 평가가 필요하다. 그런데 새로운 데이터를 통해 평가를 하려면 그 데이터가 생길 때까지 기다려야 하는 비효율성이 발생하기 때문에 기존 데이터를 학습 데이터(Trainig Data)와 테스트 데이터(Test Data)로 나누어 학습 데이터를 통해 모델을 구축하고 테스트 데이터로 이를 평가한다.

### 게으른 학습(Lazy Learning)

머신러닝에서 게으른 학습(Lazy Learning)을 하는 모델로는 대표적으로 KNN(K-Nearnest Neighbors)이 있는데 KNN은 새로운 데이터가 주어졌을 때 해당 데이터의 특성과 유사한 학습 데이터를 찾아내는 방식으로 작동하기 때문에 새로운 데이터가 들어올 때까지 기다려야 해서 게으른 학습 또는 **사례 기반 학습(Instance based Learning)**이라 한다. 또한 모델이 결국 기존의 데이터를 통해 학습을 하는 형태가 아니기 때문에 학습 데이터라 부르지 않고 **참조 데이터(Reference Data)**라 한다.

### 즉각적인 학습(Eager Learning)

반대로 즉각적인 학습(Eager Learning)의 경우 대표적으로 결정 트리(Decision Tree)나 비지도 학습에서의 K-평균 알고리즘(K-Means Algorithm)이 있는데 게으른 학습과 달리 우리가 앞서 이야기한 것처럼 기존 데이터를 학습 데이터와 테스트 데이터로 구분하여 모델을 구축하고 평가한 뒤 새로운 데이터가 들어올 경우 구축한 모델을 기반으로 이를 예측한다. 따라서 즉각적인 학습 또는 모델을 기반으로 학습을 하기 때문에 **모델 기반 학습(Model based Learning)**이라 한다.

## 웹에서의 게으름과 부지런함

### 지연 로딩(Lazy Loading)

웹 페이지에서 고화질의 여러 이미지 파일을 한번애 보여줘야 한다고 생각해보자. 예를 들면 나사(NASA) 홈페이지에서 제임스 웹이 촬영한 여러 장의 우주 고화질 사진을 한번에 불러와야 하는 경우다. (해당 사진은 나사의 [James Webb Space Telescope](https://www.nasa.gov/content/goddard/webb-telescope-image-galleries-from-nasa)에서 볼 수 있다.) 여러 사람들의 이목이 집중되어 있는 만큼 홈페이지에 접속하여 고화질의 이미지를 로딩하는 사람이 무척 많을 것이다. 그러면 그 많은 고화질의 이미지가 다 로딩될 때까지 사용자는 웹 페이지에서 하염없이 모자이크처럼 뿌연, 덜 로딩된 이미지만을 보고 있어야 하는 걸까? 차라리 현재 사용자가 보고 있는 화면에 놓여 있는 이미지만 우선 로딩시키고 아직 스크롤을 내려서 보지 않은 아래 이미지들은 로딩하지 않고 대기시키면 어떨까? 그렇다면 사용자는 본인이 스크롤을 내리면서 보게 되는 이미지는 해당 이미지만 로딩되기 때문에 기다릴 필요 없이 즉시 볼 수 있고 나머지는 대기 상태에 들어가게 된다. 처음 웹 페이지에 접속했을 때 기다려야 하는 신호 없이 곧바로 사용자와 상호작용(Interaction)한다는 측면에서 사용자 경험(User Experience, UX)이 좋다고 할 수 있다.

이러한 해결 방식, 다시 말해 사용자가 현재 화면에서 보는 이미지 -혹은 콘텐츠- 만을 우선적으로 로딩시키고 나머지는 대기 상태에 두었다가 사용자가 해당 부분에 접근하게 되면 그제서야 로딩시키는 걸 **지연 로딩(Lazy Loading)**이라 한다. 단어 그대로 로딩을 지연시켜서 사용자가 콘텐츠를 하염없이 기다릴 필요도 없고 서버 입장에서도 현재 보고 있는 컨텐츠에 대해서만 로딩하면 되기 때문에 자원이 절약된다.

### 구현 방법

자바스크립트의 이벤트 핸들러를 사용하는 등 여러 구현 방법이 있지만 이미지 태그의 속성으로도 가능한 방법 하나만을 간단하게 소개하려 한다. 아래 HTML 코드와 같이 `<img />` 태그 내에 `loading` 속성의 값을 `"lazy"` 혹은 `"eager"`로 전달하면 지연 로딩 혹은 즉시 로딩(Eager Loading)으로 이미지가 불러와진다. **즉시 로딩**은 단어 그대로 지연 로딩의 반대로 웹 페이지를 최초 로딩할 때 즉각적으로 모든 콘텐츠를 한 번에 로딩하는 걸 의미한다.

```HTML
<img src="cat.jpg" loading="lazy" />
<img src="dog.jpg" loading="eager" />
```

지연 로딩을 사용할 때 유의할 점은 검색 엔진 최적화 부분에 있어 **CLS(Cumulative Layout Shift)**를 신경써야 한다는 것이다. CLS는 단어 그대로 레이아웃 이동의 누적에 대한 부분으로 페이지를 로딩할 때 레이아웃의 변경이 얼마나 일어났는지 확인하는 것이다. 어떤 특정 이미지에 대해 지연 로딩을 설정할 경우 만약 해당 이미지 아래에 텍스트가 있을 때 이미지가 순간적으로 로딩되면서 텍스트가 아래로 밀리게 된다. 왜냐하면 이전까지는 로딩을 하고 있지 않았기 때문에 이미지가 존재하지 않던 것에서 스크롤을 내려 로딩이 되는 순간 해당 텍스트가 이미지의 크기 만큼 아래로 밀리기 때문이다. 이 과정에서 레이아웃 변경이 발생하고 검색 엔진은 이에 대해 패널티를 부여해 가독성이 떨어지는 웹 사이트로 평가한다. 따라서 이를 예방하기 위해 반드시 이미지의 기본적인 높이 값을 설정하여 로딩이 되지 않더라도 해당 높이 만큼 빈 공간을 갖게 만들어 레이아웃 변경이 발생하지 않게 해야 한다. 아래 CSS 코드와 같이 지연 로딩의 대상이 되는 이미지 태그의 `height` 속성값에 `auto`를 부여할 경우 자동으로 이미지의 본래 높이만큼 빈 공간이 부여된다.

```CSS
img {
    max-width: 100%;
    height: auto;
}
```

물론 제대로 구현하지 않았을 때의 검색 엔진 패널티 외에도 이런 네이티브 방식, 다시 말해 HTML 내의 `<img />` 태그를 사용한 방식은 여러 단점이 존재한다. 관련해서는 궁금할 경우 더 찾아보길 바란다.

## ORM에서의 게으름과 부지런함

### ORM(Object-Relatinoal Mapping)

ORM(Object-Relational Mapping)이란 객체와 데이터베이스 관계를 연결해주는 API(Application Programming Interface)로 쉽게 웹 애플리케이션에서 데이터베이스에 접근하여 데이터를 객체로 다루게 해주는 역할을 한다고 생각하면 된다.

### 쟝고(Django)의 쿼리셋(QuerySet)

파이선 웹 프레임워크인 장고(Django)에는 쿼리셋(QuerySet)이라는 ORM이 내장되어 있는데 이를 사용하면서 겪게 되는 것 중 하나가 바로 지연 로딩(Lazy Loading)이다. 기본적으로 공식 문서 중 [Laziness in Django](https://docs.djangoproject.com/en/4.1/topics/performance/) 부분을 확인해보면 쿼리셋에 대해 장고는 아래와 같이 설명하고 있다.

> Django is itself quite lazy. A good example of this can be found in the evaluation of QuerySets. QuerySets are lazy. Thus a QuerySet can be created, passed around and combined with other QuerySets, without actually incurring any trips to the database to fetch the items it describes. What gets passed around is the QuerySet object, not the collection of items that - eventually - will be required from the database.

쉽게 쿼리셋은 정말 필요할 때가 아니면 쿼리를 실행하지 않는다고 생각하면 된다. 이게 정확히 무슨 뜻인지 딜리버리 히어로 코리아의 김성렬님께서 2020년 PyCon Korea에서 발표한 [Django ORM (QuerySet)구조와 원리 그리고 최적화전략](https://www.youtube.com/watch?v=EZgLfDrUlrk) 영상 속 설명 및 예제를 조금 각색해서 가볍게 살펴보자.

아래와 같이 `User` 테이블에 있는 모든 사용자 데이터를 조회하는 로직이 있다고 가정해보자. 주석으로 표시한 1번 부분에서 쿼리가 실행이 될까 아니면 2번 부분에서 쿼리가 실행이 될까?

```Python
def user_view(request: WSGIRequest):
    users: QuerySet = User.objects.all() # 1번
    user_list: list[User] = list(users) # 2번
```

정답은 2번이다. 쿼리셋은 우리가 생각했을 때 쿼리사 수행될 것 같은 1번 부분에서는 아직 쿼리셋 객체이며 실질적으로 쿼리셋을 `list` 함수를 통해 배열 객체로 만드는 순간에 쿼리를 수행해서 사용자 데이터를 조회한다. 다시 말해 앞서 말했던 것처럼 정말 필요한 순간에 쿼리를 수행한 것이다. 그리고 이를 곧 **지연 로딩(Lazy Loading)**이라 한다.

그렇다면 이제 아래 코드를 한 번 살펴보자. 첫 번째 사용자와 전체 사용자를 조회하는 로직이다. 아래의 경우 쿼리는 총 몇 번 호출될까?

```Python
def user_view(request: WSGIRequest):
    users: QuerySet = User.objects.all()
    first_user: QuerySet = users[0]
    user_list: list[User] = list(users)
```

`users`라는 변수에 쿼리셋 객체를 저장한 뒤에 첫 번째 사용자를 조회하고 다음에 전체 사용자를 조회했기 때문에 쿼리가 한 번만 실행되었다고 생각할 수 있지만 실질적으로는 아래 쿼리문과 같이 쿼리가 각각 개별적으로 호출되어 두 번 실행된다.

```SQL
-- 첫 번째 사용자 조회
SELECT *
FROM User
LIMIT 1;

-- 전체 사용자 조회
SELECT *
FROM User;
```

이유는 아까와 같이 정말 꼭 필요할 때만 쿼리가 실행되기 때문에 첫 번째 사용자를 조회하는 `first_user` 변수 정의 부분에서 쿼리가 해당 로직에 맞춰 실행되고 다음에 전체 사용자 조회를 위한 쿼리가 추가적으로 실행된 것이다. 이러한 비효율성을 없애려면 아래와 같이 둘의 순서를 바꿔주면 된다.

```Python
def user_view(request: WSGIRequest):
    users: QuerySet = User.objects.all()
    user_list: list[User] = list(users)
    first_user: QuerySet = users[0]
```

그러면 쿼리셋은 더 큰 집합이 되는 쿼리의 결과를 캐싱한 뒤 해당 결과를 토대로 작은 집합의 쿼리를 실행하게 되기 때문에 실질적으로 쿼리가 전체 사용자를 조회하는 쿼리만 한 번 실행된다. 이를 쿼리셋에서는 결과 캐시(Result Cache)라 부른다.

그런데 문제는 여러 테이블을 한 번에 묶어 조회하려 할 때 발생한다.

### N+1 문제

`User` 테이블과 1:1 관계로 연결되어 있는 `UserInfo` 테이블을 함께 조회한다고 생각해보자. 그러면 아래와 같은 로직을 생각해볼 수 있다.

```Python
def user_view(request: WSGIRequest):
    users: QuerySet = Users.object.all()
    for user in users:
        user.userinfo

    user_list: list[User] = list(users)
```

앞서 쿼리셋은 꼭 필요할 때만 쿼리를 호출한다고 하였다. 따라서 `users` 변수 자체는 아직 쿼리를 호출하기 이전인 쿼리셋 객체이고 반복문을 수행하면서 결국 쿼리가 매번 한 번씩 더 수행되기 때문에 실질적으로 수행해야 하는 쿼리보다 데이터의 개수만큼 더 많은 쿼리를 호출하게 된다. 데이터의 개수를 N개라 할 때 실제 호출해야하는 쿼리보다 N번 더 많은 쿼리를 호출하기 때문에 이를 N+1 문제라 부른다. 이것이 ORM을 통해 지연 로딩을 사용할 때 발생하는 대표적인 문제 중 하나다.

이를 해결하기 위해서는 쿼리셋에서 제공하는 메서드들 중 `select_related` 및 `prefectch_related`를 사용하면 되는데 각각 `JOIN` 구를 수행하는 메서드와 추가적인 쿼리를 더 호출하여 일종의 서브쿼리로서 `WHERE` 구를 활용한 방법이라 생각하면 된다. 관련해서는 [참고](#) 부분에 남긴 링크를 통해 더 자세히 살펴보길 바란다.

### 기타 다른 프레임워크

지연 로딩과 N+1 문제는 ORM에 존재하는 공통적인 특징과 문제기 때문에 장고 뿐만 아니라 다른 프레임워크에서도 볼 수 있다. 예를 들어 자바의 스프링(Spring) 웹 프레임워크에서 JPA(Java Persistence API)를 사용할 때도 쿼리셋과 똑같이 지연로딩과 함께 N+1 문제를 잘 다뤄야 한다. 현재 나는 스프링과 JPA를 다뤄본 적이 없기 때문에 기회가 된다면 나중에 한 번 작성해보도록 하겠다. 관련된 좋은 유뷰트 영상을 찾아서 맨 아래 [참고](#참고) 부분에 링크를 첨부하겠으니 궁금한 사람은 더 확인해봐도 좋을 것 같다.

## 함수형 프로그래밍에서의 게으름과 부지런함

### 함수형 프로그래밍(Functional Programming)

함수형 프로그래밍은 객체 지향 프로그래밍처럼 하나의 패러다임이다. 쉽게 객체 지향 프로그래밍은 각 객체들 간의 협업에 초점을 맞춰 객체를 설계하는데 집중했다고 하면 함수형 프로그래밍은 구현에 초점을 맞춰 어떤 함수를 가져와 구현할 것인지를 고민하는 형태다. 함수라는 단어에서 알 수 있듯 프로그래밍을 일종의 함수로 취급하여 입력하는 값에 대한 결괏값을 고정시켜둔다고 생각해도 좋다. `y = 2x + 1`이라는 함수가 있으면 `y` 값은 `x`의 값이 `1`일 때 무조건 `3`이다. 동일한 입력값에 대해 항상 동일한 결괏값을 반환하는 것이다. 이런 함수식 사고 덕분에 객체 지향 프로그래밍에서는 입력값과 결괏값이 객체 내에 숨겨져 예상하지 못한 부작용이 발생할 수 있는 것에 반해 함수형 프로그래밍에서는 신뢰가 가능해진다. 그리고 함수형 프로그래밍에서 중요한 개념 중 하나가 **지연 평가(Lazy Evaluation)**다. (함수형 프로그래밍에 관해서는 아래 [참고](#참고) 부분에 첨부한 유튜브 영상을 확인하길 바란다. 글을 쓰는 나 또한 관련해서 정확하게 개념을 모르고 있다. 한 가지 확실하게 말할 수 있는 건 패러다임이라는 단어에서 알 수 있듯 사고를 바꿔 생각해야 하는 개념이라는 점과 객체 지향 프로그래밍과 함수형 프로그래밍은 대척점에 놓여 있는 것이 아닌 상호보완적으로 사용할 수 있다는 점이다. 본 글에서는 함수형 프로그래밍 입문을 위한 글이 아닌 지연 평가를 설명하기 위한 글로 지연 평가에 대한 개념이 함수형 프로그래밍에서 중요하다는 점만 확실하게 강조하고 싶다.)

### 지연 평가(Lazy Evaluation)

지연 평가란 말 그대로 평가를 지연시키는 방법으로 여기서 평가는 곧 쉽게 어떤 로직에 대한 연산이라 생각하면 된다. 예를 들어 아래와 같이 파이썬 언어로 작성된 1부터 10,000,000까지의 자연수의 제곱을 배열에 저장하는 반복문이 있다고 가정해보자.

```Python
eager_evaluation: list[int] = []
for number in range(1, 10000001):
    eager_evaluation.append(number * number)
```

이를 `map`과 `lambda` 함수를 사용해서 구현하면 아래와 같다.

```Python
lazy_evaluation: list[int] = list(
    map(lambda number: number * number, range(1, 10000001))
)
```

끝으로 리스트 컴프리헨션까지 사용한 방법에 대해 소요 시간을 출력하면 아래와 같다. 지연 평가가 기본적인 반복문보다 수행 시간이 빠른 것을 확인할 수 있다. (리스트 컴프리헨션이 훨씬 적게 걸린 이유는 함수 호출 방법에 대한 부분 때문인데 관련해서는 스택오버플로우의 [Why is a list comprehension so much faster than appending to a list?](https://stackoverflow.com/questions/30245397/why-is-a-list-comprehension-so-much-faster-than-appending-to-a-list) 글을 참고하길 바란다.)

```
Eager Evaluation:  1.7933549880981445
Lazy Evaluation:  1.4221057891845703
List Comprehension:  1.133929967880249
```

그렇다면 지연 평가가 어째서 시간이 더 적게 걸린 걸까? 앞서 개념에 대해 이야기하면서 연산을 지연시키는 방법이라 이야기했다. 일반적으로 반복문을 사용하는 경우 전체에 대한 계산을 수행하기 때문에 `print` 함수로 해당 전체에 대한 결괏값을 볼 수 있지만 지연 평가의 경우 반복문이 수행될 때 하나씩, 다시 말해 필요할 때마다 연산을 수행하기 때문에 `print` 함수를 실행해고 전체 결괏값이 아닌 메모리 주소를 반환한다. 그리고 이러한 차이 때문에 지연 평가가 훨씬 빠른 것이다.

지연 평가를 사용하는 대표적인 방법으로는 제너레이터(Generator)가 있으며 이는 피보나치 수열에서 메모리를 더 효율적으로 사용하고 싶을 때 이용할 수 있다.

### 피보나치 수열

#### 도입

피보나치 수열이란 연속된 두 항 사이의 비로 쉽게 첫 번째 수와 두 번째 수가 각각 1일 때 세 번째 수부터는 바로 전의 수와 두 번째 전의 수의 합으로 반복되는 수열을 의미한다. 따라서 그 수열을 간단하게 나열해보면 `1 1 2 3 5 8 ... `과 같다.

#### 다이나믹 프로그래밍(Dynamic Programming, DP)

반복문을 활용해 피보나치 수열을 구현하면 아래와 같다. 이러한 알고리즘은 한 번 계산이 완료된 부분을 재계산하는 비효율이 발생하지 않게 하기 때문에 다이나믹 프로그래밍(Dynamic Programming, DP)이라 한다.

```Python
f1, f2 = 1, 1
for _ in range(3, 100001):
    result: int = f1 + f2
    f1, f2 = f2, result

print(result)
```

#### 메모리 최적화 다이나믹 프로그래밍

반복문을 사용해 계산한 피보나치 수열을 제너레이터를 활용해서 구현하면 아래와 같다.

```Python
def lazy_loading_dp(number: int) -> int:
    f1, f2 = 1, 1
    while True:
        result: int = f1 + f2
        yield result
        f1, f2 = f2, result


for _ in range(3, 100001):
    result: int = next(fibonacci)

print(result)
```

각각의 메모리 사용을 비교하기 위해 `gc` 및 `psutil` 패키지를 활용해 계산해보면 아래와 같다.

```
After Dynamic Programming: 0.0078125
After Lazy Loading Dynamic Programming: 0.0
```

#### 기타 다른 풀이

보통 피보나치 수열을 배울 때는 재귀함수를 사용한 방법은 물론 시간 복잡도에 대한 이야기와 함께 분할 정복 또한 함께 배울 때가 많다. 관련해서는 해당 키워드를 통해 더 찾아보길 추천한다.

## 결론

Lazy 및 Eager를 각각 게으름과 부지런함이라 번역했다. 살다보면 게으른 건 배척해야 하는 태도로 여겨지고 부지런한 건 추구해야 할 덕목처럼 여겨질 때가 많다. 하지만 게으른 게 꼭 나쁜 것일까?

프로그래밍을 처음 배우는 사람들이 내게 학습 방법을 물을 때면 엔지니어를 게으른 사람이라 생각하고 어떻게 하면 그들이 게으름을 잘 유지할 수 있을지에 대해 의심하고 연구하는 과정에서 기술이 발전했다고 생각하면 큰 도움이 되는 것 같다고 답하곤 한다. 이를 테면 생활코딩 유튜브의 이고잉님께서 [WEB2 CSS - 3.CSS의 등장](https://youtu.be/L41Zjl7XANI?list=PLuHgQVnccGMAnWgUYiAW2cTzSBywFO75B) 강의에서 이야기하는 것처럼 게으름은 곧 폭발적인 힘을 만들어내는 것이다.

나는 참 게으른 사람이다. 그리고 더 게으르려고 부지런하게 산다. 요즘 여러 생각도 많고 감정도 흔들리며 스스로를 괴롭힌 날들이 길어졌는데 게으름의 미덕을 다시 한 번 되새겨보며 내 안의 폭발적인 힘을 이끌어 내야겠다. 늘 부지런함이 우선이었다가 게으름을 만들어낸 프로그래밍의 세계처럼 나의 게으름이 더 나은 미래를 만들 힘을 가질 것이라 믿으며 이 글을 마치려 한다.

## 참고

### 웹에서의 게으름과 부지런함

- [레이지 로딩 - Lazy Loading, 네이버 블로그, 딜룽](https://blog.naver.com/PostView.nhn?blogId=dilrong&logNo=221544559266)
- [HTML 속성으로 네이티브 이미지 지연 로딩(Lazy Loading) 하기, 티스토리, 어포스트](https://blogpack.tistory.com/m/858)

### ORM에서의 게으름과 부지런함

- [Django ORM (QuerySet)구조와 원리 그리고 최적화전략 - 김성렬 - PyCon Korea 2020, 유튜브 영상, PyCon Korea](https://www.youtube.com/watch?v=EZgLfDrUlrk)
- [JPA @ManyToOne 단방향 관계, "왜 생각보다 select 쿼리가 더 많이 생기지?", 유튜브 영상, 백기선](https://www.youtube.com/watch?v=4aMYNNBnWXo)
- [JPA @ManyToOne 단방향 관계 쿼리 문제 해설편, 유튜브 영상, 백기선](https://www.youtube.com/watch?v=MpXdx8-qWzo)

### 함수형 프로그래밍에서의 게으름과 부지런함

- [함수형 프로그래밍이 뭔가요?, 유튜브 영상, 얄팍한 코딩사전](https://www.youtube.com/watch?v=jVG5jvOzu9Y)
- [40.1 제너레이터와 yield 알아보기, 코딩도장](https://dojang.io/mod/page/view.php?id=2412)
- [python filter 로 게으르게 커피한잔 하고 가세요! 향이 좋아요!, 티스토리, hnanmal - 흔한말과 흔한생각](https://hnanmal.tistory.com/m/entry/python-filter-%EB%A1%9C-%EA%B2%8C%EC%9C%BC%EB%A5%B4%EA%B2%8C-%EC%BB%A4%ED%94%BC%ED%95%9C%EC%9E%94-%ED%95%98%EA%B3%A0-%EA%B0%80%EC%84%B8%EC%9A%94-%ED%96%A5%EC%9D%B4-%EC%A2%8B%EC%95%84%EC%9A%94)

### 결론

- [WEB2 CSS - 3. CSS의 등장, 유튜브 영상, 생활코딩](https://youtu.be/L41Zjl7XANI?list=PLuHgQVnccGMAnWgUYiAW2cTzSBywFO75B)
