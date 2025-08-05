# ✅ 실습 환경 준비 (Setup Checklist)

본격적인 실습에 앞서 아래 체크리스트를 따라 필요한 모든 도구를 설치하고 설정합니다.

### 1. Windows 환경 설정 (WSL2 활성화)
PowerShell (관리자 권한)으로 다음을 실행 후 재부팅합니다.
```powershell
wsl --install
```
### 2. Docker 환경 설정
WSL 터미널(Ubuntu 등)을 열고 아래 명령어로 Docker 데몬을 시작합니다.
```bash
sudo /etc/init.d/docker start
```
`docker ps` 가 잘 실행되면 성공입니다.

### 3. Gemini CLI 환경 설정
WSL 터미널(Ubuntu 등)을 열고 아래 명령어로 Node.js v20 이상을 설치합니다.
```bash
# nvm 설치
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
# nvm 설치 후:
nvm install 20
nvm use 20
```
다른 방법으로 Node.js 도커 이미지를 사용하여 설치할 수가 있지만, 웬만한 패키지를 다 apk add로 처음부터 들여와야 하기 때문에 추천하진 않습니다.

다음으로 Gemini CLI를 설치합니다.
```bash
npm install -g @google/gemini-cli
```

Google Cloud 프로젝트 및 API 키 발급 후 GEMINI_API_KEY 환경변수를 설정합니다.

1.  [Google Cloud Console](https://console.cloud.google.com/projectcreate)에서 새 프로젝트를 생성합니다.
2.  [Google AI Studio](https://aistudio.google.com/apikey)에서 '새 API 키 만들기'를 클릭하여 키를 발급받고 복사합니다.
3. 환경변수를 설정합니다. 아래처럼 프로젝트 폴더에 .envrc 파일을 생성하고 환경변수를 설정할 수 있습니다.
```bash
sudo apt-get install direnv

echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
source ~/.zshrc

# 프로젝트 폴더에서 .envrc 파일 생성
echo 'export GEMINI_API_KEY="복사한_API_키"' > .envrc

direnv allow

# (이미 완료) .gitignore에 .envrc 추가
echo ".envrc" >> .gitignore
```

### 4. Kubernetes 도구 설치 (WSL 터미널)
  - **[kubectl](https://kubernetes.io/ko/docs/tasks/tools/install-kubectl-linux/)**: 쿠버네티스 클러스터와 통신하기 위한 도구
```bash
# Node.js 이미지를 사용할 경우 먼저 apk add curl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
# Node.js 이미지를 사용할 경우 먼저 apk add sudo
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```
  - **[Minikube](https://minikube.sigs.k8s.io/docs/start/)**: 로컬 쿠버네티스 클러스터를 생성하는 도구
```bash
# 자기 환경에 맞게 - https://github.com/kubernetes/minikube/releases/tag/v1.36.0 서 확인
curl -LO https://github.com/kubernetes/minikube/releases/download/v1.36.0/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
```
### 5. 최종 확인
```bash
docker --version
kubectl version --client
minikube version
node -v
gemini --version
```