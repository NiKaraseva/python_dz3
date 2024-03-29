# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.
# (Может помочь метод translate из модуля string)

LIMIT = 10

text = """Она несла в руках отвратительные, тревожные желтые цветы. 
Черт их знает, как их зовут, но они первые почему-то появляются в Москве. 
И эти цветы очень отчетливо выделялись на черном ее весеннем пальто. 
Она несла желтые цветы! Нехороший цвет. 
Она повернула с Тверской в переулок и тут обернулась. 
Ну, Тверскую вы знаете? 
По Тверской шли тысячи людей, но я вам ручаюсь, что увидела она меня одного и поглядела не то что тревожно, 
а даже как будто болезненно. И меня поразила не столько ее красота, сколько необыкновенное, 
никем не виданное одиночество в глазах!
Повинуясь этому желтому знаку, я тоже свернул в переулок и пошел по ее следам. 
Мы шли по кривому, скучному переулку безмолвно, я по одной стороне, а она по другой. 
И не было, вообразите, в переулке ни души. Я мучился, потому что мне показалось, 
что с нею необходимо говорить, и тревожился, что я не вымолвлю ни одного слова, а она уйдет, 
и я никогда ее более не увижу.
И, вообразите, внезапно заговорила она:
— Нравятся ли вам мои цветы? 
Я отчетливо помню, как прозвучал ее голос, низкий довольно-таки, но со срывами, и, как это ни глупо, 
показалось, что эхо ударило в переулок и отразилось от желтой грязной стены. 
Я быстро перешел на ее сторону и, подходя к ней, ответил:
— Нет.
Она поглядела на меня удивленно, а я вдруг, и совершенно неожиданно, понял, 
что я всю жизнь любил именно эту женщину! 
Вот так штука, а? Вы, конечно, скажете, сумасшедший?
— Ничего я не говорю, — воскликнул Иван и добавил: — Умоляю, дальше!
И гость продолжал:
— Да, она поглядела на меня удивленно, а затем, поглядев, спросила так:
— Вы вообще не любите цветов?
В голосе ее была, как мне показалось, враждебность. Я шел с нею рядом, стараясь идти в ногу, 
и, к удивлению моему, совершенно не чувствовал себя стесненным.
— Нет, я люблю цветы, только не такие, — сказал я.
— А какие?
— Я розы люблю.
Тут я пожалел о том, что это сказал, потому что она виновато улыбнулась и бросила свои цветы в канаву. 
Растерявшись немного, я все-таки поднял их и подал ей, но она, усмехнувшись, оттолкнула цветы, 
и я понес их в руках.Так шли молча некоторое время, пока она не вынула у меня из рук цветы,
 не бросила их на мостовую, затем продела свою руку в черной перчатке с раструбом в мою, и мы пошли рядом.
— Дальше, — сказал Иван, — и не пропускайте, пожалуйста, ничего.
— Дальше? — переспросил гость. — Что же, дальше вы могли бы и сами угадать. 
— Он вдруг вытер неожиданную слезу правым рукавом и продолжал: 
— Любовь выскочила перед нами, как из-под земли выскакивает убийца в переулке, и поразила нас сразу обоих! 
Так поражает молния, так поражает финский нож! 
Она-то, впрочем, утверждала впоследствии, что это не так, что любили мы, конечно, друг друга давным-давно, 
не зная друг друга, никогда не видя, и что она жила с другим человеком... и я там, тогда... с этой, как ее...
— С кем? — спросил Бездомный.
— С этой... ну... с этой... ну... — ответил гость и защелкал пальцами.
— Вы были женаты?
— Ну да, вот же я и щелкаю... На этой... Вареньке... Манечке... нет, Вареньке... 
еще платье полосатое... музей... Впрочем, я не помню. 
Так вот она говорила, что с желтыми цветами в руках она вышла в тот день, чтобы я наконец ее нашел, 
и что, если бы этого не произошло, она отравилась бы, потому что жизнь ее пуста. 
Да, любовь поразила нас мгновенно. Я это знал в тот же день, уже через час, 
когда мы оказались, не замечая города, у Кремлевской стены на набережной. 
Мы разговаривали так, как будто расстались вчера, как будто знали друг друга много лет. 
На другой день мы сговорились встретиться там же, на Москве-реке, и встретились. 
Майское солнце светило нам. И скоро, скоро стала эта женщина моею тайною женой."""

# приводим текст к нормальному списку (удаляем знаки препинания, делаем нижний регистр, сплитуем по пробелу)
translation = str.maketrans("", "", ".,?!—:")
new_text = text.translate(translation).lower()
list_text = new_text.split()
# print(list_text)

# создаю словарь и заполняю его элементами ключ-значение
word_dict = {}

for word in list_text:
    word_dict.setdefault(word, list_text.count(word))
# print(word_dict)

# сортирую
sorted_values = sorted(word_dict.values())
sorted_dict = {}

for i in sorted_values:
    for k in word_dict.keys():
        if word_dict[k] == i:
            sorted_dict[k] = word_dict[k]
# print(sorted_dict)

# вывожу
for item in (list(sorted_dict))[-LIMIT:]:
    print(f"Слово '{item}' встречается в тексте {sorted_dict[item]} раз")
