import json
import random

def get_smth(smth):
	with open("C:\\Users\\denis\\Desktop\\archive\\generator\\бункер\\new.json", 'r', encoding='utf-8') as json_file:
		json_data = json.load(json_file)
	my_file = open("C:\\Users\\denis\\Desktop\\archive\\generator\\бункер\\persons\\NEW_CHAR.txt", 'w')

	text = ""

	for name, description in json_data.items():
		if name == smth:
			descr = rand_output(description)
			text += description[descr]

	my_file.writelines(text)
	my_file.close()

def create_event(person, bun_str):
	event_file = open("C:\\Users\\denis\\Desktop\\archive\\generator\\бункер\\persons\\event.txt", 'w', encoding='utf-8')
	event_file.writelines("Катастрофа - " + str(person["catastrophe"]["name"]) + ".\nОписание: "+ str(person["catastrophe"]["desc"]))
	event_file.writelines(bun_str)
	event_file.close()

def rand_output(desc): #генерация случайного элемента из значений ключа
	item = random.randint(0, len(desc)-1)
	return item

def write_person(person, num, cards, bun_str):
	file_name = "C:\\Users\\denis\\Desktop\\archive\\generator\\бункер\\persons\\" + str(num) + ".txt"
	
	age = str(random.randint(15, 90))

	my_file = open(file_name, 'w')#создание файла для каждого игрока
	
	file_text = "Биологическая информация: " + str(person["gender"]) + ", " + age + " лет," + "\n" + str(person["orientation"]) + "\nПрофессия: " + str(person["occupation"]) + "\nХобби: " + str(person["hobbies"]) +"\nБагаж: " + str(person["baggage"])+ "\nДругая информация: " + str(person["additional info"]) + "\nЗдоровье: " + str(person["health status"]) + "\nХарактер: " + str(person["temper"]) + "\nФобия: " + str(person["phobia"]["name"])
	
	if (person["phobia"]["desc"]):#Чтобы избежать строки с описанием в том случае, если фобии нет
		file_text += ". Описание: " + str(person["phobia"]["desc"])

	file_text += "\nВаши карты: \n1. " + str(cards["card1"]['name']) + ": " + str(cards["card1"]['desc']) + "\n2. " + str(cards["card2"]['name']) + ": " + str(cards["card2"]['desc']) 

	my_file.writelines(file_text)
	my_file.close()

	create_event(person, bun_str)


def generate_person(data, cards):
	with open("C:\\Users\\denis\\Desktop\\archive\\generator\\бункер\\new.json", 'r', encoding='utf-8') as json_file:
		json_data = json.load(json_file)


	for name, description in json_data.items():
		kek = rand_output(description)#генерируем случайное значение

		for kword, key in data.items(): #записываем сгенерированные данные в data
			if kword == name:
				data[kword] = description[kek]

			if name == "special conditions": #костыль, выполняется кучу раз, зотя нужен 1. Считает кол-во карточек
				cards_len = len(description)

				r = random.randint(0, cards_len-1)
				r2 = random.randint(0, cards_len-1)

				cards["card1"] = description[r]
				cards["card2"] = description[r2]

				while r == r2: #костыль на проверку, не совпадают ли карты действий
					r2 = random.randint(0, cards_len-1)

			if name == "bunker_info":
				bun_str = ""
				lx = random.randint(20, 350)

				lenn = random.randint(0, len(description[0]["things"])-1)
				lenn3 = random.randint(0, len(description[1]["desc"])-1)

				items_count = random.randint(2, 4)
				tems_indxs = random.sample(range(0, len(description[0]["things"])-1), items_count)

				bunker_item = description[0]["things"]#copy
				bun_str += "\nВ бункере есть: "

				for x in tems_indxs:
					el = bunker_item[x]
					bun_str += str(el) + ", "

				nunker_time = description[1]["desc"][lenn3]

				bun_str += "\nОписание бункера: " + str(lx) + "м², " + "время пребывания " + str(nunker_time)

	write_person(data, i+1, cards, bun_str)

if __name__ == '__main__':
	data = {"gender": "","occupation": "", "orientation": "", "hobbies": "", "baggage": "", "additional info": "", "health status": "", "temper": "",  "phobia":"", "catastrophe": ""}
	cards = {"card1": "", "card1": ""}
	cards_len = 0

	ch = int(input("1 - создать личности, 2 - отдельную характеристику: "))

	if ch == 1:
		gen_times = int(input("Введите количество игроков Бункера: "))

		for i in range(gen_times): #создаем gen_times личностей
			person = generate_person(data, cards)
	else:
		ch = input("Название хар-ки: ")
		get_smth(ch)

	