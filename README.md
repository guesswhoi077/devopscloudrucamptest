# Результаты выполнения тестового задания от DevOps Cloud.ru Camp


# Инструкция по применению:

**Задание 1:**

Перед исполнением плэйбука укажите в yml файле:
1) Имя хоста/группу хостов заменив **\<hostname\>**
2) Путь к публичному ключу под таском "upload user pub key" заменив **\<pub key location\>**
   
Плейбук запускается следующей командой:

&emsp;**ansible-playbook ansibleplaybook.yml -K**

Заметка:
Задачи выполняются с привелигироваными правами, поэтому после запуска нужно будет ввести пароль от соответствующей учетки(sudo).
Так же, пароль от учетки cloudru был хеширован с sha512 алгоритмом для предотвращения его перехвата.

**Задание 2:**

**Docker**

&emsp;Для построения образа запускается следующая команда, предварительно примонтировавшись к папке, где лежат dockerfail и webapp папка с веб приложением:

&emsp;**docker build -t webapp ./**

После завершения постройки можно создать контейнер с указанием порта:

&emsp;**docker run -d -p 8000:8000 --name webapp webapp**

**Kubernetes**

Для локального запуска кластера было использованы инструменты Docker Desktop и kind. В качестве образа в деплойманте использовалось ранее созданное веб приложение. Для проверки работоспособности проб используется TCP сокет на 8000 порту, а проверка доступности пробы в сети происходит путем отправки запроса HTTP GET.

После создания кластера, применяются манифесты.


&emsp;**kubectl apply -f .\webapp-namespace.yaml**

&emsp;**kubectl apply -f .\deployment-webapp.yaml**

&emsp;**kubectl apply -f .\webapp-сlusterIp-service.yaml**



Для проверки веб проиложения задается перенаправление портов:

&emsp;**kubectl port-forward deployment/webapp 8000:8000 -n webapp-namespace**


**http://localhost:8000/hostname**

