#include <cstdint>
#include <iostream>

int64_t recursive_dynamic_imp(int64_t n, int64_t* val_array) {
    if (n < 2) {
        return n;
    }
    if(val_array[n] != -1) {
        return val_array[n];
    }
    return (val_array[n] = recursive_dynamic_imp(n-1,val_array)+recursive_dynamic_imp(n-2,val_array));
}

int64_t* mat_mult(int64_t* A, int64_t* B) {
    int64_t* C = new int64_t[4];
    C[0] = A[0]*B[0]+A[1]*B[2];
    C[1] = A[0]*B[1]+A[1]*B[3];
    C[2] = A[2]*B[0]+A[3]*B[2];
    C[3] = A[2]*B[1]+A[3]*B[3];
    return C;
}

int64_t* copy_mat(int64_t* A) {
    int64_t* newA = new int64_t[4];
    for(std::size_t i = 0; i < 4; ++i) {
        newA[i] = A[i];
    }
    return newA;
}

int64_t* build_power_matrix(int64_t* A, int64_t n) {
    if(n == 1) {
        return copy_mat(A);
    }
    if(n%2 == 0) {
        int64_t* Anew = build_power_matrix(A,n/2);
        int64_t* result = mat_mult(Anew, Anew);
        delete [] Anew;
        return result;
    } else {
        int64_t* Aev = build_power_matrix(A,n/2); int64_t* Aodd = mat_mult(Aev,A);
        int64_t* result = mat_mult(Aev,Aodd);
        delete [] Aev;
        delete [] Aodd;
        return result;
    }
}

extern "C" int64_t recursive_dynamic(int64_t n) {
    // Create value array
    int64_t* val_array = new int64_t[n+1];
    // Initialize
    for(int64_t i = 0; i < n+1; ++i) {
        val_array[i] = -1;
    }

    int64_t answer = recursive_dynamic_imp(n, val_array);

    // cleanup
    delete [] val_array;
    return answer;
}

extern "C" int64_t iterative(int64_t n) {
    if(n < 2) {
        return n;
    }
    int64_t f[3];
    f[1] = 1;
    f[0] = 0;
    for(int64_t i = 2; i <= n; ++i) {
        f[2] = f[1];
        f[1] = f[1]+f[0];
        f[0] = f[2];
    }
    return f[1];
}

extern "C" int64_t power_matrix(int64_t n) {
    if (n == 0) {
        return 0;
    }
    if (n <= 2) {
        return 1;
    }
    int64_t init_vec[2] = {1,1};
    int64_t* A = new int64_t[4];
    A[0] = 1;
    A[1] = 1;
    A[2] = 1;
    A[3] = 0;

    int64_t* A_power = build_power_matrix(A, n-2);

    int64_t answer = A_power[0]*init_vec[0]+A_power[1]*init_vec[0];

    // Cleanup matrices.
    delete [] A_power;
    delete [] A;

    return answer;
}

extern "C" int64_t iterative_asm(int64_t n) {
    if(n < 2) {
        return n;
    }
    int64_t fh = 1;
    int64_t fl = 0;
    int64_t count = n-1;

    asm("L0:\n\t"
        "xorq %%rax,%%rcx\n\t"
        "xorq %%rcx,%%rax\n\t"
        "xorq %%rax,%%rcx\n\t"
        "addq %%rcx,%%rax\n\t"
        "decq %%rdx\n\t"
        "jnz L0\n\t"
        : "=a" (fh)
        : "a" (fh),
          "c" (fl),
          "d" (count)
        :);

    return fh;
}
