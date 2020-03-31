## Вторая версия программы.
import random
X = "X"
O = "0"
moves_ii = [1, 2, 3]

## создаем поле (create field)
field = [[".", ".", "."],
         [".", ".", "."],
         [".", ".", "."]]

## отображаем поле на экране(display the field on the screen)
def field_in_display():
	for row in field:
		print(row[0], row[1], row[2])
field_in_display()

## добавляем выбор кто первый ходит
print("Выбери какими символами будешь играть X или 0")
choose_first = input().upper()
def choose():
	if choose_first == "X":
		print("\n Ходи тогда первым")
		human = X
		computer = O
	else:
		print("\n Ходи тогда вторым")
		human = O
		computer = X
	return human, computer

# Добавляем условия победы
def win(field):
	path_of_win = ((field[0][0], field[0][1], field[0][2]),
	               (field[1][0], field[1][1], field[1][2]),
	               (field[2][0], field[2][1], field[2][2]),
	               (field[0][0], field[1][0], field[2][0]),
	               (field[0][1], field[1][1], field[2][1]),
	               (field[0][2], field[1][2], field[2][2]),
	               (field[0][0], field[1][1], field[2][2]),
	               (field[0][2], field[1][1], field[2][0]))
	
	for line in path_of_win:
		if line[0] == line[1] == line[2]:
			return [line[0]]
	return False

def computer_step():
	computer, human = choose()
	a = random.choice(moves_ii)
	a = int(a)
	b = random.choice(moves_ii)
	b = int(b)
	while field[a - 1][b - 1] == "0" or "X":
		print("Выбираю другие координаты другие координаты")
		a = random.choice(moves_ii)
		b = random.choice(moves_ii)
		if field[a - 1][b - 1] == ".":
			if computer == X:
				field[a - 1][b - 1] = "0"
			else:
				field[a - 1][b - 1] = "X"
			break
	else:
		
		if computer == X:
			field[a - 1][b - 1] = "0"
		else:
			field[a - 1][b - 1] = "X"
	print("Порядковый номер строки", a)
	print("Порядковый номер солбца", b)

def human_step():
	a = []
	b = []
	computer, human = choose()
	povt = 0
	while (a != "1" and a != "2" and a != "3") or (b != "1" and b != "2" and b != "3"):
		field_in_display()
		a = input("Введите порядковый номер строки от 1 до 3: ")
		b = input("Введите порядковый номер столбца от 1 до 3: ")
		povt += 1
		if povt >= 4:
			print("Тебе рановато еще в это играть. Читать еще не умеешь")
			return
	else:
		a = int(a)
		b = int(b)
		while field[a - 1][b - 1] != ".":
			print("Это место занято. Пожалуйста выберете другое")
			field_in_display()
			a = input("Введите снова номер строки от 1 до 3: ")
			a = int(a)
			b = input("Введите снова номер столбца от 1 до 3: ")
			b = int(b)
			povt += 1
			if povt >= 3:
				print("Тебе рановато еще в это играть. Читать еще не умеешь")
				return
		else:
			if human == X:
				field[a - 1][b - 1] = "0"
			else:
				field[a - 1][b - 1] = "X"

# и делаем тело нашей программы
def main():
	computer, human = choose()
	count = 0
	wins = False
	while not wins:
		while count <= 8:
			if count == 0 or count == 2 or count == 4 or count == 6 or count == 8:
				print("Ходит 1 игрок ")
				if computer == O:
					print("компьютер")
					computer_step()
				else:
					print("человек")
					human_step()
					field_in_display()
						
				if count > 4:
					tmp = win(field)
					if tmp:
						print(tmp, "Выйграл")
						wins = True
						field_in_display()
						break
				if count == 8:
					print("ничья")
					wins = True
					break
			else:
				print("Ходит 2й игрок")
				if human == X:
					print("человек")
					human_step()
					field_in_display()
				else:
						print("компьютер")
						computer_step()
				if count > 4:
					tmp = win(field)
					if tmp:
						print(tmp, "Выйграл")
						wins = True
						field_in_display()
						break
			count += 1
			win(field)

main()
input("\n\n Нажмите Enter, чтобы выйти.")

