﻿# Вы можете расположить сценарий своей игры в этом файле.
# курсор мыши
# define config.mouse = {"default" :[("":,0,0)}
# Определение персонажей игры.
define a = Character('Боря', color="#217166")
define b = Character('Некит', color="#0E92A2")
define n = Character(None, kind=nvl, what_color="#000000")
define c = Character('OSU', color="#D02EBC")
define d = Character('Максим Симонов', color="#D02EBC")

#music
define audio.alarm = "audio/Musics/Effects/alarm.ogg" #звук будильника
define audio.SMS = "audio/Musics/Effects/SMS.mp3" #SMS
define audio.floor_creak = "audio/Musics/Effects/floor_creak.mp3" #Скрип полов
define audio.tap_water = "audio/Musics/Effects/tap_water.mp3" #Звук воды из под крана
define audio.Keyboard = "audio/Musics/Effects/Keyboard.mp3" #Клавиатура
define audio.hitting_the_table = "audio/Musics/Effects/hitting_the_table.mp3" #Удар по столу
define audio.Childhood_Grave = "audio/Musics/Soundtrack/Childhood_Grave.mp3"
define audio.everlasting = "audio/Musics/Soundtrack/everlasting.mp3"
define audio.Gnossiene_III = "audio/Musics/Soundtrack/Gnossiene_III.mp3"
# Игра начинается здесь:
label start:
    stop music
    play sound SMS
    scene simple_room_awake
    a "...{w}эммм"
    window hide
    with fade
    scene simple room
    with fade
    stop sound fadeout 2
    a "А? Что такое?"
    a "Кто опять?"
    a "Нужно проверить телефон"
    play music Childhood_Grave fadein(5.0)
    $ renpy.music.set_volume(0.3)
    with fade
    show hand_with_phone1
    "- У вас 3 непрочитанных сообщения от Никиты -"
    a "А, это Некит"
    menu:
        "Прочитать сообщения":
            jump protchital
    return

label protchital:
    "Боря решает прочитать сообщения"
    b "Здорова чукча,{w} ты сделал зачёт по математике на завтра?"
    hide hand_with_phone
    with fade
    "-Боря выключил телефон и медленно потянул левую руку ко лбу, попутно раскидываясь на игровом кресле-"
    window hide
    scene simple_room_awake
    #with fade
    with dissolve
    n "{color=#35A496}Зачет... {w}Как это зачет?.. Еще вчера был май, или март. {w}Не так уж и сложно потерять счет времени, когда ты уже 5 месяцев сидишь на карантине. {w}Дистанционные занятия так выматывают, особенно когда ты сам ничего не делаешь.{/color} "
    nvl clear
    scene main_menu_blurred
    with fade
    play sound Keyboard
    n"{color=#35A496}Боря потянулся и зевнул. Уставился на монитор, горевший ярко-розовым светом на котором огромными буквами было написано OSU.
    Боря машинально начал клацать по клавиатуре. {w}В Последнее время со стрессом он справляется, играя в OSU.{/color}"
    nvl clear
    stop sound fadeout 2
    a"Так сыграю пока две-три катки, и начну работать"
    with fade
    a "Да что за!? Как!? Да как!?"
    play sound hitting_the_table
    "-Послышался глухой удар по столу. Боря резко встал и сгорбился у монитора.-"
    stop sound fadeout 1
    a "Как может так не везти!?"
    scene simple room
    "-Боря схватился за бутылку и, чтобы его не услышали спящие родители, со всей силы кинул газированный напиток на кровать.-"
    a "Так, нет.... {w} в OSU я что-то не хочу"
    show hand_with_phone_0251
    "Боря взял телефон. На часах было {color=#E32636}02:51{/color}."                  #Поменять фрейм с телефоном!
    a "Них** себе...{w}Как так время-то пролетело? "
    hide hand_with_phone_0251
    with fade
    a "Ненавижу эту вонючую OSU, сделаю пока перерыв на денёк."
    a "Наверное мне стоит найти кого-нибудь, кто скинет работу."
    a "Я уже привык идти путем наименьшего сопротивления."
    "Физиономия Бори с ехидной улыбки изменилась, когда он понял, что в 3 часа ночи, кроме некоторых ребят, все одногруппники уже спали"
    a"Да блин... {w} Некиту может написать?"
    a "Он вроде нормальный, разве что со мной в OSU уже давно не играет... {w} Или может Стёпе....{w}Или Дамиру."
    "Боря нажал на диалог со Степой и прочитал последнее сообщение 'Делай сам!'.{w}Тоже самое было и с Дамиром."
    a "От них мне помощи не дождаться.... {w} Как так!?"
    a "Я же всегда получал от них готовые ответы, правда последнее время я совсем стал этим злоупотреблять...
    В последний раз вживую я с ними общался еще зимой, точно помню."
    a"Кажется наши отношения поменялись когда вышло обновление в OSU, как же это отвратительно, я даже не могу вспомнить, что было месяц назад не говоря о том, что было всего неделю назад."
    a"Я каждый день играл в OSU от 9 до 13 часов..."

    "-Боря встал со стула, выпрямился и направился по коридору в сторону ванной."
    scene corridor
    play sound floor_creak
    with fade
    "Стараясь никого не разбудить, Борис, передвигался медленно, наступая на скрипучий паркет"
    "Открыв дверь в ванную, Боря включил свет и почти не узнал себя в зеркале."
    stop sound fadeout 2
    scene bathroom
    with fade
    "Ямы под глазами, грязные волосы, уставший вид, Боря не видел своего отражения уже 8 дней."
    a "Кажется, я похудел"
    "отчасти это было так, Боря за весь день только завтракал на ужин, или ужинал на завтрак"
    a "Щас бы бутик с ветчиной и сыром.{w} У нас же вроде осталась еще та колбаса..."
    "Глаза Бори на секунду опустились на руки и через мгновение, когда Боря помотал головой, поднялись обратно"
    a "Так, есть вообще-то дела поважнее!"
    a "Мне нужно как-то сдать зачет, а если точнее, определиться как именно мне его сделать."
    a "Вариантов вцелом немного, но мне стоит решить, каким путём я пойду."
    "Левая рука потянулась к крану и включила его."
    play sound tap_water
    "Полилась сначала холодная а затем теплая вода, Боря помыл руки и умылся."
    a "Пока обойдусь умыванием теплой водичкой, {w} хотя бы что-то, перед длительной скучной работой."
    stop sound fadeout 2
    "Боря выключил кран, вытер лицо об полотенце и вернулся к разглядыванию себя в отражении."
    a "И так! {w}Вариантов не шибко много как я уже сказал, а точнее всего два:{color=#E32636} сделать самому{/color}, {w}или{color=#E32636} списать{/color}, а точнее вежливо попросить типа я что-то там не понял "
    menu:
        "Сделать самому":
            jump Sdelal_Sam
        "Списать":
            jump Spisal
    nvl clear
    return

    label Sdelal_Sam:
    scene bathroom
    a "Если честно, я мог бы попытаться сделать все сам."
    scene corridor
    with fade
    play sound floor_creak
    "Борис повернулся к двери и медленно пошагал в свою комнату"
    a "Я могу решить первые примеры, я когда списывал вроде что-то понял. {w}Конечно я мало что понял, но зато, у меня все записано в тетради и я могу всегда посмотреть."
    a "Тем более это всего лишь математика"
    "'Я же гений':{w} Подумал Борис"
    a "что там может быть сложного?"
    stop sound fadeout 1
    scene simple_room_osu
    with fade
    "Зайдя в комнату Борис увидел на мониторе оставленную им OSU."
    "Боря почти физически почуствовал, что злощастная игра манит его к себе."
    c "Забудь о зачете, пора апнуть 400пп"
    "Но Борис был непреклонен."
    with dissolve
    scene main_menu_osu
    "Только он сел за стол, как вышел из OSU и нажал дважды на иконку chrome."
    "Одной рукой он заходил в мудл, а другой искал тетрадь по математике."
    "Удивительно для него самого, первые примеры прошли не так уж и тяжело. {w}Где-то за час-два Борис расправился с первой частью из пяти."
    a "Первый пошел! {w} Теперь второй!"
    "Настало утро, на кухне закопошились родители, а Борис все так же сидел за столом и писал зачетную работу."
    "Ему было абсолютно все равно на внешние раздражители, он уже доделывал третью часть с головой погрузившись в примеры и формулы."
    "Правда Борис конечно отвлекся на еду, когда уже совсем приспичело, и пока он ел, он думал только об одном:"
    a "А если в четвертом подставить переменную, а потом поделить на общий множитель, да не, бред"
    "Проблемы возникли только с последними примерами- они были слишком большими и сложными. {w} Но даже так, Борис смог справиться с ними, и наконец, вздохнуть с облегчением."
    a "Я это сделал! {w}Я правда сделал это!"
    show hand_with_phone1513
    "Борис потянулся к телефону, на часах было уже {color=#E32636}15:13{/color}"
    hide hand_with_phone1513
    "Срок сдачи в 22:00"
    "Боря потянулся и зевнул"
    a "Осталось ей скинуть и можно спать ложиться."
    "Глаза Бориса остановились на сообщениях Никиты, еще вчерашних сообщениях."
    b "Никита: 'привет чукча', {w}cделал зачет по математике?"
    "Борис зашел в личные сообщения с Никитой и написал ему"
    a "Привет. {w}Да, сделал"
    "Никита был в сети поэтому моментально ответил."
    b "Внатуре?"
    b "Скинь 5 пожалуйста и 4, и 3..."
    "Боря скинул пятый номер в общий чат группы и лег на кровать."
    "Он закрыл глаза и уснул, крепко."
    scene simple room
    play music everlasting
    with fade
    "Прошел год"
    "Борис изменился до неузнаваемости, его жизнь, лично для него, стала ярче прежней"
    "Наконец занялся спортом, что было его детской мечтой, и уже сейчас представляет из себя груду мышц"
    "Борис начал работать в канторе отца, ведь времени теперь достаточно"
    "Дистанционное обучение в техникуме продлили"
    "Иногда, после тренировки, или возвращаясь после работы Борис думает:"
    a "Неужели все мои положительные изменения в жизни связаны только с тем, что я перестал играть в OSU"
    a "Я точно не буду утверждать, что это не так, вся моя жизнь раньше крутилась вокруг этой игры"
    a "Возможно, это просто связано с тем, что в тот день, когда я сдал зачет, всю работу я выполнил самостоятельно"
    a "И вообще, в дальнейшем, именно самостоятельность помогала мне в решении проблем"
    a "Не хочу даже думать о том, как могла измениться моя жизнь, {w}а точнее, как она бы не изменилась,{w} если бы в день, когда мы сдавали зачет по математике"
    a "я предпочел бы привычку полагаться и надеяться на других, самостоятельному решению проблемы..."
    "Конец"
    scene black
    with fade
    "Спасибо за то, что играли в нашу игру!"
    return

    label Spisal:
    scene bathroom
    a "Что-то я вообще не хочу сегодня работать."
    a "Тем более когда я всегда могу попросить моих дорогих друзей о небольшом одолжении."
    scene corridor
    with fade
    play sound floor_creak
    "Борис повернулся к двери и медленно пошагал в свою комнату"
    a "Хотя я их и так наверно достал уже со своими просьбами"
    a "Ну да ладно, если я спрошу сразу всех то кто-то мне точно скинет"
    stop sound fadeout 1
    scene simple_room_osu
    with fade
    "Боря зашел в комнату, сел за стол и застыл"

    scene main_menu
    "Глаза его просто замерли на мониторе, на открытой во весь экран OSU"
    "Боря поматал головой и свернул игру."
    scene main_menu_osu
    with fade
    a "Так, OSU, любимая, сейчас не до тебя."
    "Боря зашел в ВК и начал писать тем не многим одногруппникам, которые были в сети."
    a "Привет"
    a "можешь скинуть по математике зачет пожалуйста"
    "Боря откинулся на кресле, и начал ждать когда ему ответят"
    scene main_menu_blurred
    "уже прошло десять минут, Боре стало откровенно скучно"
    "Никто не ответил и даже более того не прочитал его сообщения"
    "От бузвыходности Боря начал писать всем одногрупникам которых знал"
    "После чего навелся на иконку OSU на панели задач"
    scene main_menu
    with fade
    a "Пока сыграю несколько каток. {w}Не помешает"
    scene main_menu_blurred
    with fade
    n "{color=#35A496}Прошло около часа и никто так и не написал Боре. {w}Боря все это время играл в OSU... {w}Лениво, безымоционально{/color}"
    nvl clear
    n "{color=#35A496}В голове у него были мысли о том, что все его друзья, то-есть недруги, предали его. {w} Пока наконец Боря не услышал звук оповещения, кто-то наконец-то ему написал{/color}"
    play sound SMS
    "Почти соскочив со стула, Боря, свернул OSU и зашел в ВК"
    stop sound fadeout 1
    scene main_menu_osu
    "Но... К его разочарованию, писал какой-то Максим Симонов"
    d "Привет"
    "Аккаунт Максима был пустой, его только что создали"
    "Боре на мгновение стало очень грустно, он сполз, почти пустил слезу как вдруг понял"
    a "Кто вообще может писать мне, как закрытому профилю, в пять часов ночи 'Привет'?"
    a "Может мне стоит добавить его в друзья и ответить?"
    menu:
        "Ответить":
            jump Otvetit
        "Продолжить играть в OSU":
            jump Play_in_OSU
    nvl clear
    return

    label Otvetit:
    a "Очень интересно"
    a"Это точно не бот, но кто это может быть?"
    a "Ладно, просто отвечу ему и будь что будет"
    d "Привет"
    d "Я слышал, ты хочешь сдать зачет? {w}Могу тебе скинуть, за определенную плату конечно"
    a "Ахах что? Ты кто?"
    d "Это не важно"
    d "Всего за 3 тыс. я скину тебе зачет"
    a "Выходит кто-то решил за деньги сдать за меня зачет, {w}при этом, этот некто, хочет сохранить анонимность"
    a "Возможно я могу узнать кто это, по его сообщениям"
    a"Для этого мне нужно..."
    play sound SMS
    d "Решай быстрее, у тебя всего 5 минут"
    stop sound fadeout 1
    a "Как ты можешь мне гарантировать что если я дам тебе 3 тысячи ты отправишь мне работу?"
    d "Никак, но я скажу тебе так"
    d "Никто, ни завтра, ни сегодня, ничего тебе не скинет"
    d "Это твоя последняя возможность получить зачет"
    a "Неужели это правда?"
    a "И ведь в действительности, никто за последний час мне не ответил"
    a "Хотя все, кому я писал сейчас в сети!"
    play sound SMS
    d "У тебя минута"
    stop sound fadeout 1
    a "Ладно, ладно, скидывай номер телефона"
    "Боре не было жалко денег, он был готов отдать даже больше"
    "И все же, ощущение того, что его обманывают, {w}не проходило"
    "Номер, на который нужно было перевести деньги, был незнакомым"
    "И все же, когда Боря перевел деньги, чуть ли не моментально пришло сообщение"
    play sound SMS
    "Аноним скинул зачет, сделанный в ворд файле"
    stop sound fadeout 1
    d "Спасибо, надеюсь на дальнейшее сотрудничество"
    with fade
    "Спустя 40 минут, Боря переписал работу, и отправил учительнице по математике"
    a "Фууух.{w} Сделал дело - гуляй смело, теперь можно и в OSU преспокойно поиграть"
    a "Денег конечно жалко, хоть и не очень сильно, но самому делать наверное было бы той еще морокой"
    "Боря отодвинул тетрадь в угол стола и запустил OSU"
    "Со спокойной душой он играл еще несколько часов, а затем лег спать"
    scene simple_room_morning
    play music Gnossiene_III
    with fade
    "Жизнь Бори не изменилась, все осталось таким же, как и год назад"
    "Дистанционное обучение в техникуме продлили"
    "Боря все так же поигрывает в OSU по 6 - 8 часов в день"
    "Максим скидывает ему готовые работы, хотя сам Боря не в восторге от такого расклада событий"
    "Поэтому иногда он что-то пытается сделать сам, что-то просит у других одногрупников, которые редко отвечают ему"
    "Время летит, когда неделями и даже месяцами только и делаешь, что играешь в OSU"
    "иногда Боря думает:"
    a "Вчерашний день похож на сегодняшний"
    a "Последнее яркое воспоминание - событие произошедшее пол года назад"
    a "Возможно мне стоило бы изменить свою жизнь к лучшему, возможно я могу изменить свою жизнь и сейчас..."
    "Конец"
    scene black
    with fade
    "Спасибо за то, что играли в нашу игру!"
    return

    label Play_in_OSU:
    a "А какой смысл? {w}Это наверняка какой-нибудь бот"
    a "Я никому кроме ботов не нужен, никому!"
    "Боря закрыл вкладку с ВК, открыл окно с OSU и начал играть"
    "Со временем грусть и злость сменились на ничего"
    "Боря просто играл, даже если бы ему выключили монитор он бы продолжил нажимать на клавиатуру и елозить мышкой по коврику"
    with fade
    "Так прошло несколько часов, {w}наступил день, {w}родители уже ушли на работу,{w} никто так и не написал"
    "Истощенный и уставший Боря все так же сидел и играл в OSU"
    "Наконец он решил посмотреть сколько время, на часах было уже {color=#E32636}17:36{/color}"
    scene main_menu_blurred
    with fade
    "Глаза у Бори начали слипаться, и вот он уже совсем заснул"
    "..."
    scene simple_room_osu_night
    play music Gnossiene_III
    with fade
    "Прошел год"
    "Зачет по математике за первый семестр Боря не сдал, {w}и теперь обязан сдать его снова уже в этом году"
    "В технекуме он был всего один день, конечно это связано с тем, что дистанционное обучение продлили"
    "И все же, именно в этот день,{w} ровно 6 месяцев назад, Боря в последний раз выходил на улицу"
    "Думаю не стоит говорить о том, что Борю начали считать психом все его одногруппники"
    "Единстенное чем он занимается - это играет в OSU, безвылазно, в день от 8 до 12 часов"
    "Боря поставил крупные рекорды в OSU, даже стал крайне популярным в узких кругах"
    "Иногда Боря просто останавливал игру и думал, думал о том, как он вообще сумел докатиться до подобной жизни"
    a "Что я сделал не так? И мог ли я сделать что-нибудь, чтобы сейчас жить иначе?"
    a "Если я и мог что-то сделать, то единственная возможность была год назад, когда мы сдавали зачет"
    a "Если бы я мог вернуться во времени, я бы точно поступил иначе...Принял бы всю инициативу на себя и сам бы сдал зачет"
    a "Но сейчас что-либо менять уже слишком поздно..."
    scene black
    with fade
    "Спасибо за то, что играли в нашу игру!"
