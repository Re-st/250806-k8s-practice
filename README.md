# 250806-k8s-practice

## 미리 읽어보기
실습에서 다룰 node, pod 등의 개념이 헷갈릴 때에는, 아래 글을 참고하세요.

**참고할 만한 글**: [Red Hat, 쿠버네티스(Kubernetes, k8s)란? ](https://www.redhat.com/ko/topics/containers/what-is-kubernetes)

> 각 노드는 자체 Linux® 환경이며 물리 또는 가상 머신일 수 있습니다.

> 쿠버네티스 노드는 포드로 구성되며, 각 포드는 애플리케이션의 단일 인스턴스를 나타냅니다. 포드는 컨테이너 실행 방식을 제어하는 옵션과 함께 하나의 컨테이너 또는 긴밀히 결합된 일련의 컨테이너들로 구성되어 있습니다.

> 여러 쿠버네티스 서비스가 함께 작동하여 자동으로 각 태스크에 가장 적합한 노드를 식별하고, 리소스를 할당하며, 필요한 작업을 수행하기 위해 해당 노드에 포드를 할당합니다.

또한, [2주차](week-2/README.md)에서 다룬 컨트롤 플레인의 요소에 대해서는 아래 글을 참고하세요.
kube-apiserver, kube-scheduler, kube-controller-manager, etcd에 대해 설명합니다.

**참고할 만한 글**: [Red Hat, 쿠버네티스 아키텍처 소개](https://www.redhat.com/ko/topics/containers/kubernetes-architecture)

## 실습하기
실습 전, [셋업](week-1/SETUP.md)은 약 30분까지 소요될 수 있습니다.

실습 [week-1](week-1/README.md)과 [week-1.5](week-1/README-continue.md)는 약 10분, [week-2](week-2/README.md)는 약 20분 정도 소요될 것으로 예상합니다.

## 연락사항

질문이나 피드백은 아래 이메일로 보내주세요.

- 이메일: [geon.park@prosys.kaist.ac.kr](mailto:geon.park@prosys.kaist.ac.kr)
- 제목: [K8s Practice] 질문 또는 피드백

또는 [깃허브 이슈](https://github.com/Re-st/250806-k8s-practice/issues/new)로 남겨주세요.