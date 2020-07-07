# docker 설치 및 사용하기 

# docker install
# window pro 일때는 docker for windows
# window pro 외 docker toolbox
# 실행후 docker run hello-world를 이용하여 설치 확인

# docker pull continuumio/miniconda3 이미지 다운
# docker run -i -t continuumio/miniconda3 /bin/bash

# python3 -c "print(3*5)" 컨테이너에 담아 실행

# 빠져 나올때 exit

# 컨테이너 상태를 설정하기 위해서 (pip3 or pip)
# pip install beautifulsoup4
# pip install requests

# - 해쉬를 확인하기 
# docker ps -a 
# - 저장하기 
# docker commit c7b81850d08f mlearn:init [저장해쉬][저장이름]:[태그]
# - 실행하기 
# docker run -i -t mlearn:init 
# - 마운트 (끼워넣기)
# docker run -i -t -v /c/users/user/sample:/sample mlearn:init

# 해당 git 에서 실행할 때 
# docker run -i -t -v /c/users/user/git/study-python/Deep-Learning/chapter02:/chapter02 mlearn:init
# cd chapter ~~ 
# python ex ~~