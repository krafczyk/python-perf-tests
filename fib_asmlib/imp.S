    .section .rodata
    .text
hellostring:
    .string "Hello World! %li\n"
    .text
    .globl iterative
iterative:
    cmpq $2, %rdi
    jnl calc_body

    movq %rdi, %rax
    ret

calc_body:
    subq $1,%rdi
    movq $0,%rcx
    movq $1,%rax

loop:
    xorq %rcx,%rax
    xorq %rax,%rcx
    xorq %rcx,%rax

    addq %rcx,%rax

    decq %rdi
    jnz loop

    ret

    .text
    .globl iterative_short
iterative_short:
    subq $1,%rdi
    movq $0,%rcx
    movq $1,%rax

loop_short:
    xorq %rcx,%rax
    xorq %rax,%rcx
    xorq %rcx,%rax

    addq %rcx,%rax

    decq %rdi
    jnz loop_short

    ret

    .text
    .globl hello
hello:
    movq %rdi, %rsi
    leaq hellostring(%rip), %rdi
    movq $0, %rax
    call printf@PLT
    ret
