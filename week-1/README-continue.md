# 1.5주차: Gemini CLI와 함께하는 쿠버네티스 심화

## 🎯 목표

  - Deployment의 확장(Scale-out/in), 업데이트(Rolling Update), 롤백(Rollback) 관리
  - ConfigMap을 이용한 애플리케이션 설정 분리 및 적용
  - Pod 로그 확인 및 리소스 상세 분석을 통한 기본 디버깅 방법 학습

## 사전 준비 (Prerequisites)

  - 이전 실습을 통해 `my-nginx` Deployment와 Service가 생성되어 있는 상태를 가정합니다. 없다면 아래 명령어로 다시 생성합니다.
  - `kubectl create deployment my-nginx --image=nginx`
  - `kubectl expose deployment my-nginx --type=NodePort --port=80`

-----

## 🚀 심화 실습

### 1\. 애플리케이션 확장 및 업데이트 (Scaling & Updating)

#### Deployment 확장 (Scale-Out)

Pod의 개수를 늘려 트래픽 증가에 대응합니다.

```bash
# 'my-nginx' Deployment의 Pod 개수를 3개로 확장하는 명령어 요청
gemini -y
kubectl 명령어로 my-nginx Deployment의 replica 수를 3개로 늘려줘.
# 예상 결과: kubectl scale deployment my-nginx --replicas=3
```

확장된 Pod들을 확인합니다. `AGE`가 다른 Pod들이 새로 생긴 것들입니다.

```bash
kubectl get pods
```

#### 롤링 업데이트 (Rolling Update)

무중단으로 애플리케이션을 새 버전으로 업데이트합니다.

```bash
# 'my-nginx' Deployment의 컨테이너 이미지를 새 버전으로 업데이트하는 명령어 요청
gemini -y
kubectl 명령어로 my-nginx Deployment의 nginx 이미지 버전을 1.25.3으로 변경해줘.
# 예상 결과: kubectl set image deployment/my-nginx nginx=nginx:1.25.3
```

업데이트 진행 상황과 완료 후 Pod들의 이미지 버전을 확인합니다.

```bash
# 업데이트 상태 실시간 확인
kubectl rollout status deployment/my-nginx

# Pod 상세 정보에서 이미지 버전 확인
kubectl describe pods | grep "Image:"
```

#### 업데이트 롤백 (Rollback)

업데이트에 문제가 발생했을 때 이전 버전으로 되돌립니다.

```bash
# 'my-nginx' Deployment 업데이트를 이전 버전으로 되돌리는 명령어 요청
gemini -y
kubectl 명령어로 my-nginx Deployment의 업데이트를 취소하고 이전 버전으로 되돌려줘.
# 예상 결과: kubectl rollout undo deployment/my-nginx
```

롤백 후 Pod들이 다시 이전 버전 이미지로 실행되는지 확인합니다.

```bash
kubectl rollout status deployment/my-nginx
kubectl describe pods | grep "Image:"
```

### 2\. 설정 관리 (Configuration Management)

#### ConfigMap 생성

애플리케이션 설정을 코드와 분리하여 관리합니다. 여기서는 Nginx의 기본 페이지 내용을 변경하는 ConfigMap을 만듭니다.

먼저, `index.html` 파일을 생성합니다.

```bash
echo "<h1>Welcome to Kubernetes with Gemini CLI!</h1>" > index.html
```

이제 Gemini CLI를 사용해 파일로부터 ConfigMap을 생성합니다.

```bash
# 'index.html' 파일로부터 ConfigMap을 생성하는 명령어 요청
gemini -y
kubectl 명령어로 'nginx-index'라는 이름의 ConfigMap을 index.html 파일로부터 생성해줘.
# 예상 결과: kubectl create configmap nginx-index --from-file=index.html
```

생성된 ConfigMap을 확인합니다.

```bash
kubectl get configmap nginx-index -o yaml
```

#### ConfigMap을 Pod에 적용

*이 단계는 `kubectl` 단일 명령어로 복잡하므로, YAML의 필요성을 이해하는 과정으로 활용합니다.*

Gemini CLI에게 YAML 파일을 생성하도록 요청할 수 있습니다.

```bash
gemini
'my-custom-nginx'라는 Deployment를 만드는 YAML을 작성해줘. nginx 이미지를 사용하고, 'nginx-index' ConfigMap을 '/usr/share/nginx/html' 경로에 볼륨으로 마운트해야 해.
```

Gemini가 생성한 YAML을 `custom-nginx-deployment.yaml` 파일로 저장한 후 아래 명령어로 배포합니다.

```bash
kubectl apply -f custom-nginx-deployment.yaml
```

이처럼 복잡한 리소스 정의에는 선언적인 YAML 방식이 유용하다는 점을 학습합니다.


#### (열어보기)
```bash
kubectl expose deployment my-custom-nginx --type=NodePort --port=80
minikube service my-custom-nginx
```

### 3\. 관찰 및 디버깅 (Observability & Debugging)

#### Pod 로그 확인

애플리케이션의 표준 출력/에러 로그를 확인하여 동작을 파악합니다.

```bash
# 특정 Pod의 로그를 확인하는 명령어 요청 (먼저 Pod 이름을 확인)
kubectl get pods

# 아래 명령어의 'my-nginx-xxxx-yyyy'는 위에서 확인한 실제 Pod 이름으로 변경
gemini -y
kubectl 명령어로 my-nginx-xxxx-yyyy 파드의 로그를 보여줘.
# 예상 결과: kubectl logs my-nginx-xxxx-yyyy
```

#### 리소스 상세 정보 확인

`describe` 명령어로 리소스의 상세 상태, 설정, 최근 이벤트를 확인하여 문제 해결의 단서를 찾습니다.

```bash
# 'my-nginx' Deployment의 상세 정보를 확인하는 명령어 요청
gemini -y
kubectl 명령어로 my-nginx Deployment의 상세 정보를 보여줘.
# 예상 결과: kubectl describe deployment my-nginx
```

출력 하단의 `Events` 섹션은 리소스 생성, 스케줄링, 오류 등 주요 이력을 보여주어 디버깅에 매우 유용합니다.

### 리소스 정리

모든 심화 실습이 끝났으므로 생성했던 리소스를 모두 삭제합니다.

```bash
kubectl delete deployment my-nginx
kubectl delete service my-nginx
kubectl delete configmap nginx-index
# kubectl delete -f custom-nginx-deployment.yaml # YAML로 생성했다면 삭제
# rm index.html custom-nginx-deployment.yaml
```