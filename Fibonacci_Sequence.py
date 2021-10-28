def fibonacci(n):
	fib_sequence = [1,1];
	index = 1;
	b = 3;
	print("1: " + str(fib_sequence[0]) + "\n2: " + str(fib_sequence[1]));
	while len(fib_sequence) < n:
		fib_sequence.append(fib_sequence[index] + fib_sequence[index-1]);
		index += 1;
		print(str(b) + ": " + str(fib_sequence[index])); #-> Printa todos os elementos do terceiro ao enésimo termo.
		#print(fib_sequence[index]/fib_sequence[index-1]); #-> golden number.
		b += 1;
	return fib_sequence[n-1];

print(fibonacci(10));


