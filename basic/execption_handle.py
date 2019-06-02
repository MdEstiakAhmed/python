import io
def show_exception():
	try:
		print("hello world")
	except ZeroDivisionError:
		print("this is Zero Division Error")
	except TypeError:
		print("this is type error")
	except FileNotFoundError:
		print("this is file not found error")
	except io.UnsupportedOperation:
		print("this is Unsupported Operation error")
	except Exception as e:
		print("this is common Exception")

show_exception()