# flask_app
# Учебный проект по настройке git 
В данном репозитарии очень простое приложение.
Цель проекта сделать настройку GitHub Actions.
Послсле git push этот проект проходит юниттесты, создается образ Docker,
готовый образ pushится на DockerHub, из DockerHuba создается рабочее приложение
на ВМ в  яндекс облаке, и в случае успеха приходит оповощение в телеграме об успешном 
запуске.

# Обратить внимание
на файл mail.yaml и на насторойки Secrets

# не забыть
прописать ssh public key ВМ в authorized_keys

# и еще не забыть
установить Докер на ВМ
