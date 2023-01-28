#	Name:	Nguyen, Peter
#	Homework:	Extra Credit
#	Due:	12/15/2022
#	Course:	cs-2640-04-f22
#
#	Description:
#		constructs an adjacency matrix and outputs the connections through user inputs by using a 2d word array. 
#
	.data
intro:	.asciiz	"Digraph by P. Nguyen\n\n"
verticesPrompt:	.asciiz	"Enter number of vertices?"
connectionPrompt:	.asciiz	"Enter connection?"
buffer:	.space	4
alphabet:	.asciiz	"ABCDEFGHIJKLMNOPQRSTUVWXYZ"


	.text
main:
	li	$v0, 4
	la	$a0, intro
	syscall

	la	$a0, verticesPrompt	# print num of vertices prompt
	syscall

	li	$v0,5	# read int, s0 = numVertices
	syscall
	move	$s0, $v0

	mul	$s1, $s0, $s0	# s1 = numElements

	# allocating array memory on stack
	sll	$t0, $s1, 2	# t0 = numBytes = numElements * 4
	mul	$t0, $t0, -1	 
	add	$sp, $sp, $t0	# allocate memory on stack
	move	$s2, $sp	# s2 = Base address of array

	# intializing array elements to 0
	li	$t0, 0	# t0 = i
	move	$t1, $s2	# t1 = effective addr, array[j]



while1:
	bge	$t0,$s1,endWhile1	# while ( i<numElements )

	sw	$zero,($t1)	# array[j] = 0
	add	$t1, $t1, 4	# j++
	add	$t0, $t0, 1	# i++
	b	while1



endWhile1:
doWhile1:
	li	$v0, 4	#prints prompt
	la	$a0, connectionPrompt
	syscall

	li	$v0, 8	# buffer = user input
	la	$a0, buffer
	li	$a1, 4
	syscall

	lb	$t2, ($a0)	#if (buffer[0]== \n ) , break loop
	beq	$t2, '\n', endDoWhile1

	la	$s3,buffer	# convert char to int vertex
	lb	$a0,($s3)
	jal	letterToInt
	move	$a2,$v0 	# a2 = letterToInt(buffer[1])

	lb	$a0,1($s3)	# convert char to int vertex
	jal	letterToInt
	move	$a3,$v0	# a3 = letterToInt(buffer[2])

	move	$a1,$s0	# a1 = num vertices | num row | num col
	move	$a0,$s2	# a0 = matrix[]
	jal	addEdge

	b	doWhile1	# while(true)



endDoWhile1:
	li	$v0, 11	#print new line
	li	$a0, '\n'
	syscall

	move	$a0,$s2	# print matrix
	move	$a1,$s0
	move	$a2,$s0
	jal	print

	li	$v0, 10	# exit
	syscall



print:
			# a0=matrix, a1=nrow, a2=ncol
	move	$t0,$a0	# t0=matrix b/c when printing will use a0
	li	$v0,11	# print '*'
	la	$a0,'*'
	syscall
	li	$a0,' '	# print space
	syscall

	# prints first line, A B C ...
	la	$t1, alphabet	# t1 = alphabet[i]
	li	$t2, 0	# t2 = i



while2:
	beq	$t2,$a1,endWhile2	# while(i<ncol)
	
	lb	$a0,($t1)	# print alphabet[i]
	syscall
	li	$a0,' '	# print space
	syscall

	add	$t2,$t2,1	# i++
	add	$t1,$t1,1	# alphabet[i+1]
	b	while2



endWhile2:
	# fixes formatting
	li	$a0,'\n'	# print new line
	syscall
	li	$a0,'A'	# print A
	syscall
	li	$a0,' '	# print space
	syscall
	la	$t1, alphabet	
	add	$t1,$t1,1	# t1 = alphabet[k] , add 1 b/c printed 'A' to fix formatting above
	mul	$t3,$a1,$a2	# t3 = nrow*ncol
	li	$t4,0	# t4 = j



while3:
	bge	$t4,$t3,endWhile3	# while (j<nrow*ncol)
	li	$v0,1
	lw	$a0,($t0)	# print matrix[j]
	addiu	$t0,$t0,4	# matrix[j+1]
	syscall
	li	$v0,11	# print space
	li	$a0,' '
	syscall
	
	add	$t5,$t4,1	# t5 = j+1
	rem	$t5,$t5,$a2	# t5 = (j+1)%ncol
	add	$t4,$t4,1	# j++ , b/c printed matrix[j] above
	bnez	$t5,endif1
	bge	$t4,$t3,endif1
	
	li	$v0,11
	li	$a0,'\n'	# print \n
	syscall
	lb	$a0,($t1)	# print alphabet[k]
	syscall
	li	$v0,11	# print space
	li	$a0,' '
	syscall
	add	$t1,$t1,1	# alphabet[k+1]



endif1:
	b	while3



endWhile3:
	li	$v0,11	# print \n
	li	$a0,'\n'	
	syscall
	jr	$ra



addEdge:
	mul	$t1, $a2, $a1	# t1 = fromInt * numRow
	add	$t1, $t1, $a3	# t1 = (fromInt * numRow + toInt)
	sll	$t1, $t1, 2	# t1 = (fromInt * numRow + toInt) * 4
	add	$t1, $t1, $a0	# t1 = matrix[a2][a3] = base + (row * nCols + col) * 4

	li	$t0, 1
	sw	$t0, ($t1)

	jr	$ra



letterToInt:
			#a0=letter
	beq	$a0,'A',caseA
	beq	$a0,'B',caseB
	beq	$a0,'C',caseC
	beq	$a0,'D',caseD
	beq	$a0,'E',caseE
	beq	$a0,'F',caseF
	beq	$a0,'G',caseG
	beq	$a0,'H',caseH
	beq	$a0,'I',caseI
	beq	$a0,'J',caseJ
	beq	$a0,'K',caseK
	beq	$a0,'L',caseL
	beq	$a0,'M',caseM
	beq	$a0,'N',caseN
	beq	$a0,'O',caseO
	beq	$a0,'P',caseP
	beq	$a0,'Q',caseQ
	beq	$a0,'R',caseR
	beq	$a0,'S',caseS
	beq	$a0,'T',caseT
	beq	$a0,'U',caseU
	beq	$a0,'V',caseV
	beq	$a0,'W',caseW
	beq	$a0,'X',caseX
	beq	$a0,'Y',caseY
	beq	$a0,'Z',caseZ

caseA:
	li	$v0,0
	b	endSwitch1

caseB:
	li	$v0,1
	b	endSwitch1

caseC:
	li	$v0,2
	b	endSwitch1

caseD:
	li	$v0,3
	b	endSwitch1

caseE:
	li	$v0,4
	b	endSwitch1

caseF:
	li	$v0,5
	b	endSwitch1

caseG:
	li	$v0,6
	b	endSwitch1

caseH:
	li	$v0,7
	b	endSwitch1

caseI:
	li	$v0,8
	b	endSwitch1

caseJ:
	li	$v0,9
	b	endSwitch1

caseK:
	li	$v0,10
	b	endSwitch1

caseL:
	li	$v0,11
	b	endSwitch1

caseM:
	li	$v0,12
	b	endSwitch1

caseN:
	li	$v0,13
	b	endSwitch1

caseO:
	li	$v0,14
	b	endSwitch1

caseP:
	li	$v0,15
	b	endSwitch1

caseQ:
	li	$v0,16
	b	endSwitch1

caseR:
	li	$v0,17
	b	endSwitch1

caseS:
	li	$v0,18
	b	endSwitch1

caseT:
	li	$v0,19
	b	endSwitch1

caseU:
	li	$v0,20
	b	endSwitch1

caseV:
	li	$v0,21
	b	endSwitch1

caseW:
	li	$v0,22
	b	endSwitch1

caseX:
	li	$v0,23
	b	endSwitch1

caseY:
	li	$v0,24
	b	endSwitch1

caseZ:
	li	$v0,25

endSwitch1:
	jr	$ra

