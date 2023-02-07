class Ascii_Creatures():
	"""
	Ascii_Creatures allows printing of ASCII creature with variable 
	moods to terminal. More creatures may be added later.
	"""
	
	"""Prints:
	  ^ ^
	 (^_^)
	/(   )\
	  U U
	 """
	def print_character_default(self):
		print("  ^ ^\n (^_^)\n/(   )\\\n  U U")

	"""
	Prints:
	  ^ ^
	 (-_-)
	/(   )\
	  U U
	"""
	def print_character_miss_1(self):
		print("  ^ ^\n (-_-)\n/(   )\\\n  U U")

	"""
	Prints:
	  ^ ^
	 (-_-)
	-(   )-
	  U U
	"""
	def print_character_miss_2(self):
		print("  ^ ^\n (-_-)\n-(   )-\n  U U")

	"""
	Prints:
	  ^ ^
	 (u_u)
	 (^ ^)
	  U U
	"""
	def print_character_miss_3(self):
		print("  ^ ^\n (u_u)\n (^ ^)\n  U U")

	"""
	Prints:
	  ^ ^
	 (u_u)
	 (^ ^)
	  o o
	"""
	def print_character_miss_4(self):
		print("  ^ ^\n (u_u)\n (^ ^)\n  o o")

	"""
	Prints:
	  ^ ^
	 (o_o)
	 (^ ^)
	  o o
	"""
	def print_character_miss_5(self):
		print("  ^ ^\n (o_o)\n (^ ^)\n  o o")

	"""Prints:
	  ^ ^
	 (^.^)
	\(   )/
	  U U
	  """
	def print_character_win(self):
		print("  ^ ^\n (^.^)\n\\(   )/\n  U U")

	"""
	Prints:
	  Y Y
	 (XOX)
	\(   )/
	  o o
	"""
	def print_character_lose(self):
		print("  Y Y\n (XOX)\n\\(   )/\n  o o")
