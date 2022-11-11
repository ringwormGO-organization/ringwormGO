
	[BITS		16]
	
	JMP	_kmain

	_kmain:

		cli
		mov	ax,	0
		mov	ss,	ax
		mov	sp,	0FFFFh
		sti
	
		cld

		mov	ax,	2000h
		mov	ds,	ax
		mov	es,	ax
		mov	fs,	ax
		mov	gs,	ax

		mov	ax,	1003h
		mov	bx,	0
		int		0x10

		call	clear
		call 	screen

		jmp	$

	;	INCLUDES
	%include "screen.s"
	%include "puts.s"
