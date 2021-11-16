
def HanoiMove(iNum, iFrom, iTo):
	if iNum> 1:
		HanoiMove(iNum- 1, iFrom, 6- iFrom- iTo)

	print(f"Move {iFrom} to {iTo}")

	if iNum> 1:
		HanoiMove(iNum- 1, 6- iFrom- iTo, iTo)

print("Hanoi Top Program")
iTop= int(input("Hanoi Top Num: "))

HanoiMove(iNum, 1, 3)

print("Pull Prac")
