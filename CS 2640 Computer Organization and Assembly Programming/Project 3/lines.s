#  Name:   Nguyen, Peter
#  Project:  # 3
#  Due:        11/3/22 
#  Course:  cs-2640-04-f22 
# 
#  Description: 
#    Stores line of text in array and once enter is hit, program terminates and prints the lines the user has entered

		.data
MAXLINES:	.word	8
LINELEN:	.word	40
lines:	.space	32
inbuf:	.space	40
newLine:	.asciiz	"\n"
promptLine:	.asciiz	"Enter Text? "
header:	.asciiz	"Lines by P. Nguyen\n\n"

	.text
main:
	addiu 	$sp, $sp, -4
	sw	$ra,0($sp)
	la	$a0, header
	jal	puts
	li	$t0, 0
	la	$t1, lines
	lw	$t2, MAXLINES

mainLoop:
	beq	$t0, $t2, endOfMainLoop

	la	$a0, promptLine
	jal	puts

	la	$a0,	inbuf
	lw	$a1,	LINELEN
	jal	gets

	beqz	$v0, endOfMainLoop
	
	la	$a0, inbuf
	jal	strdup
	sw	$v0, 0($t1)
	addi $t0, $t0, 1
	addi $t1, $t1, 4
	j	mainLoop

endOfMainLoop:
	la	$t1, lines

mainPrintLoop:
	beqz	$t0, returnMain

	lw	$a0, 0($t1)
	jal	puts

	la	$a0, newLine
	jal	puts

	addi	$t0, $t0, -1
	addiu $t1, $t1, 4
	j	mainPrintLoop

returnMain:
	lw	$ra, 0($sp)
	addiu $sp, $sp, 4
	jr	$ra

strlen:
	li	$v0, 0
	move	$a1, $a0

strLenLoop:
	lb	$v1, 0($a1)
	beqz	$v1,	returnStrLen
	beq	$v1, 10, returnStrLen

	addiu $a1, $a1, 1
	addi	$v0, $v0, 1
	j 	strLenLoop

returnStrLen:
	jr	$ra

malloc:
	li	$v0, 9
	syscall
	jr	$ra

puts:
	li	$v0, 4
	syscall
	jr	$ra

strdup:
	addiu $sp, $sp, -8
	sw	$ra, 0($sp)
	sw	$a0,	4($sp)
	jal	strlen
	addi	$a0, $v0, 1
	jal	malloc
	addiu $v1, $v0, 0
	lw	$a0, 4($sp)

strdupLoop:
	lb	$a1, 0($a0)
	beqz	$a1, returnStrDup
	beq	$a1,	10,	returnStrDup

	sb	$a1,	0($v1)

	addiu $a0, $a0, 1
	addiu $v1, $v1, 1
	j strdupLoop

returnStrDup:
	sb	$0, 0($v1)
	lw	$ra, 0($sp)
	addiu $sp, $sp, 8
	jr	$ra

gets:
	addiu $sp, $sp, -4
	sw	$ra, 0($sp)
	li	$v0, 8
	syscall
	
	jal	strlen

	lw	$ra, 0($sp)
	addiu $sp, $sp, 4
	jr	$ra

End:
		li	$v0,	10
		syscall