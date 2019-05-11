import command_parser as cp

"""
	test_driver is used to test input commands without hooking the bot up to a live discord server
	Set booleans to run tests
"""
testSets = True
testSingle = True
singleTest = "!roll"

"""
	similar to on_message method in dice_bot.py
	if changes are made to that module, they may need to be adjusted here as well
"""
def process(messages):
	for message in messages:
		print("Input: " + message)
		if message[0] == "!":
			command = cp.Command()
			command.parseCommand(message)
			if not command.isValid:
				print("Driver Error: " + command.errorMsg)
			elif command.action == "help":
				print("Driver Help: " + command.helpMsg)
			elif command.action == "kill":
				print("Driver Shutdown")
			elif command.action == "roll":
				print("Driver rolls: " + str(command.numRolls) + "d" + str(command.diceSize) + str(command.modifierSign) + str(command.modifier) + ": " + str(command.rolls) + " -> " + str(command.total)) 
		else:
			print("Not a bot command")
		print("\n")

if __name__ == "__main__":
	positiveInputs = ["!roll d20", "!roll d20+1", "!roll d20 + 1", "!roll d20+ 1", "!roll d20 +1", "!roll d20-1", "!roll d20 - 1", "!roll 2d20", "!roll 2d20+10", "!roll 2d20-2", "!roll 2d20- 2", "!roll 2d20 - 2", "!rolld20", "!roll2d20+2",  "!help", "!kill"]
	negativeInputs = ["roll d20", "!try d20", "!roll dd99", "!roll 10"]
	
	if testSets:
		print("***********PROCESSING POSITIVE INPUTS**********")
		process(positiveInputs)
		print("***********PROCESSING NEGATIVE INPUTS**********")
		process(negativeInputs)

	if testSingle:
		print("***********PROCESSING SINGLE INPUT**********")
		process([singleTest])