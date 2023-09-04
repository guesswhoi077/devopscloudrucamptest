# Результаты выполнения тестового задания для поступления в DevOps Cloud.ru Camp

**Хазиев Айнур Вазихович**  
Контакты:  
&emsp;email: ha31ev@yandex.ru  
&emsp;whatsapp: +79372914666  
&emsp;telegram: @onlyhazart  



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

&emsp;
**Kubernetes**

Для локального запуска кластера было использовано инструменты Docker Desktop и kind.
