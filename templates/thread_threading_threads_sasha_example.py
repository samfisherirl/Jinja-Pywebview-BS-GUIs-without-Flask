import threading

data = []


def thr(line):
	if "x" in line:
		data.append(line)

def main():
	threads = []
	with open('index.html', 'r') as f:
		for line in f.readlines():

			t = threading.Thread(target=thr, args=[line])
			t.start()
			threads.append(t)

		for thread in threads:
			thread.join()

	print(data)


if __name__ == '__main__':
	main()