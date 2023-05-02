---
title: 네트워크 가상화 기술과 도커 엔진
subtitle: 네트워크 가상화 기술과 도커 엔진에서 사용되는 기술
description: VLAN, 오버레이 네트워크, VPN, SDN, OpenFlow, NFV, SD-WAN 등의 네트워크 가상화 기술과 함께 도커 엔진에서 사용하는 네트워크 가상화 기술에 대해 공식 문서를 통해 정리
date: 2023-05-03
comments: true
---

# 네트워크 가상화 기술과 도커 엔진

## 네트워크 가상화 기술

### VLAN

### 오버레이 네트워크(Overlay Network)

#### 터널(Tunnel)

#### 터널링(Tunneling)

터널링이란 네트워크 통신에 사용되는 데이터 단위인 패킷(Packet)을 다른 패킷으로 덧씌워서 전송하는 것을 의미한다. 대표적으로 VPN(Virtual Private Network)의 암호화나 IPv6의 패킷을 IPv4 네트워크에 통과시키는 경우 등에 사용된다. 오버레이 네트워크에서는 물리적 네트워크 구성에 영향을 받지 않고 원하는 가상 네트워크에 데이터를 전달하는 데 터널링을 사용한다.

#### 스플릿 터널링(Split Tunneling)

#### 퓰 터널링(Full Tunneling)

### VPN(Virtual Private Network)

#### IPSec



### SDN(Software Defined Networking)

#### OpenFlow

### NFV(Network Functions Virtualization)

#### VNF(Virtual Network Function)

#### NFVI(NFV Infrastructure)

#### NFV MANO(NFV Management and Orchestration)

### SD-WAN(Software Defined Wide Area Network)

#### CPE(Customer Premises Equipment)

CPE(Customer Premises Equipment)는 

#### ZTP(Zero Touch Provisioning)

ZTP(Zero Touch Provisioning)


## 클라우드 서비스에서의 네트워크 가상화

### AWS VPC(Virtual Private Cloud)

AWS VPC(Virtual Private Cloud)는 여러 가지 네트워크 가상화 기술을 사용해 구축되지만, 기본적으로 SND(Software Defined Networking) 기반의 가상 네트워크를 사용해 논리적으로 격리된 네트워크 환경을 제공한다.

## 도커 엔진에서의 네트워크 가상화

### 컨테이너

컨테이너에는 브릿지(Bridge), 오버레이 네트워크(Overlay