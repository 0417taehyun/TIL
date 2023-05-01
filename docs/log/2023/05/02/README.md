---
title: <Google Cloud Skills Boost> Kubernetes in Google Cloud - 1
subtitle: <Google Cloud Skills Boost> Kubernetes in Google Cloud 퀘스트(Quest) 학습 내용 정리
description: Google Cloud Skills Boost의 Kubernetis in Google Cloud 퀘스트(Quest) Introduction to Docker, Kubernetes Engine, Orchestrating the Cloud with Kubernetes 학습 내용 정리
date: 2023-05-02
comments: true
---

# [Google Cloud Skills Boost] Kubernetes in Google Cloud - 1

## Introduction to Docker

### 전박적인 내용

도커가 무엇인지에 대해 간략하게 설명하며 직접 `Dockerfile`을 만들고 터미널에서 명령어를 활용해 이미지를 만들어 배포 및 컨테이너를 실행해보는 실습을 진행했다.

### 컨테이너(Container)

하이퍼바이저(Hypervisor)와의 가상화(Virtualization) 차이점에 대해 이해하면 좋은데, 쉽게 운영체제에서 커널 영역까지 함께 격리가 되는 것인지 여부로 비교된다고 생각하면 편하다. 하이퍼바이저를 활용한 가상 기계(Virtual Machine, VM)의 경우 커널까지 가상화하여 사용하기 때문에 호스트 운영체제와는 완전히 분리된 다른 운영체제를 게스트 운영체제로 사용할 수 있고, 베어메탈(Bar Metal)과 같은 수준의 하이퍼바이저 가상화의 경우 Type-1이라 부르며 하드웨어와 운영체제의 의존성을 분리해주는 인터페이스 역할 또한 담당하게 된다. 이러한 역할을 담당하는 계층을 보통 하드웨어 추상화 계층(Hardware Abstraction Layer)이라고도 한다.

컨테이너의 경우 호스트 운영체제와 커널은 공유한 채로 네임스페이를 독립적으로 가져가는 형태이기 때문에 결국 호스트 운영체제에 의존적인 형태일 수밖에 없다. 일례로 도커에서 컨테이너를 통해 실행하는 프로세스는 결국 호스트 운영체제를 통해 통제할 수 있으며, 반대로 특정 컨테이너에서 발견된 보안 취약점 때문에 호스트 운영체제의 커널까지 위협 받을 수 있다. 하이퍼바이저와 비교했을 때는 상대적으로 완전한 격리가 되지는 않는다. 그럼에도 매번 커널 단위까지 격리하여 배포하고 적용하는 것보다 훨씬 경량화되기 때문에 빠르게 발전하는 소프트웨어 추세에 알맞다고 할 수 있다.

### 이미지 아이디(Image ID)

이미지 아이디를 만드는 데 SHA-256 알고리즘을 활용해서 고유한 아이디를 만든다. 해시 충돌이 발생할 확률이 거의 낮지만 혹시 모를 경우를 예방하기 위해 태그(Tag)와 함께 레포지토리(Repository) 이름을 함께 활용한다. 예를 들어서, 이미지 아이디가 `1eba91607...`이며 레포지토리가 `python:3.10-alpine`인 경우 추가로 `3.10.11-alpine3.17` 같은 태그를 가진다. 이때 이미지 아이디가 동일 하더라도, 추가적인 레포지토리 및 태그 정보 등을 활용해 이미지를 구분할 수 있게 된다.

도커는 컨테이너를 빌드하여 애플리케이션을 실행할 때 우선적으로 로컬에서 이미지를 먼저 찾은 뒤, 로컬 환경에 이미지가 존재하지 않을 경우 공개 레지스트리에서 이미지를 찾는다.

### 레지스트리(Registry)

레포지토리(Repository)랑 혼용되어 사용되는 경우가 많은 것 같은데, 레포지토리의 경우 연관된 이미지들의 집합으로 동일한 애플리케이션에 대해 여러 버전이 존재하는 상황을 생각하면 된다. 레지스트리(Reigtry)의 경우 마치 깃허브(GitHub)처럼 이미지를 관리하는 호스팅 서비스를 지칭하는 단어로 대표적으로는 도커 허브(Docker Hub), AWS에서 운영하는 ECR(Elastic Container Registry), 그리고 GCP에서 운영하는 컨테이너 레지스트리(Container Registry)가 있다. 추가로 GCP의 경우 완전 관리형 서비스를 제공하기 위해 아티팩트 레지스트리(Artifact Registry)를 만들었으며, 이를 통해 펍/섭(Pub/Sub) 알림 등의 여러 기능을 지원하고 있다. GCP에서 제공하는 컨테이너 레지스트리를 이야기할 때는 이제 아티팩트 레지스트리라고 생각하면 될 것 같다.

## Kubernetes Engine: Qwik Start

### 쿠버네티스

### 클러스터(Cluster)


## Orchestrating the Cloud with Kubernetes

### 파드(Pods)

파드는 하나의 이상의 컨테이너 집합이라 생각하면 편하다. 만약 여러 컨테이너가 서로 강한 의존성을 가지고 있을 경우 두 컨테이너를 하나의 파드로 생성해 관리하는 게 효율적이다.

파드는 볼륨(Volumnes)을 갖는다. 볼륨은 파드와 동일한 생명 주기를 가지는 데이터 디스크를 의미하며, 파드 내의 컨테이너가 접근해서 사용할 수 있다. 하나의 파드로 구성된 여러 컨테이너는 볼륨 뿐만 아니라 네임스페이스(Namespace)를 공유하기 때문에 동일한 파드 내의 여러 컨테이너끼리 쉽게 통신할 수 있다. 공유하는 네임스페이스 중에는 네트워크 네임스페이스 또한 포함되며, 이는 곧 파드 하나에 하나의 아이피 주소(IP Address)가 할당된다는 걸 의미한다.

예를 들어 아래와 같이 YAML 파일 템플릿을 활용해 파드를 정의할 수 있다. 

```YAML
kind: Pod
apiVersion: v1
metadata:
    name: monolith
    labels:
        app: monolith
spec:
    containers:
        - name: monolith
          image: kelseyhightower/monolith:1.0.0
          args:
            - "-http=0.0.0.0:80"
            - "-health=0.0.0.0:81"
            - "-secret=secret"
        ports:
            - name: http
              containerPort: 80
            - name: health
              containerPort: 81
        resource:
            limits:
                cpu: 0.2
                memory: "10Mi"
```

### 서비스(Service)

파드의 경우 오류로 인해 멈췄을 때 이전에 할당 받았던 아이피 주소를 잃어버린다. 파드끼리 원활한 통신을 하기 위해서는 파드가 재시작되더라도 이전과 동일한 고정 아이피 주소를 할당 받고 있어야 한다. 이를 위해 존재하는 게 서비스다. 서비스는 파드에 대해 내부(Internal) 또는 외부(External) 통신을 위한 고정 아이피 주소를 할당해준다.

서비스는 라벨(Label)을 활용해 파드를 

서비스 유형에 따라 파드에 부여할 수 있는 세 가지 종류의 네트워크 유형이 있다.

1. `ClusterIP`: 
2. `NodePort`:
3. `LoadBalancer`:

```YAML
kind: Service
apiVersion: v1
metadata:
    name: "monolith"
spec:
    selector:
        app: "monolith"
        secure: "enabled"
    ports:
    - protocol: "TCP"
      ports: 443
      targetPort: 443
      nodePort: 31000
    type: NodePort
```

### 네트워크

## Managing Deployments Using Kubernetes Engine

### 배포의 종류

#### 롤링 배포(Rolling Deployments)

#### 블루/그린 배포(Blue/Green Deployments)

#### 카나리 배포(Canary Deployments)

## Continuous Delivery with Jenkins in Kubernetes Engine

## 추가 학습

### Hello Node Kubernetes

### Setting up a Private Kubernetes Cluster
