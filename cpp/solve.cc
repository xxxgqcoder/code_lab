#include "solve.h"

int main(int argc, char **argv) {
    using namespace std;

    for (int i = 0; i < argc; i++) {
        cout << "arg " << i << " len: " << strlen(argv[i]) << endl;
        for (int j = 0; j < strlen(argv[i]); j++) {
            cout << hex << argv[i][j];
        }
        cout << endl;
    }
}