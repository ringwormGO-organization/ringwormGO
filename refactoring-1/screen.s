	clear:
		pusha

		mov	ah,	0x00
		mov	al,	0x03
		int		0x10

		popa
		ret

    screen:
        call clear
        xor al, al

		mov	ah,	09h
		mov	cx,	2000d
		mov	al,	32d
		mov	bl,	0x1F
		int		0x10

		call _string

		mov ah, 0x00
		int     0x16

		call clear
        xor al, al

		mov	ah,	09h
		mov	cx,	2000d
		mov	al,	32d
		mov	bl,	0x2F
		int		0x10

		call _string

		mov ah, 0x00
		int     0x16

        call clear
        xor al, al

		mov	ah,	09h
		mov	cx,	2000d
		mov	al,	32d
		mov	bl,	0x4F
		int		0x10

		call _string

		mov ah, 0x00
		int     0x16


        call clear
        xor al, al

		mov	ah,	09h
		mov	cx,	2000d
		mov	al,	32d
		mov	bl,	0x5B
		int		0x10

		call _string

		mov ah, 0x00
		int     0x16


        call clear
        xor al, al

		mov	ah,	09h
		mov	cx,	2000d
		mov	al,	32d
		mov	bl,	0x6E
		int		0x10

		call _string

		mov ah, 0x00
		int     0x16

		jmp screen

        ret

    _string:
        mov si, cake
        call    print
        ret
