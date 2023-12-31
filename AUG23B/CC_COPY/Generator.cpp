#include <bits/stdc++.h>
using namespace std;

#define TEST 10000
#define TEST_CASES true

int randint(int a, int b) {
    return a + rand() % (b + 1 - a);
}

void generate() {
    int n = 8;
    for(int i = 0; i < n; i++) {
        printf("%c", randint(97, 123));
    }
    printf("\n");
}

int main(int argc, char* argv[]) {
    srand(atoi(argv[1]));
    int test_cases = randint(TEST, TEST);
    if(TEST_CASES) {
        printf("%d\n", test_cases);
    }
    for(int test = 0; test < test_cases; test++) {
        generate();
    }
    return 0;
}