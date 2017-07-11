
n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
	
media = (n1*2+n2*3+n3*4+n4)/10

if media > 7:
	print("Aluno Aprovado.")
elif media < 5:
	print("Aluno Reprovado.")
else:
	print("Aluno em exame.")
	rec = float(input())
	print("Nota do exame: %1.1f" % rec)
	media = (media+rec)/2
	if media > 5:
		print("Aluno Aprovado.")
	else:
		print("Aluno Reprovado.")
	print("Media final: %1.1f" % media)
