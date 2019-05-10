import command_parser as cp

"""
	test_driver is used to test input commands without hooking the bot up to a live discord server
"""
def process(message):
	if message[0] == "!":
		command = cp.Command(message)

		# MATCH THIS SECTION to changes in dice_bot.py on_message() method
		if not command.isValid:
			print("Driver Error: " + command.errorMsg)
			return
		if command.action == "help":
			print("Driver Help: " + command.helpMsg)
			return
		if command.action == "roll":
			print("Driver roll: " + str(command.rolls) + " -> " + str(command.total))
			return

"""
	Change testInput to test the specified command
"""
if __name__ == "__main__":
	testInput = "!roll d20-1"
	process(testInput)